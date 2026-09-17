#!/usr/bin/env python3
"""Fetch decklist(s) from Moxfield and write them into knowledgebase/podlist/.

Usage:
    python tools/moxfield_extract.py <moxfield-url-or-deck-id>
    python tools/moxfield_extract.py --user <moxfield-username>

Single-deck mode writes one file. --user mode extracts every public deck
the given username has on Moxfield.

Moxfield has no official public API; this uses the same unauthenticated
endpoints (api2.moxfield.com) moxfield.com's own frontend calls; see
CLAUDE.md for the source used to confirm them.

Writes to knowledgebase/podlist/<owner-username>/decks/<deck-name-slug>.md,
following the knowledgebase/_template-decklist.md frontmatter.
"""
import argparse
import json
import re
import urllib.error
import urllib.request

from decklist_common import REPO_ROOT, build_markdown, classify_type, write_decklist, resolve_handle

API_BASE = "https://api2.moxfield.com"
HEADERS = {"Accept": "application/json", "User-Agent": "Mozilla/5.0"}


def deck_id_from_arg(arg: str) -> str:
    match = re.search(r"/decks/([^/?#]+)", arg)
    return match.group(1) if match else arg


def fetch_json(url: str) -> dict:
    """Direct fetch, falling back to the r.jina.ai reader proxy on a 403
    (some networks block api2.moxfield.com directly; see CLAUDE.md/SKILL.md)."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code != 403:
            raise
        proxied = urllib.request.Request(f"https://r.jina.ai/{url}")
        with urllib.request.urlopen(proxied) as resp:
            text = resp.read().decode("utf-8")
        _, _, body = text.partition("Markdown Content:\n")
        return json.loads(body.strip())


def fetch_deck(deck_id: str) -> dict:
    return fetch_json(f"{API_BASE}/v3/decks/all/{deck_id}")


def fetch_user_decks(username: str) -> list[dict]:
    """All public decks for username. Handles pagination."""
    decks = []
    page_number = 1
    while True:
        url = (
            f"{API_BASE}/v2/decks/search-sfw?authorUserNames={username}"
            f"&pageNumber={page_number}&pageSize=50&sortType=updated&sortDirection=descending"
        )
        page = fetch_json(url)
        decks.extend(page["data"])
        if page_number >= page["totalPages"]:
            break
        page_number += 1
    return decks


def card_type(card: dict) -> str:
    front_face = card["type_line"].split("//")[0].split("—")[0]
    return classify_type(front_face.split())


def extract_one(deck_id: str, source_url: str):
    deck = fetch_deck(deck_id)
    if deck.get("format") != "commander":
        raise ValueError(f"deck {deck_id} ({deck['name']!r}) is not a Commander deck (format != commander)")

    commander_entries = list(deck["boards"]["commanders"]["cards"].values())
    mainboard_entries = list(deck["boards"]["mainboard"]["cards"].values())

    commander_names = [c["card"]["name"] for c in commander_entries]
    colors = sorted(
        {col for c in commander_entries for col in c["card"]["color_identity"]},
        key="WUBRG".index,
    )

    norm_cards = [
        {
            "name": c["card"]["name"],
            "qty": c["quantity"],
            "type": card_type(c["card"]),
            "foil": c.get("isFoil", False),
        }
        for c in mainboard_entries
    ]

    markdown = build_markdown(
        title=deck["name"],
        owner=deck["createdByUser"]["userName"],
        commander_names=commander_names,
        colors=colors,
        cards=norm_cards,
        bracket=deck.get("bracket"),
        source_url=source_url,
        updated=deck["lastUpdatedAtUtc"][:10],
        source_label="Moxfield",
    )
    return write_decklist(deck["createdByUser"]["userName"], deck["name"], markdown)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("deck", nargs="?", help="Moxfield deck URL or public deck ID")
    group.add_argument("--user", help="Moxfield username; extracts all their public decks")
    args = parser.parse_args()

    if args.user:
        target_user = resolve_handle(args.user)
        targets = fetch_user_decks(target_user)
        print(f"Found {len(targets)} public deck(s) for {target_user}")
        for summary in targets:
            deck_id = summary["publicId"]
            source_url = summary["publicUrl"]
            try:
                out_path = extract_one(deck_id, source_url)
                print(f"Wrote {out_path.relative_to(REPO_ROOT)}")
            except ValueError as e:
                print(f"Skipped: {e}")
    else:
        deck_id = deck_id_from_arg(args.deck)
        source_url = args.deck if args.deck.startswith("http") else f"https://moxfield.com/decks/{deck_id}"
        out_path = extract_one(deck_id, source_url)
        print(f"Wrote {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
