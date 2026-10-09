# EDH Oracle — Antigravity Assistant Context & Rules

## 1. Governance & Operational Bounds

* **Core Anchor (Tiers 1 & 2):** You MUST adhere to the Dual-Flow resolution engine and safety constraints in [`~/agent-core/templates/global/core-anchor.md`](file:///home/cpc9181/agent-core/templates/global/core-anchor.md) (Universal Ethics, Host Fences, Privacy Isolation, Explanation ≠ Execution).
* **Domain Standard (Tier 3):** Implement MTG EDH domain standards in [`~/agent-core/core/domains/edh.md`](file:///home/cpc9181/agent-core/core/domains/edh.md).

---

## 2. Core Operating Invariants (Tier 4)

* **Pre-Code State:** This repository is currently a research archive and structured knowledgebase. No application code, build, or test frameworks exist. Do not invent build commands.
* **Decklist Mirror Policy:** Decklists under `knowledgebase/podlist/**/decks/*.md` are mirrors of external lists (Archidekt/Moxfield). Never edit card quantities or contents locally; owners change lists on the site, then refresh via `tools/*_extract.py`.
* **Extraction & Sync Tools:** Use `python tools/archidekt_extract.py`, `python tools/moxfield_extract.py`, and `python tools/sync_scryfall_bulk.py`.
* **Authoritative Card Ground Truth (No Hallucinations / Assumptions):** Always verify cards against the local Scryfall database (`knowledgebase/_cache/scryfall.db` via `python tools/sync_scryfall_bulk.py --query "<card>"` or `tools/scryfall_cache.py`) before conducting deck reviews, card evaluations, synergy analysis, or suggesting upgrades. NEVER fabricate, hallucinate, or assume card oracle text, mana values, card types, or color identities from LLM parametric memory.
* **Scryfall Cache Requirement:** Reference the local Scryfall database (`knowledgebase/_cache/scryfall.db` via `tools/scryfall_cache.py` or `python tools/sync_scryfall_bulk.py`) before querying Scryfall or Spellbook. Follow cache rules in [`.claude/skills/edh-research/SKILL.md`](.claude/skills/edh-research/SKILL.md).
* **Color Identity:** Strictly enforce format color identity rules across hybrid mana, MDFC back faces, and activation costs before suggesting cards.
* **Set Delta Protocol:** Counter LLM parametric training cutoff bias during card searches. Identify training cutoff baseline, discover post-cutoff sets via Scryfall (`GET /sets`), and execute two-pronged searches (historical synergy + targeted post-cutoff delta queries `date>=<cutoff-date>`) to guarantee modern cards are evaluated and cached.
* **Terminal Link Integrity / No Entity Masking:** The CLI terminal renderer forcibly replaces `file://` link text with target basenames (e.g., `[Commander](file://.../README.md)` renders as `README.md`) and wipes directory links. NEVER wrap headings (`#`, `##`, `###`), commander names, or deck names in `file://` links. Keep entity names in plain text/bold, link files separately using their exact basename (e.g. `Gluntch, the Bestower ([README.md](file://...))` or `[02-decklist.md](file://...)`), and format directory paths as inline code without `file://` wrappers.

