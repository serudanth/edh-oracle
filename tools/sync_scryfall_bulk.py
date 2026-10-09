#!/usr/bin/env python3
"""Sync Scryfall Bulk Data to Local SQLite Cache & FTS Index.

Downloads Scryfall's authoritative 'Oracle Cards' bulk data export (.jsonl.gz or .json)
and builds an indexed local SQLite database (knowledgebase/_cache/scryfall.db)
with full-text search (FTS5) and alias mapping for multi-faced cards (MDFCs).

Usage:
    python tools/sync_scryfall_bulk.py                  # Sync bulk data and build SQLite DB
    python tools/sync_scryfall_bulk.py --query "Sol Ring" # Test lookup
    python tools/sync_scryfall_bulk.py --search "draw a card" # FTS search test
    python tools/sync_scryfall_bulk.py --stats          # Inspect cache stats
"""
import argparse
import datetime
import gzip
import json
import os
import pathlib
import sqlite3
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, Iterator, List, Optional, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = REPO_ROOT / "knowledgebase" / "_cache" / "scryfall.db"
DEFAULT_RAW_PATH = REPO_ROOT / "knowledgebase" / "_cache" / "oracle-cards.raw.jsonl.gz"

SCRYFALL_BULK_META_URL = "https://api.scryfall.com/bulk-data/oracle-cards"
FALLBACK_PROXY_PREFIX = "https://r.jina.ai/"


