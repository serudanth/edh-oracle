---
type: profile
title: "fowlplays — Deckbuilder Profile"
owner: fowlplays
tags: [#profile]
related: []
decks: knowledgebase/podlist/fowlplays/decks/
last_updated: 2026-09-10
---

## Overview
| Profile Field | Assessment |
|---|---|
| Median Threat | **★★★☆☆** |
| Designation | **Adaptive Combat-Engine Architect** |
| Summary | A roaming planeswalker who builds each deck around a distinct engine, turning beasts, armies, graveyards, stolen power, and copied spells into pressure. Most battles are fought through combat and board development, but a few lists sharpen that broad arsenal into denial, explosive tempo, or a deterministic combat finish. |

fowlplays has 13 eligible decks with a mean local Power Score of **5.7 / 10.0**, a median of **5.2** (★★★☆☆), and a range of **4.2–7.8** (brackets 1–3). Under the EDH Oracle Analyzer Engine, the portfolio primary piloting archetypes are **Midrange / Engine Value** (10 decks), **Spellslinger / Storm** (1 deck), **Big Mana / Landfall** (1 deck), and **Voltron / Equipment** (1 deck). Across the 13 decks, the portfolio holds 15 fast mana sources, 10 tutors, and 2 verified combo configurations (*The Rush* and *The Copied Factory*). Automated analysis records are stored in `knowledgebase/podlist/fowlplays/analysis/`.

fowlplays prefers distinct game plans over repeatedly tuning one shell. The decks are generally creature-, combat-, and value-oriented, with carefully built mana bases and a creative spread of strategies rather than a uniform power level.

## Color & Archetype Tendencies
Color identity across 13 active decks:

| Color | Commander identities | Share |
|---|---:|---:|
| White | 6 | 46.2% |
| Blue | 4 | 30.8% |
| Black | 4 | 30.8% |
| Red | 7 | 53.8% |
| Green | 5 | 38.5% |
| Colorless | 0 | 0% |

- fowlplays builds broadly, but not randomly: each deck starts with a commander-specific engine and commits to a recognizable proactive plan. The portfolio favors creature combat, board development, and value over spell-heavy control, with The Queen of Theft and The Copied Factory as the main interactive exceptions.
- The player revisits strategic categories without simply copying lists. Equipment and aura voltron use different resource systems, while the aristocrats, recursion, tribal, and token decks each turn narrow commander text into a separate shell.
- Construction is generally deliberate and resilient rather than maximally fast. Land counts and fixing are well-supported, singleton discipline is strong, and higher-efficiency staples are concentrated in the bracket-3/4 decks instead of spread uniformly across the collection.

## Power Level & Construction Habits
- Archidekt brackets, updated for 13 decks: six at bracket 2, five at bracket 3, one outlier at bracket 4 (The Rush, a Winota hatebears/combo-aggro build with Drannith Magistrate, Aven Mindcensor, Thalia, Spirit of the Labyrinth, and Eidolon of Rhetoric as stax pieces), and **1 with no bracket recorded at all** (Crystal Braves, the only addition to the archive since the original pass). The original 12-deck bracket distribution is unchanged.
- Pricier, more clearly "cEDH-adjacent" staples (Rhystic Study, Cyclonic Rift, Dark Confidant, Snapcaster Mage, Demonic Tutor, Skullclamp, Toxic Deluge, Bribery) still concentrate almost entirely in the bracket-3/4 decks (Copied Factory, Queen of Theft, Best of Friends, The Rush); the bracket-2 decks lean more on thematic and synergy-driven picks over raw efficiency. Crystal Braves hasn't been checked against this specific claim in detail, but it runs a genuine assembled engine per its dedicated research note, so it doesn't read as bracket-2-style budget/thematic on a first pass.
- Land counts still average right around the 36-37 norm; Crystal Braves (37 lands) sits squarely in that band rather than extending either outlier (Dirt Kicker's 40-land high, The Rush's 30-land low).
- Land-base construction still correlates with color count: mono-color decks (Best of Friends, Dirt Kicker) stay basics-heavy, while multicolor decks carry larger fixing suites.
- The `power_level` frontmatter field is left blank across all 13 decks; the Archidekt bracket noted under Notes (where present) is the only power-level signal actually recorded.
- Singleton discipline is intact throughout all 13 decklists — no repeated nonbasic cards within any single decklist.

## Notable Patterns
- The portfolio is deliberately wide: fowlplays repeatedly explores a commander-specific engine instead of tuning one preferred shell. The result is unusually low overlap between decks, but the underlying construction quality remains consistent.
- Most lists are proactive creature or combat decks that generate value while advancing a board. The exceptions are meaningful: The Queen of Theft plays a slower resource-denial game, The Copied Factory uses spell and enter-the-battlefield engines, and The Rush shifts toward taxes and tempo.
- Voltron, aristocrats, recursion, tokens, and tribal plans are not interchangeable labels here. Each uses a different primary resource: equipment, deaths, graveyards, token production, or creature density. This suggests experimentation with mechanics rather than superficial commander swaps.
- The strongest strategic pattern is a split ceiling: most decks sit near the pod midpoint, while The Rush reaches the upper tail through a low land count, Winota pressure, hatebears, extra combats, protection, and the complete Kiki-Jiki + Combat Celebrant infinite-combat route. The Copied Factory remains a highly consistent spell engine, but its Dualcaster Mage + Ghostly Flicker loop has no clearly documented payoff in the list, so its high setup and interaction scores do not become deterministic Win Conversion. The Queen of Theft is theft-first rather than pure mill: milling supplies the graveyards Tasha needs to access opposing cards, while stolen threats and Rise of the Dark Realms provide credible secondary closes. The deck-specific index matters more than the portfolio median when choosing a table matchup.

## Decks
Full decklist archive: `knowledgebase/podlist/fowlplays/decks/` (13 decks — see `INDEX.md` for individual entries).

## External Cross-References
Original pass 2026-07-10 against EDHREC (direct fetch), Commander Spellbook (via WebSearch), and Scryfall (via WebSearch). Extended 2026-08-22 with direct API access for the new addition, following the mechanical-first-then-EDHREC methodology (read the commander's own oracle text and work out why a card fits before checking whether the crowd agrees — EDHREC's synergy score is a popularity aggregate across thousands of differently-goaled decks, not a verdict on fit for this specific 99). Figures are as returned by these sources at lookup time and may drift — see the j-py profile's Sunforger/Spellslinger example of exactly that happening between passes.

**The Crystal Braves (new)**: has its own dedicated deep-dive at `research/2026-08-06-the-crystal-braves-deck-profile.md` — full card-by-card mechanical read, owner-confirmed sequencing (cheap cantrips cast first specifically to free the second-spell slot for the real payoff), EDHREC/Scryfall verification, and a confirmed-empty Commander Spellbook check for the commander pairing. Not re-derived here; that note is the source of truth for this deck.

**EDHREC synergy alignment — the headline finding: despite the crossover/flavor-first framing, most decks' actual card choices track unusually close to EDHREC's top-synergy list for their commander:**
- Zenos yae Galvus // Shinryu (The Best of Friends) plays 7 of EDHREC's top-10 synergy cards outright: Summon: Primal Odin, Vorpal Sword, Maha Its Feathers Night, Rogue's Passage, Overkill, Massacre Wurm, and Unstoppable Slasher. EDHREC's top archetype tags are Voltron/Infect/Aggro/Equipment/Control, not "aristocrats" — the profile's "aristocrats/drain" grouping of this deck alongside Warrior of Darkness is EDHREC-plausible (Infect/combat-damage-as-drain-adjacent) but not a clean archetype match.
- Bruenor Battlehammer (The Gate of Babylon): EDHREC's #1 tag is literally Equipment (1,022 decks), #2 Voltron (230) — matches the profile's "equipment voltron" label exactly. Danitha Capashen Paragon, Puresteel Paladin, Colossus Hammer, and Sword of Vengeance are all EDHREC top-10 synergy cards present in the actual list.
- Tasha, the Witch Queen (The Queen of Theft): EDHREC's top tags are Exile/Theft/Mill/Control — an exact match to the profile's "Dimir control/mill-steal" label. 7 of EDHREC's top-10 synergy cards are in the deck: Gonti Lord of Luxury, Hostage Taker, Thief of Sanity, Memory Plunder, Siphon Insight, Extract Brain, Cunning Rhetoric.
- Quintorius, History Chaser (The Lorehold Redux): 8 of EDHREC's top-10 synergy cards appear, including both other Quintorius planeswalker printings (Field Historian, Loremaster) alongside Serra Paragon, Hofri Ghostforge, Sevinne's Reclamation, Mistveil Plains, Currency Converter, and Anger — a near-total match to EDHREC's Reanimator/Graveyard/Self-Mill archetype read, confirming the profile's "graveyard-recursion value engine" label.
- Winota, Joiner of Forces (The Rush): the deck plays 8 of EDHREC's top-10 synergy cards (Blade Historian, Angrath's Marauders, Ornithopter, Lena Selfless Champion, Loyal Apprentice, Combat Celebrant, Legion Warboss, Aven Mindcensor) plus Archon of Emeria and Spirit of the Labyrinth from further down the synergy list — this is one of the most "on-rails EDHREC-optimal" builds in the archive, reinforcing the profile's read of The Rush as function-over-theme.
- Divergence worth flagging: EDHREC's top archetype tags for Ardbert, Warrior of Darkness are +1/+1 Counters (623 decks) and Legends (609), with Aristocrats a distant tag at only 43 decks — the profile's grouping of Warrior of Darkness into "aristocrats/drain builds" (alongside Best of Friends) is a thinner EDHREC match than the profile implies; EDHREC would frame it primarily as a counters/legends-aggro shell.
- Divergence worth flagging: of the two Gruul decks the profile calls "both creature/vehicle-forward midrange-aggro shells," only Balthier and Fran (The Last Ride) actually centers on EDHREC's Vehicles tag (262 decks, its #1 archetype, and the deck plays 6 of its top-10 synergy vehicle cards: Lumbering Worldwagon, Rocketeer Boostbuggy, Smuggler's Copter, The Regalia, Thunderous Velocipede, Mech Hangar). Minsc & Boo (The Hamster Catapult) is not vehicle-centric on EDHREC at all — its top tags are +1/+1 Counters, Aggro, Fling, and Stompy, with only Fling and Halana and Alena, Partners from the top-10 list actually present in the deck. The two "Gruul creature/vehicle" decks are built around different EDHREC archetype centers.
- Inalla, Archmage Ritualist (The Copied Factory): EDHREC's tags are Wizards/Combo/Spellslinger/Clones/Reanimator/Tokens/Control/Blink — "Combo" (547 decks) and "Spellslinger" are the closest analogs to the profile's "storm" label; EDHREC doesn't use a distinct Storm tag for Inalla. Archaeomancer, Azami Lady of Scrolls, Harmonic Prodigy, Naban Dean of Iteration, Step Through, and Riptide Laboratory are all present from the top synergy list.
- Miirym, Sentinel Wyrm (The Koronation): 5 of EDHREC's top-10 synergy dragons are in the deck (Dragonlord's Servant, Ganax Astral Hunter, Korlessa Scale Singer, Lathliss Dragon Queen, Thrakkus the Butcher), consistent with EDHREC's dominant Dragons tag (4,514 decks).

