#!/usr/bin/env python3
"""MTG Local Database CLI & Query Engine (mtg.db).

Provides sub-millisecond MTG card lookups, Commander-aware color identity filtering,
FTS5 full-text Oracle search, detailed card views, and delta update synchronization
against MTGJSON and Scryfall.

Usage:
    python tools/mtg_db.py --stats
    python tools/mtg_db.py --card "Emet-Selch, Unsundered // Hades, Sorcerer of Eld"
    python tools/mtg_db.py --search --ci UB --type Creature --text "graveyard" --cmc-min 6
    python tools/mtg_db.py --search --commander --ci UB --limit 10
    python tools/mtg_db.py --update
"""

import argparse
import datetime
import json
import pathlib
import sqlite3
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Set, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DB_PATH = REPO_ROOT / "knowledgebase" / "_cache" / "mtg.db"


def get_connection(db_path: pathlib.Path = DB_PATH) -> sqlite3.Connection:
    if not db_path.exists():
        print(f"Error: Database {db_path} does not exist. Run 'python tools/ingest_mtgjson.py' first.")
        sys.exit(1)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------------------------------------------------------
# Python API (for programmatic use by analyzer engine and agents)
# -------------------------------------------------------------------------

def get_card(name: str, db_path: pathlib.Path = DB_PATH) -> Optional[Dict[str, Any]]:
    """Fetches a canonical card dictionary by name (exact or front face)."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM cards WHERE name = ? OR face_name = ?", (name, name))
    row = cur.fetchone()
    if not row:
        # Try case-insensitive lookup
        cur.execute("SELECT * FROM cards WHERE LOWER(name) = LOWER(?) OR LOWER(face_name) = LOWER(?)", (name, name))
        row = cur.fetchone()
    conn.close()
    if row:
        d = dict(row)
        for k in ["colors", "color_identity", "types", "subtypes", "supertypes", "keywords"]:
            if d.get(k):
                d[k] = json.loads(d[k])
        return d
    return None


def search_cards(
    *,
    name: Optional[str] = None,
    set_code: Optional[str] = None,
    color_identity: Optional[str] = None,
    exact_ci: bool = False,
    type_line: Optional[str] = None,
    oracle_text: Optional[str] = None,
    cmc: Optional[float] = None,
    cmc_min: Optional[float] = None,
    cmc_max: Optional[float] = None,
    is_commander: Optional[bool] = None,
    edh_legal: bool = True,
    sort_by: str = "edhrec_rank",
    limit: int = 25,
    db_path: pathlib.Path = DB_PATH,
) -> List[Dict[str, Any]]:
    """Performs structured MTG search with Commander color identity and FTS text indexing."""
    conn = get_connection(db_path)
    cur = conn.cursor()

    conditions = []
    params: List[Any] = []

    if edh_legal:
        conditions.append("cards.edh_legal = 1")

    if is_commander is not None:
        conditions.append("cards.is_commander = ?" if is_commander else "cards.is_commander = 0")
        if is_commander:
            params.append(1)

    if name:
        conditions.append("cards.name LIKE ?")
        params.append(f"%{name}%")

    if type_line:
        conditions.append("cards.type_line LIKE ?")
        params.append(f"%{type_line}%")

    if cmc is not None:
        conditions.append("cards.mana_value = ?")
        params.append(cmc)
    if cmc_min is not None:
        conditions.append("cards.mana_value >= ?")
        params.append(cmc_min)
    if cmc_max is not None:
        conditions.append("cards.mana_value <= ?")
        params.append(cmc_max)

    fts_join = ""
    if oracle_text:
        # Use SQLite FTS5 table
        fts_join = "JOIN cards_fts ON cards.rowid = cards_fts.rowid"
        if '"' in oracle_text:
            fts_query = oracle_text
        else:
            tokens = oracle_text.strip().split()
            fts_query = " AND ".join(tokens)
        conditions.append('cards_fts.oracle_text MATCH ?')
        params.append(fts_query)

    # Color Identity Filtering (Commander Rules)
    if color_identity is not None:
        allowed = set(color_identity.upper().replace("{", "").replace("}", ""))
        all_colors = {"W", "U", "B", "R", "G"}
        disallowed = all_colors - allowed

        if exact_ci:
            for c in allowed:
                conditions.append("cards.color_identity LIKE ?")
                params.append(f'%"{c}"%')
            for c in disallowed:
                conditions.append("cards.color_identity NOT LIKE ?")
                params.append(f'%"{c}"%')
        else:
            # Commander legal identity: identity must be a subset of allowed colors
            for c in disallowed:
                conditions.append("cards.color_identity NOT LIKE ?")
                params.append(f'%"{c}"%')

    printings_join = ""
    if set_code:
        printings_join = "JOIN printings ON cards.name = printings.card_name"
        set_list = [s.strip().upper() for s in set_code.split(",") if s.strip()]
        placeholders = ",".join("?" for _ in set_list)
        conditions.append(f"printings.set_code IN ({placeholders})")
        params.extend(set_list)

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

    sort_order = "cards.edhrec_rank ASC NULLS LAST"
    if sort_by == "cmc":
        sort_order = "cards.mana_value ASC, cards.name ASC"
    elif sort_by == "cmc_desc":
        sort_order = "cards.mana_value DESC, cards.name ASC"
    elif sort_by == "name":
        sort_order = "cards.name ASC"

    query = f"""
        SELECT DISTINCT cards.* FROM cards
        {fts_join}
        {printings_join}
        {where_clause}
        ORDER BY {sort_order}
        LIMIT ?
    """
    params.append(limit)

    cur.execute(query, params)
    results = []
    for row in cur.fetchall():
        d = dict(row)
        for k in ["colors", "color_identity", "types", "subtypes", "supertypes", "keywords"]:
            if d.get(k):
                try:
                    d[k] = json.loads(d[k])
                except Exception:
                    pass
        results.append(d)
    conn.close()
    return results


# -------------------------------------------------------------------------
# CLI Commands
# -------------------------------------------------------------------------

def show_stats(db_path: pathlib.Path = DB_PATH):
    """Displays local database health, metadata, and sizing."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT key, value FROM db_meta;")
    meta = dict(cur.fetchall())

    cur.execute("SELECT count(*) FROM sets;")
    sets_count = cur.fetchone()[0]

    cur.execute("SELECT count(*) FROM cards;")
    cards_count = cur.fetchone()[0]

    cur.execute("SELECT count(*) FROM cards WHERE edh_legal = 1;")
    edh_count = cur.fetchone()[0]

    cur.execute("SELECT count(*) FROM cards WHERE is_commander = 1;")
    commander_count = cur.fetchone()[0]

    cur.execute("SELECT count(*) FROM printings;")
    printings_count = cur.fetchone()[0]

    size_mb = db_path.stat().st_size / (1024 * 1024)
    conn.close()

    print("\n================ MTG LOCAL DATABASE STATS ================")
    print(f" Database File:     {db_path}")
    print(f" Size on Disk:      {size_mb:.2f} MB")
    print(f" Schema Version:    {meta.get('schema_version', '1.0')}")
    print(f" MTGJSON Version:   {meta.get('mtgjson_version', 'Unknown')}")
    print(f" MTGJSON Date:      {meta.get('mtgjson_date', 'Unknown')}")
    print(f" Last Updated:      {meta.get('last_updated_at', 'Unknown')}")
    print(f" Total Sets:        {sets_count:,}")
    print(f" Unique Cards:      {cards_count:,}")
    print(f" EDH Legal Cards:   {edh_count:,}")
    print(f" Eligible Cmdrs:    {commander_count:,}")
    print(f" Total Printings:   {printings_count:,}")
    print("==========================================================\n")


