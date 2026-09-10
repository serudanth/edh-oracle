# Copilot Instructions for edh-oracle

Operational reference for GitHub Copilot sessions in the EDH Oracle repository.

---

## 1. Repository Purpose & Architecture
* **Status:** Pre-code knowledge base and research archive for Magic: The Gathering Commander (EDH).
* **Primary Products:** `knowledgebase/podlist/<owner>/decks/<slug>.md`, `knowledgebase/research/`, `tools/`.
* **Decklist Ingestion:** Use `python tools/archidekt_extract.py` and `python tools/moxfield_extract.py`.
* **Mirror Policy:** External deck sites (Archidekt/Moxfield) are the source of truth. Do not manually edit local decklists.

---

## 2. Live Research & Cache Rules
* **Cache First:** Always check `knowledgebase/_cache/scryfall-cards.json` before querying external APIs.
* **Network Egress Probe:** Probe `api.scryfall.com` directly; only use `https://r.jina.ai/` prefix if direct connection returns HTTP 403.
* **Color Identity:** Validate candidate cards against commander color identity before suggesting recommendations.

---

## 3. Authoritative Core References
* Universal Protocols: `/media/Zodiark/Atelier/agent-core/core/ethics-and-risk.md`
* EDH Domain Standards: `/media/Zodiark/Atelier/agent-core/core/domains/edh.md`
