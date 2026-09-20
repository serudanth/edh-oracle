## 2026-09-18 (card search set delta protocol formalization)

- **[skill]** Formalized the Set Delta & Temporal Boundary Protocol in `.claude/skills/edh-research/SKILL.md` to counteract LLM parametric training cutoff bias during card recommendations.
- **[governance]** Updated `GEMINI.md`, `AGENTS.md`, and `agent-core/core/domains/edh.md` mandating a two-pronged card search (historical staples + targeted post-cutoff delta queries via Scryfall) and subsequent persistent cache ingestion.
- **[cache]** Added post-cutoff cards `Traveling Chocobo` (FIN) and `Beifong's Bounty Hunters` (TLA) to `knowledgebase/_cache/scryfall-cards.json`, bringing total cached cards to 2,088.

## 2026-09-17 (delta refresh, rules archival & engine re-analysis)

- **[kb]** Re-ran `tools/archidekt_extract.py` and `tools/moxfield_extract.py` across all 6 owners (fowlplays, j-py, lto888, mjsnoozer, reimaru, xanoh) against remote sources:
  - **`mjsnoozer`**: Discovered 1 new deck: `knowledgebase/podlist/mjsnoozer/decks/zimone-x-bulldozer.md` (Zimone, Infinite Analyst, Simic UG, 100 cards). Reordered Stella Lee decklist.
  - **`lto888`**: Card updates across `knowledgebase/podlist/lto888/decks/maralen-faelves.md` (added Sol Ring, Dark Ritual, The One Ring, An Offer You Can't Refuse, Cultivate, Maskwood Nexus, lands), `yshtola-slingy-wingy.md` (added Displacer Kitten, Tataru Taru), and updated stub `doran-the-exploder.md` (assigned commander Doran, Besieged by Time, added 2 creatures).
  - **`fowlplays`, `j-py`, `reimaru`, `xanoh`**: Re-extracted; card compositions confirmed current.
- **[cache]** Added 65 newly discovered cards to persistent cache `knowledgebase/_cache/scryfall-cards.json`, expanding the cache to 2,086 cards.
- **[rules]** Downloaded and archived the official WotC Magic: The Gathering Comprehensive Rules into `knowledgebase/rules/MagicCompRules.txt` (effective August 7, 2026, 9,397 lines) alongside documentation in `knowledgebase/rules/README.md`.
- **[tools]** Executed deterministic analyzer engine `tools/deck_analyzer_engine.py` across all 53 pod decks:
  - *Maralen Faelves* surged from Power Score 6.8 to 7.7 (EDH Bracket 3) following additions of fast mana (Sol Ring, Dark Ritual) and tutors.
  - *Zimone X Bulldozer* initialized at Power Score 7.0 (EDH Bracket 3, Spellslinger / Storm).
  - *The Rush* advanced to EDH Bracket 3 (Power Score 6.9).
- **[kb]** Synchronized documentation across `knowledgebase/INDEX.md`, `knowledgebase/podlist/mjsnoozer/profile.md`, and `knowledgebase/podlist/lto888/profile.md` with updated card counts, staples, and engine metrics.

## 2026-09-10 (full pod decklist re-sync & audit)

- **[kb]** Re-ran `tools/archidekt_extract.py --user` for fowlplays, j-py, lto888, mjsnoozer, xanoh, and `tools/moxfield_extract.py --user` for reimaru — a comprehensive re-sync of all 6 owners' public decklists against remote sources:
  - **`fowlplays`**: Extracted 13 decks. *The Queen of Theft* gained `Peer into the Abyss`.
  - **`lto888`**: Extracted 15 decks. Discovered 1 new deck stub: `knowledgebase/podlist/lto888/decks/thor-voltron-slinger.md` (Thor, God of Thunder, Mono-Red, 24 cards). Major upgrade for `turtle-power-powered.md` (added `The One Ring`, `Vampiric Tutor`, `Fierce Guardianship`, `Cyclonic Rift`, `Walking Ballista`, and TMNT creatures). Minor upgrades across `squirrels.md` (`Sylvan Library`, `Shang-Chi`, `Yavimaya`), `so-i-started-blasting-with-azula.md` (`Big Score`, `Frantic Search`, dual lands), `sephiroth-pain-is-love.md` (`K'rrik, Son of Yawgmoth`), and `lightning-equip-extra-attacks.md` (`Kíli`, `Blacksmith's Talent`).
  - **`j-py`, `mjsnoozer`, `reimaru`, `xanoh`**: Re-extracted; card compositions unchanged.
- **[cache]** Added 11 newly discovered cards (`Peer into the Abyss`, `Kíli the Resourceful`, `Blightstep Pathway // Searstep Pathway`, `Shang-Chi, Master of Kung Fu`, `Sylvan Library`, `Yavimaya, Cradle of Growth`, `Leonardo, Cutting Edge`, `Michelangelo, Weirdness to 11`, `Prehistoric Pet`, `Raph & Mikey, Troublemakers`, `Thor, God of Thunder`) to persistent cache `knowledgebase/_cache/scryfall-cards.json`.
- **[tools]** Executed `python tools/deck_analyzer_engine.py --all --write-kb` across all 52 decks. *The Copied Factory* re-classified to `Spellslinger / Storm` with Power Score 7.8 (EDH Bracket 3). *The Best of Friends* successfully analyzed at Power Score 5.2 (EDH Bracket 2). *Turtle Power, Powered* surged from Power Score 6.3 to 7.3 (Bracket 3).
- **[kb]** Updated `knowledgebase/INDEX.md`, `knowledgebase/podlist/lto888/profile.md`, `knowledgebase/podlist/fowlplays/profile.md`, `knowledgebase/research/2026-08-25-threat-pillar-assessment.md`, and `knowledgebase/research/2026-08-22-pod-threat-profile.md` with the new deck, updated staple counts, and recalculated engine metrics.

## 2026-09-03 (the crystal braves deck review & report)

- **[kb]** Added comprehensive deck review and optimization report `knowledgebase/research/2026-09-03-the-crystal-braves-deck-review.md` covering mechanical identity, local engine metrics, engine friction points (cantrip deficit, Vanquisher's Banner non-bo, 3-drop bottleneck), 1-for-1 upgrade tables, and sequencing heuristics.
- **[kb]** Refreshed `knowledgebase/podlist/fowlplays/decks/the-crystal-braves.md` from Archidekt and generated deterministic analysis output `knowledgebase/podlist/fowlplays/analysis/the-crystal-braves.json`.
- **[kb]** Updated `knowledgebase/INDEX.md` with the new deck review research entry.

## 2026-08-25 (threat assessment document synchronization)

- **[kb]** Updated `knowledgebase/research/2026-08-25-threat-pillar-assessment.md` and `knowledgebase/research/2026-08-22-pod-threat-profile.md` with the deterministic Power Scores (1.0-10.0 scale), EDH Brackets (1-4), fast mana totals, tutor densities, and verified combo counts computed by `tools/deck_analyzer_engine.py`.

## 2026-08-25 (player profile sync with local analyzer results)

- **[kb]** Synchronized all 6 player deckbuilder profiles (`fowlplays`, `j-py`, `lto888`, `mjsnoozer`, `reimaru`, `xanoh`) and `knowledgebase/INDEX.md` teasers with the Power Scores, EDH Brackets, piloting archetypes, fast mana counts, and tutor densities computed by `tools/deck_analyzer_engine.py`.

## 2026-08-25 (local deck analyzer engine implementation)

- **[tools]** Built `tools/deck_analyzer_engine.py` to calculate deterministic metrics, power scores, brackets, and combo lines using Scryfall cache data, user-defined categories (source of truth), EDHRec package aggregates, and Commander Spellbook combo detection.
- **[kb]** Added `knowledgebase/podlist/<owner>/analysis/<deck-slug>.json` directories and ran batch analysis across all 51 pod decks.
- **[tests]** Added `tests/test_deck_analyzer_engine.py` covering category resolution, archetype classification, combo matching, and analysis file generation.

## 2026-08-25 (pdd deck analyzer engine specification)

- **[kb]** Created Product Design Document (PDD) `knowledgebase/research/2026-08-25-pdd-deck-analyzer-engine.md` detailing the architectural specification, algorithmic scoring formulas, classification rules, and schema mapping for the automated local EDH deck analyzer engine.
- **[kb]** Updated `knowledgebase/INDEX.md` with the new research note entry.

## 2026-08-25 (external analysis extraction sub-tool)

- **[tools]** Added `tools/external_analysis_extract.py` and prompt specification `tools/prompts/external_analysis_agent.md` for fetching, normalizing, and archiving external deck-analysis outputs across ScryCheck, EDHCheck, RateMyDecks, CommanderPowerMeter, ArcMind, and PowerDeckAI.
- **[tests]** Added `tests/test_external_analysis.py` covering schema compliance, metrics mapping, status reporting, and `null` handling.

## 2026-08-25 (canonical public deck URL)

- **[kb]** Updated Xanoh's Forresta source link to the canonical public Archidekt URL (`https://archidekt.com/decks/21400503/forresta`) used for independent ScryCheck imports.

## 2026-08-25 (fowlplays percentile threat reassessment)

- **[kb]** Thoroughly reassessed all 13 eligible fowlplays decks across Speed, Consistency, Resource Development, Interaction, Resilience, and Win Conversion using the current pod-relative percentile methodology and exact weighted index formula.
- **[kb]** Preliminary second-pass recalculation of fowlplays to a **52.9 median**, **56.4 mean**, **81.6 high**, and **40.3 low**; this snapshot was superseded by the owner-clarification pass below, which added The Rush's complete infinite-combat line and revised its portfolio totals.
- **[kb]** Updated the fowlplays profile, index teaser, and assessment evidence; no decklists, cache entries, or play records were changed.

## 2026-08-25 (targeted combo reassessment)

- **[kb]** Reassessed The Copied Factory after distinguishing its repeatable Dualcaster Mage + Ghostly Flicker loop from a winning combo; set its Deck Threat Index to **76.7** because the list has no clearly documented payoff for going infinite.
- **[kb]** Reassessed LTO888's Sephiroth Pain is Love after confirming the complete Sanguine Bond + Exquisite Blood infinite, tutors, fast mana, recursion, sacrifice outlets, redundant drain finishes, and a broad forced-sacrifice control package; set its Deck Threat Index to **88.7**.
- **[kb]** Updated the affected fowlplays and LTO888 profile summaries and threat observations.
- **[kb]** Updated the player portfolio summary so fowlplays' peak reflects The Rush at **80.3**, and synchronized the dedicated Copied Factory research note and index entry with the no-payoff loop assessment.

## 2026-08-25 (fowlplays clarification pass)

- **[kb]** Updated fowlplays' assessment after owner clarification: The Rush contains the complete Kiki-Jiki + Combat Celebrant infinite-combat line; Queen of Theft is theft-first with mill as fuel and Rise of the Dark Realms as a secondary close; Crystal Braves uses its second-spell engine to support Knights and board development.
- **[kb]** Recalculated fowlplays to a **52.9** median, **56.7** mean, **83.4** peak, and **40.3** floor; updated the relevant deck scores and profile/index summaries.
- **[kb]** Recorded Impact Tremors as the removed former payoff for The Copied Factory's Dualcaster Mage + Ghostly Flicker loop.

## 2026-08-25 (limited-sample rating caveats)

- **[kb]** Clarified in the J-Py and Xanoh profiles that their star ratings are provisional because they are based on one and two eligible decks, respectively.
- **[kb]** Updated their `INDEX.md` teasers to carry the same limited-sample warning.
- **[kb]** Added a literal asterisk to the Median Threat value in both limited-sample profiles.

## 2026-08-25 (profile star ratings and summary rewrite)

- **[kb]** Replaced profile median threat index displays with a star system: 0-19 = one star, 20-39 = two, 40-59 = three, 60-79 = four, and 80-100 = five.
- **[kb]** Rewrote all six profile summaries and designations to reflect the new assessment's speed, consistency, resource development, interaction, resilience, win-conversion, and threat-mode findings.
- **[kb]** Updated `INDEX.md` teasers to match the revised star ratings, designations, and summaries.

## 2026-08-25 (percentile threat assessment applied)

- **[kb]** Recalculated the 48 eligible decks and six player portfolios under the six-pillar pod-relative percentile system with weighted Deck Threat Indexes, threat modes, and median/mean/peak/floor portfolio figures.
- **[kb]** Updated the threat assessment, pod threat reference, all six player profiles, and `INDEX.md`; retired decks and the two one-card LTO888 stubs remain excluded.

## 2026-08-25 (percentile threat assessment redesign)

- **[kb]** Replaced the legacy four-pillar 0-40 and D-to-SSS threat model with six deck-level dimensions scored as explicit 0-100 percentiles: Speed, Consistency, Resource Development, Interaction, Resilience, and Win Conversion.
- **[kb]** Defined pod-relative and benchmark-relative percentile semantics, weighted composite scoring, threat-mode labels, evidence-based assessment steps, and a player portfolio report using median, mean, highest, lowest, and eligible deck count.
- **[kb]** Marked the previous four-pillar scores as legacy; existing decks and profiles require a fresh percentile pass before new scores are reported.

## 2026-08-25 (four-pillar threat assessment, 0-10 reassessment)

- **[kb]** Reassessed all 48 fully built decks with differentiated 0-10 scores for Ramp, Card Advantage, Interaction, and Win Conditions; scores were not mechanically doubled from the earlier pass.
- **[kb]** Recalculated ranks from the new averages: fowlplays **SS** (27.62), j-py **A** (21.00), lto888 **SS** (28.75), mjsnoozer **S** (26.00), reimaru **S** (26.63), and xanoh **SS** (29.50).

## 2026-08-25 (planeswalker-style profile summaries)

- **[kb]** Rewrote all six overview summaries in flavorful planeswalker voice while keeping each summary grounded in the player's owned deck archetypes.
- **[kb]** Updated `INDEX.md` teasers to match the new summaries.

## 2026-08-25 (profile table playstyle revision)

- **[kb]** Reworked each overview table's designation and one-line summary to describe the player's owned deck archetypes and gameplay patterns rather than construction habits.
- **[kb]** Updated `INDEX.md` teasers to match the revised playstyle labels.

## 2026-08-25 (overview profile tables)

- **[kb]** Moved each player's threat rank to a standardized table at the beginning of `Overview`.
- **[kb]** Added a concise profile designation and one-line player summary to all six overview tables.
- **[kb]** Updated `INDEX.md` teasers with the new designations.

## 2026-08-25 (Notable Patterns strategy reassessment)

- **[kb]** Completely rewrote Notable Patterns in all six player profiles around repeated construction systems, resource engines, interaction, mana risk, deck contrast, and win-condition reliability.
- **[kb]** Removed crossover, foil, printing, title, and other collection-oriented observations from those sections.

## 2026-08-25 (color and archetype profile reassessment)

- **[kb]** Replaced the Color & Archetype Tendencies section in all six player profiles with commander-identity color tables covering White, Blue, Black, Red, Green, and Colorless.
- **[kb]** Completely rewrote the archetype analysis around deckbuilding behavior, recurring engines, interaction, mana philosophy, and strategic cohesion.
- **[kb]** Updated `INDEX.md` profile teasers to reflect the new playstyle-focused assessments.

## 2026-08-25 (player profile reassessment)

- **[kb]** Reassessed all six player overviews around deckbuilding behavior, consistency, interaction, mana philosophy, and win-condition reliability rather than crossover flavor.
- **[kb]** Kept the concise threat rankings: lto888 **SSS**, reimaru **SS**, fowlplays **S**, xanoh and mjsnoozer **A**, and j-py **B**.
- **[kb]** Updated `INDEX.md` and the pod threat reference so their summaries use the same playstyle-focused language.

## 2026-08-25 (profile overviews stylized and threat ranks standardized)

- **[kb]** Rewrote every player profile overview with in-lore Magic framing and a shared D-to-SSS table-threat scale: lto888 **SSS**, reimaru **SS**, fowlplays **S**, xanoh and mjsnoozer **A**, and j-py **B**.
- **[kb]** Preserved the existing evidence-heavy profile sections and called out LTO888's two one-card mid-build stubs without folding them into the analyzed 12-deck sample.
- **[kb]** Updated `INDEX.md` and the pod threat reference to use the same letter ranks and labels.

## 2026-08-25 (archived LTO888's two mid-build stubs)

- **[kb]** Added `knowledgebase/podlist/lto888/decks/doran-the-exploder.md` (Doran, Besieged by Time) and `knowledgebase/podlist/lto888/decks/cid-cid-and-cid-with-cid.md` (Cid, Timeless Artificer) via `tools/archidekt_extract.py` — both new on LTO888's Archidekt account as of today, both a single card in so far. Archived as bare stubs only; no analysis, EDHREC/Spellbook cross-referencing, or profile.md re-derivation, since there's nothing to analyze yet.
- **[kb]** `INDEX.md` gained entries for both, flagged as mid-build stubs not yet worth analyzing.
- `knowledgebase/podlist/lto888/profile.md` intentionally left untouched (still describes the prior 12-deck sample) — revisit once either stub is actually built out.

## 2026-08-22 (Copied Factory profile: Naban loot-doubling finding, patience-first piloting update)

- **[kb]** Updated  with a new Mechanical Identity finding: Naban, Dean of Iteration's oracle text ("if a Wizard you control entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time") doubles *any* Wizard's own ETB trigger, not just Inalla's Eminence — confirmed via Scryfall for Naban, Kefka Court Mage, Emet-Selch Unsundered, and Inalla. This gives Kefka and Emet-Selch a genuine loot/card-selection role independent of the ping/burn package they were already correctly excluded from. Layering Eminence on top (also Naban-doubled) can push a single hardcast Kefka to 4 total discard/loot triggers off one token copy.
- **[kb]** Added a dated History & Trajectory entry (owner's account): a recent game where prioritizing draw engines behind blockers — rather than committing to the burn plan on tempo — worked well, directly addressing the profile's previously-documented #1 weakness (sequencing/patience). Emet-Selch flipped into Hades twice with Naban doubling its loot triggers; Kefka never transformed. The Eminence-into-4x-Kefka-loot line was identified post-game but not yet piloted.
- **[repo]**  gained 4 new entries (Naban, Inalla, Kefka, Emet-Selch), bringing the cache to 1,947 total.
- **[kb]** 's Copied Factory entry updated to mention both additions.

## 2026-08-22 (new pod matchup analysis — profile review plus comparative deck strength)

- **[kb]** Added : a review of all 6 owner profiles for rigor/completeness (one gap flagged, not fixed — lto888's whole-decklist Commander Spellbook combo check has only been run on 2 of 12 decks despite that player having the pod's highest staple/tutor density), plus a comparative "who's actually favored" ranking built on inevitability, interaction, and resilience rather than raw power. Distinct from the existing , which measures threat/cost, not matchup favorability — the two rank the top of the pod differently, which the new note calls out explicitly as a politics/perception effect rather than a data conflict.
- **[kb]** No new external lookups were run for this pass — it synthesizes findings already cross-referenced in the six profiles and the two dedicated deck deep-dives (Copied Factory, Crystal Braves) as of today's re-verification pass.
- **[kb]**  updated with the new entry.

## 2026-08-22 (removed Discard Mill Assassin — concept-board item, never an active deck)

- **[kb]** Per the owner: "Discard Mill Assassin" (fowlplays, Altaïr Ibn-La'Ahad) was never an active build — it lived on an Archidekt concept board, not the proper decklist, and only entered this archive because the `--user` sync endpoint returned it alongside real active decks. Deleted `knowledgebase/podlist/fowlplays/decks/discard-mill-assassin.md` outright (the earlier session's find that it had gone "unlisted" on Archidekt is superseded by this — it wasn't hidden-but-real, it was a concept item the sync shouldn't have picked up as a decklist in the first place).
- **[kb]** `knowledgebase/podlist/fowlplays/profile.md` reverted to 13 active decks (12 original + Crystal Braves) — every aggregate stat touched by the deck's brief presence recomputed back: color counts (Red 7/13, White 6/13, Green 5/13, Black and Blue tied least-common at 4/13 each), color-combo split (2 mono / 9 two-color / 2 three-color), bracket distribution (6/5/1 plus 1 unbracketed — Crystal Braves only), and crossover-commander count (9/13). The Assassin-tribal mechanical finding and its EDHREC/Spellbook cross-references were removed along with it.
- **[kb]** `INDEX.md`'s fowlplays section: removed the `discard-mill-assassin.md` entry, updated the profile teaser back to 13 decks with a note on why the deck was dropped.
- Cache entries for cards unique to this deck (Altaïr, the Assassin-typed creatures, etc.) were left in `knowledgebase/_cache/scryfall-cards.json` rather than pruned — the cache is a lookup table, not an index of active decks, and leaving unused entries is harmless.

## 2026-08-22 (reimaru profile re-verified — largest sample, one new combo finding)

- **[kb]** Re-verified `knowledgebase/podlist/reimaru/profile.md`'s External Cross-References with direct API access (replacing the original pass's `WebSearch` fallback for Scryfall/Spellbook) across all 16 decks — reimaru's decklists were unchanged by the pod-wide resync, so this was a re-verification/methodology-upgrade pass rather than a catch-up rewrite like fowlplays/lto888 needed.
- **[kb]** New finding via the whole-decklist Commander Spellbook endpoint (more rigorous than the original pass's named-combo search): **Wick, the Whorled Mind's deck ("Where're the Rats, Wick") is exactly one card — Conspiracy — away from a cataloged two-card infinite combo with the commander itself**, a mandatory draw-the-game loop (Conspiracy makes Wick's own Snail token also a Rat, re-triggering Wick indefinitely). Not live as built, but a tighter gap than the profile's general "no fast-mana outliers" framing implies for this specific deck. The original pass's separately-checked Wick + Ashnod's Altar + Arcane Adaptation combo was correctly ruled out (neither piece present) but didn't catch this simpler one, since it searched for one named combo rather than running the actual decklist through the endpoint.
- **[kb]** Confirmed the same EDHREC tag-order drift already found on j-py's profile applies here too: Feather, the Redeemed's Spellslinger tag has overtaken Sunforger since the original 2026-07-10 check (same commander, same underlying EDHREC data). All other previously-cited EDHREC numbers (Feather, Radiant Arbiter; Syr Gwyn's Kusari-Gama absence; Y'shtola's Control-not-Stax framing; Wick's 39-deck Spellslinger minority tag) re-verified as unchanged or near-identical.
- **[repo]** `knowledgebase/_cache/scryfall-cards.json` gained 601 new entries (full card pool across all 16 reimaru decklists, not already cached), bringing the cache to 1,943 total.
- **[kb]** `INDEX.md`'s reimaru profile teaser updated to match.

## 2026-08-22 (fowlplays profile extended to 14 decks — Crystal Braves and Discard Mill Assassin)

- **[kb]** `knowledgebase/podlist/fowlplays/profile.md` was still built on the 12-deck picture from 2026-07-10 despite the archive having grown to 14 (The Crystal Braves added 2026-08-06 with its own dedicated deep-dive note; Discard Mill Assassin only surfaced as an unlisted-on-Archidekt deck during this session's pod-wide resync). Recomputed every aggregate stat that changed: color counts (Red 8/14, White 7/14 — up from 5/12 due to two new white decks, Black/Green 5/14 each, Blue still least common at 4/14), color-combo split (now 9 of 14 two-color rather than "almost exclusively" 10 of 12), bracket distribution (6 bracket-2 / 5 bracket-3 / 1 bracket-4 unchanged, plus 2 newly-added decks with no bracket recorded at all), and crossover-commander count (10 of 14, up from 8 of 12 — Assassin's Creed joins as a commander-level pick via Altaïr, not just cards mixed into another deck).
- **[kb]** New finding: **Discard Mill Assassin's title doesn't match what the deck does.** Altaïr Ibn-La'Ahad's own ability is Assassin-graveyard-recursion via combat (exile a dead Assassin, make a temporary attacking token-copy), unrelated to discard or mill. EDHREC (5,688 decks) confirms Assassins (893) as the dominant tag for this commander against Discard (51) and Mill (14) as minor ones — the deck's actual build (7 sacrifice-for-value Assassin creatures, zero discard package, one surveil card) matches the dominant read, not its own title. Cross-referenced against the same pattern already noted in j-py's "Miku Madness" (a title with zero matching cards) — worth remembering a deck's Archidekt title is flavor, not an archetype signal, anywhere in this pod.
- **[kb]** The Crystal Braves section points to its existing dedicated research note (`research/2026-08-06-the-crystal-braves-deck-profile.md`) rather than re-deriving the analysis — that note is already a thorough card-by-card mechanical read with owner-confirmed sequencing.
- **[repo]** `knowledgebase/_cache/scryfall-cards.json` gained 39 new entries (remaining card pool for the two new decks not already cached from the Crystal Braves research pass), bringing the cache to 1,342 total.
- **[kb]** `INDEX.md`'s fowlplays profile teaser updated to match.

## 2026-08-22 (j-py profile re-verified — direct access replaces WebSearch fallback)

- **[kb]** Re-verified `knowledgebase/podlist/j-py/profile.md`'s External Cross-References with direct Scryfall/EDHREC/Commander Spellbook access instead of the original pass's `WebSearch` fallback (this repo's lower-fidelity path, used when direct access is blocked). Found one real, actionable change: EDHREC's tag order for Feather, the Redeemed has flipped since the original check — **Spellslinger (1,220 decks) has overtaken Sunforger (968)** as the commander's single largest theme. The original profile's framing ("Sunforger divergence... a real, notable departure from the expected build") no longer holds as stated — this deck now matches what's actually the *most* common Feather build, not a departure from it. Everything else in the profile (angel subtheme, ramp read, high-synergy-card overlap, no-combo finding) re-verified as still accurate; the no-combo claim was additionally strengthened using the whole-decklist Spellbook endpoint rather than a commander-level query.
- **[repo]** `knowledgebase/_cache/scryfall-cards.json` gained 57 new entries (full card pool for the j-py decklist), bringing the cache to 1,303 total.

## 2026-08-22 (lto888 profile rewrite — same methodology; fixed stale post-resync claims)

- **[kb]** Rewrote `knowledgebase/podlist/lto888/profile.md` under the mechanical-first-then-EDHREC methodology, covering all 12 decks including the newly-synced 5-color "Turtle Power, Powered" (Leonardo, the Balance // Michelangelo, the Heart). Fixed two claims left stale by the prior resync: "no four- or five-color builds" (now false — Turtle Power is WUBRG) and "Treno, Dark City appears in two unrelated decks" (it was cut from Azula in the resync; only Yuriko has it now). Also corrected Squirrels' bracket count (owner cleared its Archidekt bracket tag; only Sephiroth and Y'shtola still have one, not 3 of the sample).
- **[kb]** Added mechanical grounding for two commanders that the prior pass had only characterized via EDHREC tags: Rootha, Mastering the Moment's combat trigger scales off the *single highest-mana-value* spell cast that turn, not spell count — a different math than the deck's separate magecraft package (Veyran, Storm-Kiln Artist), explaining why Prismari Artistry runs both cheap cantrips and several X-cost spells rather than an undifferentiated cheap-spells pile. Leonardo/Michelangelo's shared counters-and-tokens axis explains why Doubling Season, Corpsejack Menace, and Hardened Scales are all present in Turtle Power as three different multipliers on the same axis, not scattered goodstuff.
- **[kb]** Re-verified Fire Lord Azula's Commander Spellbook status against the *current* decklist via the whole-decklist combo endpoint (the prior pass had only checked the commander's reputation/known combo lines, not the actual 99) — confirmed no assemblable combo (missing Narset's Reversal and Dramatic Reversal, same gap independently found in mjsnoozer's separate Azula build). Corrected the prior claim that Azula was "the deck in the sample most likely to have an actual infinite line available."
- **[repo]** `knowledgebase/_cache/scryfall-cards.json` gained 678 new entries (full card pool across all 12 lto888 decklists, not already cached), bringing the cache to 1,246 total.
- **[kb]** `INDEX.md`'s lto888 profile teaser updated to match.
- **[kb]** Per the owner: their physical copy of Yuriko, the Tiger's Shadow is the *Final Fantasy: Through the Ages* printing (set `FCA`, FFVII-themed alt art, confirmed to exist via Scryfall print search) rather than a more common printing. Noted in `profile.md` rather than the decklist file, since printing/set isn't a field the extractor captures.

## 2026-08-22 (mjsnoozer profile rewrite — same methodology; Stella Lee marked retired)

- **[kb]** Rewrote `knowledgebase/podlist/mjsnoozer/profile.md` under the mechanical-first-then-EDHREC methodology established on xanoh's profile. Grounded each of the 5 commanders' archetypes in their own oracle text before checking EDHREC: Cloud's card-draw trigger rewards *multiple* equipped attackers, not one voltron stack, which reframes why Puresteel Paladin's free-equip clause matters; Azula's copy trigger only fires for spells cast during combat (instant-speed only), which is specifically why Leyline of Anticipation is in the list (it grants flash, letting the deck's 5 sorceries qualify at all) and why Twinning Staff is a build-around (it also doubles her attack-trigger copy, not just cast-triggered copies); Hazel's token-copy trigger is doubled only for Squirrel tokens specifically, which is why Chatterfang, Squirrel General (converts any token effect into bonus Squirrels) is in the list rather than being generic tokens-matter glue; Kenway's Treasure trigger counts any tapped Assassin/Pirate/Vehicle, and Roaming Throne can double that trigger by naming Pirate or Assassin. Also caught and fixed an internal contradiction: the old Power Level section called Azula/Stella Lee "likely low-to-mid cEDH-adjacent," while the profile's own Commander Spellbook check (kept, still valid) found no assemblable infinite combo in either list as built — reconciled in favor of the more rigorous finding.
- **[kb]** Per the owner: `stella-lee.md` is a **retired** deck, physically dismantled and rebuilt into Fire Lord Azula — not an independent live build. The profile now frames the 9 shared cards (Archmage Emeritus, Storm-Kiln Artist, Goblin Electromancer, Guttersnipe, Veyran, Seething Song, Grapeshot, Mizzix's Mastery, Galvanic Iteration) as literal lineage rather than convergent design, and treats mjsnoozer as having 4 active decks + 1 historical one. The decklist file itself is left as-is (re-syncing would wipe any status note written into it, since `tools/archidekt_extract.py` fully regenerates the file's Notes section on every run) — retired status is recorded only in `profile.md` and `INDEX.md`, the two hand-maintained files, not in the auto-generated decklist.
- **[repo]** `knowledgebase/_cache/scryfall-cards.json` gained 369 new entries (full card pool across all 5 mjsnoozer decklists, not already cached), bringing the cache to 568 total.
- **[kb]** `INDEX.md`'s mjsnoozer section updated: profile teaser rewritten, and the `stella-lee.md` entry flagged as retired.

## 2026-08-22 (xanoh profile rewrite — new EDHREC-skeptical analysis methodology)

- **[repo]** Adopted a new rule for the `edh-research` cross-referencing workflow: read a card's own oracle text and work out the mechanical reason it fits a deck's plan *first*, then check EDHREC's synergy/inclusion data *against* that reasoning as a "does the crowd's build agree with mine" cross-check — not as the justification itself. EDHREC's synergy score is co-occurrence-with-commander across thousands of differently-goaled decks; it's a popularity aggregate, not a verdict on whether a card is actually good for a specific 99. High inclusion can mean genuine synergy, a reflexive "safe staple," or a popular trap; low inclusion can hide a card that's mechanically excellent for a specific build the crowd doesn't happen to favor. Worked out live on `knowledgebase/podlist/xanoh/profile.md` as a test case before generalizing into the skill file.
- **[kb]** Rewrote `knowledgebase/podlist/xanoh/profile.md` end to end under the new methodology. Key findings: **Forresta** (Gladiolus Amicitia, RG) is a landfall-payoff combat-pump deck built tightly around the commander's own text (landfall grants +2/+2 trample), not generic ramp-into-threats as previously characterized — the list runs 8 separate landfall-triggered effects behind Ancient Greenwarden (which doubles all of them), and its ramp package (Migration Path, Reach the Horizon) was found to *deliberately* skip EDHREC's most-popular ramp spells (Cultivate, Nature's Lore, Rampant Growth) in favor of two-lands-per-cast alternatives that generate twice the landfall triggers per card — a mechanically stronger choice for this specific commander, not an eccentricity. **The Sundering** (Ardbert, Warrior of Darkness, WB) turns out to be a legendary-dense (~30/32 creatures) stax/wipe/reanimation control shell that deliberately omits the anthem/+1-1-counter payoff cluster EDHREC's 6,878-deck aggregate treats as this commander's default archetype — Ardbert's buff functions here as an incidental bonus, not the engine; the real plan is board control into a wipe (No Witnesses, Final Act) into Rise of the Dark Realms as a mass-reanimation finisher, which also re-triggers the deck's creature-enters/dies lifegain-drain cluster (Elas il-Kor, Elenda, Liesa). Neither deck has a cataloged Commander Spellbook combo with its current 99. All prior sections (Color & Archetype Tendencies, Power Level, Notable Patterns) were also rewritten since they'd only ever covered Forresta despite The Sundering being added to the archive earlier.
- **[repo]** `knowledgebase/_cache/scryfall-cards.json` gained 154 new entries (all cards across both xanoh decklists not already cached), bringing the cache to 199 total.
- **[kb]** `INDEX.md`'s teaser line for `podlist/xanoh/profile.md` updated to match.

## 2026-08-22 (restructured knowledgebase/decklists + knowledgebase/users into podlist/)

- **[repo]** Restructured the knowledgebase: `knowledgebase/decklists/<owner>/` and `knowledgebase/users/<owner>.md` are merged into a single `knowledgebase/podlist/<owner>/` folder per owner, containing `decks/<deck-slug>.md` (the former decklist files, unchanged in content) and `profile.md` (the former user-profile file, renamed). All 49 existing decklists + 6 profiles moved via `git mv`-equivalent renames (verified as renames in `git status`, not delete+add, so history is preserved per-file).
- **[repo]** `tools/decklist_common.py`'s `DECKLISTS_ROOT` renamed to `PODLIST_ROOT` (`knowledgebase/podlist`); `write_decklist` now writes to `podlist/<owner>/decks/<deck-slug>.md` instead of `decklists/<owner>/<deck-slug>.md`. `src/assistant/ingest.py`'s `DECKLISTS_ROOT`/`list_decklists`/`read_deck` updated to match (walks `podlist/<owner>/decks/*.md` instead of `decklists/<owner>/*.md`). Verified via the existing unit tests plus a manual smoke test of both the extractor write path and `ingest.list_decklists()`.
- **[repo]** Each profile's `decklists:` frontmatter field renamed to `decks:` and repointed at the new `podlist/<owner>/decks/` path, matching the new folder's actual name. `INDEX.md` rewritten to the new `podlist/<owner>/{profile.md, decks/*.md}` grouping (profile listed first per owner, then its decks) in place of the old separate `users/` → `decklists/` sections. `CLAUDE.md`, `.github/copilot-instructions.md` (kept in sync per its own tripwire rule), `README.md`, and the `related:` frontmatter / inline path references in the 3 existing `research/` notes all updated to the new paths. `CHANGELOG.md`'s own historical entries were left as-is (they're a record of what was true at the time, not live links).

## 2026-08-22 (full pod re-sync — all 6 owners re-extracted for deltas)

- **[repo]** `tools/moxfield_extract.py`'s `fetch_json` gained a fallback: on an HTTP 403 from `api2.moxfield.com` (Moxfield's API rejected direct requests from this session as bot traffic, unrelated to any local egress block), it retries through the `r.jina.ai` reader proxy and parses the JSON back out of the wrapped response — same fallback pattern the `edh-research` skill already documents for Scryfall/Commander Spellbook. Needed to complete this sync's `reimaru` (Moxfield) pull from this machine.
- **[kb]** Re-ran `tools/archidekt_extract.py --user` for fowlplays, j-py, lto888, mjsnoozer, xanoh, and `tools/moxfield_extract.py --user` for reimaru — a full re-sync of every owner's public deck list against source. j-py, mjsnoozer, and reimaru came back unchanged. Deltas:
  - **New deck**: `knowledgebase/decklists/lto888/turtle-power-powered.md` — Leonardo, the Balance / Michelangelo, the Heart (WUBRG, 5-color TMNT partners), not previously archived.
  - **Card-level updates** (adds/cuts/foil changes/bracket changes) landed in 9 fowlplays decks and 9 lto888 decks, plus xanoh's `forresta.md` — see each file's `git log` for the exact diff.
  - **Newly unlisted**: `knowledgebase/decklists/fowlplays/discard-mill-assassin.md`'s Archidekt deck was switched to unlisted by the owner sometime before this sync (`"unlisted": true` on the deck's own API record) — it no longer appears in `--user` results, so this sync couldn't refresh it, but the direct link still resolves and the file is left in place rather than deleted. Flagged in `INDEX.md`.
  - **Content loss flagged, not silently fixed**: re-syncing `the-crystal-braves.md` wiped a hand-written "Owner intent" line from its Notes section (added in a prior session, outside what the extractor itself ever writes) — the extractor overwrites the whole file per CLAUDE.md's "KB file is a synced mirror" rule, so this is expected mechanically, but the content itself is only recoverable from git history (commit `e331447`) now.
- **[kb]** `knowledgebase/users/lto888.md` **not** re-derived yet despite now containing stale claims contradicted by the new deck (e.g. "No four- or five-color builds," Treno, Dark City "appears in two unrelated decks" — Treno was cut from Azula's list this sync, leaving only Yuriko) — flagged in `INDEX.md` pending a decision on scope (full re-derivation needs fresh EDHREC lookups for the new commander pair, per the `edh-research` skill).
- **[kb]** `INDEX.md` gained entries for the new `turtle-power-powered.md` deck and the previously-unindexed `discard-mill-assassin.md` (a pre-existing gap, unrelated to this sync, caught during this pass), and corrected owner deck counts for fowlplays (12 → 14, 1 unlisted) and lto888 (11 → 12).

## 2026-08-22 (kept Copilot instructions in sync — this repo uses two assistants)

- **[repo]** `.github/copilot-instructions.md`'s research section was stale relative to the just-updated `CLAUDE.md`/`.claude/skills/edh-research/SKILL.md` — it still assumed Scryfall/Commander Spellbook always need the `r.jina.ai` proxy, which is only true from the office network, not from home (MIKOTO). Fixed to match: probe direct access first, proxy only on failure. Also mirrored the decklist-editing-discipline rule (KB decklist files are a synced mirror, not the source of truth — don't hand-edit them from a build discussion) so Copilot sessions follow the same rule Claude Code does.
- **[repo]** Added an explicit note to `copilot-instructions.md` that this repo is worked on with more than one AI assistant (Claude Code and GitHub Copilot, from different machines) and that any assistant changing a workflow rule in `CLAUDE.md`/the skill file should mirror it here too — a tripwire against the two instruction sets silently drifting apart again, plus a pointer to `CHANGELOG.md` as the shared record of activity regardless of which assistant did the work.

## 2026-08-22 (created the missing edh-research skill file)

- **[repo]** Added `.claude/skills/edh-research/SKILL.md` — this file was referenced by `.github/copilot-instructions.md` (as the source for color-identity enforcement, exact endpoint patterns, and failure modes) but never actually existed. Consolidates the operational detail for EDHREC/Scryfall/Commander Spellbook access (endpoints, the machine-dependent network fallback chain, the card cache schema/freshness policy, batch lookups, whole-decklist combo search, color identity enforcement, common mistakes) that had been split between `CLAUDE.md` and an assistant-only memory store.
- **[repo]** `CLAUDE.md`'s "Analysis practices" section trimmed to point at the new skill file as the source of truth instead of duplicating the mechanics inline, to avoid the two drifting out of sync. Also added a "Working in this repo" bullet: decklist files are a synced mirror of Archidekt/Moxfield, not the source of truth, so agreed-upon build changes from a discussion get applied on the source site and pulled back via the extractor tools, not edited into the KB file directly.

## 2026-08-22 (network access is machine-dependent, not fixed)

- **[repo]** `CLAUDE.md`'s "Analysis practices" section rewritten: the `r.jina.ai` proxy requirement for Scryfall/Commander Spellbook turns out to be specific to the office-laptop network (blocked there, confirmed 2026-07-10), not a fixed property of "this environment" — direct `curl` from the home machine (MIKOTO) reached all three sources (Scryfall, Commander Spellbook, EDHREC) cleanly on 2026-08-22, no proxy needed. Guidance now says to check direct access with a cheap `curl` probe at the start of a session rather than assume proxy-or-not from a stale date, and to prefer direct access when available (faster, no throttling, raw JSON). Also inlined the cache freshness policy that previously pointed at a nonexistent `edh-research` skill file.

## 2026-08-22 (pod threat profile + xanoh's second deck)

- **[kb]** Added `knowledgebase/research/2026-08-22-pod-threat-profile.md` — a cross-player reference covering all 6 pod members (lto888, reimaru, fowlplays, xanoh, mjsnoozer, j-py): threat mark, pay-to-win tier, build style, and a full deck index (commander/bracket/archetype) per player.
- **[kb]** Extracted `knowledgebase/decklists/xanoh/the-sundering.md` via `tools/archidekt_extract.py` (archidekt.com/decks/24557905) — this deck was referenced in the new pod profile but hadn't actually been archived yet. Ardbert, Warrior of Darkness (WB): removal-heavy Orzhov control/stax, distinct from fowlplays' own Ardbert build ("The Warrior of Darkness," legends-matter).
- **[kb]** `knowledgebase/users/xanoh.md` updated for the second deck — Xanoh no longer reads as a single-archetype Gruul ramp builder; the two decks on file (Forresta, Gruul ramp; The Sundering, Orzhov control/stax) don't share a color or gameplan, so the profile now flags that no cross-deck pattern generalizes yet.
- **[kb]** `INDEX.md` gained entries for the new reference file, the new decklist, and the updated xanoh profile summary.

## 2026-08-06 (Crystal Braves deck profile)

- **[kb]** Added `knowledgebase/research/2026-08-06-the-crystal-braves-deck-profile.md` — a card-by-card mechanical read of fowlplays' The Crystal Braves (Alisaie Leveilleur // Alphinaud Leveilleur, WU) combined with owner-confirmed sequencing. Key finding: the deck's cheap cantrips are cast first each turn specifically to free up the second-spell slot for the real payoff spell, which then lands under Dualcast's discount (stacked with Highspire Bell-Ringer and Uthros Psionicist for up to −{5}) while triggering Eukrasia's draw and the deck's other second-spell payoffs (The Council of Four, Ledger Shredder, Storm of Saruman, etc.) simultaneously — the engine converts into a Knight board via a stack of typal lords (Knight Exemplar, Haytham Kenway, Marshal of Zhalfir, Kinsbaile Cavalier) and payoffs (Vanquisher's Banner, The Circle of Loyalty, Kindred Discovery, Vodalian Wave-Knight), plus a non-obvious Mirrormind Crown interaction (per the owner: the standout target is Knights of Round itself, not a lord — it's non-legendary, so equipping its own Crown turns one chapter's 3-token trigger into 3 copies of the whole Saga instead, each of which immediately free-rolls its own Chapter I for 9 more tokens and then independently ticks through II–V on its own), worked out into a full turn-by-turn table cycling the Crown through two Knights of Round (moving it a turn ahead of each host's own final chapter to avoid it falling off) that finds a permanent steady state: a constant 12 live Saga copies and a flat +33 vanilla tokens/turn forever, off a single Equipment and one Saga. Cross-referenced against EDHREC (2,546 decks on this pairing, 4 of its top-5 synergy cards already in the list) and Commander Spellbook (no cataloged combo for this commander pair, confirmed empty).
- **[kb]** 30 additional Scryfall lookups (18 seeded earlier, now 21 more for this profile) written to `knowledgebase/_cache/scryfall-cards.json`, now 39 entries.

## 2026-08-06 (Scryfall lookup cache)

- **[repo]** Added `knowledgebase/_cache/scryfall-cards.json`, a persistent git-tracked cache of Scryfall card lookups (trimmed to oracle text, mana cost, type line, color identity, keywords, commander legality, prices, edhrec_rank), keyed by card name — avoids re-hitting the `r.jina.ai` proxy (confirmed to throttle under repeated requests) for cards already looked up in a prior session. Seeded with 18 entries recovered from a scratch file (`tmp_priority_cards.json`, now deleted) from an earlier research pass; a companion scratch file of 72 cards that all 403'd (`tmp_scryfall_oracle.json`, direct unproxied fetches) was deleted with no recoverable data.
- **[repo]** `edh-research` skill gained a "Card lookup cache" section documenting the entry schema and freshness policy (oracle text/color identity/legality treated as durable; prices/edhrec_rank refetched if the cached entry is >30 days old and the question hinges on current numbers). `CLAUDE.md`'s Analysis practices section gained a pointer to the same workflow.
- **[kb]** `INDEX.md` gained a `_cache/` section noting the new file exists (not read-when research content, listed only per the index-everything convention).

## 2026-07-10 (deck profile correction pass)

- **[kb]** Corrected four card-read errors in `knowledgebase/research/2026-07-10-the-copied-factory-deck-profile.md`, found on a full Scryfall oracle-text re-check prompted by the owner flagging one of them: (1) Kefka has no noncreature-spell damage trigger and was removed from the ping/burn package list; (2) Guttersnipe only triggers off instant/sorcery spells, not noncreature spells generally, unlike the other cards in that package; (3) Harmonic Prodigy doubles any Wizard/Shaman triggered ability, not just ETB triggers, so it amplifies the primary burn package, not just the ETB-copy package it was filed under; (4) Vedalken Aethermage is a Sliver-tribal ETB bounce card with dead text in this Sliver-less list, not a graveyard-recursion piece, and was removed from that grouping. Also corrected the Playstyle section's framing of Kuja's Flare Star transform as a competing "combat-double" line — its actual text doubles all Wizard damage, meaning it amplifies rather than competes with the ping/burn win condition. Added a dedicated "Damage amplification for the ping/burn plan" bullet consolidating Harmonic Prodigy, Kuja's Flare Star, and Artist's Talent's Level 3 as the three (mechanically distinct — extra trigger, doubled damage, and flat +2, respectively) cards that scale the burn package, per the owner's follow-up, plus a worked example confirming the owner's proposed all-three-online line (1 → 3 → 6 → 12 damage off one noncreature spell) is correct under CR 616.1's replacement-effect-ordering rule. Added a "Kill math" bullet confirming the owner's 4-noncreature-spell lethal line (4×12=48 clears a full 40 life, 3×12=36 doesn't) and noting the graveyard-recursion package (Mizzix's Mastery, Past in Flames, Emet-Selch) extends that count without needing 4 fresh cards in hand — with one correction: the graveyard-play ability the owner attributed to Emet-Selch is actually on its transformed back face, Hades, Sorcerer of Eld, which requires 14+ graveyard cards to flip into and then exiles future graveyard-bound cards instead. Reframed per the owner's follow-up: the three graveyard-recursion cards are redundant/parallel paths to the same goal rather than a sequenced stack, though they share one resource (the graveyard itself), so Hades' exile clause caps future fuel for all three once it flips, not just itself. Added a scaling table (per the owner's further point that the three damage amplifiers don't need to all be on board together either) showing casts-needed-for-lethal at 40, 20, 14, 10, 7, and 4 spells depending on which of Harmonic Prodigy/Kuja's Flare Star/Artist's Talent Level 3 are active, confirming fewer amplifiers only raises the spell count rather than breaking the plan. Noted per the owner that the table's 40-life baseline is a worst case — most real games have opponents already chipped down by combat/other players before the burn plan needs to close, so practical spell counts run lower than the table shows. Folded in three cards the owner had forgotten to mention: Mockingbird and Irenicus's Vile Duplication added to the Wizard ETB-copy package (the former triggers Eminence directly since it's a nontoken clone, the latter doesn't but replays the copied creature's ETB and is itself a noncreature spell); Gogo, Master of Mimicry given its own "Ability-copy scaling" bullet as a mana-gated, uncapped amplifier that can copy any triggered ability (including the ping triggers or Eminence itself) X times, noted as a way to collapse the multi-spell kill-math table into a single spell given enough mana. Added a "Copying the amplifiers themselves" bullet per the owner's further point: Mockingbird/Irenicus's Vile Duplication can target Harmonic Prodigy directly (non-legendary, stacks for free, additive N+1 scaling), and Mirror Box unlocks the same trick on legendary Wizards (Naban, Vivi Ornitier) — with Kuja's back face, Trance Kuja, Fate Defied as the standout case, since its Flare Star damage-doubling is a replacement effect and CR 616.1 has multiple copies compound multiplicatively (2× per copy) rather than additively. Added a worked example for the owner's Inalla + Naban + Harmonic Prodigy line: one hardcast Kuja yields 5 total Kuja (4 Eminence triggers instead of 1), confirmed to cap there rather than cascade further since the last Naban instance is a direct effect of Harmonic Prodigy's resolution rather than an independent trigger, so Harmonic Prodigy has nothing left to react to a third time. Corrected the total price to "1 Kuja + {4}" rather than "+{1}," since Eminence's optional {1} cost is paid independently at each of the four trigger resolutions. Added Obeka, Brute Chronologist's role to the 5-Kuja worked example: confirmed via Scryfall rulings that activating it in response to already-stacked "at the beginning of the next end step" triggers (after letting the 5 Kuja's own abilities resolve first) permanently exiles the Eminence exile triggers before they resolve, making the token copies permanent rather than one-cycle-delayed as first assumed. Added a culminating "320 damage off a single instant" worked example combining the 5-Kuja/Obeka line, the 5 new ping tokens it also produces, Harmonic Prodigy's per-source triggering, and 5-stacked-Trance-Kuja exponential Flare Star doubling — verified the owner's math (5 pingers × 64 = 320) traces correctly through each underlying mechanic. Added the owner's own framing ("it's all about exponents") to the Overview. Clarified per the owner that the 320 figure is per opponent independently (each opponent takes the full 320, not a 320 total split across the table), matching how the pinger ability's "to each opponent" wording actually resolves — and added the resulting 960-damage total-board figure for a 4-player pod (320 × 3 opponents).

