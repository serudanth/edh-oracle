---
type: profile
title: "J-Py — Deckbuilder Profile"
owner: j-py
tags: [#profile]
related: []
decks: knowledgebase/podlist/j-py/decks/
last_updated: 2026-08-22
---

## Overview
This profile is based on a single public decklist (Feather, the Redeemed, Boros spellslinger), so any pattern below is provisional — one deck cannot establish a real trend, only a starting impression. Within that one data point, the deck reads as a focused, on-theme build around a specific mechanical payoff (cheap targeted instants triggering Feather and other spells-matter creatures) rather than a generic goodstuff pile.

## Color & Archetype Tendencies
- Colors: White/Red (Boros).
- Commander: Feather, the Redeemed — a "spells that target your own creatures" payoff engine.
- The 96-card body is built tightly around that payoff: 30 instants (the largest category by far) and 7 sorceries, most of them cheap pump/protection spells (Defiant Strike, Gods Willing, Guided Strike, Shelter, Boon of Safety, Valorous Stance, Temur Battle Rage) rather than removal-heavy or ramp-heavy staples.
- Secondary sub-theme: prowess/spellslinger creatures that also benefit from a high spell count independent of Feather — Young Pyromancer, Guttersnipe, Electrostatic Infantry, Tenth District Legionnaire, Zada, Hedron Grinder — so the deck is doing double duty as both a Feather deck and a generic Boros spells deck.
- Light angel sub-theme (Giada, Font of Hope; Gisela, Blade of Goldnight; Anya, Merciless Angel; Akroma, Angel of Fury; two separate Aurelias) sits on top without being the deck's main engine.

## Power Level & Construction Habits
- No `power_level` or Archidekt bracket is recorded in the frontmatter or notes for this deck, unlike the template's expectation — worth checking the source link if a bracket number is needed later.
- Strict singleton discipline throughout; the only >1x entries are basic lands (12 Mountain, 12 Plains), exactly as expected for Commander.
- Card pool is a mix of format staples (Sol Ring, Path to Exile, Boros Charm, Command Tower, Austere Command) and clearly synergy-first, lower-power picks (Magnifying Glass, Crumb and Get It, Blacksmith's Skill, Sazacap's Brew) — reads as a deck tuned for its own game plan over raw power level.
- Only one board wipe (Austere Command) and minimal interaction outside combat tricks/protection spells — the deck leans aggressive/combo-ish rather than controlling.
- Ramp is light (Sol Ring, Talisman of Conviction only) — no dedicated ramp package, consistent with a curve that's cheap by design (lots of 1-2 mana instants).

## Notable Patterns
- Deck title ("Miku Madness!?!? Miku Sparta!!!") references Hatsune Miku, but the decklist itself contains no Universes Beyond or Miku cards — the name appears to be a meme/flavor title unrelated to the card pool, not a crossover-themed build.
- Land base is 37 lands, roughly two-thirds basics (24 of 37) with a modest but real nonbasic fixing/utility suite (Command Tower, Path of Ancestry, Boros Garrison, Furycalm Snarl, Stone Quarry, Abraded Bluffs, Wind-Scarred Crag, Temple of Triumph, two creature-lands in Needle Spires and Slayers' Stronghold, Windbrisk Heights, Sunhome) — enough fixing to support a two-color deck without over-investing in expensive nonbasics.
- Includes two different "Aurelia" legendaries (Aurelia, Exemplar of Justice and Aurelia, the Law Above) as non-commander creatures — plausibly a thematic/character preference rather than pure power-level optimization, since neither is the build-around.
- One foil-flagged pair (Feather, Radiant Arbiter and Boros Charm) suggests at least some cards were picked/kept for collectibility as well as function.

## Decks
Full decklist archive: `knowledgebase/podlist/j-py/decks/` (1 deck — see `INDEX.md` for the entry).

## External Cross-References
*Original pass 2026-07-10 via EDHREC + WebSearch fallback for Scryfall/Spellbook (lower-fidelity, per the `edh-research` skill's own note on that fallback). Re-verified 2026-08-22 with direct API access to all three sources — methodology note: mechanical reasoning off Feather's own text comes first, EDHREC/Spellbook checked after as a cross-check, not the justification.*

- **Feather's own ability, mechanically**: `{R}{W}{W}`, "whenever you cast an instant or sorcery that targets a creature you control, exile it instead of it going to the graveyard, return it to hand at the next end step." She's a recursion engine, not a discount or copy effect — the actual payoff for repeatedly recasting the same cheap spell comes from *other* cards that reward spell count (Young Pyromancer, Guttersnipe, Zada, Hedron Grinder, Electrostatic Infantry, Tenth District Legionnaire), exactly matching the profile's "double duty as Feather deck and generic Boros spells deck" read.
- **Archetype fit, updated**: fresh EDHREC data (13,382 decks on file now, salt 0.90 — Feather is a genuinely salty commander at the table) shows the tag order has flipped since the original check: **Spellslinger (1,220) is now the single largest theme, ahead of Sunforger (968)** — Voltron (576), Aggro (404), Cantrips (199) follow. This deck's build matches Spellslinger/Aggro/Cantrips.
- **Sunforger divergence, reframed**: at the original check Sunforger was the largest tag and this deck's lack of a Sunforger toolbox read as a real departure from "the" expected build. With Spellslinger now the more common archetype, that framing overstates it — this deck now matches what's actually the *most common* Feather build, and simply skips the second-most-common sub-archetype rather than diverging from the dominant one. Worth remembering EDHREC tag rankings aren't static; a "departure from the norm" claim has a shelf life.
- **Angel sub-theme, still secondary**: Angels remains a minor EDHREC theme relative to the primary archetypes, consistent with the profile's read that the angel package sits on top of the deck without being its engine.
- **High synergy-score overlap, re-confirmed**: Defiant Strike (82.0% synergy), Shelter (78.7%), Expedite (76.9%), Zada, Hedron Grinder (71.6%), and Fists of Flame (68.9%) are all EDHREC's top synergy cards for Feather and all appear in this exact list — numbers essentially unchanged from the original check despite the much larger current sample (11,000+ decks tracking each card vs. the original check's smaller base), so this specific finding held up well over time even where the Sunforger/Spellslinger ordering didn't.
- **No live combo, re-verified via whole-decklist check**: Commander Spellbook's `find-my-combos` endpoint against this exact 99 (not just a commander-level query, which is what the original pass used) returns zero included or near-included combos for this commander — confirms, with a more rigorous method than before, that this is a value/aggro shell with no assemblable combo.
- **Sazacap's Brew, confirmed as on-theme**: Oracle text (Scryfall via WebSearch) is `{1}{R}` instant — discard a card, target player draws two; if a Fish token is gifted to an opponent, target creature you control also gets +2/+0. It's a cheap instant that can target your own creature, fitting the deck's Feather/prowess payoff pattern rather than being pure card draw.
- **Crumb and Get It, confirmed as on-theme**: Oracle text is `{W}` instant — target creature you control gets +2/+2; if a Food token is gifted to an opponent, that creature also gains indestructible. A cheap, on-color combat trick/protection spell, consistent with the profile's "pump/protection" characterization.
- **Two Aurelias, refined read**: Aurelia, Exemplar of Justice (combat-trigger pump/keyword grant to one creature) and Aurelia, the Law Above (flying/vigilance/haste with attack-trigger draw and damage) are mechanically distinct, not near-duplicates — so including both isn't redundant. EDHREC also shows the two are frequently paired (27% deck overlap, 24% synergy) as a recognized support-piece combo rather than a purely idiosyncratic pick, which softens (but doesn't rule out) the profile's "thematic/character preference" read.
