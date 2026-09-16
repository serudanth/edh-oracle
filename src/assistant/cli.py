"""Simple CLI for interacting with the knowledgebase via src.assistant.ingest

Usage examples:
  python src/assistant/cli.py list
  python src/assistant/cli.py show <owner> <slug>
  python src/assistant/cli.py find-commander "Atraxa"
"""
import argparse
from pathlib import Path
import sys
import textwrap

# Ensure src/ is on sys.path when invoked directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from assistant import ingest


def cmd_list(args):
    for owner, slug, path in ingest.list_decklists():
        print(f"{owner}/{slug}")


def cmd_show(args):
    d = ingest.read_deck(args.owner, args.slug)
    if not d:
        print("Deck not found")
        return
    fm = d["frontmatter"]
    print("Frontmatter:")
    for k, v in fm.items():
        print(f"  {k}: {v}")
    print("\nContent preview:\n")
    print(textwrap.indent(d["content"][:1000], "  "))


def cmd_find(args):
    matches = ingest.find_decks_by_commander(args.commander)
    if not matches:
        print("No matches")
        return
    for m in matches:
        p = m["path"]
        print(f"{p.relative_to(Path(__file__).resolve().parents[2])}")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers()

    p_list = sub.add_parser("list")
    p_list.set_defaults(func=cmd_list)

    p_show = sub.add_parser("show")
    p_show.add_argument("owner")
    p_show.add_argument("slug")
    p_show.set_defaults(func=cmd_show)

    p_find = sub.add_parser("find-commander")
    p_find.add_argument("commander")
    p_find.set_defaults(func=cmd_find)

    args = p.parse_args()
    if not hasattr(args, "func"):
        p.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