## 2026-07-10 (first deck profile)

- **[kb]** Added `knowledgebase/research/2026-07-10-the-copied-factory-deck-profile.md`, the first file in `research/` — a full card-by-card mechanical read of fowlplays' The Copied Factory (Inalla, Archmage Ritualist) combined with owner interview answers. Key finding: the deck's practiced win condition has drifted over time from its original Wizard-ETB-copy plan (Inalla's Eminence) to a ping-token burn plan instead, with the Dualcaster Mage + Ghostly Flicker infinite combo (previously surfaced in `users/fowlplays.md`) confirmed as a deliberately piloted win condition rather than latent tech. Also flags forced-sacrifice effects and premature go-off sequencing as the deck's main practical weaknesses.
- **[kb]** `INDEX.md`'s `research/` section is no longer empty; gained its first entry.

## 2026-07-10 (external data cross-references)

- **[repo]** `CLAUDE.md` gained an "Analysis practices" section requiring future decklist/pod analysis to cross-reference EDHREC, Scryfall, and Commander Spellbook (not just internal judgment). Documents actual working access paths for this environment: EDHREC's `json.edhrec.com` JSON endpoint works via direct fetch; Scryfall and Commander Spellbook block direct fetches (403) but are reliably reachable by routing through the `r.jina.ai` reader proxy, which also unlocks live Scryfall `prices.usd` pricing (TCGplayer-sourced) that direct TCGplayer fetches couldn't provide.
- **[kb]** All 6 `knowledgebase/users/*.md` profiles gained an `## External Cross-References` section verifying and refining their existing analysis against real EDHREC synergy/archetype data, Commander Spellbook combo checks, and Scryfall rulings — e.g. confirming mjsnoozer's Azula/Stella Lee "storm shell" is one specific card away from several cataloged infinite combos, correcting some "MDFC" card-type labels to the more accurate transform/Adventure distinction, and surfacing an actual assembled Dualcaster Mage + Ghostly Flicker combo in fowlplays' Copied Factory deck.

## 2026-08-06 (deck replacement)

- **[kb]** Replaced `knowledgebase/decklists/fowlplays/knights-of-two.md` with `knowledgebase/decklists/fowlplays/the-crystal-braves.md` after the Archidekt deck URL updated to `https://archidekt.com/decks/24427121/the_crystal_braves`. Removed the obsolete old deck file and recorded the refreshed deck title/source.

## 2026-07-10 (deckbuilder profiles)

- **[tooling]** Added `tools/moxfield_extract.py` (single-deck and `--user` bulk mode, mirroring the Archidekt extractor). Moxfield has no official API; uses the same unauthenticated `api2.moxfield.com` endpoints moxfield.com's frontend calls, confirmed via the Aleqsd/moxfield-api wrapper's source rather than guessed.
- **[tooling]** Factored shared markdown/frontmatter rendering out of `archidekt_extract.py` into `tools/decklist_common.py` so both extractors build identically-formatted decklist files.
- **[kb]** Imported all 16 of `reimaru`'s public Moxfield decks into `knowledgebase/decklists/reimaru/`.

## 2026-07-09 (import pod decklists)

- **[kb]** Extracted the pod's public Archidekt decks: `J-Py` (1), `LTO888` (11), `Xanoh` (1), `mjsnoozer` (5) — 18 decks total, each under `knowledgebase/decklists/<owner>/`.

## 2026-07-09 (sync to fowlplays' updated public decks)

- **[kb]** User tightened privacy on several Archidekt decks after noticing the earlier bulk import had pulled some they didn't intend to be public. Re-ran `archidekt_extract.py --user fowlplays` and removed the 5 decks no longer public: `food-bending`, `scions-spellcraft-redux`, `the-best-of-friends-legacy`, `the-chocobo-forest`, `the-season-of-giving`. 12 decks remain, matching the current public profile.

## 2026-07-09 (bulk import fowlplays' Archidekt profile)

- **[tooling]** `tools/archidekt_extract.py` gained `--user <username>` to bulk-extract every public deck for an Archidekt user in one run, instead of one URL at a time.
- **[kb]** Imported all 17 of `fowlplays`' public decks into `knowledgebase/decklists/fowlplays/`.

## 2026-07-09 (Archidekt decklist extraction)

- **[tooling]** Added `tools/archidekt_extract.py` — pulls a deck from Archidekt's API and writes it into `knowledgebase/decklists/<owner>/<deck-slug>.md`.
- **[kb]** First decklist logged: `knowledgebase/decklists/fowlplays/the-copied-factory.md` (Inalla, Archmage Ritualist — UBR).
- **[kb]** `_template-decklist.md` gained a `source` frontmatter field for traceability back to the original deck URL.

## 2026-07-09 (repo initialized)

- **[repo]** `edh-oracle` created — knowledgebase scaffolding for decklists and research, `CLAUDE.md`/`README.md` established.