**Commander Spellbook — checking the profile's flagged stax/combo pieces:**
- Drannith Magistrate and Eidolon of Rhetoric are both real, documented Commander Spellbook combo pieces — but every documented pairing requires a partner card (Knowledge Pool, Possibility Storm, Uba Mask, Eye of the Storm, Omen Machine, or Shared Fate) to complete a lock. None of those partner cards appear anywhere in The Rush's decklist (confirmed by direct grep — zero matches). So despite being "known combo pieces" on paper, they function purely as standalone stax taxes in this build, not an assembled lock — this sharpens rather than contradicts the profile's read of The Rush as hatebears/stax rather than a true combo deck. Thalia, Guardian of Thraben has no documented direct combo with Eidolon of Rhetoric on Commander Spellbook; her role here is pure tempo/tax, same conclusion.
- Unexpected find in The Copied Factory: Dualcaster Mage and Ghostly Flicker — both actually present in the decklist — form a documented two-card infinite combo on Commander Spellbook (`commanderspellbook.com/combo/147-1987/`, ~16,000+ decks recorded running it). Dualcaster Mage's ETB copies Ghostly Flicker targeting itself, re-blinking Dualcaster Mage and re-triggering the copy indefinitely, producing infinite ETB/LTB triggers and infinite mana from any land that enters untapped. This means "The Copied Factory" isn't just storm-*adjacent* in theme — it's carrying a genuine assembled infinite engine, which is a stronger cEDH-adjacent signal than the profile's "bracket 3, pricier staples" framing suggests (several fan combo pages also note an even bigger mana/token variant when Inalla, Archmage Ritualist herself joins the loop, though that three-card line isn't independently hosted on Commander Spellbook).

**Scryfall — checking the "modal double-faced card" claim in Notable Patterns:**
- Cecil, Dark Knight // Cecil, Redeemed Paladin and Kefka, Court Mage // Kefka, Ruler of Ruin are not modal double-faced cards — Scryfall confirms both are transform (nonmodal) DFCs: they're cast/enter as their front face only, and flip to the back face solely via an in-game trigger (Cecil transforms off a damage-linked ability; Kefka via an 8-mana sacrifice-and-transform activated ability), not a "choose either face when you cast/play it" MDFC choice.
- Zanarkand, Ancient Metropolis // Lasting Fayth is also not a true MDFC — it's a Land with an Adventure side (Lasting Fayth, a {4}{G} sorcery making a Hero token, after which the land becomes playable from exile), the same Adventure structure as Throne of Eldraine's Murderous Rider // Swift End rather than a Zendikar-Rising-style pick-a-face MDFC.
- Net correction: the profile's "Modal double-faced cards are unusually dense across the archive" line conflates three distinct mechanics — transform DFCs (Cecil, Kefka), Adventure cards (Zanarkand, and likely Murderous Rider // Swift End if it's in the archive), and true MDFCs — under one label. The underlying observation (dual-faced/dual-mode cards are dense, largely FF-sourced) holds up; the "modal" terminology doesn't, for the specific examples checked.
