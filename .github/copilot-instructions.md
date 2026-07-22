Repository: edh-oracle — Copilot session guidance

Purpose
- Primary goal: this repository is intended to become a Commander (EDH) deckbuilding assistant — the knowledgebase, extractors, and research workflows exist to support that assistant.
- Short: help future Copilot/Copilot CLI sessions understand how this repo is organized, how to perform common tasks (decklist extraction, research lookups, and where to add new extractors), and how the knowledgebase feeds the eventual assistant.

Quick status / tooling
- This repo is "pre-code" (research + knowledgebase). No build/test/lint toolchain or CI present.
- Runtime: Python scripts in /tools are standalone and use only stdlib. Use Python 3.9+ to run them.

Build / test / lint commands
- There is no CI or linting configured. A small test suite was added for core helpers.
- Run tests (unittest):
  - Run the full tests: python -m unittest
  - Run the specific decklist_common module tests: python -m unittest tests.test_decklist_common
  - Run a single test case: python -m unittest tests.test_decklist_common.TestDecklistCommon.test_slugify
- Running a single extractor (the practical runnable operations):
  - Single deck (Archidekt):
    python tools/archidekt_extract.py https://archidekt.com/decks/<deck-id>
  - All public decks for a user (Archidekt):
    python tools/archidekt_extract.py --user <username>
  - Single deck (Moxfield):
    python tools/moxfield_extract.py https://moxfield.com/decks/<public-id>
  - All public decks for a user (Moxfield):
    python tools/moxfield_extract.py --user <username>
- Example single-deck run writes one file and prints the path; --user mode paginates and writes multiple files.

High-level architecture (big picture)
- knowledgebase/ is the primary product: organized into decklists/, users/, research/, templates, and INDEX.md.
- tools/ holds small site-specific extractors and a shared helper:
  - tools/decklist_common.py — canonical helpers: slugify, classify_type, build_markdown, write_decklist. Extractors normalize remote JSON → list of card dicts and call build_markdown/write_decklist.
  - tools/archidekt_extract.py — Archidekt public API usage and mainboard selection rules.
  - tools/moxfield_extract.py — Moxfield unauthenticated endpoints (api2.moxfield.com) usage.
- File outputs: knowledgebase/decklists/<owner-username>/<deck-name-slug>.md (frontmatter based on _template-decklist.md).
- INDEX.md is an index/signpost (update after adding/removing files). CHANGELOG.md should get an entry when knowledgebase files change.

Key conventions (repo-specific)
- Decklist and user file locations:
  - Decklists go in knowledgebase/decklists/<owner-username>/*.md
  - Owner folder name = slugified owner username (tools use decklist_common.slugify)
  - Deck file name = slugified deck name (use provided templates for frontmatter)
- Frontmatter (required fields used by repo): type: decklist, title, owner, commander, colors, last_updated, source. See _template-decklist.md for exact fields.
- Extractor pattern to add new sites: tools/<site>_extract.py must:
  1) fetch the site API (or public JSON endpoints),
  2) normalize response to cards list: {"name","qty","type","foil"} and commander names/colors,
  3) call build_markdown(...)/write_decklist(...).
- Archidekt mainboard rule: a card is mainboard only if every category it's tagged with is includedInDeck (tools encode this exact logic).
- Type classification: decklist_common.TYPE_PRIORITY determines ordering (Creature, Planeswalker, Battle, Instant, Sorcery, Artifact, Enchantment, Land). classify_type() uses that order.
- Slug rules: decklist_common.slugify lowercases, strips non-word chars, spaces → dashes.
- Update workflow: after adding/editing knowledgebase files, update knowledgebase/INDEX.md and add a CHANGELOG.md entry.

Research and live-data patterns (from CLAUDE.md and .claude skill)
- Proxy pattern: this network may block Scryfall and Commander Spellbook. Use the reader proxy when needed: prepend https://r.jina.ai/ to Scryfall or Spellbook URLs (examples in CLAUDE.md/.claude skill). EDHRec JSON is fetchable directly.
- Color identity enforcement (used in research flows): always establish the Active Color Identity before recommendations; validate each card's color_identity as subset; drop off-color results.
- When enriching research with card details or pricing, prefer EDHRec (commander pages via json.edhrec.com), Scryfall (via proxy when required), and Commander Spellbook (via proxy) in that order where appropriate.

Where to look for more repo-specific rules
- CLAUDE.md — canonical working rules for assistants; includes decklist naming and extraction rules, the proxy guidance, data sources, and workflow points. Read and follow it.
- .claude/skills/edh-research/SKILL.md — operational rules for live research (color identity enforcement, exact endpoint patterns, failure modes). Consult this for any research-oriented Copilot requests.

Adding new extractors or changes
- Follow tools/decklist_common.py pattern exactly (normalize then hand off). Don't modify build_markdown unless changing repository-wide frontmatter shape — prefer adapting extractor normalization.
- Avoid inventing a build/test stack for now — this repo intentionally remains a knowledgebase with simple stdlib scripts.

Notes for Copilot sessions
- Before suggesting cards/combinations or writing research entries, re-check CLAUDE.md and .claude SKILL for identity/proxy rules.
- Use the extractor scripts rather than manual transcriptions when ingesting decks from Archidekt or Moxfield.
- Do not assume network-level access to Scryfall/Spellbook; apply the r.jina.ai proxy pattern when performing WebFetch calls if those endpoints fail.

Files to consult when running assistants
- README.md, CLAUDE.md, knowledgebase/_template-decklist.md, tools/decklist_common.py, .claude/skills/edh-research/SKILL.md

Summary
- This file documents: there is no build/test/lint tooling; how to run extractors; the knowledgebase-first architecture; and the repository-specific conventions (slugging, type priority, mainboard rules, proxy and color-identity enforcement). Consult CLAUDE.md and .claude skill for authoritative assistant rules and data-source patterns.

Questions
- Any adjustments or extra coverage to add (examples: CI that runs extractors in a reproducible environment, tests for slugify/classify_type, or a requirements/dev setup)?

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