def show_card(name: str, db_path: pathlib.Path = DB_PATH):
    """Prints a detailed view of a card and its printings."""
    card = get_card(name, db_path)
    if not card:
        print(f"Card '{name}' not found in local database.")
        sys.exit(1)

    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT set_code, collector_number, rarity, release_date
        FROM printings
        WHERE card_name = ?
        ORDER BY release_date DESC
        LIMIT 10;
    """, (card["name"],))
    printings = cur.fetchall()
    conn.close()

    print("\n" + "=" * 60)
    print(f" {card['name']}  {card.get('mana_cost') or ''}")
    print(f" Type: {card.get('type_line', '')}")
    if card.get("power") is not None and card.get("toughness") is not None:
        print(f" P/T:  {card['power']}/{card['toughness']}")
    if card.get("loyalty"):
        print(f" Loyalty: {card['loyalty']}")
    print("-" * 60)
    if card.get("oracle_text"):
        print(card["oracle_text"])
    print("-" * 60)
    ci = "".join(card.get("color_identity", [])) or "Colorless"
    print(f" CMC: {card.get('mana_value')} | Color Identity: {ci} | EDH Rank: #{card.get('edhrec_rank') or 'N/A'}")
    legal_str = "Legal" if card.get("edh_legal") else "Banned/Not Legal"
    cmdr_str = "Yes" if card.get("is_commander") else "No"
    print(f" Commander Legal: {legal_str} | Can Be Commander: {cmdr_str}")

    if printings:
        print("\n Recent Printings:")
        for p in printings:
            print(f"   [{p['set_code']}] #{p['collector_number']} ({p['rarity'].capitalize()}) — {p['release_date']}")
    print("=" * 60 + "\n")


def run_delta_update(db_path: pathlib.Path = DB_PATH):
    """Checks MTGJSON and Scryfall for set/card deltas and updates the database."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT value FROM db_meta WHERE key = 'last_updated_at';")
    row = cur.fetchone()
    last_updated = row[0] if row else "2026-01-01T00:00:00Z"
    last_date = last_updated.split("T")[0]

    print(f"Checking for updates newer than {last_date}...")

    # Step 1: Check MTGJSON SetList.json
    setlist_url = "https://mtgjson.com/api/v5/SetList.json"
    req = urllib.request.Request(setlist_url, headers={"User-Agent": "EDH-Oracle/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sets_data = data.get("data", [])
    except Exception as e:
        print(f"Note: Could not reach MTGJSON SetList API ({e}). Falling back to Scryfall delta query.")
        sets_data = []

    new_sets = []
    if sets_data:
        cur.execute("SELECT code FROM sets;")
        existing_codes = {r[0] for r in cur.fetchall()}
        for s in sets_data:
            code = s.get("code")
            release_date = s.get("releaseDate", "")
            if code not in existing_codes and release_date >= last_date:
                new_sets.append(s)

    if new_sets:
        print(f"Found {len(new_sets)} new sets to ingest from MTGJSON:")
        for s in new_sets:
            code = s.get("code")
            name = s.get("name")
            print(f"  Downloading set: {code} ({name})...")
            set_url = f"https://mtgjson.com/api/v5/{code}.json"
            try:
                set_req = urllib.request.Request(set_url, headers={"User-Agent": "EDH-Oracle/1.0"})
                with urllib.request.urlopen(set_req, timeout=15) as set_resp:
                    set_full = json.loads(set_resp.read().decode("utf-8")).get("data", {})
                    # Ingest set
                    cur.execute("""
                        INSERT OR REPLACE INTO sets (code, name, release_date, type, base_set_size, total_set_size)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (code, name, s.get("releaseDate"), s.get("type"), s.get("baseSetSize"), s.get("totalSetSize")))

                    # Ingest cards
                    from tools.ingest_mtgjson import parse_is_commander
                    for card in set_full.get("cards", []):
                        name = card.get("name")
                        if not name:
                            continue
                        cur.execute("""
                            INSERT INTO cards (
                                name, face_name, mana_cost, mana_value, colors, color_identity,
                                type_line, types, subtypes, supertypes, oracle_text, power,
                                toughness, loyalty, keywords, layout, edhrec_rank, edhrec_saltiness,
                                is_commander, edh_legal, scryfall_id
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ON CONFLICT(name) DO UPDATE SET
                                oracle_text = COALESCE(excluded.oracle_text, cards.oracle_text),
                                edhrec_rank = COALESCE(excluded.edhrec_rank, cards.edhrec_rank),
                                edh_legal = excluded.edh_legal,
                                is_commander = excluded.is_commander
                        """, (
                            name, card.get("faceName"), card.get("manaCost"), card.get("manaValue", 0.0),
                            json.dumps(card.get("colors", [])), json.dumps(card.get("colorIdentity", [])),
                            card.get("type", ""), json.dumps(card.get("types", [])),
                            json.dumps(card.get("subtypes", [])), json.dumps(card.get("supertypes", [])),
                            card.get("text", ""), card.get("power"), card.get("toughness"),
                            card.get("loyalty"), json.dumps(card.get("keywords", [])),
                            card.get("layout", "normal"), card.get("edhrecRank"), card.get("edhrecSaltiness"),
                            parse_is_commander(card), 1 if card.get("legalities", {}).get("commander") == "Legal" else 0,
                            card.get("identifiers", {}).get("scryfallId")
                        ))
                    conn.commit()
            except Exception as e:
                print(f"  Warning: Failed to ingest set {code}: {e}")

    # Step 2: Query Scryfall Temporal Delta
    print(f"Querying Scryfall for card printings with date>={last_date}...")
    scryfall_url = f"https://api.scryfall.com/cards/search?q=date%3E%3D{last_date}"
    sf_req = urllib.request.Request(scryfall_url, headers={"User-Agent": "EDH-Oracle/1.0", "Accept": "application/json"})

    sf_count = 0
    try:
        with urllib.request.urlopen(sf_req, timeout=10) as sf_resp:
            sf_data = json.loads(sf_resp.read().decode("utf-8"))
            cards_list = sf_data.get("data", [])
            for c in cards_list:
                c_name = c.get("name")
                if not c_name:
                    continue
                cmc = c.get("cmc", 0.0)
                colors = json.dumps(c.get("colors", []))
                ci = json.dumps(c.get("color_identity", []))
                type_line = c.get("type_line", "")
                oracle_text = c.get("oracle_text", "")
                legalities = c.get("legalities", {})
                edh_legal = 1 if legalities.get("commander") == "legal" else 0
                is_cmdr = 1 if "Legendary" in type_line and "Creature" in type_line else 0
                scryfall_id = c.get("id")

                cur.execute("""
                    INSERT INTO cards (
                        name, mana_cost, mana_value, colors, color_identity,
                        type_line, oracle_text, power, toughness, loyalty,
                        keywords, layout, edhrec_rank, is_commander, edh_legal, scryfall_id
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(name) DO UPDATE SET
                        oracle_text = COALESCE(excluded.oracle_text, cards.oracle_text),
                        edh_legal = excluded.edh_legal,
                        is_commander = excluded.is_commander,
                        scryfall_id = excluded.scryfall_id
                """, (
                    c_name, c.get("mana_cost"), cmc, colors, ci,
                    type_line, oracle_text, c.get("power"), c.get("toughness"),
                    c.get("loyalty"), json.dumps(c.get("keywords", [])),
                    c.get("layout", "normal"), c.get("edhrec_rank"),
                    is_cmdr, edh_legal, scryfall_id
                ))
                sf_count += 1
            conn.commit()
            print(f"Ingested/updated {sf_count} recent cards from Scryfall.")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("No new cards found since last check.")
        else:
            print(f"Scryfall query returned HTTP {e.code}.")
    except Exception as e:
        print(f"Scryfall check note: {e}")

    # Update metadata
    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cur.execute("UPDATE db_meta SET value = ? WHERE key = 'last_updated_at';", (now_iso,))
    conn.commit()

    # Rebuild FTS
    cur.execute("INSERT INTO cards_fts(cards_fts) VALUES('rebuild');")
    conn.commit()
    conn.close()
    print("Delta synchronization finished successfully.")


# -------------------------------------------------------------------------
# Main CLI Dispatcher
# -------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="EDH Oracle MTG Local Database Engine")
    parser.add_argument("--stats", action="store_true", help="Display local database statistics and metadata")
    parser.add_argument("--card", "-c", type=str, help="Display detailed view of a card by name")
    parser.add_argument("--search", "-s", action="store_true", help="Search the card database")
    parser.add_argument("--name", "-n", type=str, help="Card name substring filter")
    parser.add_argument("--ci", "--color-identity", dest="color_identity", type=str, help="Allowed Commander Color Identity (e.g. UB, WUBRG)")
    parser.add_argument("--exact-ci", action="store_true", help="Exact color identity match")
    parser.add_argument("--type", "-t", type=str, help="Type line filter (e.g. Creature, Instant)")
    parser.add_argument("--text", "-q", type=str, help="Oracle text full-text search (FTS5)")
    parser.add_argument("--cmc", type=float, help="Exact CMC")
    parser.add_argument("--cmc-min", type=float, help="Minimum CMC")
    parser.add_argument("--cmc-max", type=float, help="Maximum CMC")
    parser.add_argument("--commander", action="store_true", help="Only show cards eligible as Commander")
    parser.add_argument("--set", "--sets", dest="sets", type=str, help="Filter by set code(s), comma-separated (e.g. FIN,FIC,FCA)")
    parser.add_argument("--sort", type=str, default="edhrec_rank", choices=["edhrec_rank", "cmc", "cmc_desc", "name"])
    parser.add_argument("--limit", type=int, default=100, help="Maximum results to return")
    parser.add_argument("--update", action="store_true", help="Check and apply delta updates from MTGJSON/Scryfall")

    args = parser.parse_args()

    if args.stats:
        show_stats()
    elif args.card:
        show_card(args.card)
    elif args.update:
        run_delta_update()
    elif args.search:
        results = search_cards(
            name=args.name,
            set_code=args.sets,
            color_identity=args.color_identity,
            exact_ci=args.exact_ci,
            type_line=args.type,
            oracle_text=args.text,
            cmc=args.cmc,
            cmc_min=args.cmc_min,
            cmc_max=args.cmc_max,
            is_commander=True if args.commander else None,
            sort_by=args.sort,
            limit=args.limit,
        )
        print(f"\nFound {len(results)} matching cards (showing up to {args.limit}):")
        print("-" * 80)
        for c in results:
            ci = "".join(c.get("color_identity", [])) or "C"
            cmc_str = f"CMC {c.get('mana_value', 0):.0f}"
            cost_str = c.get("mana_cost") or ""
            rank_str = f"#{c.get('edhrec_rank')}" if c.get("edhrec_rank") else "unranked"
            print(f"• {c['name']:<35} {cost_str:<10} | {ci:<4} | {cmc_str:<6} | {c.get('type_line', ''):<25} ({rank_str})")
        print("-" * 80 + "\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
