---
type: profile
title: "mjsnoozer — Deckbuilder Profile"
owner: mjsnoozer
tags: [#profile]
related: []
decks: knowledgebase/podlist/mjsnoozer/decks/
last_updated: 2026-08-25
---

## Overview
| Profile Field | Assessment |
|---|---|
| Median Threat | **★★★★☆** |
| Designation | **Burst-Momentum Artificer** |
| Summary | An aggressive planeswalker who turns every attack, copied incantation, token, and Treasure into momentum, building toward sudden bursts of cards, mana, and damage. The engines are coherent and capable of explosive turns, but lean mana and limited interaction make the portfolio less forgiving when the first surge is stopped. |

mjsnoozer has 5 decks evaluated by the EDH Oracle Analyzer Engine with a median Power Score of **7.2 / 10.0** (★★★★☆), a mean of **7.0**, and a range of **5.4–8.3** (brackets 2–3). Archetypes span **Spellslinger / Storm** (2 decks), **Midrange / Engine Value** (2 decks), and **Voltron / Equipment** (1 deck). Across 5 decks, the portfolio holds 12 tutors and 7 fast mana sources. Automated analysis records are stored in `knowledgebase/podlist/mjsnoozer/analysis/`.

Across four active decks, mjsnoozer consistently chooses proactive engines that can create sudden bursts of cards, mana, combat damage, or copied spells. The builds are coherent, but their low land counts make early development less forgiving, and none has a recorded bracket or confirmed live infinite.

## Color & Archetype Tendencies
Color identity across 4 active decks; retired Stella Lee is excluded:

| Color | Commander identities | Share |
|---|---:|---:|
| White | 1 | 25.0% |
| Blue | 2 | 50.0% |
| Black | 2 | 50.0% |
| Red | 3 | 75.0% |
| Green | 2 | 50.0% |
| Colorless | 0 | 0% |

- mjsnoozer favors proactive engines that generate resources through action: equipped attackers draw cards, attacking Azula copies spells, Hazel multiplies tokens, and Kenway converts tapped creatures into Treasures. Each deck turns its central commander trigger into momentum.
- The portfolio is more midrange and burst-oriented than controlling. Threats are developed through creatures, artifacts, and combat, then amplified in a decisive turn; broad removal and defensive redundancy are less central than acceleration and payoff density.
- The lists show practical adaptation rather than a single repeated shell. Azula inherited a spell package from Stella Lee, but Cloud, Hazel, and Kenway use different resource engines. The main structural weakness is mana margin, especially in Kenway's 25-land build.

## Power Level & Construction Habits
- None of the four active Archidekt imports has a bracket number recorded — power level has to be inferred from card choices.
- Land counts sit below the 36-40 norm across the board: Cloud 32, Azula 35, Hazel 37, Kenway 25 (extreme outlier, propped up by Sol Ring + 3 guild Signets + 3 Talismans + Chromatic Lantern).
- Azula carries real storm/combo-adjacent pieces (Dark Ritual, Seething Song, Mizzix's Mastery, Grapeshot, Isochron Scepter, Twinning Staff) inherited from the Stella Lee build, but as currently constructed this reads as a strong non-infinite value/storm-adjacent package rather than a live cEDH combo line — see the Commander Spellbook check below, which found no assemblable infinite combo in the deck as built. Twinning Staff is worth flagging as a build-around specifically for *this* commander though: it also triggers off Azula's own attack-trigger copy, not just spells copied by casting, so a resolved Twinning Staff turns her "copy the spell" into "copy it twice" automatically.
- Cloud and Hazel read as more conventional midrange (equipment-voltron-but-wide, and token/aristocrats value respectively), with ramp spells substituting for a full land count rather than fast mana.
- Foils are concentrated in Cloud (Cloud, Planet's Champion; Buster Sword; Mantle of the Ancients; Thornspire Verge) and Azula (Bria, Riptide Rogue; Enduring Curiosity) — no foils recorded in Hazel or Kenway, suggesting these two are the more personally-invested active builds.

## Notable Patterns
- The active decks all seek resource generation through action rather than passive control: attacks draw cards or create Treasures, spells are copied, and tokens are multiplied. This gives the portfolio a consistent preference for momentum and visible board development.
- The four lists occupy different engine spaces, but Azula and Cloud are the clearest examples of payoff-first construction. Cloud needs many equipped attackers instead of one voltron threat, while Azula needs combat-window spell timing and flash support to convert attacks into advantage.
- Mana is treated as a constraint to solve with artifacts and cost reduction. The approach supports explosive turns, but the low land totals, especially Kenway's 25, make missed land drops more punishing than in a conventional midrange portfolio.
- The retired Stella Lee list matters as construction history, not as a separate pattern: Azula inherited its spell core. The active decks therefore show adaptation around a few proven engines more than broad experimentation with control or combo.

## Decks
Full decklist archive: `knowledgebase/podlist/mjsnoozer/decks/` (5 decks on file — 4 active, 1 retired; see `INDEX.md` for individual entries).

## External Cross-References

Methodology note: mechanical reasoning off each commander's own oracle text comes first (see Color & Archetype Tendencies above); EDHREC and Commander Spellbook are checked afterward as a "does this hold up independently" cross-check, not cited as the justification itself.

**Commander Spellbook — is the Azula/Stella-Lee-inherited shell an actual infinite combo, in Azula as built?**
- Confirmed named combo: **Storm-Kiln Artist + Seething Song + Reiterate** (infinite mana/Treasures/storm) — Azula doesn't run Reiterate, so this line isn't assemblable.
- Confirmed named combo: **Veyran, Voice of Duality + Storm-Kiln Artist + View from Above** — Azula doesn't run View from Above.
- Confirmed named combo: **Isochron Scepter + Dramatic Reversal** — Azula runs Isochron Scepter but not Dramatic Reversal (Dramatic Reversal was in the old Stella Lee list, not carried over).
- Mizzix's Mastery's only cataloged combo is with Worldfire, which isn't in the list — it functions as a big one-shot spell-recursion payoff here, not a combo piece.
- **Verdict unchanged from the prior pass**: strong non-infinite storm/spellslinger value package, one specific missing card away from several different cataloged infinites, not a live combo engine as built today.

**EDHREC — sanity checks on the four active decks (used to check the mechanical read above, not to establish it)**
- Cloud, Ex-SOLDIER: top tags Equipment (2,594 decks), Voltron (1,474), Artifacts (559) — consistent with the mechanical read, though "Voltron" undersells that Cloud's own draw trigger specifically wants multiple equipped attackers rather than a single stacked creature; EDHREC's tag doesn't distinguish those two shapes of "equipment deck." Puresteel Paladin (0.864 synergy) and Sram, Senior Edificer both show as top synergy cards, agreeing with the mechanical case made above for why free/cheap equip costs matter here specifically.
- Fire Lord Azula: tags Spellslinger (1,881), Combo (610), Spell Copy (581), Storm (367) — Spell Copy ranking is the one that actually matches this commander's literal ability (copying cast spells); Storm and Combo reflect the generic Izzet-adjacent card pool more than Azula's own text, which doesn't care about storm count directly.
- Hazel of the Rootbloom: tags Tokens (2,010), Aristocrats (856), Squirrels (650), Sacrifice (260) — Squirrels ranking third rather than first is notable given Hazel's own ability rewards Squirrel tokens specifically over generic tokens; Chatterfang's presence in this list (converting the whole token package to Squirrel-flavored) is exactly the kind of build choice that would close that gap between the commander's actual preference and a more generic token-based build.
- Edward Kenway (lighter check): tags Pirates (3,001), Treasure (2,922), Vehicles (1,381) — matches the mechanical read; Kenway's own ability isn't Vehicle-specific for the Treasure half (any tapped Assassin/Pirate/Vehicle counts), so the deck's heavy Pirate-tribal lean is a choice layered on top of a broader-than-Pirates-alone trigger, not a requirement of the card itself.
- Roaming Throne (in the Kenway list) is worth flagging on its own merits, independent of any EDHREC ranking: choosing Pirate or Assassin as its type lets it double Kenway's own end-step Treasure trigger, since Kenway qualifies as both — a commander-specific interaction, not generic tribal glue.

*Pricing not looked up, consistent with repo guidance that live price data isn't reliably obtainable in this environment.*
