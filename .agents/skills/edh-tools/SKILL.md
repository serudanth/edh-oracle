---
name: edh-tools
description: Use when running or automating local EDH Oracle tools — deterministic deck analysis (deck_analyzer_engine.py), remote decklist extraction (archidekt_extract.py, moxfield_extract.py), external analysis extraction (external_analysis_extract.py), or navigating and managing the knowledgebase podlist and theorycrafting archives.
---

# EDH Oracle Tools Runbook

Operational procedures and workflows for executing the deterministic analysis engine, remote deck extractors, and managing knowledgebase artifacts.

## Core Directives & Invariants

1. **Decklist Mirror Policy (Strict):**
   - External platforms (Archidekt and Moxfield) are the sole source of truth for decklists in `knowledgebase/podlist/**/decks/*.md`.
   - **Never manually edit card counts, names, or categories directly in local deck markdown files.**
   - All deck changes must occur on the remote site, then pulled locally via `archidekt_extract.py` or `moxfield_extract.py`.
2. **Terminal Link Integrity:**
   - Never wrap headings, commander names, or deck names in `file://` links (CLI renderer forcibly displays basenames). Always write names in bold and link files separately using their exact basename (e.g. `Gluntch, the Bestower ([README.md](file:///...))`).
   - Format directory paths as inline code without `file://` wrappers (e.g. `knowledgebase/podlist/`).

---

## 1. Local Deterministic Deck Analyzer (`tools/deck_analyzer_engine.py`)

Calculates 100% deterministic metrics without LLM hallucinations: power ratings, curve metrics, fast mana counts, tutor counts, CFP 53 Game Changers, Hard Stax & Lock pieces, and Commander Spellbook infinite combos.

### Common Invocations

- **Single Deck Audit (Stdout preview):**
  ```bash
  python tools/deck_analyzer_engine.py --deck knowledgebase/podlist/<owner>/decks/<slug>.md
  ```
- **Single Deck Audit & Update KB Analysis:**
  ```bash
  python tools/deck_analyzer_engine.py --deck knowledgebase/podlist/<owner>/decks/<slug>.md --write-kb
  ```
  *(Updates or creates `knowledgebase/podlist/<owner>/analysis/<slug>.md`)*
- **All Decks for an Owner:**
  ```bash
  python tools/deck_analyzer_engine.py --owner <owner> --write-kb
  ```
- **Full Podlist Batch Analysis:**
  ```bash
  python tools/deck_analyzer_engine.py --all --write-kb
  ```

### Key Detection Sets
- **Fast Mana:** Sol Ring, Mana Crypt, Lotus Petal, Chrome Mox, Mox Diamond, Mox Opal, Mana Vault, Grim Monolith, Ancient Tomb, Gemstone Caverns, Dark Ritual, Pyretic Ritual, Seething Song, Cabal Ritual, Elvish Spirit Guide, Simian Spirit Guide, Jeweled Lotus.
- **CFP Game Changers:** 53 format-defining staples tracked by CFP / WotC (Ad Nauseam, Thassa's Oracle, Rhystic Study, The One Ring, Smothering Tithe, etc.).
- **Hard Stax:** Oppression and turn-denial pieces (Winter Orb, Stasis, Drannith Magistrate, Blood Moon, Armageddon, etc.).

---

## 2. Remote Decklist Extraction & Synchronization

### Archidekt (`tools/archidekt_extract.py`)

Fetches public decks from Archidekt via public API.
- **Single Deck Sync:**
  ```bash
  python tools/archidekt_extract.py <archidekt-url-or-deck-id>
  ```
  *Example:* `python tools/archidekt_extract.py https://archidekt.com/decks/1234567/my-deck`
- **All Public Decks for a User:**
  ```bash
  python tools/archidekt_extract.py --user <archidekt-username>
  ```
- **Archidekt Mainboard Rule:** A card is included in the mainboard only if *every* assigned category has `includedInDeck == true`.

### Moxfield (`tools/moxfield_extract.py`)

Fetches public decks from Moxfield via `api2.moxfield.com` unauthenticated endpoints (with automatic `r.jina.ai` proxy fallback on 403).
- **Single Deck Sync:**
  ```bash
  python tools/moxfield_extract.py <moxfield-url-or-deck-id>
  ```
  *Example:* `python tools/moxfield_extract.py https://www.moxfield.com/decks/abc123xyz`
- **All Public Decks for a User:**
  ```bash
  python tools/moxfield_extract.py --user <moxfield-username>
  ```

---

## 3. External Deck-Analysis Extraction (`tools/external_analysis_extract.py`)

Extracts, normalizes, and archives external analysis reports from supported third-party deck analyzers: ScryCheck, EDHCheck, RateMyDecks, CommanderPowerMeter, ArcMind, PowerDeckAI.

### Usage
- **From URL:**
  ```bash
  python tools/external_analysis_extract.py --url <Moxfield-or-Archidekt-URL>
  ```
- **From JSON input payload:**
  ```bash
  python tools/external_analysis_extract.py --input payload.json
  ```
- **From stdin:**
  ```bash
  cat payload.json | python tools/external_analysis_extract.py
  ```

---

## 4. Deck Advisory, Upgrade & Theorycrafting Workflow

When asked to analyze a deck, suggest upgrades, or recommend cuts/adds:

1. **Inspection:**
   - Read the decklist at `knowledgebase/podlist/<owner>/decks/<slug>.md`.
   - Run `python tools/deck_analyzer_engine.py --deck knowledgebase/podlist/<owner>/decks/<slug>.md` to inspect current deterministic metrics, curve, and bracket indicators.
2. **Research & Validation:**
   - Consult `edh-research` skill.
   - Establish Active Color Identity. Check Scryfall cache (`knowledgebase/_cache/scryfall-cards.json`) before making external lookups.
   - Strictly filter out off-color cards. Apply Set Delta Protocol for modern printings.
3. **Advisory Presentation:**
   - Present cut/add recommendations in chat grouped logically (Ramp, Draw, Removal, Synergy, Combos).
   - State reasoning: CMC delta, mana color consistency, salt impact, synergy percentage from EDHRec.
   - Provide a clean copy-pasteable card swap list (e.g. `1 Card Name` format) for the remote site.
4. **Theorycrafting Archiving (When Requested):**
   - If the user requests saving the upgrade plan or deck theory, write to `knowledgebase/theorycrafting/<slug>-upgrade.md` using `knowledgebase/_template.md`.
5. **Post-Update Synchronization:**
   - Remind or offer to run the sync script (`python tools/*_extract.py <url>`) once remote changes are saved.
   - Re-run `python tools/deck_analyzer_engine.py --deck <path> --write-kb` to refresh analysis.
