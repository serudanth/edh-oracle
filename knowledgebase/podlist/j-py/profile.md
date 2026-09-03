---
type: profile
title: "J-Py — Deckbuilder Profile"
owner: j-py
tags: [#profile]
related: []
decks: knowledgebase/podlist/j-py/decks/
last_updated: 2026-08-25
---

## Overview
| Profile Field | Assessment |
|---|---|
| Median Threat | **★★★★☆**\* |
| Designation | **Recursive Combat Spellcaster** |
| Summary | A battle-mage planeswalker who recycles cheap targeted spells into a growing storm of cards, tokens, prowess, and protection, pressing the attack through a chosen champion while accepting that stalled combat and broad disruption can halt the assault. |

j-py has 1 eligible deck evaluated by the EDH Oracle Analyzer Engine at a Power Score of **7.6 / 10.0** (★★★★☆\*, Bracket 3). **Limited sample:** the four-star rating describes this single observed deck only (*Miku Madness!?!? Miku Sparta!!!*). Its primary piloting archetype is classified as **Spellslinger / Storm** (high instant/sorcery density with cheap targeted instant recycling). Automated analysis file is stored in `knowledgebase/podlist/j-py/analysis/miku-madness-miku-sparta.json`.

With one deck, the clearest pattern is a focused Feather spellslinger plan: cheap targeted instants recur for value while prowess and token payoffs turn repeated casting into pressure. The list is light on ramp, sweepers, and broad interaction.

## Color & Archetype Tendencies
Color identity across 1 active deck:

| Color | Commander identities | Share |
|---|---:|---:|
| White | 1 | 100% |
| Blue | 0 | 0% |
| Black | 0 | 0% |
| Red | 1 | 100% |
| Green | 0 | 0% |
| Colorless | 0 | 0% |

- j-py builds a single, tightly focused engine: Feather rewards repeatedly casting cheap spells that target friendly creatures, and the rest of the deck converts that repetition into cards, tokens, prowess, and combat damage.
- The deck is aggressive and protection-oriented rather than controlling. Its interaction is mostly attached to combat tricks, with only one sweeper and a very small ramp package, so it wants to keep pressure on the table instead of trading resources broadly.
- The list shows a preference for synergy density over raw card quality. The angel package is secondary, while Zada and the other spells-matter creatures provide redundancy when Feather is unavailable.

## Power Level & Construction Habits
- No `power_level` or Archidekt bracket is recorded in the frontmatter or notes for this deck, unlike the template's expectation — worth checking the source link if a bracket number is needed later.
- Strict singleton discipline throughout; the only >1x entries are basic lands (12 Mountain, 12 Plains), exactly as expected for Commander.
- Card pool is a mix of format staples (Sol Ring, Path to Exile, Boros Charm, Command Tower, Austere Command) and clearly synergy-first, lower-power picks (Magnifying Glass, Crumb and Get It, Blacksmith's Skill, Sazacap's Brew) — reads as a deck tuned for its own game plan over raw power level.
- Only one board wipe (Austere Command) and minimal interaction outside combat tricks/protection spells — the deck leans aggressive/combo-ish rather than controlling.
- Ramp is light (Sol Ring, Talisman of Conviction only) — no dedicated ramp package, consistent with a curve that's cheap by design (lots of 1-2 mana instants).

## Notable Patterns
- The deck is built around redundancy rather than a single fragile combo: Feather, Zada, Young Pyromancer, Guttersnipe, and prowess creatures all reward the same high volume of cheap targeted spells in different ways.
- Its strongest turns are recursive and explosive, but its interaction is mostly protective or combat-based. That makes the deck good at forcing damage through and preserving an engine, less good at answering a developed opposing board.
- The 37-land base is conservative for the low curve and compensates for the unusually light ramp package. This is a deliberate trade: reliable land drops support repeated spell turns, while card slots remain committed to the central engine.
- The list's main limitation is conversion. It can generate a large board or a tall attacker, but it has no confirmed infinite and few sweepers, so stalled combat or repeated board wipes are difficult to recover from.

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
