---
name: edh-research
description: Use whenever researching Commander/EDH cards, synergies, combos, or pricing for the knowledgebase — fetching oracle text, EDHRec synergy data, Commander Spellbook combos, or TCGplayer market prices, and whenever recommending or validating cards against a commander's color identity.
---

# Commander/EDH Research Skill

Structured workflows for fetching live data from four sources used in this repo's Commander/EDH
research (`knowledgebase/research/`, deckbuilder profiles, deck reviews). Always prefer live API
data over memory for card text, pricing, and synergy statistics — these change over time.

## Network note (this repo)

On this network (office), direct fetches to `api.scryfall.com` and `backend.commanderspellbook.com`
return HTTP 403 — this is a network-level block, not necessarily bot-protection from the source
itself. Route those two through the `r.jina.ai` reader proxy instead: prepend
`https://r.jina.ai/` to the target URL and `WebFetch` that. `json.edhrec.com` is unaffected and can
be fetched directly. If direct (non-proxied) access to Scryfall or Spellbook ever starts working
(e.g. off this network), prefer that over the proxy — don't keep routing through it out of habit.
The proxy also throttles under repeated requests (seen as 403s that a retry a few seconds later
clears) — batch lookups with short pauses between them rather than firing many in a burst.

---

## Card lookup cache — check before fetching

`knowledgebase/_cache/scryfall-cards.json` is a persistent, git-tracked cache of Scryfall lookups
already paid for, keyed by exact card name. **Before** fetching a card via the proxy, check this
file for an existing entry — skip the network call entirely on a hit. **After** any successful
named-card fetch, add/update the entry so the next session (or the next question in this one)
doesn't re-pay for it.

Entry shape (trimmed from the full Scryfall response — don't cache the full payload, it's mostly
image URIs and marketplace links no research question needs):

```json
"Card Name": {
  "mana_cost": "{2}{W}", "cmc": 3.0, "type_line": "Enchantment",
  "oracle_text": "...", "colors": ["W"], "color_identity": ["W"], "keywords": [],
  "legal_commander": "legal",
  "prices_usd": "0.27", "prices_usd_foil": null,
  "edhrec_rank": 5389, "scryfall_uri": "...", "set": "tdc", "released_at": "2025-04-11",
  "fetched_at": "2026-08-06"
}
```

For MDFC/split/adventure cards with no top-level `oracle_text`, build it from `card_faces` (join
as `"Face Name: text\n//\nFace Name: text"`); same fallback for `mana_cost`.

**Freshness policy:** `oracle_text`, `type_line`, `color_identity`, `keywords`, and
`legal_commander` almost never change (only on errata/banlist moves) — a cache hit is good
indefinitely for these. `prices_usd`/`prices_usd_foil` and `edhrec_rank` drift over time — if
`fetched_at` is more than ~30 days old and the user's question hinges on current price or
popularity, refetch and overwrite the entry rather than quoting a stale number; otherwise a cache
hit is fine and faster. Never silently serve a stale price without noting its `fetched_at` date if
asked directly for "current" pricing.

This cache only covers single-card Scryfall lookups. EDHRec and Commander Spellbook responses
aren't cached (EDHRec isn't proxy-throttled; Spellbook combo queries are multi-card and less likely
to repeat verbatim) — if that changes, extend the same pattern rather than inventing a new format.

---

## ⚠️ Color identity enforcement — mandatory

Applies to every recommendation, combo suggestion, and card mention. Commander's color identity
rule is absolute: a deck may only contain cards whose combined color identity is a subset of the
commander's color identity.

### Step 1 — establish the Active Color Identity before recommending anything

1. **Commander known** → fetch it (via the proxy pattern above), read `color_identity`.
   Example: Atraxa → `["W","U","B","G"]`.
2. **User states colors** (e.g. "Grixis deck") → map to letters: White=W, Blue=U, Black=B, Red=R,
   Green=G, Colorless=C. Two-color guild names (Azorius=WU, Rakdos=BR, etc.) and three-color wedge/
   shard names (Grixis=UBR, Abzan=WBG, etc.) map the same way.
3. **Neither given** → ask before recommending cards.

