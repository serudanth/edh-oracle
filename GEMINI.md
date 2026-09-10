# EDH Oracle — Antigravity Assistant Context & Rules

## 1. Core Operating Invariants

* **Pre-Code State:** This repository is currently a research archive and structured knowledgebase. No application code, build, or test frameworks exist.
* **Decklist Mirror Policy:** Decklists under `knowledgebase/podlist/**/decks/*.md` are mirrors of external lists (Archidekt/Moxfield). Never edit card quantities or contents locally; owners change lists on the site, then refresh via `tools/*_extract.py`.
* **Scryfall Cache Requirement:** Always check `knowledgebase/_cache/scryfall-cards.json` before querying Scryfall or Spellbook. Write back successful lookups.
* **Color Identity:** Strictly enforce format color identity rules across hybrid mana, MDFC back faces, and activation costs before suggesting cards.

---

## 2. Authoritative Core References

* Universal Ethics & Risk: `~/agent-core/core/ethics-and-risk.md`
* EDH Domain Standards: `~/agent-core/core/domains/edh.md`
* Active Host Profile: `~/.config/agent-device.md`
