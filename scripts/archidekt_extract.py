#!/usr/bin/env python3
"""Fetch decklist(s) from Archidekt and write them into knowledgebase/decklists/.

Usage:
    python scripts/archidekt_extract.py <archidekt-url-or-deck-id>
    python scripts/archidekt_extract.py --user <archidekt-username>

Single-deck mode writes one file. --user mode extracts every deck the
Archidekt API returns for that username — since that endpoint is
unauthenticated, it only ever returns what's publicly visible on their
profile (folder placement is private account organization, not a public
signal, so it's ignored).

Writes to knowledgebase/decklists/<owner-username>/<deck-name-slug>.md,
following the knowledgebase/_template-decklist.md frontmatter.
"""
import argparse
import json
import re
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DECKLISTS_ROOT = REPO_ROOT / "knowledgebase" / "decklists"

COLOR_LETTERS = {"White": "W", "Blue": "U", "Black": "B", "Red": "R", "Green": "G"}
TYPE_PRIORITY = [
    "Creature", "Planeswalker", "Battle", "Instant", "Sorcery",
    "Artifact", "Enchantment", "Land",
]


def deck_id_from_arg(arg: str) -> str:
    match = re.search(r"/decks/(\d+)", arg)
    return match.group(1) if match else arg


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-")


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def fetch_deck(deck_id: str) -> dict:
    return fetch_json(f"https://archidekt.com/api/decks/{deck_id}/")


def fetch_user_decks(username: str) -> list[dict]:
    """All decks owned by username, across every folder. Handles pagination."""
    url = f"https://archidekt.com/api/decks/v3/?ownerUsername={username}"
    decks = []
    while url:
        page = fetch_json(url)
        decks.extend(page["results"])
        url = page.get("next")
    return decks


def mainboard_cards(deck: dict) -> list[dict]:
    # A card is mainboard only if every category it's tagged with is
    # includedInDeck (Archidekt uses categories for maybeboard/outbound too,
    # and a card can carry more than one category).
    included = {c["name"]: c["includedInDeck"] for c in deck["categories"]}
    def is_mainboard(card):
        cats = card.get("categories") or []
        return all(included.get(c, True) is not False for c in cats)
    return [c for c in deck["cards"] if is_mainboard(c)]


def primary_type(oracle_card: dict) -> str:
    types = oracle_card.get("types", [])
    for t in TYPE_PRIORITY:
        if t in types:
            return t
    return types[0] if types else "Other"


def format_entry(card: dict) -> str:
    name = card["card"]["oracleCard"]["name"]
    qty = card["quantity"]
    foil = " *(foil)*" if card.get("modifier") == "Foil" else ""
    return f"- {qty}x {name}{foil}"


def build_markdown(deck: dict, source_url: str) -> str:
    cards = mainboard_cards(deck)
    commanders = [c for c in cards if "Commander" in (c.get("categories") or [])]
    commander_ids = {c["id"] for c in commanders}
    others = [c for c in cards if c["id"] not in commander_ids]

    commander_names = ", ".join(c["card"]["oracleCard"]["name"] for c in commanders)
    colors = sorted(
        {COLOR_LETTERS[col] for c in commanders
         for col in c["card"]["oracleCard"]["colorIdentity"]},
        key="WUBRG".index,
    )

    grouped: dict[str, list[dict]] = {}
    for card in others:
        t = primary_type(card["card"]["oracleCard"])
        grouped.setdefault(t, []).append(card)

    owner = deck["owner"]["username"]
    title = deck["name"]
    updated = deck["updatedAt"][:10]
    bracket = deck.get("edhBracket")

    fm = [
        "---",
        "type: decklist",
        f'title: "{title}"',
        f"owner: {owner}",
        f'commander: "{commander_names}"',
        f"colors: [{', '.join(colors)}]",
        "power_level:",
        "tags: []",
        "related: []",
        f"last_updated: {updated}",
        f"source: {source_url}",
        "---",
        "",
    ]

    body = ["## Decklist", "", f"**Commander:** {commander_names}", ""]
    ordered_types = [t for t in TYPE_PRIORITY if t in grouped]
    ordered_types += [t for t in grouped if t not in TYPE_PRIORITY]
    for t in ordered_types:
        entries = sorted(grouped[t], key=lambda c: c["card"]["oracleCard"]["name"])
        body.append(f"### {t} ({sum(c['quantity'] for c in entries)})")
        body.extend(format_entry(c) for c in entries)
        body.append("")

    body.append("## Notes")
    body.append("")
    if bracket is not None:
        body.append(f"- Archidekt bracket: {bracket}")
    body.append(f"- Imported from [Archidekt]({source_url})")
    body.append("")

    return "\n".join(fm + body)


def extract_one(deck_id: str, source_url: str) -> Path:
    deck = fetch_deck(deck_id)
    if deck.get("deckFormat") != 3:
        raise ValueError(f"deck {deck_id} ({deck['name']!r}) is not a Commander deck (deckFormat != 3)")

    owner = deck["owner"]["username"]
    out_dir = DECKLISTS_ROOT / slugify(owner)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slugify(deck['name'])}.md"
    out_path.write_text(build_markdown(deck, source_url), encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("deck", nargs="?", help="Archidekt deck URL or numeric deck ID")
    group.add_argument("--user", help="Archidekt username; extracts all their public decks")
    args = parser.parse_args()

    if args.user:
        targets = fetch_user_decks(args.user)
        print(f"Found {len(targets)} public deck(s) for {args.user}")
        for summary in targets:
            deck_id = str(summary["id"])
            source_url = f"https://archidekt.com/decks/{deck_id}"
            try:
                out_path = extract_one(deck_id, source_url)
                print(f"Wrote {out_path.relative_to(REPO_ROOT)}")
            except ValueError as e:
                print(f"Skipped: {e}")
    else:
        deck_id = deck_id_from_arg(args.deck)
        source_url = args.deck if args.deck.startswith("http") else f"https://archidekt.com/decks/{deck_id}"
        out_path = extract_one(deck_id, source_url)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