def get_bulk_download_url(user_agent: str = "EDHOracle/1.0") -> Tuple[str, Dict[str, Any]]:
    """Fetches the latest download URI for oracle-cards bulk export."""
    headers = {"User-Agent": user_agent, "Accept": "application/json"}
    req = urllib.request.Request(SCRYFALL_BULK_META_URL, headers=headers)

    def extract_uri(data: Dict[str, Any]) -> str:
        # Scryfall bulk endpoint supports 'jsonl_download_uri' (.jsonl.gz) and legacy 'download_uri' (.json)
        uri = data.get("jsonl_download_uri") or data.get("download_uri")
        if not uri:
            raise KeyError(
                f"Neither 'jsonl_download_uri' nor 'download_uri' found in Scryfall bulk response. Keys: {list(data.keys())}"
            )
        return uri

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return extract_uri(data), data
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print("Direct Scryfall access returned HTTP 403. Attempting proxy fallback...", file=sys.stderr)
            proxy_url = f"{FALLBACK_PROXY_PREFIX}{SCRYFALL_BULK_META_URL}"
            proxy_req = urllib.request.Request(proxy_url, headers={"User-Agent": user_agent})
            with urllib.request.urlopen(proxy_req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return extract_uri(data), data
        raise


def download_stream(url: str, output_path: pathlib.Path, user_agent: str = "EDHOracle/1.0"):
    """Downloads large file with progress output."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": user_agent}
    req = urllib.request.Request(url, headers=headers)

    print(f"Downloading bulk data from {url}...")
    with urllib.request.urlopen(req, timeout=120) as resp, open(output_path, "wb") as out_f:
        total_size = int(resp.headers.get("Content-Length", 0))
        downloaded = 0
        chunk_size = 1024 * 1024  # 1MB chunks

        while True:
            chunk = resp.read(chunk_size)
            if not chunk:
                break
            out_f.write(chunk)
            downloaded += len(chunk)
            if total_size > 0:
                percent = downloaded / total_size * 100
                mb_dl = downloaded / (1024 * 1024)
                mb_total = total_size / (1024 * 1024)
                print(f"\rProgress: {mb_dl:.1f}/{mb_total:.1f} MB ({percent:.1f}%)", end="", flush=True)
            else:
                mb_dl = downloaded / (1024 * 1024)
                print(f"\rDownloaded: {mb_dl:.1f} MB", end="", flush=True)

    print("\nDownload complete.")


def iterate_cards(filepath: pathlib.Path) -> Iterator[Dict[str, Any]]:
    """Yields card dicts from .json, .jsonl, or .jsonl.gz / .gz files."""
    name_str = str(filepath).lower()
    if name_str.endswith(".gz"):
        with gzip.open(filepath, "rt", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield json.loads(line)
    elif name_str.endswith(".jsonl"):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield json.loads(line)
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            content = json.load(f)
            if isinstance(content, list):
                yield from content
            elif isinstance(content, dict):
                for k, v in content.items():
                    if isinstance(v, dict):
                        if "name" not in v:
                            v["name"] = k
                        yield v


def normalize_card_entry(raw_card: Dict[str, Any], fetch_date: str) -> Tuple[Dict[str, Any], List[str]]:
    """Normalizes a Scryfall card into the EDH Oracle cache schema.
    
    Returns:
        (normalized_dict, aliases_list)
    """
    name = raw_card.get("name", "").strip()
    cmc = float(raw_card.get("cmc", 0.0))
    color_identity = raw_card.get("color_identity", [])
    colors = raw_card.get("colors", [])
    keywords = raw_card.get("keywords", [])
    edhrec_rank = raw_card.get("edhrec_rank")
    mana_cost = raw_card.get("mana_cost", "")
    type_line = raw_card.get("type_line", "")
    oracle_text = raw_card.get("oracle_text", "")
    layout = raw_card.get("layout", "normal")
    
    legalities = raw_card.get("legalities", {})
    legal_commander = legalities.get("commander", "not_legal")
    
    prices = raw_card.get("prices", {})
    prices_usd = prices.get("usd")
    prices_usd_foil = prices.get("usd_foil")

    aliases: List[str] = []

    # Handle multi-faced cards (transform, modal_dfc, split, flip, adventure)
    card_faces = raw_card.get("card_faces")
    if card_faces and isinstance(card_faces, list) and len(card_faces) > 0:
        face_names = []
        face_texts = []
        face_types = []
        face_costs = []
        all_face_colors = set(colors)

        for face in card_faces:
            fn = face.get("name", "").strip()
            if fn:
                face_names.append(fn)
                if fn.lower() != name.lower():
                    aliases.append(fn)
            ft = face.get("oracle_text", "").strip()
            if ft:
                face_texts.append(ft)
            ftp = face.get("type_line", "").strip()
            if ftp:
                face_types.append(ftp)
            fc = face.get("mana_cost", "").strip()
            if fc:
                face_costs.append(fc)
            for c in face.get("colors", []):
                all_face_colors.add(c)

        if not oracle_text and face_texts:
            oracle_text = "\n//\n".join(face_texts)
        if not type_line and face_types:
            type_line = " // ".join(face_types)
        if not mana_cost and face_costs:
            mana_cost = " // ".join(face_costs)
        if not colors and all_face_colors:
            colors = sorted(list(all_face_colors))

    normalized = {
        "cmc": cmc,
        "color_identity": color_identity,
        "colors": colors,
        "edhrec_rank": edhrec_rank,
        "fetched_at": fetch_date,
        "keywords": keywords,
        "legal_commander": legal_commander,
        "mana_cost": mana_cost,
        "oracle_text": oracle_text,
        "prices_usd": prices_usd,
        "type_line": type_line,
    }
    if prices_usd_foil:
        normalized["prices_usd_foil"] = prices_usd_foil

    return normalized, aliases


def build_sqlite_cache(json_filepath: pathlib.Path, db_path: pathlib.Path) -> int:
    """Builds an SQLite database from the bulk file with batching and atomic replacement."""
    fetch_date = datetime.date.today().isoformat()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    temp_db = db_path.with_suffix(".tmp.db")

    if temp_db.exists():
        temp_db.unlink()

    conn = sqlite3.connect(temp_db)
    cur = conn.cursor()

    cur.execute("PRAGMA synchronous = OFF")
    cur.execute("PRAGMA journal_mode = MEMORY")

    # Schema
    cur.execute("""
        CREATE TABLE cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE COLLATE NOCASE,
            mana_cost TEXT,
            cmc REAL,
            type_line TEXT,
            oracle_text TEXT,
            colors TEXT,
            color_identity TEXT,
            keywords TEXT,
            legal_commander TEXT,
            edhrec_rank INTEGER,
            prices_usd TEXT,
            prices_usd_foil TEXT,
            layout TEXT,
            fetched_at TEXT,
            data TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE card_aliases (
            alias TEXT PRIMARY KEY COLLATE NOCASE,
            canonical_name TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE VIRTUAL TABLE cards_fts USING fts5(
            name,
            type_line,
            oracle_text,
            content='cards',
            content_rowid='id'
        )
    """)

    print(f"Reading and ingesting bulk data from {json_filepath}...")
    batch_size = 2000
    card_rows = []
    alias_rows = []
    total_cards = 0
    total_aliases = 0

    for raw in iterate_cards(json_filepath):
        name = raw.get("name", "").strip()
        if not name:
            continue

        normalized, aliases = normalize_card_entry(raw, fetch_date)
        card_data_json = json.dumps(normalized, ensure_ascii=False)

        card_rows.append((
            name,
            normalized["mana_cost"],
            normalized["cmc"],
            normalized["type_line"],
            normalized["oracle_text"],
            json.dumps(normalized["colors"]),
            json.dumps(normalized["color_identity"]),
            json.dumps(normalized["keywords"]),
            normalized["legal_commander"],
            normalized["edhrec_rank"],
            normalized["prices_usd"],
            normalized.get("prices_usd_foil"),
            raw.get("layout", "normal"),
            fetch_date,
            card_data_json,
        ))

        for alias in aliases:
            alias_rows.append((alias, name))

        if len(card_rows) >= batch_size:
            cur.executemany("""
                INSERT OR REPLACE INTO cards (
                    name, mana_cost, cmc, type_line, oracle_text, colors,
                    color_identity, keywords, legal_commander, edhrec_rank,
                    prices_usd, prices_usd_foil, layout, fetched_at, data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, card_rows)
            cur.executemany("""
                INSERT OR IGNORE INTO card_aliases (alias, canonical_name)
                VALUES (?, ?)
            """, alias_rows)
            total_cards += len(card_rows)
            total_aliases += len(alias_rows)
            card_rows = []
            alias_rows = []

    if card_rows:
        cur.executemany("""
            INSERT OR REPLACE INTO cards (
                name, mana_cost, cmc, type_line, oracle_text, colors,
                color_identity, keywords, legal_commander, edhrec_rank,
                prices_usd, prices_usd_foil, layout, fetched_at, data
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, card_rows)
        cur.executemany("""
            INSERT OR IGNORE INTO card_aliases (alias, canonical_name)
            VALUES (?, ?)
        """, alias_rows)
        total_cards += len(card_rows)
        total_aliases += len(alias_rows)

    # Populate FTS
    cur.execute("""
        INSERT INTO cards_fts (rowid, name, type_line, oracle_text)
        SELECT id, name, type_line, oracle_text FROM cards
    """)

    # Indices
    cur.execute("CREATE INDEX idx_cards_cmc ON cards(cmc)")
    cur.execute("CREATE INDEX idx_cards_legal ON cards(legal_commander)")
    cur.execute("CREATE INDEX idx_cards_edhrec ON cards(edhrec_rank)")

    conn.commit()
    cur.execute("PRAGMA optimize")
    conn.close()

    # Atomic move
    if db_path.exists():
        db_path.unlink()
    temp_db.rename(db_path)

    print(f"Successfully indexed {total_cards} cards and {total_aliases} aliases into {db_path}.")
    return total_cards




def print_stats(db_path: pathlib.Path):
    if not db_path.exists():
        print(f"Database {db_path} does not exist.")
        return

    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM cards")
    total_cards = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM card_aliases")
    total_aliases = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM cards WHERE legal_commander = 'legal'")
    commander_legal = cur.fetchone()[0]

    cur.execute("SELECT fetched_at FROM cards LIMIT 1")
    fetch_date = cur.fetchone()
    fetch_date_str = fetch_date[0] if fetch_date else "unknown"

    db_size_mb = db_path.stat().st_size / (1024 * 1024)
    print("\n--- Scryfall Local Cache Statistics ---")
    print(f"Database File:    {db_path.resolve()}")
    print(f"Database Size:    {db_size_mb:.2f} MB")
    print(f"Total Cards:      {total_cards:,}")
    print(f"Total Aliases:    {total_aliases:,}")
    print(f"Commander Legal:  {commander_legal:,}")
    print(f"Last Synced:      {fetch_date_str}")
    print("---------------------------------------\n")
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Sync Scryfall Bulk Data to Local SQLite Cache")
    parser.add_argument("--db-path", type=pathlib.Path, default=DEFAULT_DB_PATH, help="Destination SQLite database")
    parser.add_argument("--raw-path", type=pathlib.Path, default=DEFAULT_RAW_PATH, help="Path for raw bulk JSON")
    parser.add_argument("--input", type=pathlib.Path, help="Use existing local JSON/JSONL file instead of downloading")
    parser.add_argument("--keep-raw", action="store_true", help="Retain raw file after indexing")
    parser.add_argument("--query", type=str, help="Look up a card by name from the local database")
    parser.add_argument("--search", type=str, help="Search cards using full-text search (FTS5)")
    parser.add_argument("--stats", action="store_true", help="Display cache statistics")

    args = parser.parse_args()

    if args.stats:
        print_stats(args.db_path)
        return

    if args.query:
        from scryfall_cache import ScryfallDatabase
        db = ScryfallDatabase(args.db_path)
        res = db.get_card(args.query)
        if res:
            print(json.dumps(res, indent=2))
        else:
            print(f"Card not found: {args.query}", file=sys.stderr)
            sys.exit(1)
        return

    if args.search:
        from scryfall_cache import ScryfallDatabase
        db = ScryfallDatabase(args.db_path)
        results = db.search_fts(args.search, limit=10)
        print(f"Found {len(results)} matches for '{args.search}':")
        for r in results:
            print(f"- {r.get('type_line')}: {r.get('mana_cost', '')} (CMC {r.get('cmc')})")
            print(f"  {r.get('oracle_text', '').replace(chr(10), ' ')[:100]}...\n")
        return

    # Ingestion flow
    raw_path = args.raw_path
    if args.input:
        raw_path = args.input
        if not raw_path.exists():
            print(f"Input file not found: {raw_path}", file=sys.stderr)
            sys.exit(1)
    else:
        download_url, meta = get_bulk_download_url()
        if download_url.endswith(".gz") and not str(raw_path).endswith(".gz"):
            raw_path = raw_path.with_name(raw_path.name + ".jsonl.gz")
        download_stream(download_url, raw_path)

    build_sqlite_cache(raw_path, args.db_path)

    if not args.keep_raw and not args.input and raw_path.exists():
        print(f"Cleaning up temporary raw bulk file: {raw_path}")
        raw_path.unlink()

    print_stats(args.db_path)


if __name__ == "__main__":
    main()