Re-establish/update if the commander changes mid-conversation (including partner commanders —
union both partners' identities; Background commanders — union commander + chosen background).

### Step 2 — validate every card

- Allowed if `color_identity` is a subset of the Active Color Identity.
- Colorless cards (`color_identity = []`) are always allowed.
- Use Scryfall's `id<=` filter on searches, e.g. `id<=WUBG` for Atraxa.

### Step 3 — EDHRec results

A commander's EDHRec page is already filtered to that commander's identity, but double-check any
card that looks unexpected (colorless utility lands can have identity quirks).

### Step 4 — Commander Spellbook combos

Every variant has a `colorIdentity` field — it must be a subset of the Active Color Identity or
the combo is dropped, including from "almost included" results. Verify individual card identities
too if a combo's identity looks narrower than expected.

### Step 5 — handling violations

Silently drop off-color cards from recommendations; don't call them out unless the user directly
asks about that specific card, in which case explain the violation. Look for an in-color
alternative via `id<=` search instead.

### Edge cases

| Situation | Rule |
|---|---|
| Hybrid mana (e.g. {W/U}) | Both colors count — blocked if either is outside the identity |
| Reminder text | Does not contribute to color identity |
| Lands with colored activation costs | The activation color counts (Dryad Arbor is Green; Reflecting Pool is colorless) |
| Devoid | No color, but mana cost still sets identity |
| Split/adventure/modal/MDFC | Identity = union of all faces/halves |
| Off-color activated abilities | Any colored symbol in the cost counts |
| Partner commanders | Union of both partners' identities |
| Background commanders | Union of commander + Background |

---

## Source 1 — Scryfall (card data & mechanics)

Authoritative oracle text, type lines, mana costs, keywords, rulings, legality, per-printing prices.

**Card by name (fuzzy):** `https://r.jina.ai/https://api.scryfall.com/cards/named?fuzzy={card+name}`

Key fields: `name`, `oracle_text`, `type_line`, `keywords`, `mana_cost`, `cmc`, `color_identity`,
`legalities.commander`, `prices.usd` / `prices.usd_foil` (TCGplayer **market price**, not cheapest
listing), `rulings_uri`, `scryfall_uri`, `edhrec_rank`.

**Rulings:** fetch `rulings_uri` from the card object (proxy the same way) → array of
`{published_at, comment}`.

**Search:** `https://r.jina.ai/https://api.scryfall.com/cards/search?q={query}` — useful query bits:
`o:"untap"`, `t:legendary t:creature`, `commander:legal`, `id<=WUBRG`, `is:commander`,
`keyword:vigilance`, `year>=2023`.

**Batch pricing:** `POST` (via proxy) to `https://api.scryfall.com/cards/collection` with
`{"identifiers": [{"name": "Sol Ring"}, ...]}` — up to 75 cards per call.

---

## Source 2 — EDHRec (synergies & trends) — fetch directly, no proxy needed

**Commander page:** `https://json.edhrec.com/pages/commanders/{slug}.json`
Slug = lowercase name, spaces → hyphens, punctuation dropped
(`Atraxa, Praetors' Voice` → `atraxa-praetors-voice`). If a slug 404s, try dropping "the",
or check for a partner/background variant page.

**Card synergy page:** `https://json.edhrec.com/pages/cards/{slug}.json`

Response shape: `container.json_dict.cardlists[]`, each with a `tag` category (`High Synergy Cards`,
`Top Cards`, `Creatures`, `Ramp`, `Card Draw`, `Removal`, `Protection`, `New Cards`, etc.) and
`cardviews[]`, each with `name`, `synergy` (decimal, e.g. 0.19 = +19%), `inclusion`/`num_decks`,
`potential_decks`, `label`. Inclusion rate = `num_decks / potential_decks × 100`. Synergy = how much
more/less this card appears in this commander's decks vs. all Commander decks (positive = unique to
this commander). Salt score (on commander pages, roughly 0–4+) is worth citing for playgroup context.

---

## Source 3 — Commander Spellbook (combos)

**Find combos containing specific cards:**
`POST https://r.jina.ai/https://backend.commanderspellbook.com/find-my-combos` with
`{"commanders": ["Commander Name"], "main_board": ["Card 1", "Card 2", ...]}` →
`results.included` (all cards present) and `results.almost_included` (1–2 cards missing).

