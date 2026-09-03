# EDH Oracle

## Purpose
A future Magic: The Gathering Commander (EDH) deckbuilding tool. Currently in the research and planning phase — no application code yet.

## What's here now
- `knowledgebase/podlist/` — one folder per pod member (mine and my playgroup's), each with a `profile.md` (deckbuilder tendencies) and a `decks/` folder of decklists, tracked as they're built or updated
- `knowledgebase/research/` — rules interactions, strategy notes, and design notes toward the eventual tool

## Status
Pre-code. See [CLAUDE.md](CLAUDE.md) for how this repo is organized while it's in planning.

Note: extractor scripts, helpers, and local analysis engine live in the tools/ directory (`tools/*_extract.py`, `tools/decklist_common.py`, `tools/external_analysis_extract.py`, `tools/deck_analyzer_engine.py`). Agent prompt specification is located at `tools/prompts/external_analysis_agent.md`. Automated analysis files are stored in `knowledgebase/podlist/<owner>/analysis/<deck-slug>.json`.

A unittest suite exists for extractors and engine (`tests/test_decklist_common.py`, `tests/test_external_analysis.py`, `tests/test_deck_analyzer_engine.py`). Run: `python -m unittest discover -s tests`

A placeholder assistant ingest module and CLI were added under src/assistant/ingest.py and src/assistant/cli.py — the ingest helpers read markdown frontmatter and provide simple queries for the future assistant.
