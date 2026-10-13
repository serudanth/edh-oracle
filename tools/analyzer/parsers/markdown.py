"""Markdown decklist parser for EDH Oracle knowledgebase deck files."""

import pathlib
import re
from typing import List
from ..models import CardEntry, DeckInfo


def clean_card_name(raw_name: str) -> str:
    """Strips annotations, set codes, and markdown artifacts from card names."""
    name = raw_name.strip()
    # Strip trailing annotations like *(ManaBox — Bulk)*, *(foil)*, etc.
    name = re.sub(r"\s+\*?\([^*]+\)\*?$", "", name).strip()
    name = re.sub(r"\s+\*.*$", "", name).strip()
    return name


def parse_deck_markdown(filepath: pathlib.Path) -> DeckInfo:
    """Parses deck markdown file returning typed DeckInfo."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter = {}
    fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                frontmatter[k.strip()] = v.strip().strip('"').strip("'")

    owner = frontmatter.get("owner", filepath.parent.parent.name if filepath.parent.name == "decks" else "unknown")
    commander = frontmatter.get("commander", "Unknown Commander")
    deck_name = frontmatter.get("title", filepath.stem.replace("-", " ").title())
    source_url = frontmatter.get("source", "")
    status = frontmatter.get("status", "complete")

    # Parse card lines & category headers
    cards: List[CardEntry] = []
    current_category = "Other"

    for line in content.splitlines():
        line_s = line.strip()
        if line_s.startswith("###"):
            # Header like ### Creature (30) or ### Instant
            cat_name = line_s.lstrip("#").strip()
            cat_name = re.sub(r"\s*\(\d+\)$", "", cat_name).strip()
            current_category = cat_name
        elif line_s.startswith("- ") or line_s.startswith("* "):
            card_match = re.search(r"[-*]\s*(\d+)x?\s+(.+)$", line_s)
            if card_match:
                qty = int(card_match.group(1))
                raw_name = card_match.group(2).strip()
                name = clean_card_name(raw_name)
                cards.append(CardEntry(name=name, qty=qty, user_category=current_category))

    return DeckInfo(
        deck_name=deck_name,
        owner=owner,
        commander=commander,
        source_url=source_url,
        status=status,
        cards=cards,
        filepath=filepath,
    )
