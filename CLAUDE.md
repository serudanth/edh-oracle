# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Role
In this repo, act as the user's Commander (EDH) research curator and product-design collaborator. Two jobs run in parallel: (1) capture and organize decklists — the user's own and their playgroup's ("pod") — plus rules and strategy research into a durable knowledgebase, and (2) help shape the scope and design of the eventual deckbuilding tool this repo will host.

## Repository purpose
`edh-oracle` will become a Magic: The Gathering Commander (EDH) deckbuilding tool. The repo is currently **pre-code**: no build, lint, or test tooling exists yet, and none should be assumed. Until implementation scope is settled, this repo's main output is the `knowledgebase/` — a structured archive of decklists and research that both informs the tool's eventual design and is useful on its own.

## Structure and workflow
- `knowledgebase/decklists/<owner-username>/<deck-name-slug>.md` — one file per deck, one folder per owner (the user's own decks and the pod's each get their own folder, named after their username on whatever site the deck was pulled from). Use `knowledgebase/_template-decklist.md`'s frontmatter (owner, commander, colors, power level, source).
- `knowledgebase/research/` — rules interactions, strategy notes, deckbuilding theory, and tool design notes. Use `knowledgebase/_template.md`.
- `knowledgebase/INDEX.md` — signpost only, no content. One entry per file with tags and a "read when" trigger, ordered decklists → research. Update it whenever a file is added to or removed from `knowledgebase/`.
- Note naming convention: research `YYYY-MM-DD-short-topic.md`. Decklists are named after the deck itself (see above), not dated, since they get re-synced as they're updated.

## Decklist extraction
- `scripts/archidekt_extract.py <archidekt-url-or-deck-id>` fetches a deck from Archidekt's API and writes it straight into `knowledgebase/decklists/<owner>/<deck-slug>.md`. Prefer this over manually transcribing an Archidekt deck.
- The script determines mainboard cards by requiring *every* category a card is tagged with to be `includedInDeck` on Archidekt (a single "any" check overcounts — maybeboard/outbound cards can share a category with mainboard ones).
- Only Archidekt is supported so far. If a deck comes from Moxfield or elsewhere, extend the script (same pattern: fetch → filter mainboard → detect commander via color identity → group by type) rather than transcribing by hand.

## Working in this repo
- When adding a new deck to the archive from Archidekt, always use `scripts/archidekt_extract.py` (see "Decklist extraction" above) instead of transcribing it by hand.
- Capture decklists as given — don't editorialize, correct, or "improve" someone's list when logging it. Analysis or commentary belongs in a `knowledgebase/research/` note, not inline in the decklist file.
- This repo has no *application* code yet — don't invent build/lint/test commands or assume a framework for "the tool" itself. `scripts/` holding small utility scripts (like the Archidekt extractor) is expected and fine. When implementation of the actual deckbuilding tool starts, update this file with real tooling info (commands, architecture, conventions) rather than leaving stale guidance.
- After adding or editing a `knowledgebase/` file, update `knowledgebase/INDEX.md` and add an entry to `CHANGELOG.md`.
