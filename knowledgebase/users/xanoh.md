---
type: profile
title: "Xanoh — Deckbuilder Profile"
owner: xanoh
tags: [#profile]
related: []
decklists: knowledgebase/decklists/xanoh/
last_updated: 2026-07-10
---

## Overview
Based on the single public decklist on file ("Forresta," a Gladiolus Amicitia RG deck), Xanoh leans toward big-mana Gruul ramp built around a strong Final Fantasy Universes Beyond flavor theme. With only one deck to go on, none of this generalizes reliably to how Xanoh builds outside of Gruul or outside a themed shell — it's one data point, not a pattern.

## Color & Archetype Tendencies
- Single data point: mono-Gruul (R/G), commander Gladiolus Amicitia.
- Core strategy is land ramp into large threats: Farseek, Migration Path, Sylvan Scrying, Roiling Regrowth, and Splendid Reclamation stack ramp and land recursion together.
- Secondary landfall/extra-land-drop subtheme (Azusa, Lost but Seeking; Moraug, Fury of Akoum; Scute Swarm; Omnath, Locus of Rage) pairs naturally with the ramp package rather than being bolted on.
- Light voltron/aura package (Blanchwood Armor, Hydra's Growth, Keen Sense, Lion Umbra) suggests comfort threatening quick damage off a single big creature, not just going wide.
- Doubling Season + From Beyond hints at a minor counters/tokens value line layered on top of the ramp shell rather than being the deck's main engine.

## Power Level & Construction Habits
- `power_level` field is blank and the Notes section carries no Archidekt bracket number — this deck's intended power tier isn't recorded, only inferable from card choices.
- Card pool mixes recognizable EDH staples (Doubling Season, Seedborn Muse, Lightning Greaves, Farseek, Sylvan Scrying, Krosan Grip) with a large number of flavor-driven Final Fantasy picks of more modest raw power, suggesting theme is weighted at least as heavily as raw efficiency.
- Fully singleton outside basic lands (10 Forest, 10 Mountain) — no format-discipline issues.
- 35 lands plus two mana dorks (Birds of Paradise, Llanowar Elves) and a half-dozen ramp spells is a notably heavy ramp count, consistent with a top end of large/expensive threats (Etali, Primal Storm; Ancient Greenwarden; Jumbo Cactuar; Omnath, Locus of Rage).
- Land base is mostly basics and utility lands (Castle Garenbrig, Rogue's Passage, Reliquary Tower) rather than a dual-heavy fixing suite — fixing leans on green ramp spells more than the manabase itself.

## Notable Patterns
- Roughly a third of the maindeck (creatures, spells, artifacts, and even a land) are Final Fantasy crossover cards — this isn't just a themed commander pick, the whole deck is built to lean into the FF flavor (Summon: Bahamut/Fenrir/Titan, Tifa Lockhart, Rydia, Zell Dincht, Chocobo Racetrack, Gongaga Reactor Town, etc.).
- Splendid Reclamation + Roiling Regrowth + fetch-style ramp (Farseek, Migration Path) forms a coherent "sac/discard lands now, get them all back at once" sub-package rather than isolated ramp spells — a bit more constructed than a generic goodstuff ramp shell.
- Four foil cards recorded (Gran Pulse Ochu, Airship Crash, Blessed Respite, Rising of the Day), all Final Fantasy-themed cards, suggesting foils were acquired/prioritized specifically for the crossover pieces rather than across the whole deck.
- No stax, counterspells, or heavy interaction package — the deck's answers are narrow (Krosan Grip as the lone piece of dedicated removal-ish interaction), consistent with a ramp-and-go-big plan more than a controlling one.

## Decks
Full decklist archive: `knowledgebase/decklists/xanoh/` (1 deck — see `INDEX.md` for the entry).

## External Cross-References

- **EDHREC commander page** (`json.edhrec.com/pages/commanders/gladiolus-amicitia.json`, 59 decks on file) tags Gladiolus Amicitia's primary themes as Lands Matter, Landfall, and Ramp, in that order — the profile's "secondary landfall/extra-land-drop subtheme" undersells it a bit; per EDHREC's own data, landfall is closer to co-primary with ramp for this commander, not a bolt-on.
- Azusa, Lost but Seeking is EDHREC's #2 highest-synergy card for this commander (0.458 synergy, 460 inclusions) — the profile's read of Azusa as core to the landfall package is well-supported, not a flavor pick.
- Several FF crossover cards the profile calls "flavor-driven ... of more modest raw power" are actually among EDHREC's top synergy cards for this commander: Zell Dincht (#1, 0.517), Tifa Lockhart (#3, 0.437), Sabotender (#4, 0.429), Sazh's Chocobo (#5, 0.415), Ancient Greenwarden (#6, 0.379). These aren't just theme picks riding along with a generic ramp shell — the deck's flavor picks and its statistically-strongest build overlap heavily.
- EDHREC's top *popular* ramp staples for this commander (Cultivate, Nature's Lore, Rampant Growth) are notably absent from Forresta's list, which instead leans on Farseek, Migration Path, and Sylvan Scrying — consistent with the profile's read that the manabase leans on green ramp spells rather than fixing lands, just via a different spell selection than the field's default.
- Commander Spellbook has no cataloged combo for Splendid Reclamation + Roiling Regrowth (or + Farseek/Migration Path). The only Splendid Reclamation combos on file require additional pieces not in this deck (Underworld Breach + Squandered Resources; Archelos + Mystic Sanctuary; Mirrorpool + Zuran Orb). This confirms the profile's framing: it's a strong synergy sub-package, not a combo finish.
- Summon: Bahamut's oracle text (via WebSearch/Scryfall) is a Saga creature: chapters I–II each destroy up to one target nonland permanent, III draws two cards, IV ("Mega Flare") deals damage to each opponent equal to the total mana value of other permanents its controller controls. In a ramp shell full of expensive threats (Etali, Ancient Greenwarden, Omnath, Jumbo Cactuar), that chapter IV scales into a genuine finisher — worth refining the profile's "modest raw power" characterization for this specific card, even if most of the other FF picks still fit that description.
- Chocobo Racetrack (Artifact, not a land, despite the name) confirmed via oracle text: "Landfall — Whenever a land you control enters, create a 2/2 green Bird creature token with 'Whenever a land you control enters, this token gets +1/+0 until end of turn.'" This is a direct landfall payoff that also produces a growing token, adding a minor go-wide angle that reinforces the profile's note about Doubling Season/From Beyond as a token subtheme layered on the ramp shell.
- Pricing was not looked up for this profile, per repo guidance that live price data isn't reliably obtainable in this environment.
