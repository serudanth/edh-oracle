"""Unified Card Data Provider.

Resolves card attributes from local SQLite database (mtg.db) with automatic
fallback to persistent scryfall-cards.json cache. Normalizes schemas across sources.
"""

import json
import pathlib
import re
from typing import Any, Dict, Optional

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
DB_PATH = REPO_ROOT / "knowledgebase" / "_cache" / "mtg.db"
SCRYFALL_DB_PATH = REPO_ROOT / "knowledgebase" / "_cache" / "scryfall.db"
SCRYFALL_CACHE_PATH = REPO_ROOT / "knowledgebase" / "_cache" / "scryfall-cards.json"


class CardDataProvider:
    """Provides normalized MTG card attributes from local offline databases."""

    def __init__(
        self,
        db_path: pathlib.Path = DB_PATH,
        cache_path: pathlib.Path = SCRYFALL_CACHE_PATH,
        cache: Optional[Dict[str, Any]] = None,
        scryfall_db_path: pathlib.Path = SCRYFALL_DB_PATH,
    ):
        self.db_path = db_path
        self.scryfall_db_path = scryfall_db_path
        self.cache_path = cache_path
        self._memory_cache: Dict[str, Optional[Dict[str, Any]]] = {}
        if cache:
            for k, v in cache.items():
                self._memory_cache[k] = self._normalize(v) if v else None
        self._json_cache: Optional[Dict[str, Any]] = None
        self._has_sqlite = self.db_path.exists()
        self._has_scryfall_db = self.scryfall_db_path.exists()

    def _get_json_cache(self) -> Dict[str, Any]:
        if self._json_cache is None:
            if self.cache_path.exists():
                try:
                    with open(self.cache_path, "r", encoding="utf-8") as f:
                        self._json_cache = json.load(f)
                except Exception:
                    self._json_cache = {}
            else:
                self._json_cache = {}
        return self._json_cache

    def clean_card_name(self, raw_name: str) -> str:
        """Strips annotations, set codes, and markdown artifacts from card names."""
        name = raw_name.strip()
        # Strip trailing parenthetical or star notes like *(ManaBox — Bulk)* or *(foil)*
        name = re.sub(r"\s+\*?\([^*]+\)\*?$", "", name).strip()
        name = re.sub(r"\s+\*.*$", "", name).strip()
        return name

    def get_card(self, card_name: str) -> Optional[Dict[str, Any]]:
        """Fetches and normalizes a card dictionary by name."""
        clean_name = self.clean_card_name(card_name)
        if clean_name in self._memory_cache:
            return self._memory_cache[clean_name]

        # 1. Try SQLite mtg.db if available
        card_data = None
        if self._has_sqlite:
            card_data = self._lookup_sqlite(clean_name)

        # 2. Try Scryfall SQLite scryfall.db if available
        if not card_data and self._has_scryfall_db:
            card_data = self._lookup_scryfall_db(clean_name)

        # 3. Fallback to scryfall-cards.json
        if not card_data:
            card_data = self._lookup_json(clean_name)

        normalized = self._normalize(card_data) if card_data else None
        self._memory_cache[clean_name] = normalized
        return normalized

    def _lookup_scryfall_db(self, name: str) -> Optional[Dict[str, Any]]:
        try:
            import sqlite3
            conn = sqlite3.connect(f"file:{self.scryfall_db_path}?mode=ro", uri=True)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT data FROM cards WHERE name = ? COLLATE NOCASE", (name,))
            row = cur.fetchone()
            if not row and " // " in name:
                cur.execute("SELECT data FROM cards WHERE name = ? COLLATE NOCASE", (name.split(" // ")[0].strip(),))
                row = cur.fetchone()
            if not row:
                cur.execute(
                    "SELECT c.data FROM cards c JOIN card_aliases a ON a.canonical_name = c.name WHERE a.alias = ? COLLATE NOCASE LIMIT 1",
                    (name,),
                )
                row = cur.fetchone()
            conn.close()
            if row:
                return json.loads(row["data"])
        except Exception:
            pass
        return None

    def _lookup_sqlite(self, name: str) -> Optional[Dict[str, Any]]:
        try:
            import sqlite3
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            # Exact match on name or face_name
            cur.execute("SELECT * FROM cards WHERE name = ? OR face_name = ?", (name, name))
            row = cur.fetchone()

            # Front-face split match if name contains ' // '
            if not row and " // " in name:
                front = name.split(" // ")[0].strip()
                cur.execute("SELECT * FROM cards WHERE name = ? OR face_name = ?", (front, front))
                row = cur.fetchone()

            # Case-insensitive fallback
            if not row:
                cur.execute("SELECT * FROM cards WHERE LOWER(name) = LOWER(?) OR LOWER(face_name) = LOWER(?)", (name, name))
                row = cur.fetchone()

            conn.close()
            if row:
                d = dict(row)
                for k in ["colors", "color_identity", "types", "subtypes", "supertypes", "keywords"]:
                    if d.get(k) and isinstance(d[k], str):
                        try:
                            d[k] = json.loads(d[k])
                        except Exception:
                            pass
                return d
        except Exception:
            pass
        return None

    def _lookup_json(self, name: str) -> Optional[Dict[str, Any]]:
        cache = self._get_json_cache()
        if name in cache:
            return cache[name]

        # Check front-face if split name
        if " // " in name:
            front = name.split(" // ")[0].strip()
            if front in cache:
                return cache[front]

        # Case-insensitive lookup
        name_lower = name.lower()
        for k, v in cache.items():
            if k.lower() == name_lower:
                return v

        return None

    def _normalize(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """Normalizes card fields across SQLite and Scryfall JSON sources."""
        cmc = float(raw.get("mana_value") if "mana_value" in raw else raw.get("cmc", 0.0))
        mana_cost = raw.get("mana_cost") or ""
        type_line = raw.get("type_line") or ""
        oracle_text = raw.get("oracle_text") or ""
        color_identity = raw.get("color_identity") or []
        saltiness = float(raw.get("edhrec_saltiness") or 0.0)

        return {
            "name": raw.get("name", ""),
            "cmc": cmc,
            "mana_value": cmc,
            "mana_cost": mana_cost,
            "type_line": type_line,
            "oracle_text": oracle_text,
            "color_identity": color_identity,
            "edhrec_saltiness": saltiness,
            "raw": raw,
        }
