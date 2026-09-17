# EDH Oracle — Antigravity Assistant Context & Rules

## 1. Governance & Operational Bounds

* **Core Anchor (Tiers 1 & 2):** You MUST adhere to the Dual-Flow resolution engine and safety constraints in [`~/agent-core/templates/global/core-anchor.md`](file:///home/cpc9181/agent-core/templates/global/core-anchor.md) (Universal Ethics, Host Fences, Privacy Isolation, Explanation ≠ Execution).
* **Domain Standard (Tier 3):** Implement MTG EDH domain standards in [`~/agent-core/core/domains/edh.md`](file:///home/cpc9181/agent-core/core/domains/edh.md).

---

## 2. Core Operating Invariants (Tier 4)

* **Pre-Code State:** This repository is currently a research archive and structured knowledgebase. No application code, build, or test frameworks exist. Do not invent build commands.
* **Decklist Mirror Policy:** Decklists under `knowledgebase/podlist/**/decks/*.md` are mirrors of external lists (Archidekt/Moxfield). Never edit card quantities or contents locally; owners change lists on the site, then refresh via `tools/*_extract.py`.
* **Scryfall Cache Requirement:** Always check `knowledgebase/_cache/scryfall-cards.json` before querying Scryfall or Spellbook. Write back successful lookups. Follow cache freshness rules in [`.claude/skills/edh-research/SKILL.md`](.claude/skills/edh-research/SKILL.md).
* **Color Identity:** Strictly enforce format color identity rules across hybrid mana, MDFC back faces, and activation costs before suggesting cards.
* **Extraction Tools:** Use `python tools/archidekt_extract.py` and `python tools/moxfield_extract.py`.
