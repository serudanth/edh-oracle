# Copilot Instructions for edh-oracle

## 1. Operational Bounds & Safety
* **Core Anchor (Tiers 1 & 2):** Adhere to the Dual-Flow resolution engine and safety constraints in [`~/agent-core/templates/global/core-anchor.md`](file:///home/cpc9181/agent-core/templates/global/core-anchor.md).
* **Domain Architecture (Tier 3):** Implement standards in [`~/agent-core/core/domains/edh.md`](file:///home/cpc9181/agent-core/core/domains/edh.md).

---

## 2. Repository Purpose & Architecture (Tier 4)
* **Status:** Pre-code knowledge base and research archive for Magic: The Gathering Commander (EDH). No application build, test, or lint tooling exists yet.
* **Primary Products:** `knowledgebase/podlist/<owner>/decks/<slug>.md`, `knowledgebase/research/`, `tools/`.
* **Decklist Ingestion:** Use `python tools/archidekt_extract.py` and `python tools/moxfield_extract.py`.
* **Mirror Policy:** External deck sites (Archidekt/Moxfield) are the source of truth. Do not manually edit local decklists.

---

## 3. Live Research & Cache Rules
* **Cache First:** Always check `knowledgebase/_cache/scryfall-cards.json` before querying external APIs.
* **Network Egress Probe:** If direct connection to Scryfall returns HTTP 403, route via `https://r.jina.ai/` reader proxy.
* **Color Identity:** Validate candidate cards against commander color identity before suggesting recommendations.
