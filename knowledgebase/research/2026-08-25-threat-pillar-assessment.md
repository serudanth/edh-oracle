---
type: reference
title: "Threat Assessment Methodology — Deck and Portfolio Percentiles"
domain: strategy
tags: [#pod, #threat, #reference, #methodology, #percentile]
related: [podlist/fowlplays/profile, podlist/j-py/profile, podlist/lto888/profile, podlist/mjsnoozer/profile, podlist/reimaru/profile, podlist/xanoh/profile]
source: decklist composition audit
last_updated: 2026-08-25
---

## Purpose

This methodology estimates threat from deck composition, not from pilot skill, spending, reputation, or observed game results. It is designed for comparing fully built Commander decks from decklists and available card metadata alone.

Retired decks, concept boards, and mid-build stubs are excluded. A deck's score is a percentile from 0 to 100, not a claim that it will win a specific game.

## What A Percentile Means

A deck percentile describes the deck's position within a named comparison pool:

- **Pod percentile:** relative to the eligible decks currently assessed in this pod.
- **Benchmark percentile:** relative to a stable reference pool of Commander decklists, if one has been established.

These must never be presented as interchangeable. A pod percentile answers "how threatening is this deck compared with these decks?" It does not answer "how threatening is this deck compared with every Commander deck ever built?"

Until a stable external benchmark exists, use pod-relative percentiles and label them clearly. Do not infer a percentile from the letter ranks in the retired four-pillar system.

## Deck Dimensions

Each dimension is independently assessed from 0 to 100 percentile points. The assessor records evidence from the list before assigning the percentile. Scores should be rounded to the nearest whole number and should not imply more precision than the comparison pool supports.

| Dimension | Evidence to assess |
|---|---|
| Speed | Early mana, low curve, haste, explosive starts, and the earliest credible pressure or win window |
| Consistency | Tutors, redundancy, cheap selection, commander access, density of enablers, and number of functional opening hands |
| Resource Development | Ramp, fixing, cost reduction, card advantage, recursion, and repeatable engines that convert mana into material |
| Interaction | Removal, countermagic, protection, disruption, stack interaction, graveyard hate, and ability to answer varied threats efficiently |
| Resilience | Recovery after removal or a board wipe, commander dependence, redundancy, recursion, and ability to operate through disruption |
| Win Conversion | Clarity, compactness, redundancy, speed, and reliability of the deck's actual closing routes |

Speed and Win Conversion are separate: a deck can win decisively once assembled but be slow to assemble, while another can apply early pressure without a reliable close. Consistency and Resilience are also separate: a deck may find its plan often but fold when the first attempt is stopped.

## Percentile Anchors

Percentiles are assigned comparatively, using the following anchors as a guide rather than as rigid bands:

| Percentile | Interpretation |
|---:|---|
| 0-19 | Bottom of the comparison pool; little meaningful contribution |
| 20-39 | Below average; narrow, slow, fragile, or inconsistent support |
| 40-59 | Typical functional Commander support |
| 60-79 | Above average; strong, redundant, or efficient support |
| 80-94 | High-end support; unusually dense, flexible, or reliable |
| 95-100 | Exceptional relative to the named pool; reserve 100 for the strongest observed examples |

The same card should not receive a fixed score in every deck. Context matters: a tutor that finds a compact win is more consequential than one that finds a role-player, and a removal spell in a deck unable to hold mana is less useful than its text suggests.

## Composite Deck Threat Index

The composite is a weighted 0-100 index built from the six dimension percentiles. It is deliberately called an index rather than a percentile: averaging percentiles does not guarantee that the result itself occupies the same rank position in the comparison pool.

```text
Deck Threat Index =
	(Speed x 20%) +
	(Consistency x 20%) +
	(Resource Development x 15%) +
	(Interaction x 15%) +
	(Resilience x 15%) +
	(Win Conversion x 15%)
```

Weights may be changed only by revising this methodology and recalculating every deck. The default weighting gives early action and reliable access to the plan slightly more influence, while preventing interaction or a theoretical combo from determining the entire result.

The index is a ranking aid, not a seventh independent claim. Always retain the six component percentiles so a deck's threat profile remains explainable.

## Calculating Percentiles

For a comparison pool of `n` decks, rank each dimension from least to most threatening. Tied decks receive the average of their occupied ranks. Convert a rank to a percentile with:

```text
Percentile = 100 x (rank - 1) / (n - 1)
```

When `n = 1`, report **not enough data** rather than assigning 0 or 100. For a small pod, retain the underlying evidence and treat close values as ties; the percentile is a position within that sample, not a measurement with laboratory precision.

## Threat Profile

Alongside the composite, label the deck's dominant threat mode using its dimensions:

- **Explosive:** Speed and Consistency are high.
- **Control:** Interaction and Resilience are high.
- **Engine:** Resource Development and Consistency are high.
- **Inevitable:** Resilience and Win Conversion are high.
- **Combat:** Speed and Win Conversion are high, with damage-based closing routes.
- **Unfocused:** no dimension is clearly high, or the plan lacks sufficient redundancy.

These labels describe how the deck becomes dangerous. They are not additional points and a deck may have more than one label.

## Player Portfolio Assessment

The player-level assessment must expose both typical and peak threat. Report:

| Statistic | Meaning |
|---|---|
| Median deck percentile | Primary measure of the player's typical eligible deck |
| Mean deck percentile | Supporting measure of the portfolio as a whole |
| Highest deck percentile | Maximum threat if the player's strongest deck is brought |
| Lowest deck percentile | Useful context for casual or lower-power selections |
| Eligible deck count | Sample size and confidence context |
| Threat modes | Recurring ways the portfolio creates danger |

Use the median as the primary portfolio figure. The mean remains useful, but it should not outrank the median when one outlier or a very large portfolio distorts the result. A one- or two-deck portfolio must be marked **limited sample**, regardless of its percentile.

Do not convert the player median into a separate letter rank. Use the percentile and plain-language bands:

| Percentile | Portfolio description |
|---:|---|
| 0-19 | Low |
| 20-39 | Below average |
| 40-59 | Typical |
| 60-79 | Elevated |
| 80-94 | High |
| 95-100 | Exceptional |

## Assessment Procedure

1. Confirm that the deck is active and sufficiently built to assess.
2. Identify the commander-independent plan, commander-enabled plan, and actual win routes.
3. Record observable evidence for each of the six dimensions.
4. Rank the deck against the named comparison pool for each dimension.
5. Assign six 0-100 percentiles, then calculate the weighted composite.
6. Record one or more threat-mode labels and a short evidence-based explanation.
7. For each player, calculate median, mean, highest, lowest, and eligible deck count.
8. Recalculate all affected decks when the comparison pool or weighting rules change.

## Limitations

This system cannot observe mulligans, piloting, threat assessment, politics, sequencing errors, table composition, or whether a player chooses to bring a particular deck. It also cannot establish a universal percentile without a stable benchmark population.

Percentile differences smaller than roughly five points should usually be treated as ties unless the underlying evidence is materially different. A high percentile means the deck is composed to produce threat efficiently relative to the comparison pool; it does not guarantee an early win or predict a player's behavior.

The previous four-pillar 0-40 scores and D-to-SSS ranks are **legacy results**. They must not be averaged, converted, or displayed alongside the new percentiles as though they were the same scale. Existing deck and profile assessments require a fresh percentile pass before they can claim new scores.
## Current Percentile Assessment

The following is the fresh assessment of the 48 eligible decks in this pod. Percentiles are pod-relative, rounded to whole points; the weighted index is rounded to one decimal. The two LTO888 one-card stubs and mjsnoozer's retired Stella Lee are excluded. Modes are descriptive labels from the methodology, not extra points.

| Player | Deck | Speed | Consistency | Resource Development | Interaction | Resilience | Win Conversion | Deck Threat Index | Modes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| fowlplays | The Best of Friends | 44 | 42 | 48 | 42 | 54 | 48 | **46.0** | Unfocused |
| fowlplays | The Copied Factory | 78 | 86 | 72 | 82 | 58 | 48 | **71.8** | Explosive, Engine |
| fowlplays | The Crystal Braves | 56 | 66 | 60 | 64 | 62 | 60 | **61.3** | Engine |
| fowlplays | The Dirt Kicker | 36 | 44 | 38 | 32 | 46 | 46 | **40.3** | Unfocused |
| fowlplays | The Gate of Babylon | 46 | 50 | 42 | 40 | 50 | 56 | **47.4** | Combat |
| fowlplays | The Hamster Catapult | 60 | 56 | 44 | 34 | 52 | 68 | **52.9** | Combat |
| fowlplays | The Koronation | 54 | 50 | 48 | 38 | 52 | 66 | **51.4** | Combat |
| fowlplays | The Last Ride | 52 | 50 | 44 | 36 | 48 | 62 | **48.9** | Combat |
| fowlplays | The Lorehold Redux | 50 | 60 | 56 | 48 | 70 | 66 | **58.0** | Engine, Inevitable |
| fowlplays | The Master Chef | 48 | 56 | 50 | 44 | 58 | 60 | **52.6** | Combat |
| fowlplays | The Queen of Theft | 48 | 74 | 78 | 78 | 70 | 72 | **69.1** | Control, Engine, Inevitable |
| fowlplays | The Rush | 92 | 88 | 74 | 86 | 56 | 100 | **83.4** | Explosive, Control, Combat |
| fowlplays | The Warrior of Darkness | 44 | 50 | 58 | 58 | 64 | 54 | **53.9** | Control, Inevitable |
| lto888 | Bau Bau Nyaa | 54 | 58 | 46 | 42 | 52 | 62 | **52.7** | Combat |
| lto888 | Celes Recursion | 58 | 72 | 62 | 56 | 78 | 68 | **65.6** | Engine, Inevitable |
| lto888 | Lightning Equip / Extra Attacks | 72 | 68 | 54 | 58 | 58 | 78 | **65.2** | Explosive, Combat |
| lto888 | Maralen Faelves | 60 | 68 | 70 | 68 | 64 | 62 | **65.2** | Engine, Control |
| lto888 | Prismari Artistry | 62 | 70 | 48 | 52 | 56 | 70 | **60.3** | Engine, Combat |
| lto888 | Sephiroth Pain is Love | 82 | 90 | 82 | 88 | 94 | 98 | **88.7** | Explosive, Control, Engine, Inevitable |
| lto888 | So I Started Blasting (with Azula) | 70 | 82 | 64 | 72 | 64 | 76 | **71.8** | Explosive, Engine |
| lto888 | Squirrels! | 74 | 76 | 48 | 46 | 62 | 86 | **66.3** | Explosive, Combat |
| lto888 | Y'shtola Slingy Wingy | 84 | 94 | 96 | 98 | 90 | 82 | **90.5** | Explosive, Control, Engine, Inevitable |
| lto888 | Yuna Enchantress | 54 | 68 | 42 | 40 | 72 | 66 | **57.4** | Engine, Inevitable |
| lto888 | Yuriko Good Ol' Ninjas | 72 | 74 | 54 | 50 | 64 | 74 | **65.5** | Explosive, Combat |
| lto888 | Turtle Power, Powered | 62 | 64 | 50 | 46 | 58 | 70 | **58.8** | Engine, Combat |
| reimaru | Aura Battler Feather | 46 | 56 | 42 | 36 | 62 | 54 | **49.5** | Inevitable |
| reimaru | Feather's Spell All You Can | 68 | 76 | 48 | 50 | 62 | 72 | **63.6** | Explosive, Combat |
| reimaru | Marneus Calgar, Captain of Tokens | 54 | 58 | 40 | 38 | 52 | 64 | **51.5** | Combat |
| reimaru | Miirym, Miirym on the Wall | 58 | 56 | 38 | 34 | 48 | 66 | **50.7** | Combat |
| reimaru | Saheeli Copy Brilliance | 64 | 74 | 48 | 48 | 62 | 70 | **61.8** | Engine, Combat |
| reimaru | Saruman's Mighty Meaty Army | 54 | 70 | 62 | 54 | 68 | 64 | **62.0** | Engine, Control |
| reimaru | Silverquill Likes to Bring a Crowd | 54 | 66 | 54 | 50 | 64 | 68 | **59.4** | Engine, Combat |
| reimaru | Siona's Enchanting Soldiers | 52 | 58 | 38 | 36 | 56 | 62 | **50.8** | Combat |
| reimaru | Solphim and Suffering | 64 | 54 | 36 | 34 | 44 | 66 | **50.6** | Combat |
| reimaru | Stop Sac'ing, Sephiroth | 76 | 82 | 58 | 62 | 82 | 88 | **75.1** | Explosive, Engine, Inevitable |
| reimaru | Swords and Slicer | 82 | 52 | 34 | 38 | 48 | 74 | **55.9** | Explosive, Combat |
| reimaru | Syr Gwyn, Armed and Crazy | 60 | 64 | 50 | 46 | 58 | 74 | **59.0** | Combat |
| reimaru | That's a Lot of Swords, Cloud | 54 | 58 | 44 | 40 | 62 | 66 | **54.2** | Inevitable, Combat |
| reimaru | Thraximundar, Lord of Sacs | 52 | 64 | 58 | 52 | 68 | 68 | **60.1** | Engine, Inevitable |
| reimaru | Where're the Rats, Wick? | 60 | 68 | 52 | 56 | 54 | 58 | **58.6** | Engine |
| reimaru | Y'shtola's Trigger, Trigger, Frown and Fall | 82 | 92 | 94 | 96 | 88 | 80 | **88.5** | Explosive, Control, Engine, Inevitable |
| mjsnoozer | Cloud, Ex-SOLDIER Upgraded | 52 | 58 | 38 | 38 | 50 | 64 | **50.5** | Combat |
| mjsnoozer | Edward Kenway Treasure, Pirates and Vehicles | 48 | 50 | 44 | 38 | 52 | 60 | **48.7** | Engine |
| mjsnoozer | Fire Lord Azula | 68 | 76 | 50 | 58 | 54 | 72 | **63.9** | Explosive, Engine |
| mjsnoozer | Squirreled Away - Food build | 58 | 68 | 44 | 42 | 62 | 72 | **58.2** | Engine, Combat |
| xanoh | Forresta | 68 | 62 | 50 | 38 | 58 | 78 | **59.6** | Explosive, Combat |
| xanoh | The Sundering | 42 | 70 | 88 | 84 | 82 | 72 | **71.3** | Control, Engine, Inevitable |
| j-py | Miku Madness!?!? Miku Sparta!!! | 64 | 72 | 38 | 44 | 54 | 66 | **57.5** | Explosive, Combat |

The unusual scores are evidence-led rather than conversions: The Copied Factory can assemble the Dualcaster Mage + Ghostly Flicker loop and has dense tutors, selection, recursion, and protection, but the loop itself only repeats the blink sequence and the list has no clearly documented payoff that converts infinite copies or enter-the-battlefield events into a win. Its Speed and Consistency remain high; Win Conversion and Resilience are reduced because assembling a non-winning loop does not create inevitability. Sephiroth Pain is Love moves further upward because Sanguine Bond + Exquisite Blood is a complete two-card infinite life-drain win, supported by Demonic Tutor, Diabolic Intent, Grim Tutor, Vampiric Tutor, Dark Ritual, Lotus Petal, sacrifice outlets, recursion, and overlapping aristocrats payoffs. Its forced-sacrifice package is also a major interaction axis: Grave Pact, Dictate of Erebos, Braids, Cabal Minion, Accursed Marauder, Fleshbag Marauder, Merciless Executioner, Plaguecrafter, and Demon's Disciple repeatedly convert creature deaths into edicts, constraining or effectively locking creature-based opponents while Sephiroth rebuilds. This justifies a high Control mode in addition to Explosive, Engine, and Inevitable. The Rush is unusually fast and interactive because of its low land count, Winota pressure, hatebears, and extra-combat package. The two Y'shtola decks score highest for interaction, consistency, and resource development because their lists combine tutors, free or cheap answers, sweepers, and repeatable engines; the reimaru list is slightly more resilient while the lto888 list is slightly faster. Forresta's resource score is held below its win-conversion score because its landfall engine is powerful once online but is not a compact infinite. Miku and the Feather lists score high in consistency or speed where their cheap recursive spell engines support explosive turns, but lower in interaction or conversion where the lists lack broad answers or a confirmed infinite.

The fowlplays second pass is evidence-led rather than inherited: The Rush is the clear portfolio peak because 30 lands, fast non-Humans, Winota triggers, hatebears, extra combats, protection, and the complete Kiki-Jiki + Combat Celebrant infinite-combat line create early pressure with a deterministic close. The Copied Factory keeps high setup and interaction scores from tutors, selection, recursion, countermagic, and its burn engine, but Dualcaster Mage plus Ghostly Flicker is only a repeatable loop in the archived list; without a documented payoff, its Win Conversion is not a deterministic win. The Queen of Theft is theft-first: mill fills graveyards so Tasha can access opposing cards, while stolen threats and a possible Rise of the Dark Realms provide credible secondary closes; its finishes are slower than The Rush's but more reliable than a pure mill reading suggests. The Crystal Braves has a genuine second-spell engine that supports Knights and board development, but no combo backstop and a board-dependent multi-turn close. The other nine scores reflect the listed ramp, draw, answers, recovery, commander dependence, and closing routes rather than generic archetype assumptions. These are pod-relative composition judgments, not play records.

## Player Portfolio Summary

The median is the primary portfolio figure. Mean, highest, and lowest are based on the rounded deck indices above; one- and two-deck portfolios are marked **limited sample**.

| Player | Eligible decks | Median index | Mean index | Highest | Lowest | Recurring threat modes | Sample |
|---|---:|---:|---:|---:|---:|---|---|
| fowlplays | 13 | **52.9** | 56.7 | 83.4 | 40.3 | Combat, Engine, Control, Inevitable, Explosive | — |
| lto888 | 12 | **65.3** | 67.3 | 90.5 | 52.7 | Engine, Explosive, Combat, Control, Inevitable | — |
| reimaru | 16 | **58.8** | 59.5 | 88.5 | 49.5 | Combat, Engine, Inevitable, Explosive, Control | — |
| mjsnoozer | 4 | **54.4** | 55.3 | 63.9 | 48.7 | Engine, Combat, Explosive | — |
| xanoh | 2 | **65.5** | 65.5 | 71.3 | 59.6 | Control, Engine, Inevitable, Explosive, Combat | **limited sample** |
| j-py | 1 | **57.5** | 57.5 | 57.5 | 57.5 | Explosive, Combat | **limited sample** |

These are pod-relative composition indices, not observed win rates or player ratings. Differences under roughly five points should normally be read as near-ties unless the component evidence differs materially.

---

## Automated EDH Oracle Engine Power Scores & Archetype Assessment (2026-09-10)

The following reflects deterministic calculations produced by `tools/deck_analyzer_engine.py` across all 52 pod deck analysis JSON files (`knowledgebase/podlist/<owner>/analysis/<deck-slug>.json`). Inputs: local Scryfall card cache, user-defined card categories as source of truth, piloting-intent classification, strategy-adaptive dynamic weight profiles, and local combo dictionary resolution. All figures are as of the last full batch run (2026-09-10T08:02Z).

### Portfolio Summary

| Player | Analyzed Decks | Median Power Score | Mean Power Score | Score Range | EDH Brackets | Primary Archetype Distribution | Total Tutors | Fast Mana | Combos | Portfolio Band |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|---|
| **fowlplays** | 13 | **5.2** | 5.7 | 4.2 – 7.8 | Brackets 1–3 | Midrange / Engine Value (10), Spellslinger / Storm (1), Big Mana / Landfall (1), Voltron / Equipment (1) | 10 | 15 | 2 | **★★★☆☆ (Typical)** |
| **j-py** | 1 | **7.6** | 7.6 | 7.6 – 7.6 | Bracket 3 | Spellslinger / Storm (1) | 0 | 1 | 0 | **★★★★☆\* (Provisional)** |
| **lto888** | 15 | **7.8** | 6.9 | 2.0 – 9.1 | Brackets 1–4 | Midrange / Engine Value (9), Spellslinger / Storm (5), Cheat / Aggro Tempo (1) | **55** | **25** | **3** | **★★★★☆ (Elevated)** |
| **mjsnoozer** | 5 | **7.2** | 7.0 | 5.4 – 8.3 | Brackets 2–3 | Spellslinger / Storm (2), Midrange / Engine Value (2), Voltron / Equipment (1) | 12 | 7 | 0 | **★★★★☆ (Elevated)** |
| **reimaru** | 16 | **7.2** | 7.1 | 5.1 – 8.6 | Brackets 2–4 | Midrange / Engine Value (6), Spellslinger / Storm (5), Voltron / Equipment (3), Aristocrats / Sacrifice (1), Cheat / Aggro Tempo (1) | 32 | 22 | 0 | **★★★★☆ (Elevated)** |
| **xanoh** | 2 | **7.1** | 7.1 | 6.7 – 7.4 | Brackets 2–3 | Big Mana / Landfall (1), Midrange / Engine Value (1) | 5 | 1 | 0 | **★★★★☆\* (Provisional)** |

> [!NOTE]
> **fowlplays** deck count is 13 eligible. The Best of Friends was successfully evaluated by the engine following the re-sync. **lto888** includes 12 developed decks plus 3 mid-build stubs (Cid, Doran, Thor). **mjsnoozer** includes Stella Lee (active); it was previously retired but the analysis JSON was produced and is counted here.

### Per-Deck Engine Breakdown

| Player | Deck | Power Score | Archetype | Bracket | Tutors | Fast Mana | Combos |
|---|---|---:|---|---:|---:|---:|---:|
| fowlplays | The Copied Factory | 7.8 | Spellslinger / Storm | 3 | 4 | 1 | 1 |
| fowlplays | The Crystal Braves | 7.0 | Midrange / Engine Value | 3 | 1 | 1 | 0 |
| fowlplays | The Gate of Babylon | 6.8 | Voltron / Equipment | 3 | 1 | 0 | 0 |
| fowlplays | The Rush | 6.7 | Midrange / Engine Value | 2 | 0 | 2 | 1 |
| fowlplays | The Queen of Theft | 5.7 | Midrange / Engine Value | 2 | 0 | 2 | 0 |
| fowlplays | The Dirt Kicker | 5.4 | Big Mana / Landfall | 2 | 0 | 1 | 0 |
| fowlplays | The Best of Friends | 5.2 | Midrange / Engine Value | 2 | 0 | 2 | 0 |
| fowlplays | The Warrior of Darkness | 5.2 | Midrange / Engine Value | 2 | 0 | 1 | 0 |
| fowlplays | The Hamster Catapult | 5.0 | Midrange / Engine Value | 2 | 1 | 1 | 0 |
| fowlplays | The Lorehold Redux | 5.0 | Midrange / Engine Value | 2 | 1 | 1 | 0 |
| fowlplays | The Master Chef | 4.9 | Midrange / Engine Value | 2 | 1 | 1 | 0 |
| fowlplays | The Koronation | 4.7 | Midrange / Engine Value | 2 | 1 | 1 | 0 |
| fowlplays | The Last Ride | 4.2 | Midrange / Engine Value | 1 | 0 | 1 | 0 |
| j-py | Miku Madness!?!? Miku Sparta!!! | 7.6 | Spellslinger / Storm | 3 | 0 | 1 | 0 |
| lto888 | Y'shtola Slingy Wingy | 9.1 | Spellslinger / Storm | 4 | 6 | 3 | 1 |
| lto888 | So I Started Blasting (with Azula) | 8.8 | Spellslinger / Storm | 4 | 4 | 3 | 0 |
| lto888 | Celes Recursion | 8.6 | Spellslinger / Storm | 4 | 7 | 4 | 0 |
| lto888 | Yuna Enchantress | 8.6 | Midrange / Engine Value | 4 | 7 | 1 | 1 |
| lto888 | Sephiroth Pain is Love | 8.5 | Midrange / Engine Value | 4 | 5 | 3 | 1 |
| lto888 | Squirrels! | 8.4 | Midrange / Engine Value | 3 | 7 | 2 | 0 |
| lto888 | Yuriko Good Ol' Ninjas | 8.0 | Cheat / Aggro Tempo | 3 | 3 | 2 | 0 |
| lto888 | Lightning Equip / Extra Attacks | 7.8 | Midrange / Engine Value | 3 | 3 | 2 | 0 |
| lto888 | Bau Bau Nyaa | 7.7 | Midrange / Engine Value | 3 | 5 | 2 | 0 |
| lto888 | Turtle Power, Powered | 7.3 | Spellslinger / Storm | 3 | 3 | 1 | 0 |
| lto888 | Maralen Faelves | 6.8 | Midrange / Engine Value | 3 | 4 | 0 | 0 |
| lto888 | Prismari Artistry | 6.1 | Spellslinger / Storm | 2 | 0 | 1 | 0 |
| lto888 | Thor Voltron-Slinger | 3.9 | Midrange / Engine Value | 1 | 1 | 1 | 0 |
| lto888 | Cid, Cid, and Cid, with Cid | 2.0 | Midrange / Engine Value | 1 | 0 | 0 | 0 |
| lto888 | Doran The Exploder | 2.0 | Midrange / Engine Value | 1 | 0 | 0 | 0 |
| mjsnoozer | Fire Lord Azula | 8.3 | Spellslinger / Storm | 3 | 4 | 3 | 0 |
| mjsnoozer | Cloud, Ex-SOLDIER Upgraded | 7.7 | Voltron / Equipment | 3 | 2 | 1 | 0 |
| mjsnoozer | Stella Lee | 7.2 | Spellslinger / Storm | 3 | 1 | 1 | 0 |
| mjsnoozer | Edward Kenway Treasure, Pirates and Vehicles Deck | 6.4 | Midrange / Engine Value | 2 | 4 | 1 | 0 |
| mjsnoozer | Squirreled Away - Food build | 5.4 | Midrange / Engine Value | 2 | 1 | 1 | 0 |
| reimaru | Syr Gwyn Armed and Crazy | 8.6 | Voltron / Equipment | 4 | 5 | 1 | 0 |
| reimaru | That's a Lot of Swords, Cloud | 8.4 | Voltron / Equipment | 3 | 3 | 1 | 0 |
| reimaru | Feather's Spell All You Can | 8.3 | Spellslinger / Storm | 3 | 2 | 1 | 0 |
| reimaru | Siona's Enchanting Soldiers | 7.4 | Voltron / Equipment | 3 | 4 | 1 | 0 |
| reimaru | Where're the Rats, Wick? | 7.4 | Spellslinger / Storm | 3 | 2 | 2 | 0 |
| reimaru | Aura Battler Feather | 7.3 | Spellslinger / Storm | 3 | 1 | 1 | 0 |
| reimaru | Marneus Calgar, Captain of Tokens | 7.2 | Midrange / Engine Value | 3 | 2 | 2 | 0 |
| reimaru | Thraximundar, Lord of Sacs | 7.2 | Cheat / Aggro Tempo | 3 | 2 | 2 | 0 |
| reimaru | Saheeli Copy Brilliance | 7.1 | Aristocrats / Sacrifice | 3 | 2 | 1 | 0 |
| reimaru | Miirym, Miirym on the Wall | 7.0 | Midrange / Engine Value | 3 | 3 | 1 | 0 |
| reimaru | Saruman's Mighty Meaty Army | 6.9 | Spellslinger / Storm | 3 | 1 | 2 | 0 |
| reimaru | Silverquill Likes to Bring a Crowd | 6.7 | Spellslinger / Storm | 2 | 3 | 2 | 0 |
| reimaru | Swords and Slicer | 6.5 | Midrange / Engine Value | 2 | 0 | 1 | 0 |
| reimaru | Y'shtola's Trigger, Trigger, Frown and Fall | 6.5 | Midrange / Engine Value | 2 | 1 | 1 | 0 |
| reimaru | Stop Sac'ing, Sephiroth | 5.7 | Midrange / Engine Value | 2 | 1 | 2 | 0 |
| reimaru | Solphim and Suffering | 5.1 | Midrange / Engine Value | 2 | 0 | 1 | 0 |
| xanoh | Forresta | 7.4 | Big Mana / Landfall | 3 | 4 | 0 | 0 |
| xanoh | The Sundering | 6.7 | Midrange / Engine Value | 2 | 1 | 1 | 0 |

### Key Engine Insights

1. **Tutor & Fast Mana Distribution**: LTO888 leads the pod in raw efficiency with **53 tutors** and **24 fast mana sources** across 14 decks, pushing the portfolio median to **7.9 / 10.0**. Reimaru trails with 32 tutors and 22 fast mana sources across 16 decks — the largest individual portfolio — placing it at an Elevated band despite the breadth.

2. **Strategy-Adaptive Dynamic Weighting**: Decks classified as Cheat / Aggro Tempo (*Yuriko Good Ol' Ninjas*, *Thraximundar, Lord of Sacs*) or Big Mana / Landfall (*Forresta*, *The Dirt Kicker*) are evaluated via dedicated archetype weight matrices rather than static ramp/curve assumptions, so high speed and evasion scores can compensate for lower raw tutor density.

3. **Verified Infinite Combos (6 configurations across 4 decks)**:
   - *Sanguine Bond* + *Exquisite Blood* → Infinite life drain & life gain — **lto888 / Sephiroth Pain is Love**
   - *Sanguine Bond* + *Exquisite Blood* → Infinite life drain & life gain — **lto888 / Y'shtola Slingy Wingy**
   - *Heliod, Sun-Crowned* + *Walking Ballista* → Infinite ping damage — **lto888 / Yuna Enchantress** *(newly detected in current batch)*
   - *Dualcaster Mage* + *Ghostly Flicker* → Infinite mana & magecraft triggers — **fowlplays / The Copied Factory** *(loop produces no documented win condition in current list; Win Conversion capped accordingly)*
   - *Kiki-Jiki, Mirror Breaker* + *Combat Celebrant* → Infinite combat steps & tokens — **fowlplays / The Rush**

4. **Archetype Coverage**: The pod skews heavily toward Midrange / Engine Value (35 of 51 decks) with meaningful clusters of Spellslinger / Storm (12), Voltron / Equipment (5), and smaller representation of Cheat / Aggro Tempo (2), Big Mana / Landfall (2), and Aristocrats / Sacrifice (1). No pure Stax or dedicated Combo (non-creature) archetypes are present.

5. **Bracket Distribution**: 4 decks sit at Bracket 4 (all lto888 — Y'shtola, Azula, Celes, Sephiroth). 1 deck sits at Bracket 1 (fowlplays / The Last Ride) and 2 stubs (lto888 / Cid, Doran) at Bracket 1 by score floor. The majority of the pod (≈39 decks) occupies Brackets 2–3, consistent with a mid-power casual-competitive pod profile.
