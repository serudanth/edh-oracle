"""Shared helpers for decklist extraction scripts (archidekt_extract.py,
moxfield_extract.py, ...). Each source module normalizes its own API
response into plain dicts and hands off to build_markdown/write_decklist.
"""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PODLIST_ROOT = REPO_ROOT / "knowledgebase" / "podlist"

TYPE_PRIORITY = [
    "Creature", "Planeswalker", "Battle", "Instant", "Sorcery",
    "Artifact", "Enchantment", "Land",
]


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-")


def classify_type(type_words) -> str:
    """type_words: iterable of type strings from a card's front face."""
    type_words = list(type_words)
    for t in TYPE_PRIORITY:
        if t in type_words:
            return t
    return type_words[0] if type_words else "Other"


HANDLE_TO_ALIAS = {
    "fowlplays": "charles",
    "lto888": "lance",
    "reimaru": "chad",
    "xanoh": "donny",
    "mjsnoozer": "mj",
    "j-py": "julius",
}

ALIAS_TO_HANDLE = {v: k for k, v in HANDLE_TO_ALIAS.items()}


def resolve_owner(username_or_alias: str) -> str:
    """Resolves an Archidekt/Moxfield username to its canonical pod alias primary key."""
    key = username_or_alias.lower().strip()
    return HANDLE_TO_ALIAS.get(key, key)


def resolve_handle(username_or_alias: str) -> str:
    """Resolves an alias to its known remote platform handle, if mapped."""
    key = username_or_alias.lower().strip()
    return ALIAS_TO_HANDLE.get(key, key)


def build_markdown(
    *, title, owner, commander_names, colors, cards, bracket, source_url, updated, source_label,
) -> str:
    """cards: list of {"name", "qty", "type", "foil"} dicts, commanders excluded."""
    canonical_owner = resolve_owner(owner)
    grouped: dict[str, list[dict]] = {}
    for c in cards:
        grouped.setdefault(c["type"], []).append(c)

    ordered_types = [t for t in TYPE_PRIORITY if t in grouped]
    ordered_types += [t for t in grouped if t not in TYPE_PRIORITY]

    commander_str = ", ".join(commander_names)

    fm = [
        "---",
        "type: decklist",
        f'title: "{title}"',
        f"owner: {canonical_owner}",
    ]
    if owner.lower().strip() != canonical_owner:
        fm.append(f"handle: {owner}")

    fm.extend([
        f'commander: "{commander_str}"',
        f"colors: [{', '.join(colors)}]",
        "power_level:",
        "tags: []",
        "related: []",
        f"last_updated: {updated}",
        f"source: {source_url}",
        "---",
        "",
    ])

    body = ["## Decklist", "", f"**Commander:** {commander_str}", ""]
    for t in ordered_types:
        entries = sorted(grouped[t], key=lambda c: c["name"])
        body.append(f"### {t} ({sum(c['qty'] for c in entries)})")
        for c in entries:
            foil = " *(foil)*" if c["foil"] else ""
            body.append(f"- {c['qty']}x {c['name']}{foil}")
        body.append("")

    body.append("## Notes")
    body.append("")
    if bracket is not None:
        body.append(f"- {source_label} bracket: {bracket}")
    body.append(f"- Imported from [{source_label}]({source_url})")
    body.append("")

    return "\n".join(fm + body)


def write_decklist(owner: str, deck_name: str, markdown: str) -> Path:
    canonical_owner = resolve_owner(owner)
    out_dir = PODLIST_ROOT / slugify(canonical_owner) / "decks"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slugify(deck_name)}.md"
    out_path.write_text(markdown, encoding="utf-8")
    return out_path
