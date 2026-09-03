---
type: profile
title: "Xanoh — Deckbuilder Profile"
owner: xanoh
tags: [#profile]
related: []
decks: knowledgebase/podlist/xanoh/decks/
last_updated: 2026-08-25
---

## Overview
| Profile Field | Assessment |
|---|---|
| Median Threat | **★★★★☆**\* |
| Designation | **Cohesion-First Control Strategist** |
| Summary | A deliberate planeswalker who builds from each commander's trigger outward, turning extra lands into escalating combat pressure in one deck and taxes, removal, wipes, and mass reanimation into inevitability in the other. The sample is small, but both lists are tightly sequenced engines with elevated threat and little wasted motion. |

xanoh has 2 decks evaluated by the EDH Oracle Analyzer Engine with a median Power Score of **7.1 / 10.0** (★★★★☆\*, mean **7.1**, range **6.7–7.4**, brackets 2–3). **Limited sample:** the four-star rating is provisional and describes these two observed decks (*Forresta* and *The Sundering*). Primary piloting archetypes are classified as **Big Mana / Landfall** (*Forresta*) and **Midrange / Engine Value** (*The Sundering*). Across 2 decks, the portfolio holds 5 tutors and 1 fast mana source. Automated analysis records are stored in `knowledgebase/podlist/xanoh/analysis/`.

## Color & Archetype Tendencies
Color identity across 2 decks:

| Color | Commander identities | Share |
|---|---:|---:|
| White | 1 | 50.0% |
| Blue | 0 | 0% |
| Black | 1 | 50.0% |
| Red | 1 | 50.0% |
| Green | 1 | 50.0% |
| Colorless | 0 | 0% |

- xanoh's two decks are narrow but highly intentional. Both begin with the commander's literal trigger and build the surrounding 99 to maximize it, rather than importing a generic version of the popular archetype.
- The two plans are structurally opposite: Forresta converts land acceleration into repeated combat growth, while The Sundering uses taxes, removal, and wipes to control the board before reanimating a large finish. Neither is a loose goodstuff deck.
- The result is strong internal cohesion and clear sequencing, but not broad evidence of a general construction style yet. Both decks use conventional land counts and artifact ramp, with no fast mana or assembled infinite combo.

## Power Level & Construction Habits
- Neither deck has an Archidekt bracket or `power_level` set — power tier isn't recorded for either, same gap as before.
- Forresta runs 35 lands, 2 mana dorks, and a dense ramp/land-recursion suite (Farseek, Migration Path, Reach the Horizon, Sylvan Scrying, Splendid Reclamation, Wrenn and Seven) that reads heavy even for a ramp deck — but the real reason is landfall-trigger count, not mana total. Migration Path and Reach the Horizon each put *two* lands onto the battlefield per casting (two landfall triggers per card), while the more commonly-run Cultivate/Nature's Lore/Rampant Growth put only one — a genuine edge for this specific commander that a "how much ramp" read would miss entirely.
- The Sundering runs 35 lands and no dedicated ramp package (just Arcane Signet and Sol Ring) — consistent with a leaner, cheaper-curve control shell rather than a big-mana plan.
- Both decks are fully singleton outside basics — no format-discipline issues.
- Fixing approaches differ for a structural reason, not just taste: Forresta leans on green ramp spells over a dual-heavy manabase, and in this specific 2-color list Farseek can *only* ever fetch a Mountain (its search text is Plains/Island/Swamp/Mountain — Forest is deliberately excluded from that template so green decks can't just grab a Forest with it), so it functions here as a narrow "fetch a Mountain," not a general fixer. The Sundering instead runs actual WB dual/pain lands (Godless Shrine, Shattered Sanctum, Silent Clearing, Scoured Barrens) since it has no ramp subtheme to fold fixing into.

## Notable Patterns
- Both decks are built from the commander's text outward. This is the strongest signal in the small sample: xanoh appears to optimize for mechanical coherence before adding generic staples.
- Forresta treats ramp as a trigger multiplier, not merely a way to reach expensive threats. The list favors land-search effects that create multiple landfall events and compounds those events with trigger and token multipliers.
- The Sundering uses a slower control sequence: taxes and neutralizing effects buy time, wipes reset the board, and mass reanimation turns the reset into a win. Its dense legendary creature base supports the commander but is not the primary engine.
- The decks share a preference for clear sequencing and conventional mana support, but not a common win condition. Neither relies on a cataloged infinite combo, leaving their strength in repeatable value and planned finishers.

## Decks
Full decklist archive: `knowledgebase/podlist/xanoh/decks/` (2 decks — see `INDEX.md` for the entries).

## External Cross-References

Methodology note: for each deck below, the mechanical read comes first — what the commander's own oracle text asks for, and whether specific card choices actually serve that — and EDHREC data is checked *against* that read afterward, not used as the justification itself. EDHREC's synergy/inclusion numbers describe what thousands of differently-skilled, differently-goaled players happened to co-play with a commander; that's a real signal worth checking, but it's a popularity aggregate, not a verdict on whether a card is good for *this* specific 99. Where the two agree, that's noted as agreement, not proof. Where they disagree, the disagreement is the interesting part.

### Forresta / Gladiolus Amicitia (EDHREC: 912 decks on file, salt 0.25 — a low-salt, casual-power commander)
- Gladiolus Amicitia's actual ability is a landfall *combat pump* (+2/+2 and trample to a target creature per land entering), not a ramp payoff. EDHREC's top tags for the commander (Lands Matter 64, Landfall 32, Ramp 23, by count in its own tag sample) read consistently with that — though "Ramp" ranking third is a bit misleading taken alone: ramp spells matter here as a *means* to more landfall triggers, not because the commander cares about total mana the way a cost-reduction or X-spell commander would.
- EDHREC's most-included ramp spells for this commander (Cultivate 507/912, Farseek 426, Nature's Lore 425, Rampant Growth 408) are the generic one-land ramp package any green deck runs. Forresta only carries Farseek from that list, running Migration Path and Reach the Horizon instead — both of which put two lands onto the battlefield per cast, doubling the landfall triggers per card compared to Cultivate/Nature's Lore/Rampant Growth. That's a mechanically stronger choice for *this* commander specifically. High inclusion on the popular three reflects "the default green ramp package," not "best card for this trigger" — this is a case where deviating from the crowd is the more correct build, not an eccentricity.
- Azusa, Lost but Seeking is EDHREC's #2 synergy card by score (0.45, 480/912 decks). That agrees with the mechanical read on its own terms: extra land drops multiply landfall triggers directly, so Azusa is a genuine engine piece here independent of its popularity — the popularity and the mechanical case just happen to point the same way.
- Ancient Greenwarden sits mid-pack by EDHREC inclusion (394/912, synergy 0.38) — well behind several other creatures in raw numbers. That ranking undersells its role in *this specific build*: this list runs eight separate landfall-triggered effects, so Greenwarden's "landfall triggers happen an additional time" clause doubles all eight simultaneously. A deck with only one or two landfall payoffs gets much less out of Greenwarden than this one does — EDHREC's aggregate number can't see that this build has an unusually dense landfall subpackage to multiply, so reading 394/912 as "moderately important" would understate its actual load-bearing role here.
- The earlier pass flagged Zell Dincht, Tifa Lockhart, Sabotender, and Sazh's Chocobo as "flavor-driven Final Fantasy picks riding EDHREC's synergy scores" — that holds up under a mechanical read too, not just a popularity one: all four have their own explicit landfall trigger (damage ping, +1/+1 counter, or power-doubling), making them structurally the same category of card as Scute Swarm or Chocobo Racetrack, just with Final Fantasy names instead of generic ones. The crossover flavor and the mechanical fit aren't competing explanations here — they're the same cards.
- Commander Spellbook: no cataloged combo involving Splendid Reclamation, Wrenn and Seven, or any other Forresta card with this commander (checked via the whole-decklist combo search, not a single-card query). This confirms the landfall package is a big, repeatable value/damage turn, not a hidden infinite.

### The Sundering / Ardbert, Warrior of Darkness (EDHREC: 6,878 decks on file — one of the more popular WB legendary commanders — salt 0.42, moderate)
- Ardbert's ability (a white spell cast puts a +1/+1 counter and vigilance on every legendary creature you control; a black spell does the same plus menace) rewards two things at once: a wide board of legendary creatures, and payoffs that capitalize on that board once it's buffed — anthems, counter-doublers, proliferate. EDHREC's top tags (+1/+1 Counters 659, Legends 648, Aggro 217) and high-synergy list (Flowering of the White Tree, Heroes' Podium, The Kenriths' Royal Funeral, Relic of Legends) are exactly that second half: payoffs for a buffed, wide, attacking legendary board.
- The Sundering independently satisfies the *first* half about as hard as this commander's colors allow — roughly 30 of its 32 creatures are legendary — but carries none of EDHREC's anthem/counter-payoff cluster: no Flowering of the White Tree, no Heroes' Podium, no proliferate effects. Mechanically, that means Ardbert's ability functions here as a passive bonus on whatever legendaries happen to be on board when a relevant spell resolves, not as the deck's engine. This isn't value left on the table so much as a deliberate choice: the deck's actual plan (prison effects, single-target Auras that neutralize instead of kill, symmetric wipes) doesn't want a wide board sitting around to protect and buff in the first place.
- That's a genuine, structural divergence from EDHREC's aggregate default, not an oversight or a budget/collection artifact: the popular build treats Ardbert as an aggro payoff commander (buff the team, swing wide); this build uses the same trigger as an incidental bonus attached to an unrelated control shell — Rule of Law / Ghostly Prison / Sigarda's Imprisonment / Trapped in the Tower for board control (the Aura-based removal specifically neutralizes rather than kills, dodging death-trigger interactions like reanimation or aristocrats payoffs an opponent might have), No Witnesses / Final Act for wipes, and Rise of the Dark Realms as the actual finisher off the back of those wipes.
- Kambal, Consul of Allocation is EDHREC's top creature by inclusion for this commander (3,939/6,878) as a generic WB tax/drain staple (punishes noncreature spells) — its presence here checks out on its own independent merits, not as a legendary-synergy pick. It's a generic-good-stuff card that happens to also be legendary, not evidence either way about how the deck engages with Ardbert's actual ability.
- Commander Spellbook: no cataloged combo for this commander with the current 99 (checked via the whole-decklist combo search). Rise of the Dark Realms following a wipe is a strong value/finisher line, not an infinite.
- Pricing was not looked up for either deck in this pass, per repo guidance that live price data isn't reliably obtainable in this environment.
