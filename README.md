# EDH Oracle

## Purpose
A future Magic: The Gathering Commander (EDH) deckbuilding tool. Currently in the research and planning phase — no application code yet.

## What's here now
- `knowledgebase/decklists/` — decklists (mine and my playgroup's), tracked as they're built or updated
- `knowledgebase/research/` — rules interactions, strategy notes, and design notes toward the eventual tool

## Status
Pre-code. See [CLAUDE.md](CLAUDE.md) for how this repo is organized while it's in planning.

Note: extractor scripts and helpers live in the tools/ directory (tools/*_extract.py, tools/decklist_common.py).

A small test suite exists for core helpers (tests/test_decklist_common.py). Run: python -m unittest

A placeholder assistant ingest module and CLI were added under src/assistant/ingest.py and src/assistant/cli.py — the ingest helpers read markdown frontmatter and provide simple queries for the future assistant.
