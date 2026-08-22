"""Simple knowledgebase ingestion helpers for the future assistant.

Provides small, dependency-free utilities to list and read decklist markdown
files under knowledgebase/podlist/<owner>/decks/ and parse their frontmatter
into a Python dict.
"""
from __future__ import annotations
import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
PODLIST_ROOT = REPO_ROOT / "knowledgebase" / "podlist"

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _parse_frontmatter(text: str) -> Dict[str, object]:
    m = _FRONTMATTER_RE.search(text)
    if not m:
        return {}
    block = m.group(1)
    data: Dict[str, object] = {}
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        # Try to interpret value as Python literal (lists, dicts, numbers)
        try:
            parsed = ast.literal_eval(val)
        except Exception:
            # Fallback to raw string, strip quotes if present
            parsed = val.strip('"')
        data[key] = parsed
    return data


def list_decklists() -> List[Tuple[str, str, Path]]:
    """Return list of (owner, slug, path) for every decklist file.

    Owner is the immediate folder name under knowledgebase/podlist.
    Slug is the filename without extension.
    """
    out: List[Tuple[str, str, Path]] = []
    if not PODLIST_ROOT.exists():
        return out
    for owner_dir in sorted(PODLIST_ROOT.iterdir()):
        decks_dir = owner_dir / "decks"
        if not decks_dir.is_dir():
            continue
        for md in sorted(decks_dir.glob("*.md")):
            out.append((owner_dir.name, md.stem, md))
    return out


def read_deck(owner: str, slug: str) -> Optional[Dict[str, object]]:
    """Read and return a dict with keys: path, frontmatter (dict), content (str).
    Returns None if not found.
    """
    path = PODLIST_ROOT / owner / "decks" / f"{slug}.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    fm = _parse_frontmatter(text)
    # Remove frontmatter block to get body
    body = _FRONTMATTER_RE.sub("", text, count=1)
    return {"path": path, "frontmatter": fm, "content": body}


def find_decks_by_commander(commander_name: str) -> List[Dict[str, object]]:
    """Case-insensitive search by commander frontmatter field.

    Returns list of read_deck() dicts for matches.
    """
    matches: List[Dict[str, object]] = []
    for owner, slug, path in list_decklists():
        d = read_deck(owner, slug)
        if not d:
            continue
        fm = d.get("frontmatter") or {}
        commander_field = fm.get("commander")
        if not commander_field:
            continue
        # commander_field can be a quoted string or comma-separated; normalize
        if isinstance(commander_field, str):
            s = commander_field.lower()
        else:
            s = str(commander_field).lower()
        if commander_name.lower() in s:
            matches.append(d)
    return matches