**Search by card:**
`https://r.jina.ai/https://backend.commanderspellbook.com/variants/?q=card%3D"{name}"` (URL-encode).

Each variant: `id`, `uses[]` (`{card: {name}, quantity}`), `requires[]`, `produces[]`,
`prerequisites`, `description`, `colorIdentity`, `status` (`OK` legal, `E` banned card involved),
permalink `https://commanderspellbook.com/combo/{id}/`.

Present each combo as: cards involved → prerequisites → steps (from `description`) → result (from
`produces`) → permalink. Show top `almost_included` results as near-combo upgrade suggestions.

---

## Source 4 — pricing (TCGplayer via Scryfall)

`prices.usd` = TCGplayer market price (weighted average of recent completed sales) — cite it as
"TCGplayer market price," not "cheapest available." For the cheapest print of a card, search with
`order=usd&dir=asc` instead. Use the printing actually in the decklist, not the globally cheapest
printing, unless pricing out a hypothetical swap. Default to non-foil unless asked otherwise. When
pricing a full list, batch via `/cards/collection`, sum, and flag any `null`-priced cards for manual
check rather than guessing.

---

## Source 5 — Set Delta Protocol (Temporal Cutoff Countermeasure)

LLMs inherently suffer from parametric training cutoff bias, favoring cards known during training and missing newer sets.
1. **Identify Cutoff Boundary:** Note model training cutoff date.
2. **Discover Delta Sets:** Fetch sets released since cutoff via Scryfall:
   `https://r.jina.ai/https://api.scryfall.com/sets`
   Filter for sets where `released_at >= <cutoff-date>` and `set_type in ["expansion", "commander", "masters", "draft_innovation"]`.
3. **Targeted Delta Search:** Execute a two-pronged search:
   - Historical staples & synergies via EDHRec / standard Scryfall queries.
   - Targeted post-cutoff query: `https://r.jina.ai/https://api.scryfall.com/cards/search?q=date%3E%3D{cutoff-date}+id%3C%3D{identity}+{mechanic_or_type}`.
4. **Cache Discoveries:** Write back any selected cards to `knowledgebase/_cache/scryfall-cards.json`.

---

## Workflow reference

**"What does [card] do?"** → Scryfall named lookup → rulings if the mechanic is complex/errata'd →
check `legalities.commander` → note `edhrec_rank` → flag color-identity fit if a deck is in context.

**"What synergizes with [commander]?"** → establish Active Color Identity → derive EDHRec slug →
fetch commander page → prioritize High Synergy Cards, then Ramp/Draw/Removal staples → validate
every card against the identity → enrich with Scryfall price/text as needed.

**"Does [card] combo with anything?"** → establish identity → `find-my-combos` with the card in
`main_board` → drop any result whose `colorIdentity` isn't a subset → present `included`, then
top in-color `almost_included` as upgrades.

**"How much does [card] cost?"** → Scryfall named lookup → `prices.usd` labeled market price
(+ `usd_foil` if relevant) → cheapest print via `order=usd&dir=asc` only if asked.

**"Build/suggest cards for [commander]"** → establish identity → build `id<=` filter → EDHRec
commander page, validate all suggestions → Spellbook combos, filter by identity → batch price
top picks → organize by category (ramp/draw/removal/synergy/combos) → flag budget vs. premium.

---

## Common mistakes to avoid

- Don't treat `prices.usd` as "cheapest" — it's median market price.
- Don't rely on memory for oracle text or color identity — always fetch fresh; errata and reprints
  happen. Never skip establishing the Active Color Identity first.
- Don't forget off-color activated-ability costs, or that colorless commanders can only run
  colorless cards (`id<=c`).
- Don't fabricate figures when a lookup fails or a source lacks data — say so instead of guessing.
- If direct (non-proxied) Scryfall/Spellbook access works in a given session, prefer it over the
  `r.jina.ai` proxy rather than defaulting to the proxy out of habit.
- Don't re-fetch a card that's already in `knowledgebase/_cache/scryfall-cards.json` with a fresh
  enough `fetched_at` — check the cache first, every time, not just when the proxy is visibly
  throttling.
- Don't leave a successful fetch out of the cache — every named-card lookup that succeeds should be
  written back, not just the ones for the current task.
