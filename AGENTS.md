# EDH Oracle — Agent Guidelines (`AGENTS.md`)

## 1. Core Operating Invariants & Governance

* **Tiers 1 & 2 Authority:** Strictly follow the Dual-Flow resolution engine and safety constraints in [`~/agent-core/templates/global/core-anchor.md`](file:///home/cpc9181/agent-core/templates/global/core-anchor.md) (Universal Ethics, Host Fences, Topology Abstraction, Explanation ≠ Execution).
* **Tier 3 Domain Standards:** Implement MTG EDH standards in [`~/agent-core/core/domains/edh.md`](file:///home/cpc9181/agent-core/core/domains/edh.md).

---

## 2. Workspace Context & Artifacts (Tier 4)

* **Pre-Code State:** Pre-code knowledge base and research archive. No application build/lint tooling exists yet; do not invent build or test commands.
* **Decklist Mirror Policy:** External deck sites (Archidekt/Moxfield) are the source of truth. Never edit decklists manually in `knowledgebase/podlist/**/decks/*.md`.
* **Tools:** Run `python tools/archidekt_extract.py` and `python tools/moxfield_extract.py`.
* **Cache Requirement:** Always check `knowledgebase/_cache/scryfall-cards.json` before querying external APIs. Follow cache freshness rules in [`.claude/skills/edh-research/SKILL.md`](.claude/skills/edh-research/SKILL.md).
* **Network Egress:** Route Scryfall/Spellbook queries through `https://r.jina.ai/` only if direct connection returns HTTP 403.
* **Color Identity:** Strictly enforce format color identity rules across hybrid mana, MDFC back faces, and activation costs before recommending cards.
* **Set Delta Protocol:** Proactively counter parametric training cutoff bias. Identify training boundary, discover post-cutoff sets via Scryfall (`GET /sets`), and execute targeted delta searches (`date>=<cutoff-date>`) to uncover recent printings.
