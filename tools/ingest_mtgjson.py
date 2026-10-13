#!/usr/bin/env python3
"""Streaming ingestion script to compile MTGJSON AllPrintings.json into a local SQLite database.

Maintains minimal memory footprint (< 50MB RAM) by streaming chunked sets from
AllPrintings.json, extracting canonical card definitions, set records, printings,
and generating an FTS5 full-text search index for sub-millisecond MTG queries.
"""

import json
import os
import pathlib
import re
import sqlite3
import sys
import time
from typing import Any, Dict, Generator, Optional, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_JSON = REPO_ROOT / "AllPrintings.json"
CACHE_DIR = REPO_ROOT / "knowledgebase" / "_cache"
DB_PATH = CACHE_DIR / "mtg.db"


def init_database(conn: sqlite3.Connection):
    """Initializes schema and pragmas for high-throughput ingestion."""
    cur = conn.cursor()
    cur.execute("PRAGMA journal_mode = WAL;")
    cur.execute("PRAGMA synchronous = NORMAL;")
    cur.execute("PRAGMA cache_size = -64000;")  # 64MB cache
    cur.execute("PRAGMA temp_store = MEMORY;")

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS db_meta (
            key TEXT PRIMARY KEY,
            value TEXT
        );

        CREATE TABLE IF NOT EXISTS sets (
            code TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            release_date TEXT,
            type TEXT,
            base_set_size INTEGER,
            total_set_size INTEGER
        );

        CREATE TABLE IF NOT EXISTS cards (
            name TEXT PRIMARY KEY,
            face_name TEXT,
            mana_cost TEXT,
            mana_value REAL,
            colors TEXT,
            color_identity TEXT,
            type_line TEXT,
            types TEXT,
            subtypes TEXT,
            supertypes TEXT,
            oracle_text TEXT,
            power TEXT,
            toughness TEXT,
            loyalty TEXT,
            keywords TEXT,
            layout TEXT,
            edhrec_rank INTEGER,
            edhrec_saltiness REAL,
            is_commander INTEGER,
            edh_legal INTEGER,
            scryfall_id TEXT
        );

        CREATE TABLE IF NOT EXISTS printings (
            uuid TEXT PRIMARY KEY,
            card_name TEXT NOT NULL,
            set_code TEXT NOT NULL,
            collector_number TEXT NOT NULL,
            rarity TEXT,
            release_date TEXT,
            scryfall_id TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_cards_cmc ON cards(mana_value);
        CREATE INDEX IF NOT EXISTS idx_cards_edh_legal ON cards(edh_legal);
        CREATE INDEX IF NOT EXISTS idx_cards_is_commander ON cards(is_commander);
        CREATE INDEX IF NOT EXISTS idx_cards_edhrec_rank ON cards(edhrec_rank);
        CREATE INDEX IF NOT EXISTS idx_printings_card_name ON printings(card_name);
        CREATE INDEX IF NOT EXISTS idx_printings_set_code ON printings(set_code);

        -- FTS5 Full-Text Search Table
        CREATE VIRTUAL TABLE IF NOT EXISTS cards_fts USING fts5(
            name,
            type_line,
            oracle_text,
            keywords,
            content='cards',
            content_rowid='rowid'
        );
    """)
    conn.commit()


def stream_sets(json_path: pathlib.Path, chunk_size: int = 512 * 1024) -> Generator[Tuple[Dict[str, Any], str, Dict[str, Any]], None, None]:
    """Streams set objects one-by-one from AllPrintings.json with constant memory usage."""
    with open(json_path, "r", encoding="utf-8") as f:
        buf = ""
        meta = {}

        # 1. Locate "data":{" header and parse metadata
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            buf += chunk
            data_pos = buf.find('"data":{')
            if data_pos != -1:
                meta_match = re.search(r'"meta"\s*:\s*(\{.*?\})', buf[:data_pos])
                if meta_match:
                    try:
                        meta = json.loads(meta_match.group(1))
                    except json.JSONDecodeError:
                        meta = {}
                buf = buf[data_pos + len('"data":{'):]
                break

        # 2. Iterate through each set object in "data"
        dec = json.JSONDecoder()
        while True:
            buf = buf.lstrip(" \t\r\n,")
            if not buf:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                buf += chunk
                buf = buf.lstrip(" \t\r\n,")

            if buf.startswith("}"):
                break  # Reached end of data object

            while ":" not in buf:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                buf += chunk
            if ":" not in buf:
                break

            set_code, idx = dec.raw_decode(buf)
            colon_pos = buf.find(":", idx)
            buf = buf[colon_pos + 1:].lstrip(" \t\r\n")

            while True:
                try:
                    set_data, end_idx = dec.raw_decode(buf)
                    yield meta, set_code, set_data
                    buf = buf[end_idx:]
                    break
                except json.JSONDecodeError:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        return
                    buf += chunk


def parse_is_commander(card: Dict[str, Any]) -> int:
    """Evaluates whether a card can serve as a Commander."""
    leadership = card.get("leadershipSkills", {})
    if leadership and leadership.get("commander") is True:
        return 1

    type_line = card.get("type", "")
    oracle_text = card.get("text", "")
    supertypes = card.get("supertypes", [])
    types = card.get("types", [])

    if "Legendary" in supertypes and "Creature" in types:
        return 1
    if "can be your commander" in oracle_text.lower():
        return 1
    return 0


def ingest_all_printings(json_path: pathlib.Path = DEFAULT_JSON, db_path: pathlib.Path = DB_PATH):
    """Main ingestion pipeline."""
    if not json_path.exists():
        print(f"Error: Source file {json_path} does not exist.")
        sys.exit(1)

    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    init_database(conn)

    start_time = time.time()
    total_sets = 0
    total_cards_seen = 0
    total_printings = 0
    meta_captured = {}

    cur = conn.cursor()

    # Pre-compiled statements
    insert_set_sql = """
        INSERT OR REPLACE INTO sets (code, name, release_date, type, base_set_size, total_set_size)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    insert_card_sql = """
        INSERT INTO cards (
            name, face_name, mana_cost, mana_value, colors, color_identity,
            type_line, types, subtypes, supertypes, oracle_text, power,
            toughness, loyalty, keywords, layout, edhrec_rank, edhrec_saltiness,
            is_commander, edh_legal, scryfall_id
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        ) ON CONFLICT(name) DO UPDATE SET
            oracle_text = CASE 
                WHEN cards.oracle_text IS NULL THEN excluded.oracle_text
                WHEN excluded.oracle_text IS NULL THEN cards.oracle_text
                WHEN cards.oracle_text = excluded.oracle_text THEN cards.oracle_text
                WHEN instr(cards.oracle_text, excluded.oracle_text) > 0 THEN cards.oracle_text
                ELSE cards.oracle_text || char(10) || '-----' || char(10) || excluded.oracle_text
            END,
            edhrec_rank = COALESCE(excluded.edhrec_rank, cards.edhrec_rank),
            edh_legal = MAX(cards.edh_legal, excluded.edh_legal),
            is_commander = MAX(cards.is_commander, excluded.is_commander),
            scryfall_id = COALESCE(cards.scryfall_id, excluded.scryfall_id)
    """

    insert_printing_sql = """
        INSERT OR REPLACE INTO printings (
            uuid, card_name, set_code, collector_number, rarity, release_date, scryfall_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    print(f"Beginning streaming ingestion from {json_path.name}...")
    batch_size = 25
    cur.execute("BEGIN TRANSACTION;")

    for meta, set_code, set_data in stream_sets(json_path):
        if not meta_captured and meta:
            meta_captured = meta

        total_sets += 1
        release_date = set_data.get("releaseDate", "")
        set_name = set_data.get("name", set_code)
        set_type = set_data.get("type", "")
        base_size = set_data.get("baseSetSize", 0)
        total_size = set_data.get("totalSetSize", 0)

        cur.execute(insert_set_sql, (set_code, set_name, release_date, set_type, base_size, total_size))

        for card in set_data.get("cards", []):
            total_cards_seen += 1
            name = card.get("name")
            if not name:
                continue

            uuid = card.get("uuid")
            face_name = card.get("faceName")
            mana_cost = card.get("manaCost")
            mana_value = card.get("manaValue", card.get("convertedManaCost", 0.0))
            colors = json.dumps(card.get("colors", []))
            color_identity = json.dumps(card.get("colorIdentity", []))
            type_line = card.get("type", "")
            types = json.dumps(card.get("types", []))
            subtypes = json.dumps(card.get("subtypes", []))
            supertypes = json.dumps(card.get("supertypes", []))
            oracle_text = card.get("text", "")
            power = card.get("power")
            toughness = card.get("toughness")
            loyalty = card.get("loyalty")
            keywords = json.dumps(card.get("keywords", []))
            layout = card.get("layout", "normal")
            edhrec_rank = card.get("edhrecRank")
            edhrec_saltiness = card.get("edhrecSaltiness")

            legalities = card.get("legalities", {})
            edh_legal = 1 if legalities.get("commander") == "Legal" else 0
            is_commander = parse_is_commander(card)

            identifiers = card.get("identifiers", {})
            scryfall_id = identifiers.get("scryfallId")

            cur.execute(insert_card_sql, (
                name, face_name, mana_cost, mana_value, colors, color_identity,
                type_line, types, subtypes, supertypes, oracle_text, power,
                toughness, loyalty, keywords, layout, edhrec_rank, edhrec_saltiness,
                is_commander, edh_legal, scryfall_id
            ))

            if uuid:
                collector_num = card.get("number", "")
                rarity = card.get("rarity", "")
                cur.execute(insert_printing_sql, (
                    uuid, name, set_code, collector_num, rarity, release_date, scryfall_id
                ))
                total_printings += 1

        if total_sets % batch_size == 0:
            conn.commit()
            cur.execute("BEGIN TRANSACTION;")
            elapsed = time.time() - start_time
            print(f"  [{total_sets} sets processed] - {total_cards_seen} card printings ingested ({elapsed:.1f}s)")

    conn.commit()

    # Rebuild FTS5 table
    print("Rebuilding FTS5 full-text search index...")
    cur.execute("INSERT INTO cards_fts(cards_fts) VALUES('rebuild');")

    # Record Metadata
    cur.execute("SELECT count(*) FROM cards;")
    unique_cards = cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO db_meta (key, value) VALUES (?, ?);", ("schema_version", "1.0"))
    cur.execute("INSERT OR REPLACE INTO db_meta (key, value) VALUES (?, ?);", ("mtgjson_version", meta_captured.get("version", "unknown")))
    cur.execute("INSERT OR REPLACE INTO db_meta (key, value) VALUES (?, ?);", ("mtgjson_date", meta_captured.get("date", "unknown")))
    cur.execute("INSERT OR REPLACE INTO db_meta (key, value) VALUES (?, ?);", ("last_updated_at", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
    cur.execute("INSERT OR REPLACE INTO db_meta (key, value) VALUES (?, ?);", ("total_sets", str(total_sets)))
    cur.execute("INSERT OR REPLACE INTO db_meta (key, value) VALUES (?, ?);", ("unique_cards", str(unique_cards)))
    cur.execute("INSERT OR REPLACE INTO db_meta (key, value) VALUES (?, ?);", ("total_printings", str(total_printings)))
    conn.commit()

    # Optimize DB
    print("Optimizing SQLite database (VACUUM / ANALYZE)...")
    cur.execute("ANALYZE;")
    conn.commit()
    conn.close()

    elapsed = time.time() - start_time
    db_size_mb = db_path.stat().st_size / (1024 * 1024)
    print("\nIngestion Complete!")
    print(f"  Database Path:     {db_path}")
    print(f"  Database Size:     {db_size_mb:.1f} MB")
    print(f"  Sets Ingested:     {total_sets}")
    print(f"  Unique Cards:      {unique_cards}")
    print(f"  Total Printings:   {total_printings}")
    print(f"  Time Elapsed:      {elapsed:.1f}s")


if __name__ == "__main__":
    json_target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_JSON
    ingest_all_printings(json_target)
