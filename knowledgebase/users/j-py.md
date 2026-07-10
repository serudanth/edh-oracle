---
type: profile
title: "J-Py — Deckbuilder Profile"
owner: j-py
tags: [#profile]
related: []
decklists: knowledgebase/decklists/j-py/
last_updated: 2026-07-10
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
Full decklist archive: `knowledgebase/decklists/j-py/` (1 deck — see `INDEX.md` for the entry).

## External Cross-References
*Checked 2026-07-10 against EDHREC (`json.edhrec.com/pages/commanders/feather-the-redeemed.json`), Scryfall (via WebSearch), and Commander Spellbook (via WebSearch); pricing skipped per this repo's analysis practices.*

- **Archetype fit, confirmed**: EDHREC's top themes for Feather are Sunforger (1,260 decks), Spellslinger (1,197), Voltron (556), Aggro (385), Cantrips (199), and Burn (170) — this deck's cheap-instant/prowess build (Young Pyromancer, Guttersnipe, Zada) squarely matches the Spellslinger/Aggro/Cantrips lane, not the Sunforger lane.
- **Sunforger divergence**: Sunforger is EDHREC's single largest Feather theme (1,260 decks) but the deck contains neither Sunforger itself nor a toolbox of fetchable instants built around it — a real, notable departure from the "expected" Feather build, not just a minor omission.
- **Angel sub-theme, confirmed as secondary**: EDHREC tags Angels as a minor theme (42 deck inclusions) rather than a primary archetype, consistent with the profile's read that the angel package (Giada, Gisela, Anya, Akroma, both Aurelias) sits on top of the deck without being its main engine.
- **Ramp read, confirmed**: EDHREC's own popular-card list for Feather leans on cheap mana rocks/Wayfarer's Bauble rather than a dedicated ramp suite, so this deck's minimal ramp (Sol Ring + Talisman of Conviction only) tracks the archetype norm rather than being an outlier.
- **High synergy-score overlap**: Several of EDHREC's top synergy cards for Feather appear in this exact list — Defiant Strike (81.9% synergy), Shelter (78.8%), Expedite (76.9%), Zada, Hedron Grinder (71.5%), and Fists of Flame (68.9%). The deck isn't just thematically on-genre, it's drawing directly from the commander's highest-synergy staples.
- **No live combo, confirmed**: Commander Spellbook lists infinite-turn combo lines for Feather, all built on Feather + Sage of Hours + a pump/fight spell that returns from exile (Increasing Savagery, Infuse with the Elements, or Strength of the Tajuru), plus a separate Verdant Confluence line. This decklist has none of those pieces (no Sage of Hours, no Verdant Confluence, none of the three exile-return spells) — supports the profile's read that this is a value/aggro shell with no assemblable combo, not an oversight in the profile.
- **Sazacap's Brew, confirmed as on-theme**: Oracle text (Scryfall via WebSearch) is `{1}{R}` instant — discard a card, target player draws two; if a Fish token is gifted to an opponent, target creature you control also gets +2/+0. It's a cheap instant that can target your own creature, fitting the deck's Feather/prowess payoff pattern rather than being pure card draw.
- **Crumb and Get It, confirmed as on-theme**: Oracle text is `{W}` instant — target creature you control gets +2/+2; if a Food token is gifted to an opponent, that creature also gains indestructible. A cheap, on-color combat trick/protection spell, consistent with the profile's "pump/protection" characterization.
- **Two Aurelias, refined read**: Aurelia, Exemplar of Justice (combat-trigger pump/keyword grant to one creature) and Aurelia, the Law Above (flying/vigilance/haste with attack-trigger draw and damage) are mechanically distinct, not near-duplicates — so including both isn't redundant. EDHREC also shows the two are frequently paired (27% deck overlap, 24% synergy) as a recognized support-piece combo rather than a purely idiosyncratic pick, which softens (but doesn't rule out) the profile's "thematic/character preference" read.
