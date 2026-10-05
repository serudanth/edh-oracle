---
type: review
title: "The Hamster Catapult — Deck Profile & Mechanical Audit"
domain: strategy
tags: [#deck-profile, #deck-review, #gruul, #minsc-and-boo, #stompy, #counters, #fling, #burn]
related: [podlist/charles/decks/the-hamster-catapult, podlist/charles/profile, research/2026-08-25-pdd-deck-analyzer-engine]
source: fowlplays
last_updated: 2026-10-05
---

# Deck Profile: The Hamster Catapult

- **Commander:** [Minsc & Boo, Timeless Heroes](https://scryfall.com/card/clb/285/minsc-and-boo-timeless-heroes) ({2}{R}{G}, Loyalty: 3)
- **Deck Source:** [Archidekt #15733915](https://archidekt.com/decks/15733915/the_hamster_catapult)
- **Local Mirror:** [`knowledgebase/podlist/charles/decks/the-hamster-catapult.md`](file:///home/cpc9181/projects/edh-oracle/knowledgebase/podlist/charles/decks/the-hamster-catapult.md)
- **Owner:** `fowlplays` (Charles)
- **Automated Engine Output:** **5.8 / 10.0** (Bracket 2 — Casual Battlecruiser)
- **Audited Realistic Power Score:** **7.3 / 10.0** (Bracket 3 — Focused Mid-Power Stompy)

---

## 1. Executive Summary & The Underestimation Thesis

*The Hamster Catapult* is built around one of the most explosive, tournament-proven planeswalker commanders printed in modern Magic: **Minsc & Boo, Timeless Heroes**. Despite its deceptive casual aesthetic, the deck operates as a high-velocity **Gruul Aggro-Stompy, +1/+1 Counter Scaling, and Threaten-Fling Burn Engine**.

The automated `deck_analyzer_engine.py` scored the deck at **5.8 / 10.0 (Bracket 2)**. This rating is artificially suppressed due to three distinct heuristic blind spots in the automated engine:

1. **The Keyword Heuristic Trap ("Aristocrats / Sacrifice"):**
   The automated engine scanned the word `"sacrifice"` on Minsc & Boo's `−2` ability and classified the entire deck as **"Aristocrats / Sacrifice"**. Under the Aristocrats weighting profile, the deck was heavily penalized for lacking recursive graveyard blood-artists (e.g. Zulaport Cutthroat, Blood Artist, Dictate of Erebos) and death loops. In reality, the sacrifice mechanic here is a ballistic **Fling finisher and card-drawing burst**, not an aristocrats attrition engine.
2. **Command Zone Card Advantage Blind Spot:**
   The engine registered only **1 repeatable draw engine** in the 99 (`Bonders' Enclave`), assigning an Engine score of `72.0`. In actual play, Minsc & Boo represents a **recurrent 4-to-8 card burst draw engine directly from the command zone** that refills your hand every other turn.
3. **The "Infinite-Combo Bias" in the Closing Metric:**
   The engine scored the deck's Closing capability at a dismal **`17.0 / 100`** because the list runs no two-card infinite combos and only 1 tutor. This metric completely discounted the deck's primary deterministic kill mechanisms: [Triumph of the Hordes](https://scryfall.com/card/nph/123/triumph-of-the-hordes) (mass trample infect), [Raphael, the Muscle](https://scryfall.com/card/tmt/17/raphael-the-muscle) (damage doubling), [Sazh Katzroy](https://scryfall.com/card/fic/89/sazh-katzroy) (exponential counter doubling), [Casey Jones, Back Alley Brute](https://scryfall.com/card/tmt/22/casey-jones-back-alley-brute) (counter-to-burn damage), [Kessig Wolf Run](https://scryfall.com/card/isd/244/kessig-wolf-run), and repeatable direct-damage flings to player faces.

When calibrated against its true operational cadence, *The Hamster Catapult* comfortably performs at **7.2 – 7.4 (Bracket 3)**.

---

## 2. The Core Strategic Engines

### Engine 1: The Command Zone Hamster Velocity Loop
Minsc & Boo enters for 4 mana ({2}{R}{G}) with 3 loyalty and an immediate ETB/upkeep trigger creating **Boo** (a 1/1 red Hamster with Trample and Haste).

```
Turn 4: Cast Minsc & Boo (Loyalty 3)
  └─> ETB creates Boo (1/1 Trample, Haste)
  └─> Activate +1: Target Boo -> Boo becomes a 4/4 Trample Haste (Loyalty 4)
  └─> Attack with 4/4 Trample Haste immediately.

Turn 5: Upkeep: Boo is already alive.
  └─> Activate +1: Target Boo -> Boo becomes a 7/7 Trample Haste (Loyalty 5)
  └─> Combat: Attack with 7/7 Trample Haste.
  └─> Postcombat: Activate −2 (Loyalty 3): Sacrifice Boo
      └─> Deal 7 damage to ANY target (dome opponent or remove threat)
      └─> Draw 7 CARDS.

Turn 6: Upkeep: Minsc & Boo creates a FRESH 1/1 Trample Haste Boo for {0} mana.
  └─> Loop repeats with a full 7-card replenished hand.
```

This sequence represents an unblockable engine cycle: **11 combat damage + 7 direct burn damage + 7 cards drawn** across two turns, powered exclusively by a 4-mana commander without casting a single additional non-land card.

---

### Engine 2: +1/+1 Counter Accelerators & Damage Multipliers
The 99 is tailored to compound the counters Minsc & Boo places, accelerating Boo well beyond the natural +3/+3 curve:

- **[Sazh Katzroy](https://scryfall.com/card/fic/89/sazh-katzroy)**: Whenever Sazh attacks, put a +1/+1 counter on target creature, **then double the number of +1/+1 counters on that creature**.
  - *Worked line:* Boo has three counters from Minsc (+1). Sazh attacks, places a counter (4 counters), and doubles to 8 counters. Boo is now a **9/9 Trample Haste** on Turn 5. Flung that turn, Boo deals 9 damage and draws 9 cards.
- **[Raphael, the Muscle](https://scryfall.com/card/tmt/17/raphael-the-muscle)**: *"Double all damage that creatures you control with counters on them would deal."*
  - Any creature with a counter deals double combat damage and double ability damage. A 7/7 Boo attacks for **14 trample damage**, and the −2 fling deals **14 direct damage**!
- **[Casey Jones, Back Alley Brute](https://scryfall.com/card/tmt/22/casey-jones-back-alley-brute)**: *"Whenever you put one or more +1/+1 counters on a creature you control, Casey Jones deals that much damage to target opponent."*
  - Activating Minsc & Boo's `+1` automatically deals **3 direct damage to an opponent's face**. Activating [Biogenic Upgrade](https://scryfall.com/card/rna/123/biogenic-upgrade) or attacking with [Leatherhead, Iron Gator](https://scryfall.com/card/tmt/26/leatherhead-iron-gator) triggers multiple simultaneous burns.
- **[Death's Presence](https://scryfall.com/card/rtr/121/deaths-presence)**: *"Whenever a creature you control dies, put X +1/+1 counters on target creature you control, where X is its power."*
  - The ultimate kinetic battery: When an 8/8 Boo is sacrificed to Minsc & Boo's `−2`, you deal 8 damage, draw 8 cards, and Death's Presence dumps **eight +1/+1 counters** onto another creature (e.g. [Wilson, Refined Grizzly](https://scryfall.com/card/clb/261/wilson-refined-grizzly), [Mowu, Loyal Companion](https://scryfall.com/card/war/167/mowu-loyal-companion), or [Halana and Alena, Partners](https://scryfall.com/card/vow/239/halana-and-alena-partners)).
- **[Bone Sabres](https://scryfall.com/card/40k/111/bone-sabres)**: Adds four +1/+1 counters on every attack, turning even small dorks into fling-ready missiles.

---

### Engine 3: The "Threaten & Catapult" Theft Sub-Plan
The list carries a dedicated package of temporary theft spells:
- [Act of Treason](https://scryfall.com/card/m10/124/act-of-treason)
- [Goatnap](https://scryfall.com/card/mh1/126/goatnap)
- [Involuntary Employment](https://scryfall.com/card/snc/110/involuntary-employment)
- [Portent of Betrayal](https://scryfall.com/card/ths/133/portent-of-betrayal)
- [Unexpected Request](https://scryfall.com/card/tmt/28/unexpected-request)

#### Tactical Application
1. **Tempo Disruption:** Steal an opponent's key blocker, indestructible threat, or commander.
2. **Combat Pressure:** Attack the owner (or another player) with their own hasted creature.
3. **Permanent Removal via Catapult:** In the postcombat main phase, sacrifice the stolen creature to Minsc & Boo's `−2` (or [Fling](https://scryfall.com/card/jmp/320/fling) / [Special Move](https://scryfall.com/card/tmt/27/special-move)). The opponent's threat is permanently removed, and its power is dealt as burn damage to another target.
4. **The [Amorphous Axe](https://scryfall.com/card/cmr/295/amorphous-axe) Interaction:**
   Amorphous Axe grants +3/+0 and makes the equipped creature **every creature type**. If you attach Amorphous Axe to a stolen creature (or use *Unexpected Request* which attaches equipment for free), **the stolen creature becomes a Hamster**! When you sacrifice it to Minsc & Boo's `−2`, you not only deal its power as damage—**you draw cards equal to its power!**

---

### Engine 4: Stompy Finishers & Overrun Closers
When the board stalls, the deck does not rely on chip damage:
- **[Triumph of the Hordes](https://scryfall.com/card/nph/123/triumph-of-the-hordes):** Gives all creatures +1/+1, trample, and **infect**. An 8-power Boo, a trampling Wilson, or an amplified Halana & Alena closes the table in a single swing.
- **[Quartzwood Crasher](https://scryfall.com/card/iko/201/quartzwood-crasher):** Triggers off all trample combat damage dealt by your team, creating an X/X Dinosaur Beast token that can itself be pumped and flung.
- **[Old One Eye](https://scryfall.com/card/40k/96/old-one-eye):** Grants universal trample to your entire board and provides a recurring 5/5 Beast token.
- **[Nyxbloom Ancient](https://scryfall.com/card/thb/190/nyxbloom-ancient):** Triples mana production, feeding directly into lethal [Kessig Wolf Run](https://scryfall.com/card/isd/244/kessig-wolf-run) activations or massive [Exocrine](https://scryfall.com/card/40k/76/exocrine) wipe/flings.

---

## 3. Calibrated Metric Audit

| Pillar | Automated Score | Calibrated Score | Calibration Rationale |
| :--- | :---: | :---: | :--- |
| **Velocity / Speed** | 85.7 | **86.0** | Accurate. Low average CMC (3.21) with natural haste on Boo. |
| **Engine / Card Advantage** | 72.0 | **95.0** | **Massive engine undercount:** Command zone draws 4–8 cards every other turn. Bugenhagen and Bonders' Enclave supplement. |
| **Interaction / Removal** | 32.0 | **65.0** | **Command zone removal overlooked:** Minsc & Boo deals 4–10 targeted damage repeatedly, killing planeswalkers and creatures at will. |
| **Resource Development** | 100.0 | **100.0** | Accurate. Solid green ramp package (Nature's Lore, Cultivate, Rampant Growth, Sol Ring, Llanowar Elves). |
| **Resilience** | 22.0 | **45.0** | Heroic Intervention, Return the Favor, and automatic Boo respawn provide strong recursive resilience. |
| **Closing / Win Conversion** | 17.0 | **65.0** | **Severe combo-bias flaw:** Overruns (Triumph), damage doubling (Raphael), counter doubling (Sazh), Kessig, and direct burn flings give fast closing power. |
| **Composite Power Score** | **5.8 / 10.0** | **7.3 / 10.0** | **Bracket 3 (Focused Casual / Mid-High Stompy)** |

---

## 4. Bottlenecks & Optimization Roadmap

While *The Hamster Catapult* is substantially stronger than its 5.8 baseline, a few tuning adjustments will cement its consistency against Lance's and Chad's top decks:

### Bottleneck A: The Land Count Surplus
- **Current State:** 38 lands in a list with an average CMC of 3.21 and a commander that draws 4–8 cards per cycle.
- **Recommendation:** Cut 2 lands down to **36 lands**. Flood risk is high when Minsc & Boo's card draw starts flowing.

### Bottleneck B: Turn-3 Minsc & Boo Acceleration
- **Current State:** The deck runs standard 2-mana and 3-mana ramp (Cultivate, Rampant Growth), meaning Minsc & Boo usually lands on **Turn 4**.
- **Optimization:** In Gruul, landing Minsc & Boo on **Turn 3** is catastrophic for opponents:
  - Add 1-mana ramp enablers: [Wild Growth](https://scryfall.com/card/afc/174/wild-growth), [Utopia Sprawl](https://scryfall.com/card/afc/172/utopia-sprawl), [Birds of Paradise](https://scryfall.com/card/rvr/133/birds-of-paradise), and [Delighted Halfling](https://scryfall.com/card/ltr/158/delighted-halfling).
  - *Result:* Turn 1 Dork/Aura → Turn 2 Setup/Counters → Turn 3 Minsc & Boo. Opponents are facing a 4/4 haste trample while still establishing their manabases.

### Bottleneck C: Protecting Minsc & Boo
- **Current State:** Minsc & Boo attracts immediate table heat once an 8-card draw or 8-damage fling occurs. The deck only runs *Heroic Intervention* and *Return the Favor*.
- **Optimization:**
  - Add cheap targeted protection: [Tamiyo's Safekeeping](https://scryfall.com/card/neo/211/tamiyos-safekeeping), [Tyvar's Stand](https://scryfall.com/card/one/190/tyvars-stand), or [Deflecting Swat](https://scryfall.com/card/c20/50/deflecting-swat) / [Bolt Bend](https://scryfall.com/card/war/115/bolt-bend).

### Bottleneck D: Threaten Reliability in Creature-Light Pods
- **Current State:** 5 sorcery-speed Threaten effects. These are devastating against Chad (Syr Gwyn, Cloud, Thraximundar) and Lance (Sephiroth, Doran), but can get stuck in hand against token or spellslinger boards.
- **Recommendation:** Trim 1–2 of the weaker Threatens (e.g. *Goatnap* or *Portent of Betrayal*) in favor of raw pump/haste enablers like [Invigorate](https://scryfall.com/card/2xm/172/invigorate) (free +4/+4 to fling for 0 mana!) or [Berserk](https://scryfall.com/card/cn2/175/berserk) (doubles Boo's power and trample before combat, then sacrifices at end of turn anyway!).

---

## 5. Pod Matchup Matrix

| Opponent / Deck | Matchup Dynamic | Strategic Priority |
| :--- | :--- | :--- |
| **Chad: Syr Gwyn / Cloud (Equipment)** | **Favorable (70/30)** | Steal their heavily equipped commander with *Act of Treason*, attack them with it, and fling it to remove it permanently while drawing cards with *Amorphous Axe*. |
| **Lance: Doran / Sephiroth** | **Favorable (65/35)** | Fling damage bypasses Doran's high toughness walls. Use Minsc & Boo's burn to snipe Sephiroth before reanimation loops stabilize. |
| **Lance: Y'shtola / Azula (Spellslinger B4)** | **Even (50/50)** | You must out-race their combo turns. Aggressively fling Boo at their life totals rather than playing control. A resolved *Triumph of the Hordes* ends them before *Citadel* loops begin. |
| **Julius: Miku Feather** | **Favored (60/40)** | Wait for Feather to tap out or target Feather with Minsc & Boo's fling activation when protection mana is down. |
