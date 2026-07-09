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

from decklist_common import REPO_ROOT, build_markdown, classify_type, write_decklist

COLOR_LETTERS = {"White": "W", "Blue": "U", "Black": "B", "Red": "R", "Green": "G"}


def deck_id_from_arg(arg: str) -> str:
    match = re.search(r"/decks/(\d+)", arg)
    return match.group(1) if match else arg


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


def extract_one(deck_id: str, source_url: str):
    deck = fetch_deck(deck_id)
    if deck.get("deckFormat") != 3:
        raise ValueError(f"deck {deck_id} ({deck['name']!r}) is not a Commander deck (deckFormat != 3)")

    cards = mainboard_cards(deck)
    commanders = [c for c in cards if "Commander" in (c.get("categories") or [])]
    commander_ids = {c["id"] for c in commanders}
    others = [c for c in cards if c["id"] not in commander_ids]

    commander_names = [c["card"]["oracleCard"]["name"] for c in commanders]
    colors = sorted(
        {COLOR_LETTERS[col] for c in commanders
         for col in c["card"]["oracleCard"]["colorIdentity"]},
        key="WUBRG".index,
    )

    norm_cards = [
        {
            "name": c["card"]["oracleCard"]["name"],
            "qty": c["quantity"],
            "type": classify_type(c["card"]["oracleCard"].get("types", [])),
            "foil": c.get("modifier") == "Foil",
        }
        for c in others
    ]

    markdown = build_markdown(
        title=deck["name"],
        owner=deck["owner"]["username"],
        commander_names=commander_names,
        colors=colors,
        cards=norm_cards,
        bracket=deck.get("edhBracket"),
        source_url=source_url,
        updated=deck["updatedAt"][:10],
        source_label="Archidekt",
    )
    return write_decklist(deck["owner"]["username"], deck["name"], markdown)


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
