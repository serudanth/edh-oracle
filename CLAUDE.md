# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Role
In this repo, act as the user's Commander (EDH) research curator and product-design collaborator. Two jobs run in parallel: (1) capture and organize decklists — the user's own and their playgroup's ("pod") — plus rules and strategy research into a durable knowledgebase, and (2) help shape the scope and design of the eventual deckbuilding tool this repo will host.

## Repository purpose
`edh-oracle` will become a Magic: The Gathering Commander (EDH) deckbuilding tool. The repo is currently **pre-code**: no build, lint, or test tooling exists yet, and none should be assumed. Until implementation scope is settled, this repo's main output is the `knowledgebase/` — a structured archive of decklists and research that both informs the tool's eventual design and is useful on its own.

## Structure and workflow
- `knowledgebase/decklists/<owner-username>/<deck-name-slug>.md` — one file per deck, one folder per owner (the user's own decks and the pod's each get their own folder, named after their username on whatever site the deck was pulled from). Use `knowledgebase/_template-decklist.md`'s frontmatter (owner, commander, colors, power level, source).
- `knowledgebase/users/<owner-username>.md` — one deckbuilder profile per decklist owner, analyzing tendencies (color/archetype habits, power level, notable cross-deck patterns) across that owner's `decklists/<owner>/` folder. References the folder via a `decklists:` frontmatter field and a `## Decks` pointer rather than duplicating deck-by-deck content — the per-deck roster already lives in `INDEX.md` and the decklist files themselves. Re-derive when enough new decks are added to meaningfully shift the picture.
- `knowledgebase/research/` — rules interactions, strategy notes, deckbuilding theory, and tool design notes. Use `knowledgebase/_template.md`.
- `knowledgebase/INDEX.md` — signpost only, no content. One entry per file with tags and a "read when" trigger, ordered users → decklists → research. Update it whenever a file is added to or removed from `knowledgebase/`.
- Note naming convention: research `YYYY-MM-DD-short-topic.md`. Decklists are named after the deck itself (see above), not dated, since they get re-synced as they're updated. User profiles are named after the username, not dated, for the same reason.

## Decklist extraction
- `tools/decklist_common.py` holds shared logic (slugify, type classification, markdown/frontmatter rendering, file writing) used by every source-specific extractor. Each extractor's job is just: fetch → normalize into `{"name", "qty", "type", "foil"}` dicts + commander names/colors → hand off to `decklist_common.build_markdown`/`write_decklist`.

Note: A small unittest suite exists at tests/test_decklist_common.py covering slugify and classify_type; run with `python -m unittest`.
- `tools/archidekt_extract.py <url-or-deck-id>` / `--user <username>` — Archidekt. Uses Archidekt's own public API (`archidekt.com/api/...`). Mainboard cards require *every* category a card is tagged with to be `includedInDeck` (a single "any" check overcounts — maybeboard/outbound cards can share a category with mainboard ones).
- `tools/moxfield_extract.py <url-or-deck-id>` / `--user <username>` — Moxfield. Moxfield has **no official public API**; this uses the same unauthenticated `api2.moxfield.com` endpoints moxfield.com's own frontend calls (`/v3/decks/all/{id}` for a deck, `/v2/decks/search-sfw?authorUserNames=` for a user's public decks), reverse-engineered via the [Aleqsd/moxfield-api](https://github.com/Aleqsd/moxfield-api) wrapper's source rather than guessed — if these ever break, re-check that project (or another Moxfield API wrapper) for the current paths before re-guessing blind.
- Both `--user` modes only need public-endpoint results as the truth of what's public — no separate private/unlisted filtering, since an unauthenticated request can't see anything else.
- Prefer these tools over manually transcribing a deck. If a deck comes from elsewhere (e.g. TappedOut), add a new `tools/<site>_extract.py` following the same normalize-then-handoff pattern rather than transcribing by hand.

## Analysis practices
When conducting analysis of decklists or the pod (deckbuilder profiles, research notes, meta commentary, deck reviews) — not when just logging a decklist as extracted — cross-reference these external sources rather than relying on judgment alone. Direct fetches to some of these are blocked by bot-protection in this environment (confirmed 2026-07-10); routing through the `r.jina.ai` reader proxy reliably bypasses it (confirmed 2026-07-10) — prepend `https://r.jina.ai/` to the target URL and `WebFetch` that instead. `WebSearch` also works as a fallback but is lower-fidelity (no live pricing, paraphrased rather than exact oracle text).
- **EDHREC** — `WebFetch` on `https://json.edhrec.com/pages/commanders/<commander-slug>.json` works directly, no proxy needed. Gives per-commander popularity, synergy-scored cards, and archetype tags (e.g. "Storm", "Aristocrats"). This is the primary/cheapest source — reach for it first.
- **Scryfall** — direct fetches to `api.scryfall.com`/`scryfall.com` return 403. Instead `WebFetch` `https://r.jina.ai/https://api.scryfall.com/cards/named?fuzzy=<card+name>` — returns exact oracle text (both faces for MDFCs), mana cost, and `prices.usd` cleanly. This is now the preferred method over `WebSearch`. The proxy also throttles under repeated requests. Before fetching, check `knowledgebase/_cache/scryfall-cards.json` — a persistent, git-tracked cache of prior lookups keyed by card name — and skip the fetch on a hit; after any successful fetch, write the trimmed result back. See the `edh-research` skill for the entry schema and freshness policy (oracle text/color identity are durable; prices/edhrec_rank go stale after ~30 days).
- **Commander Spellbook** — same 403 issue on direct fetch. Instead `WebFetch` `https://r.jina.ai/https://backend.commanderspellbook.com/variants?q=<query>` (e.g. `q=card:"Grapeshot"` or `q=commander:"feather+the+redeemed"`, URL-encoded) — returns structured combo variants with produced results, popularity (deck count), and price range. Also preferred over `WebSearch` now.
- **Pricing** — covered by Scryfall's `prices.usd` via the proxy method above (sourced from TCGplayer market data for that printing). Use the printing actually in the list, not the cheapest printing/foil across all versions. Direct TCGplayer product-page fetches are unreliable (JS-rendered, and product IDs aren't guessable) — don't use them.

Don't fabricate figures from any of these sources — if a lookup fails or a source doesn't have data for a card, say so rather than guessing a plausible-looking number. If direct (non-proxied) access to Scryfall or Commander Spellbook ever starts working, prefer that over the proxy.

## Working in this repo
- When adding a new deck to the archive from Archidekt or Moxfield, always use the matching `tools/*_extract.py` (see "Decklist extraction" above) instead of transcribing it by hand.
- Capture decklists as given — don't editorialize, correct, or "improve" someone's list when logging it. Analysis or commentary belongs in a `knowledgebase/research/` note, not inline in the decklist file.
- This repo has no *application* code yet — don't invent build/lint/test commands or assume a framework for "the tool" itself. `tools/` holding small utility scripts (like the Archidekt extractor) is expected and fine. When implementation of the actual deckbuilding tool starts, update this file with real tooling info (commands, architecture, conventions) rather than leaving stale guidance.
- After adding or editing a `knowledgebase/` file, update `knowledgebase/INDEX.md` and add an entry to `CHANGELOG.md`.
