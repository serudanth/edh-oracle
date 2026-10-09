"""Unified Scryfall Cache Access Layer.

Provides fast, indexed card lookups across the local SQLite database
(knowledgebase/_cache/scryfall.db) with sub-millisecond query performance,
full-text search (FTS5), and multi-faced card alias resolution.
"""
import collections.abc
import json
import pathlib
import sqlite3
import sys
from typing import Any, Dict, List, Optional, Union

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_DB_CACHE = REPO_ROOT / "knowledgebase" / "_cache" / "scryfall.db"


class ScryfallDatabase:
    """Read-only interface to local Scryfall SQLite database."""

    def __init__(self, db_path: pathlib.Path = DEFAULT_DB_CACHE):
        self.db_path = db_path
        self._conn: Optional[sqlite3.Connection] = None

    def _get_connection(self) -> Optional[sqlite3.Connection]:
        if self._conn is not None:
            return self._conn
        if not self.db_path.exists():
            return None
        # Read-only URI connection
        uri = f"file:{self.db_path}?mode=ro"
        self._conn = sqlite3.connect(uri, uri=True, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        return self._conn

    def is_available(self) -> bool:
        return self.db_path.exists()

    def ensure_available(self):
        """Raises FileNotFoundError if local database does not exist."""
        if not self.is_available():
            raise FileNotFoundError(
                f"Local Scryfall database not found at {self.db_path}.\n"
                "Initialize it by running: python tools/sync_scryfall_bulk.py"
            )

    def get_card(self, name: str) -> Optional[Dict[str, Any]]:
        conn = self._get_connection()
        if conn is None:
            return None

        # 1. Exact match on canonical name
        cur = conn.cursor()
        cur.execute("SELECT data FROM cards WHERE name = ? COLLATE NOCASE", (name,))
        row = cur.fetchone()
        if row:
            return json.loads(row["data"])

        # 2. Match via aliases (front face, back face, normalized name)
        cur.execute(
            """
            SELECT c.data FROM cards c
            JOIN card_aliases a ON a.canonical_name = c.name
            WHERE a.alias = ? COLLATE NOCASE
            LIMIT 1
            """,
            (name,),
        )
        row = cur.fetchone()
        if row:
            return json.loads(row["data"])

        return None

    def search_fts(self, query: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Searches card names, type lines, and oracle text via SQLite FTS5."""
        conn = self._get_connection()
        if conn is None:
            return []

        cur = conn.cursor()
        try:
            cur.execute(
                """
                SELECT c.data FROM cards c
                JOIN cards_fts f ON f.rowid = c.rowid
                WHERE cards_fts MATCH ?
                ORDER BY c.edhrec_rank ASC NULLS LAST
                LIMIT ?
                """,
                (query, limit),
            )
            return [json.loads(r["data"]) for r in cur.fetchall()]
        except sqlite3.OperationalError:
            # Fallback if query syntax isn't valid FTS5 syntax
            cur.execute(
                """
                SELECT data FROM cards
                WHERE name LIKE ? OR oracle_text LIKE ?
                ORDER BY edhrec_rank ASC NULLS LAST
                LIMIT ?
                """,
                (f"%{query}%", f"%{query}%", limit),
            )
            return [json.loads(r["data"]) for r in cur.fetchall()]

    def count(self) -> int:
        conn = self._get_connection()
        if conn is None:
            return 0
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM cards")
        return cur.fetchone()[0]

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None


class UnifiedScryfallCache(collections.abc.Mapping):
    """Transparent dict-like mapping for Scryfall cards.

    Checks:
    1. In-memory dictionary (for overrides / cached hits).
    2. SQLite database (knowledgebase/_cache/scryfall.db) on cache miss.
    
    Caches database hits in-memory for zero repeated lookups.
    """

    def __init__(
        self,
        db_path: Optional[pathlib.Path] = DEFAULT_DB_CACHE,
        json_path: Optional[pathlib.Path] = None,
    ):
        self._memory_cache: Dict[str, Any] = {}
        self.json_path = json_path
        self.db = ScryfallDatabase(db_path or DEFAULT_DB_CACHE)

        if json_path and json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    self._memory_cache = json.load(f)
            except Exception:
                self._memory_cache = {}

    def is_available(self) -> bool:
        return self.db.is_available() or len(self._memory_cache) > 0

    def __getitem__(self, key: str) -> Dict[str, Any]:
        if key in self._memory_cache:
            return self._memory_cache[key]

        if self.db.is_available():
            card = self.db.get_card(key)
            if card is not None:
                self._memory_cache[key] = card
                return card

        raise KeyError(key)

    def __contains__(self, key: object) -> bool:
        if not isinstance(key, str):
            return False
        if key in self._memory_cache:
            return True
        if self.db.is_available():
            card = self.db.get_card(key)
            if card is not None:
                self._memory_cache[key] = card
                return True
        return False

    def __iter__(self):
        if self.db.is_available():
            conn = self.db._get_connection()
            if conn:
                cur = conn.cursor()
                cur.execute("SELECT name FROM cards ORDER BY name ASC")
                for row in cur.fetchall():
                    yield row["name"]
                return
        yield from self._memory_cache

    def __len__(self) -> int:
        if self.db.is_available():
            return max(len(self._memory_cache), self.db.count())
        return len(self._memory_cache)

    def get(self, key: str, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def to_dict(self) -> Dict[str, Any]:
        """Returns the in-memory cache dictionary."""
        return self._memory_cache


def get_scryfall_cache(
    db_path: Optional[pathlib.Path] = DEFAULT_DB_CACHE,
    json_path: Optional[pathlib.Path] = None,
) -> UnifiedScryfallCache:
    """Convenience factory returning a UnifiedScryfallCache instance."""
    return UnifiedScryfallCache(db_path=db_path, json_path=json_path)
