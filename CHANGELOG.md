# Changelog

## 2026-07-09 (Moxfield support)

- **[tooling]** Added `scripts/moxfield_extract.py` (single-deck and `--user` bulk mode, mirroring the Archidekt extractor). Moxfield has no official API; uses the same unauthenticated `api2.moxfield.com` endpoints moxfield.com's frontend calls, confirmed via the Aleqsd/moxfield-api wrapper's source rather than guessed.
- **[tooling]** Factored shared markdown/frontmatter rendering out of `archidekt_extract.py` into `scripts/decklist_common.py` so both extractors build identically-formatted decklist files.
- **[kb]** Imported all 16 of `reimaru`'s public Moxfield decks into `knowledgebase/decklists/reimaru/`.

## 2026-07-09 (import pod decklists)

- **[kb]** Extracted the pod's public Archidekt decks: `J-Py` (1), `LTO888` (11), `Xanoh` (1), `mjsnoozer` (5) — 18 decks total, each under `knowledgebase/decklists/<owner>/`.

## 2026-07-09 (sync to fowlplays' updated public decks)

- **[kb]** User tightened privacy on several Archidekt decks after noticing the earlier bulk import had pulled some they didn't intend to be public. Re-ran `archidekt_extract.py --user fowlplays` and removed the 5 decks no longer public: `food-bending`, `scions-spellcraft-redux`, `the-best-of-friends-legacy`, `the-chocobo-forest`, `the-season-of-giving`. 12 decks remain, matching the current public profile.

## 2026-07-09 (bulk import fowlplays' Archidekt profile)

- **[tooling]** `scripts/archidekt_extract.py` gained `--user <username>` to bulk-extract every public deck for an Archidekt user in one run, instead of one URL at a time.
- **[kb]** Imported all 17 of `fowlplays`' public decks into `knowledgebase/decklists/fowlplays/`.

## 2026-07-09 (Archidekt decklist extraction)

- **[tooling]** Added `scripts/archidekt_extract.py` — pulls a deck from Archidekt's API and writes it into `knowledgebase/decklists/<owner>/<deck-slug>.md`.
- **[kb]** First decklist logged: `knowledgebase/decklists/fowlplays/the-copied-factory.md` (Inalla, Archmage Ritualist — UBR).
- **[kb]** `_template-decklist.md` gained a `source` frontmatter field for traceability back to the original deck URL.

## 2026-07-09 (repo initialized)

- **[repo]** `edh-oracle` created — knowledgebase scaffolding for decklists and research, `CLAUDE.md`/`README.md` established.
