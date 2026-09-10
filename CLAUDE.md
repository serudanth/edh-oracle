# EDH Oracle — Claude Code Context

<!-- 1. Universal Core & Operational Protocols -->
@~/agent-core/core/ethics-and-risk.md
@~/agent-core/core/domains/edh.md

<!-- 2. Host Device Context -->
@~/.config/agent-device.md

---

## Local Repository Context

- **Repository Role:** MTG Commander decklist curator & deckbuilding assistant pre-code knowledge base.
- **Pre-Code Status:** No application build, test, or lint tooling exists yet. Do not invent build commands.
- **Deck Mirror Policy:** Source of truth is always Archidekt or Moxfield. Do not manually edit decklists in `knowledgebase/podlist/**/decks/*.md`.
- **Extraction Tools:** Use `python tools/archidekt_extract.py` and `python tools/moxfield_extract.py`.
- **Research Operations:** Follow [`.claude/skills/edh-research/SKILL.md`](.claude/skills/edh-research/SKILL.md) and [`agent-core/core/domains/edh.md`](~/agent-core/core/domains/edh.md) for cache and network egress rules.
