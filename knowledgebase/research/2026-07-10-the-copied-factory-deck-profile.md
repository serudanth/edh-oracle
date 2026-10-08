---
type: profile
title: "The Copied Factory — Deck Profile"
domain: strategy
tags: [#profile, #deck-profile, #wizards, #spellslinger, #storm, #inalla]
related: [podlist/charles/decks/the-copied-factory, podlist/charles/profile]
source: fowlplays
last_updated: 2026-10-07
---

## Overview

**The Copied Factory** is an explosive Grixis (UBR) Spellslinger/Storm combo deck commanded by **Inalla, Archmage Ritualist** (Bracket 4 / High-Power Spellslinger Combo). Rather than relying on Inalla as an on-board combatant, the deck uses her command-zone Eminence ability as a low-cost force multiplier for utility Wizards, ETB engines, and combo lines.

The deck's primary identity operates on four distinct, lethal axes:
1. **The Deterministic Machine Loop:** Assembling infinite mana, untaps, and spell casts via **Isochron Scepter + Dramatic Reversal**, feeding directly into win conditions like **Brain Freeze**, any active pinger, or drawing out via **Archmage Emeritus**.
2. **The Infinite Swarm Loop:** Generating infinite hasty 2/2 attackers via **Dualcaster Mage + Twinflame** for an immediate combat win that requires zero board setup.
3. **The Breach-Freeze Mill Engine:** Looping **Underworld Breach + Brain Freeze** to rapidly mill libraries, escape rituals and tutors, and eliminate opponents through deck exhaustion.
4. **The Exponential Combustion Engine:** Stacking additive damage replacements, multiplicative damage replacements, and trigger duplication on top of ping-producing Wizard tokens and creatures to deal overwhelming noncombat damage in a single burst turn.

---

## Architectural Evolution & Optimization Through-Lines (October 2026 Audit)

A comprehensive mechanical audit re-evaluated the list’s historical bottlenecks, formalizing its transition from an awkward high-power casual list into a fully realized **Bracket 4** deterministic powerhouse. The evolution followed four clear through-lines:

### Through-Line 1: Mana Rock Saturation & Scepter Viability (The 5-to-8 Pivot)
* **The Diagnostic Bottleneck:** The archived list ran only 5 mana rocks (`Sol Ring`, `Arcane Signet`, `Fellwar Stone`, `Izzet Signet`, `Talisman of Creativity`). To achieve net-positive mana with `Isochron Scepter + Dramatic Reversal` without drawing `Sol Ring`, the pilot was required to find 3 of the remaining 4 rocks—a statistical anomaly in a 99-card deck without artifact tutors. Scepter operated as an inconsistent high-roll.
* **The "Pseudo-Ramp" Audit (`Urza's Incubator`):** Incubator cost `{3}` and provided zero mana under `Dramatic Reversal` untaps. Furthermore, over half the deck’s core Wizards (`Coruscation Mage`, `Naban`, `Harmonic Prodigy`, `Tomik`, `Snapcaster`, `Timestream Navigator`, `Dualcaster`, `Vivi`) possess only `{1}` generic pip in their cost, while `Patron Wizard` has `{0}`. Incubator wasted 50% of its discount across the deck while missing noncreature spells entirely.
* **Trimming Low-Velocity Dead Ends:**
  * **Dark Confidant ("Bob"):** Inalla’s Eminence token copies exile at end of turn, meaning paid copies never saw an upkeep trigger. Bob was a slow, non-spell body with zero burst velocity on storm turns that punished life totals against high-CMC payoffs.
  * **Obsessive Search:** A low-floor `{U}` draw-1 cantrip with narrow discard utility.
* **The Resolution:** Added **`Talisman of Dominance`**, **`Dimir Signet`**, and **`Talisman of Indulgence`** while cutting Bob, Obsessive Search, and Urza's Incubator. Rock density expanded to **8**, ensuring consistent Turn 2 ramp into Turn 3 engines and making IsoRev net-positive mana trivial to achieve.

### Through-Line 2: Resolving the "Orphaned Dualcaster" Dilemma (The Twinflame Loop)
* **The Diagnostic Bottleneck:** `Dualcaster Mage` sat in the list without its companion loop piece (`Twinflame`), functioning as an opportunistic reactive spell copier.
* **Trimming Dead-Weight Interaction (`Kasmina's Transmutation`):** A 2-mana sorcery-speed aura that left opposing bodies on board, failed to cantrip, and lacked synergy with storm or flashback lines.
* **The Resolution:** Swapped Transmutation for **`Twinflame`**. This activated a compact 5-mana (`{2}{R}{R}{R}`) instant/sorcery combat combo producing infinite hasty 2/2 attackers. Outside the combo, Twinflame functions as a cheap 2-CMC spell triggering pingers and *Magecraft*, reduced to `{R}` by Level 2 `Artist's Talent`, and recurrable via Escape.

### Through-Line 3: Bracket 4 Formalization & The Game Changer Threshold
* **The Diagnostic Bottleneck:** With two compact 2-card deterministic infinites, 7 tutors, and a 9.0 composite power score, the deck tripped CFP / EDH Oracle Bracket 4 gates by default. Artificially abiding by Bracket 3’s $\le 3$ Game Changer cap meant the deck bore the archenemy perception of a B4 combo shell without its top-tier tools.
* **Deliberate Rejection of `Jeska's Will`:** Because Inalla stays safe in the command zone for Eminence, Jeska's Will virtually never unlocks its "choose both" blowout mode. Tapping 3 mana for only mana or only cards in a predominantly U/B shell represented poor efficiency.
* **The Resolution:**
  * **`Cyclone Summoner` $\rightarrow$ `Cyclonic Rift`:** Replaced a 7-mana sorcery creature whose ETB bounce failed on Inalla token copies (*"if you cast it from your hand"*) with an instant-speed, one-sided reset that wipes all opposing nonland permanents (including *Rule of Law* stax).
  * **`Past in Flames` $\rightarrow$ `Underworld Breach`:** Cut recursion cost from 4 to 2 mana and expanded flashback from instants/sorceries to universal Escape across all nonland cards (recovering countered rocks, Scepter, and Dualcaster).

### Through-Line 4: Deep Integration of Underworld Breach + Brain Freeze
* **The Engine Loop:** `Underworld Breach` ({1}{R}) + `Brain Freeze` ({1}{U}) creates an exponential self-mill engine. Target yourself with every storm copy to mill $3 \times (S + 1)$ cards into the graveyard while paying only 3 cards to escape.
* **Net Fuel Scaling:** With each iteration, the graveyard grows by $+3, +6, +9\dots$ cards, effectively "drawing" the entire deck into the graveyard.
* **Mana Sustenance:** Escaping `Dramatic Reversal` ({1}{U} + exile 3 cards) untaps the 8 mana rocks to net surplus colored mana, cycling between Freeze and Reversal.
* **Decisive Table Finish:** Once the storm count reaches 40+, Brain Freeze targets all three opponents to mill their entire libraries, or Breach escapes `Dualcaster Mage + Twinflame` from the yard.

---

### Quantitative Metric Delta

| Evaluation Metric | Archived Baseline | Calibrated State (Oct 2026) | Strategic Delta |
| :--- | :---: | :---: | :--- |
| **Archidekt / CFP Bracket** | Bracket 3 | **Bracket 4** | Formally calibrated for high-power combo play. |
| **Average CMC** | 2.53 | **2.42** | Curve floor lowered by -0.11; faster Turn 3 initiation. |
| **Dedicated Mana Rocks** | 5 | **8** | +60% increase; eliminates IsoRev mana deficit. |
| **Cataloged Infinite Combos** | 1 | **2 (+1 Emergent)** | Dual deterministic loops + Breach/Freeze self-mill. |
| **Official Game Changers** | 3 | **5** | Added `Cyclonic Rift` & `Underworld Breach`. |
| **Tutor Density** | 7 | **7** | Retains high-redundancy assembly suite. |
| **Closing Efficiency** | 100.0% | **100.0%** | Quad-vector lethal conversion matrix. |
| **Interaction Pillar** | 80.0% | **80.0%** | Upgraded with instant-speed asymmetric reset. |

---

---

## Mechanical Architecture

### 1. The Ping & Combustion Engine
The deck's primary damage-dealing chassis triggers whenever a noncreature spell is cast, dealing noncombat damage directly to all opponents:

* **Direct Creature Pingers:**
  * **Coruscation Mage** (`{1}{R}`): Deals 1 damage to each opponent on noncreature cast. Includes Offspring to create an additional token pinger.
  * **Black Waltz No. 3** (`{2}{U}{R}`): Deals 1 damage to each opponent on noncreature cast; also flies and offers targeted removal upon dealing damage.
  * **Vivi Ornitier** (`{1}{U}{R}`): Deals 1 damage to each opponent on noncreature cast while functioning as a repeatable mana ritual for future casts.
* **Token Ping Generators:**
  * **Mysidian Elder**, **Transpose**, **Circle of Power**, **Cornered by Black Mages**, and **Kuja, Genome Sorcerer** produce disposable 0/1 black Wizard tokens with: *"Whenever you cast a noncreature spell, this token deals 1 damage to each opponent."*
  * These tokens hit each opponent simultaneously, accumulate passively, trigger Eminence as Wizards, and double as sacrifice fuel for **Diabolic Intent**.

---

### 2. The Damage Amplification Matrix
Four distinct amplifiers scale the ping triggers. Because they operate across different mechanical layers (additive replacements, multiplicative replacements, and trigger duplication), they stack compoundingly rather than linearly:

1. **Harmonic Prodigy** (`{1}{R}`, Shaman/Wizard Trigger Duplicator):
   * *"If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time."*
   * Duplicates every ping trigger from ping tokens, Coruscation Mage, Black Waltz No. 3, and Vivi Ornitier, effectively doubling the number of damage events. Also duplicates Inalla's Eminence and Naban triggers.
2. **Trance Kuja, Fate Defied** (Transform Face of Kuja, Genome Sorcerer — Damage Multiplier):
   * *Flare Star:* *"If a Wizard you control would deal damage to a permanent or player, it deals double that damage instead."*
   * Multiplies the actual damage value of every Wizard damage event by 2.
3. **Tomik, Izzet Sparkmage** (`{1}{R}`, Additive Damage Replacement & Prowess):
   * *"If a source you control would deal noncombat damage to an opponent or a permanent an opponent controls, it deals that much damage plus 1 instead."*
   * A 2-drop Wizard that triggers Inalla's Eminence, triggers Naban, counts toward Kuja's 4-Wizard transform condition, and adds +1 flat damage to every ping source.
4. **Artist's Talent** (Class Enchantment — Additive Damage Replacement & Cost Reducer):
   * *Level 2:* Reduces all noncreature spells by `{1}`.
   * *Level 3:* *"If a source you control would deal noncombat damage to an opponent or a permanent an opponent controls, it deals that much damage plus 2 instead."*
5. **Gogo, Master of Mimicry** (`{2}{U}`, Arbitrary Ability Multiplier):
   * *"{X}{X}, {T}: Copy target activated or triggered ability you control X times."*
   * Can copy any trigger—including a damage ping, Eminence, or tutor trigger—as many times as available mana allows, bypassing the need for multiple spell casts.

#### Replacement Effect Stacking (CR 616.1)
Under Comprehensive Rule 616.1, the affected player or controller of the affected permanent chooses the order in which multiple replacement effects apply to a damage event. In an offensive burn sequence, additive modifiers are ordered before multiplicative modifiers:

$$\text{Per-Trigger Damage} = \Big(\text{Base } (1) + \text{Tomik } (+1) + \text{Artist's Talent } (+2)\Big) \times \text{Kuja's Flare Star } (2) = 8 \text{ damage}$$

When **Harmonic Prodigy** is present, that 8-damage event triggers twice:

$$8 \times 2 = \mathbf{16\text{ damage to each opponent per noncreature spell cast}}$$

---

### 3. The Deterministic Machine Engines

#### A. The Isochron Loop (IsoRev)
* **Engine:** **Isochron Scepter** + **Dramatic Reversal**.
* **Condition:** Nonland permanents capable of generating at least `{3}` mana. The deck runs **8 dedicated mana rocks** (`Sol Ring`, `Arcane Signet`, `Dimir Signet`, `Fellwar Stone`, `Izzet Signet`, `Talisman of Creativity`, `Talisman of Dominance`, `Talisman of Indulgence`).
* **Loop Mechanics:**
  1. Tap nonland mana sources for 3+ mana.
  2. Pay `{2}` and tap Isochron Scepter to copy and cast Dramatic Reversal.
  3. Dramatic Reversal resolves, untapping Isochron Scepter and all mana sources.
  4. Yields infinite mana, infinite untap steps, and infinite noncreature spell casts / storm count.
* **Outlets to Victory:**
  * **Any Pinger on Board:** Each Scepter activation casts a spell, dealing infinite damage to the table.
  * **Brain Freeze:** Mill every opponent's library out immediately.
  * **Archmage Emeritus:** Magecraft draws the entire library, finding free counter protection (`Pact of Negation`, `An Offer You Can't Refuse`) and closing spells.

#### B. The Dualcaster Infinite Swarm
* **Engine:** **Dualcaster Mage** + **Twinflame**.
* **Condition:** Any creature on your board to initiate Twinflame targeting, plus `{2}{R}{R}{R}` (5 total mana, reducible by `Artist's Talent`).
* **Loop Mechanics:**
  1. Cast Twinflame targeting any creature you control.
  2. Holding priority, cast Dualcaster Mage with flash.
  3. Dualcaster ETB triggers, copying Twinflame on the stack.
  4. Change target of the copy to Dualcaster Mage.
  5. Copy resolves, creating a token copy of Dualcaster Mage with haste.
  6. Token enters, triggering another ETB targeting the original Twinflame.
  7. Repeat infinitely to create arbitrary numbers of 2/2 hasty Dualcaster Mages for an immediate combat win.

#### C. The Breach-Freeze Engine
* **Engine:** **Underworld Breach** + **Brain Freeze** + mana rock/ritual.
* **Mechanics:**
  1. Cast Underworld Breach ({1}{R}).
  2. Cast Brain Freeze targeting yourself to fill your graveyard (3 cards per storm count).
  3. Escape Brain Freeze by exiling nonessential cards from the yard.
  4. Loop to generate arbitrary storm count, escape all necessary tutors and rituals, and mill out all opponents.

---

### 4. Card Advantage, Velocity, & Graveyard Fuel
To ensure storm chains never fizzle and setup phases stay well-resourced:

* **Velocity Engines:**
  * **Archmage Emeritus** (`{3}{U}`): *Magecraft* draws a card on every cast or copy of an instant or sorcery. Turns any sequence of cheap cantrips into a full hand refill.
  * **Rhystic Study**: Dominant tax and continuous draw engine that punishes opponent development.
  * **Azami, Lady of Scrolls**: Tap untapped Wizards to dig heavily at instant speed.
* **ETB Loot & Filtering:**
  * **Emet-Selch, Unsundered** & **Kefka, Court Mage**: Enter the battlefield to loot and disrupt opponent hands. Amplified by **Naban, Dean of Iteration** or Inalla's Eminence to dig deep into the library.
* **Graveyard Recursion & Escape:**
  * **Underworld Breach**: Replaces one-shot flashback with universal Escape for all nonland cards, enabling re-casting of countered combo pieces (`Isochron Scepter`, rocks) or recursive spell chains.
  * **Mizzix's Mastery**: Overloaded one-sided graveyard cast to close games without needing mana for individual spells.
  * **Hades, Sorcerer of Eld** (Transformed Emet-Selch): Allows playing any card from the graveyard during your turn once the 14-card threshold is met.
  * **Snapcaster Mage**: Targeted flashback on a Wizard body.

---

### 5. Wizard Cloning, Eminence, & Legend Rule Bypass
Inalla's Eminence triggers whenever a nontoken Wizard enters, offering a temporary hasty token copy for `{1}`. The deck leverages this across several axes:

* **Naban, Dean of Iteration & Harmonic Prodigy:**
  * Naban doubles triggers caused by Wizards entering the battlefield (including Eminence itself and ETB abilities).
  * Harmonic Prodigy duplicates triggered abilities of Shamans and Wizards, chaining with Naban and Inalla to produce up to 4 extra token copies for `{4}`.
* **Permanent Retention via Obeka, Brute Chronologist:**
  * Token copies made by Eminence carry a delayed trigger: *"Exile it at the beginning of the next end step."*
  * At the beginning of the end step, allow beneficial end-step triggers (such as Kuja's transform check) to resolve, then activate Obeka to end the turn. Ending the turn exiles all remaining triggers on the stack, permanently keeping the token copies on the battlefield.
* **Bypassing the Legend Rule:**
  * **Mirror Box**: Static removal of the legend rule for all controlled permanents. Enables multiple copies of legendary amplifiers (e.g., stacking multiple Trance Kujas for $2 \times 2 \times 2$ exponential damage, multiple Nabans, or multiple Tomiks).
  * **Hall of Echoes**: A land that taps for `{C}` and features: *"{5}: This land becomes a copy of target creature you control until end of turn. The 'legend rule' doesn't apply to permanents you control this turn."* Serves as an uncounterable, land-slot backup to Mirror Box.
  * **Irenicus's Vile Duplication**: Creates a non-legendary flying token copy of any creature while acting as a noncreature spell that triggers all pingers.
  * **Mockingbird**: A scalable nontoken clone that enters as a copy of any Wizard, directly triggering Inalla's Eminence.

---

### 6. Tutoring & Interaction Suite

* **Wizard Tutors (Instant Speed & Uncounterable):**
  * **Step Through** (*Wizardcycling* `{2}`) and **Vedalken Aethermage** (*Wizardcycling* `{3}`) search directly for any Wizard in the library to hand, bypassing creature counters.
* **Direct Tutors:**
  * **Demonic Tutor**, **Diabolic Intent** (sacrificing a 0/1 ping token), and **Gamble**.
* **Protection & Disruption:**
  * **Cyclonic Rift**: Premium instant-speed board bounce to eliminate stax, hatebears, and blockers right before your turn.
  * **Pact of Negation**, **Counterspell**, **An Offer You Can't Refuse**, **Negate**, and **Long River's Pull** protect win turns.
  * **March of Swirling Mist** phases out disruptive stax pieces or opposing boards.
  * **Return the Favor** & **Wyll's Reversal** redirect opposing removal or copy pivotal spells.
  * **Propaganda** protects life totals against go-wide aggression while sculpting hand state.

---

## Kill Math & Threshold Table

The following table demonstrates the number of noncreature spells required to deal a full 40 damage to every opponent simultaneously from a single ping source, depending on active amplifiers:

| Active Amplifiers | Damage per Spell | Spells Needed (Full 40 Life) |
| :--- | :---: | :---: |
| **None** (Base Ping) | 1 | 40 |
| **Tomik** only | 2 | 20 |
| **Harmonic Prodigy** only | 2 | 20 |
| **Trance Kuja** (Flare Star) only | 2 | 20 |
| **Artist's Talent** (Level 3) only | 3 | 14 |
| **Tomik + Harmonic Prodigy** | 4 | 10 |
| **Tomik + Trance Kuja** | 4 | 10 |
| **Harmonic Prodigy + Trance Kuja** | 4 | 10 |
| **Artist's Talent + Harmonic Prodigy** | 6 | 7 |
| **Artist's Talent + Trance Kuja** | 6 | 7 |
| **Tomik + Artist's Talent + Trance Kuja** | 8 | 5 |
| **Tomik + Artist's Talent + Harmonic Prodigy** | 8 | 5 |
| **Artist's Talent + Trance Kuja + Harmonic Prodigy** | 12 | 4 |
| **All Four (Tomik + Artist's + Kuja + Harmonic)** | **16** | **3** |

*Note: In typical pods, opponents take incidental combat damage from each other throughout the game, drastically reducing the actual spell count required below the 40-life worst-case baseline.*

---

## Inherent Weaknesses & Strategic Vulnerabilities

### 1. Premature Deployment & Fragile Board States
* The deck's primary pingers and multipliers are fragile 1/2, 2/2, and 0/1 creature bodies. Deploying them incrementally without the mana or protection to execute a storm sequence invites cheap spot removal and incidental board wipes, stranding the deck without win conditions.

### 2. Rule of Law & Cast-Restriction Stax
* As a storm-velocity combo deck, static cast restrictors (**Rule of Law**, **Archon of Emeria**, **Eidolon of Rhetoric**, **Deafening Silence**) completely paralyze the deck's primary game plans, shutting down both the Dramatic Reversal loop and multi-spell ping sequences until removed via **Cyclonic Rift**, **March of Swirling Mist**, or **Fatal Push**.

### 3. Forced Sacrifice & Edict Effects
* The combo and ping engines require keeping specific creatures on the battlefield to duplicate triggers. Forced sacrifice effects (**Plaguecrafter**, **Grave Pact**, **Sheoldred's Edict**) force the sacrifice of valuable combo pieces or drain fuel before ping engines can ignite.

### 4. Graveyard Hate
* While the Scepter and Twinflame lines operate from hand and board, backup burst lines rely heavily on Escape and reanimation (**Underworld Breach**, **Mizzix's Mastery**, **Hades, Sorcerer of Eld**). Asymmetric graveyard exile (**Rest in Peace**, **Dauthi Voidwalker**) strips the deck's secondary velocity reserves.

### 5. Table Threat Perception & Archenemy Dynamics
* Because Grixis storm and Inalla represent well-known explosive combo potential, experienced opponents may apply early combat pressure before defensive measures (**Propaganda**) or countershields (**Pact of Negation**, **Counterspell**) are fully assembled.

---

## Piloting Protocol & Strategy

To pilot the deck with maximum consistency and table confidence, follow this three-phase mental model:

### Phase 1: Concealed Setup (Turns 1 – 4)
* **Objective:** Establish mana acceleration and card velocity without telegraphing a storm turn.
* **Execution:**
  * Deploy rocks (`Sol Ring`, Signets, Talismans).
  * Establish steady draw and filtering (`Rhystic Study`, `Kefka`, `Emet-Selch`, `Archmage Emeritus`). Use Naban or Eminence to double ETB filtering triggers.
  * **Threat Discipline:** Do not play naked pingers or damage amplifiers early to deal 1–2 chip damage. Dealing minor chip damage alerts the table that you are playing storm and makes your 1/2 and 2/2 Wizards priority removal targets. Keep win pieces protected in hand.

### Phase 2: Assembly & Assessment (Turns 5 – 6)
* **Objective:** Evaluate the table's shields and identify which win line is open.
* **Route Selection:**
  * **Route A (The Scepter Machine):** If you possess `Isochron Scepter`, `Dramatic Reversal`, and 3+ nonland mana, assemble the loop with 1-mana protection held in reserve (`Pact of Negation`, `An Offer You Can't Refuse`).
  * **Route B (The Twinflame Swarm):** If Scepter is blocked or unavailable, cast `Twinflame` and flash in `Dualcaster Mage` for an immediate infinite combat win.
  * **Route C (The Breach-Freeze Mill):** If you have `Underworld Breach` and `Brain Freeze`, loop casts from the graveyard to mill out the entire table.
  * **Route D (The Combustion Burst):** If combos are disrupted, assemble 2+ amplifiers from the matrix and chain 5–7 low-cost spells with `Mizzix's Mastery` or active pingers.

### Phase 3: The Decisive Detonation
* **Objective:** Win the game cleanly in a single turn.
* **Execution:**
  * Cast your multiplier or combo engine.
  * If targeted by interaction, evaluate whether the loop or instant-speed spells can be initiated on top of the removal spell.
  * Execute your sequence, track your mana and trigger multipliers, and close the game across all opponents in one unified step.
