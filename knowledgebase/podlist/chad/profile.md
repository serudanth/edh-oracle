---
type: profile
title: "Chad (reimaru) — Deckbuilder Profile"
owner: chad
handle: reimaru
alias: Chad
signature_commander: "Y'shtola, Night's Blessed"
tags: [#profile]
related: [podlist/chad/persona]
decks: knowledgebase/podlist/chad/decks/
last_updated: 2026-09-17
---

## Overview
| Profile Field | Assessment |
|---|---|
| Signature Commander | **Y'shtola, Night's Blessed** ([*Y'shtola's Trigger, Trigger, Frown and Fall*](decks/yshtolas-trigger-trigger-frown-and-fall.md)) |
| Median Threat | **★★★★☆** |
| Designation | **Resilient Combat-Engine Warlord** |
| Summary | A warlord planeswalker who repeatedly turns equipment, sacrifice, tokens, enchantments, and creature deaths into durable engines, advancing the board while banking value for the next exchange. Most decks win through combat or attrition, but a control peak and several resilient sacrifice shells can make the battlefield increasingly difficult to recover. |

reimaru has 16 decks evaluated by the EDH Oracle Analyzer Engine with a median Power Score of **7.2 / 10.0** (★★★★☆), a mean of **7.1**, and a range of **5.1–8.6** (brackets 2–4; Y'shtola Control peak 8.6). Primary piloting archetypes span **Midrange / Engine Value** (6 decks), **Spellslinger / Storm** (5 decks), **Voltron / Equipment** (3 decks), **Aristocrats / Sacrifice** (1 deck), and **Cheat / Aggro Tempo** (1 deck). Across 16 decks, the portfolio holds 32 tutors and 22 fast mana sources. Automated analysis records are stored in `knowledgebase/podlist/chad/analysis/`.

reimaru's decks reveal a repeatable construction system: dependable artifact ramp, familiar interaction, and a small number of proven engines adapted across many commanders. Equipment-voltron and aristocrats recur most often, while the Wick list is one card from a documented infinite. Most decks avoid fast mana.

## Color & Archetype Tendencies
Color identity across 16 decks:

| Color | Commander identities | Share |
|---|---:|---:|
| White | 8 | 50.0% |
| Blue | 7 | 43.8% |
| Black | 8 | 50.0% |
| Red | 10 | 62.5% |
| Green | 2 | 12.5% |
| Colorless | 0 | 0% |

- reimaru's defining habit is iterative construction: a dependable ramp and interaction package is reused across many commanders, then reshaped into the commander's preferred engine. This produces a broad portfolio without sacrificing baseline consistency.
- Two strategic families dominate. Equipment decks spread or stack artifacts onto combat threats, while aristocrats decks turn sacrifice into cards, mana, and life swings. Feather, enchantress, dragons, tokens, and spellslinger lists expand the range without displacing those recurring systems.
- The player generally prefers proactive board development and value loops over pure control, but maintains one clear control/stax peak in Y'shtola. Green avoidance and the absence of fast mana impose a ceiling on speed, while repeated staples make the decks reliable once they establish themselves.

## Power Level & Construction Habits

- Brackets cluster tightly: 7 decks at bracket 2, 8 at bracket 3, and exactly one outlier at bracket 4 (Y'shtola's Trigger, Trigger, Frown and Fall, a stax/control build running Rhystic Study, Bolas's Citadel, Toxic Deluge, Fierce Guardianship, and Dovin's Veto). No bracket 1 (precon-level) or bracket 5 (cEDH) decks appear.
- Land counts average 35.3 across the 16 decks, right in the conventional 35-37 range, with no extreme outliers. The low end (32-33 lands: That's a Lot of Swords Cloud, Saheeli, Solphim) is explained by low curves and heavy mana-artifact/cost-reduction packages rather than genuine land-light risk-taking.
- Mono-color decks run correspondingly basic-heavy manabases (Solphim: 28 of 33 lands are Mountain; Slicer: 27 of 35 are Mountain; Stop Sac'ing Sephiroth: 25 of 37 are Swamp; Cloud: 21 of 32 are Plains), while the two- and three-color decks lean on shocklands, checklands, slow lands ("snarls"), and triomes rather than basics — fixing scales sensibly with color count.
- No fetch lands, original dual lands, or fast-mana artifacts (Mox-class, Mana Crypt) appear anywhere in the sample, even in the bracket 4 deck — ramp is consistently Sol Ring + Arcane Signet + signets/talismans/Commander's Sphere, a repeated low-variance package rather than a min-maxed one.
- Card choices mix genuine format staples (Sol Ring in all 16 decks; Vampiric Tutor in 3; Bolas's Citadel in 4; Fierce Guardianship in 2) with flavor/janky inclusions (Regal Bunnicorn, Three Dog, Galaxy News DJ, Cass, Hand of Vengeance, Suspicious Bookcase) — power-conscious but not optimized to the exclusion of theme.
- Singleton discipline holds throughout; deviations from 1-of are limited to basic lands, as expected for the format.

## Notable Patterns

- The two Feather decks demonstrate that reimaru adapts a commander concept instead of copying a list. One is aura-voltron with a high enchantment count; the other is a low-curve spellslinger deck with more than twice as many instants and a token/prowess finish.
- Equipment is the clearest repeated construction system: three decks share a substantial equipment and artifact-ramp core. This is a proven way to turn combat into cards, mana, or evasion rather than merely a repeated card package.
- Aristocrats is the other major system. Multiple decks reuse sacrifice outlets and death payoffs to convert creatures into cards, Treasures, and drain, giving the player a resilient plan that can recover value from board wipes.
- The portfolio is overwhelmingly proactive and value-oriented, with Y'shtola as the deliberate control exception. Even at its highest bracket, it uses conventional ramp rather than fast mana; Wick's missing Conspiracy is a near-combo warning, not a live combo.

## Decks

Full decklist archive: `knowledgebase/podlist/chad/decks/` (16 decks — see `INDEX.md` for individual entries).

## External Cross-References

*Original spot-checks 2026-07-10 against EDHREC (direct fetch), Scryfall (via WebSearch), and Commander Spellbook (via WebSearch) — not exhaustive across all 16 decks. Re-verified 2026-08-22 with direct API access throughout (replacing the WebSearch fallback) and the whole-decklist Spellbook endpoint where a combo claim is being checked, following the mechanical-first-then-EDHREC methodology: read the commander's own text and work out why a card fits before checking whether the crowd agrees, since EDHREC's synergy score is a popularity aggregate across thousands of differently-goaled decks, not a verdict on fit for a specific 99.*

**The two Feather decks — "opposites" claim confirmed at the archetype-tag level, not just by deck inspection.**
- EDHREC's tags for **Feather, the Redeemed** have shifted order since the original check: Spellslinger is now the largest theme (1,220 decks, per the fresh pull done for j-py's profile — same commander, same finding applies here), ahead of Sunforger (968), with Voltron (576), Aggro (404), and Cantrips (199) following. Sunforger was the largest tag at the original 2026-07-10 check (1,260 vs. 1,197) — a real reordering, not a citation error, and a reminder that EDHREC tag rankings aren't static. Either way, no Auras/Enchantress tag registers for this commander, and reimaru's build (Young Pyromancer, Monastery Mentor, Zada Hedron Grinder) matches the Spellslinger lane regardless of which tag is #1.
- EDHREC's tags for **Feather, Radiant Arbiter** re-checked fresh: Auras (173 decks), Enchantress (46), Voltron (26), Spell Copy (22) — same order as the original check, no drift. Top synergy card Kor Spiritdancer still matches the profile's "Aura Battler Feather" payoff callout directly.
- These remain EDHREC's two most-different tag sets for the same commander concept — the "opposites, not variants" framing holds up.

**Equipment voltron shell — partially, not wholly, an EDHREC-recognized package. Re-checked fresh, unchanged from the original finding.** Syr Gwyn, Hero of Ashvale (9,010 decks, salt 0.29): Whispersilk Cloak (0.071 synergy, 1,122 decks) and Commander's Sphere (0.031, 1,472) both still appear as recognized staples. **Kusari-Gama still does not appear anywhere in Syr Gwyn's EDHREC card lists** — the finding holds at essentially identical numbers to the original check. Two of the three signature pieces are broadly-played staples; Kusari-Gama still reads as a personal habit rather than an algorithmically-flagged synergy card for this archetype.

**Y'shtola deck — "control," not "stax," is still the EDHREC-recognized label. Re-checked fresh.** Y'shtola, Night's Blessed (51,088 decks now, salt 0.92 — genuinely one of the saltier commanders checked across this whole archive): Control (2,980) is still the dominant tag, ahead of Spellslinger (1,888), Lifegain (1,164), Burn (850), Lifedrain (806) — same order as the original check, no distinct Stax tag registers, so "control with a personal stax overlay" (Ghostly Prison/Propaganda) is still the more accurate framing than a commander-driven stax archetype.

**Commander Spellbook: no formal combo line among the Y'shtola deck's flagship cards** (unchanged from the original check) — Bolas's Citadel's actual cataloged combo partners (Aetherflux Reservoir, Sensei's Divining Top, Walking Ballista, Doomsday lines) don't appear in reimaru's list; Fierce Guardianship has no combo page, just free protective interaction. Consistent with the deck's bracket-4 (not bracket-5) self-rating.

**Wick deck leans into a minority archetype for its commander — re-checked fresh, unchanged.** Wick, the Whorled Mind (12,920 decks): Rats (1,630) and Rat Colony (664) still dominate; Spellslinger is still a minor tag at exactly 39 decks (identical count to the original check). Reimaru's list still sits in that minority spellslinger lane rather than the dominant tribal one.

**Wick + Conspiracy, re-checked via the whole-decklist endpoint (a more rigorous method than the original pass, which only searched for named combo pages).** The original check found a documented Wick + Ashnod's Altar + Arcane Adaptation combo and correctly noted neither piece is in this decklist. Running the actual 99 through Commander Spellbook's `find-my-combos` surfaces a *different*, simpler combo one card away: **Wick + Conspiracy** (naming Rat) is a cataloged two-card infinite loop — see Notable Patterns for the mechanism. Worth flagging precisely because it wasn't found by the original named-search approach; whole-decklist checking catches near-misses that checking one specific known combo by name does not.

**MDFC-as-flavor-payoff claim: mechanically accurate, terminology needs a correction.** Both Ishgard, the Holy See // Faith & Grief and Midgar, City of Mako // Reactor Raid are **Adventure cards, not modal double-faced cards (MDFCs)** — each is a single-faced land (Ishgard taps for W, Midgar taps for B, both enter tapped) with an Adventure sorcery half (Faith & Grief returns up to two artifact/enchantment cards from graveyard to hand; Reactor Raid sacrifices an artifact or creature to draw two cards) that exiles itself and can later be played as the land. The "fixing now, spell now, land later" behavior the profile describes is correct in substance, but future notes should call these Adventure lands rather than MDFCs.
