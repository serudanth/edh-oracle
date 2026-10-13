#!/usr/bin/env python3
"""EDH Oracle Local Deck Analyzer & Metric Calculation Engine (CLI Orchestrator).

Executes deterministic curve calculations, 5-bracket format auditing, and strategic
inference across local markdown decklists in knowledgebase/podlist/.

Usage:
    python tools/deck_analyzer_engine.py --deck knowledgebase/podlist/charles/decks/the-sorcerer-of-eld.md
    python tools/deck_analyzer_engine.py --deck <path> --write-kb
    python tools/deck_analyzer_engine.py --owner charles --write-kb
    python tools/deck_analyzer_engine.py --all --write-kb
"""

import argparse
import json
import pathlib
import sys
from typing import Any, Dict

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

from analyzer import DeckAnalyzer
from analyzer.parsers.markdown import parse_deck_markdown


def analyze_deck(deck_info_or_dict: Any, cache: Any = None) -> Dict[str, Any]:
    """Legacy compatibility bridge for programmatic analyze_deck calls."""
    analyzer = DeckAnalyzer()
    if hasattr(deck_info_or_dict, "cards"):
        result = analyzer.analyze_deck(deck_info_or_dict)
    elif isinstance(deck_info_or_dict, dict) and "filepath" in deck_info_or_dict and deck_info_or_dict["filepath"]:
        result = analyzer.analyze_file(deck_info_or_dict["filepath"])
    else:
        # Fallback if raw dict passed
        from analyzer.models import CardEntry, DeckInfo
        cards = [CardEntry(name=c["name"], qty=c.get("qty", 1), user_category=c.get("user_category", "Other")) for c in deck_info_or_dict.get("cards", [])]
        deck = DeckInfo(
            deck_name=deck_info_or_dict.get("deck_name", "Unknown"),
            owner=deck_info_or_dict.get("owner", "unknown"),
            commander=deck_info_or_dict.get("commander", "Unknown Commander"),
            source_url=deck_info_or_dict.get("source_url", ""),
            cards=cards
        )
        result = analyzer.analyze_deck(deck)
    return analyzer.format_json(result)


def write_analysis_to_kb(deck_filepath: pathlib.Path, analysis_data: Dict[str, Any]) -> pathlib.Path:
    """Writes analysis output JSON to knowledgebase/podlist/<owner>/analysis/<deck-slug>.json."""
    owner = deck_filepath.parent.parent.name
    deck_slug = deck_filepath.stem
    analysis_dir = REPO_ROOT / "knowledgebase" / "podlist" / owner / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)
    out_file = analysis_dir / f"{deck_slug}.json"

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(analysis_data, f, indent=2)

    return out_file


def main():
    parser = argparse.ArgumentParser(description="EDH Oracle Local Deck Analyzer & Metric Engine (v2.0 Modular)")
    parser.add_argument("--deck", help="Path to deck markdown file")
    parser.add_argument("--owner", help="Owner username to analyze all their decks")
    parser.add_argument("--all", action="store_true", help="Analyze all decks in knowledgebase/podlist/")
    parser.add_argument("--write-kb", action="store_true", help="Save analysis JSON into knowledgebase/podlist/<owner>/analysis/")
    parser.add_argument("--llm", action="store_true", help="Enable deep LLM strategic inference pass")

    args = parser.parse_args()

    analyzer = DeckAnalyzer()
    podlist_dir = REPO_ROOT / "knowledgebase" / "podlist"

    deck_files = []
    if args.deck:
        deck_files.append(pathlib.Path(args.deck).resolve())
    elif args.owner:
        from decklist_common import resolve_owner
        canonical_owner = resolve_owner(args.owner)
        owner_dir = podlist_dir / canonical_owner / "decks"
        if owner_dir.exists():
            deck_files.extend(owner_dir.glob("*.md"))
        else:
            print(f"Owner directory {owner_dir} not found.")
            sys.exit(1)
    elif args.all:
        deck_files.extend(podlist_dir.glob("*/decks/*.md"))

    if not deck_files:
        print("No deck files found to analyze.")
        sys.exit(1)

    for df in deck_files:
        try:
            deck_info = parse_deck_markdown(df)
            if deck_info.status == "stub" or len(deck_info.cards) < 10:
                print(f"Skipping stub decklist: {df.name}")
                continue

            result = analyzer.analyze_deck(deck_info, enable_llm=args.llm)
            analysis = analyzer.format_json(result)

            if args.write_kb:
                out_path = write_analysis_to_kb(df, analysis)
                print(f"Wrote analysis to {out_path.relative_to(REPO_ROOT)}")
            else:
                print(json.dumps(analysis, indent=2))
        except Exception as e:
            print(f"Error analyzing {df}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
