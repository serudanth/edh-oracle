# The Apex Rush (Winota, Joiner of Forces) — Theorycrafting & Architecture Archive

This directory serves as the centralized theorycrafting, architecture, and deckbuilding workspace for **Winota, Joiner of Forces**, titled **The Apex Rush**. 

This build synthesizes Charles's (`fowlplays`) physical card collection ([`manabox-collection.csv`](../../podlist/charles/inventory/manabox-collection.csv)) and active 13-deck archive to assemble the absolute highest-power, cEDH-adjacent Commander deck possible with 100% owned card parity ($0.00 acquisition spend).

---

## File Directory

| File | Type | Description | Status |
|---|---|---|:---:|
| **[01-salvage-pool.md](01-salvage-pool.md)** | Donor Inventory | Detailed audit of all 30 scavenged power cards from *The Gate of Babylon*, *The Lorehold Redux*, *The Copied Factory*, *The Master Chef*, *The Last Ride*, and ManaBox Bulk. | Ready |
| **[02-decklist.md](02-decklist.md)** | Complete Decklist | Complete 100-card decklist for *The Apex Rush* (Power Score 8.5 / 10.0, Archidekt Bracket 4). | Ready |
| **[archidekt-export.txt](archidekt-export.txt)** | Export | Formatted text file ready for direct 1-click import into Archidekt. | Ready |

---

## Core Strategy Overview

* **Commander:** **Winota, Joiner of Forces** ({2}{R}{W})
* **Identity:** Boros ({R}{W})
* **Archetype:** Stax-Aggro / Combo-Velocity
* **Target Power Score:** 8.5 / 10.0 (High-Power / cEDH-Fringe)
* **Creature Density:** 51 Total Creatures (27 Humans including Witch Enchanter MDFC, 24 Non-Humans)
* **Average Non-Land CMC:** 2.50

---

## Strategic Pillars

### 1. Velocity Non-Human Curve (Turns 1–2)
* Deploys 0-to-1 CMC evasive non-Humans (**Rograkh, Son of Rohgahh**, **Ornithopter**, **Gingerbrute**, **Phoenix Chick**, **Skrelv, Defector Mite**, **Momo, Friendly Flier**, **Momo, Playful Pet**, **Topplegeist**) or aggressive value engines (**Magda, Brazen Outlaw**, **Grenzo, Havoc Raiser**, **Remorseful Cleric**, **Selfless Spirit**).
* Follows up with recurring token generators (**Goblin Rabblemaster**, **Legion Warboss**, **Loyal Apprentice**, **Oltec Matterweaver**, **Sami, Ship's Engineer**) to flood the board with permanent non-Human attackers.
* Accelerates with **Sol Ring**, **Simian Spirit Guide**, **Talisman of Conviction**, **Arcane Signet**, and **Fellwar Stone** to reliably drop Winota and swing on Turn 3.

### 2. Zero-Whiff Probability Engine (Hypergeometric Tuning)
* Dropped the entire clunky equipment package (**Conqueror's Flail**, **Lightning Greaves**, **Skullclamp**, **Umezawa's Jitte**, **Cloud, Midgar Mercenary**) and eliminated non-creature bloat (**Raise the Alarm**, **Secure the Wastes**, **Hordeling Outburst**, **Warleader's Call**, **Relentless Assault**).
* Mainboard Human count boosted from 19 to **27 Humans** (including Witch Enchanter MDFC).
* **Single-trigger whiff rate** plummeted from **27.34%** down to **12.90%** (87.1% hit rate).
* **Dual-trigger whiff rate** dropped from **7.48%** down to **1.66%** (98.34% chance to hit at least one Human).
* **Triple-trigger whiff rate** dropped to **0.21%** (99.79% guaranteed hit rate).

### 3. Asymmetric Stax Lockdown (Turns 2–3)
* Completely unhindered under Rule of Law effects (**Archon of Emeria**, **Eidolon of Rhetoric**, **Deafening Silence**, **High Noon**). Opponents are chained to one cast per turn while Winota cheats armies directly onto the battlefield without casting.
* Shuts off opposing commanders and exile casting with **Drannith Magistrate**, stops Underworld Breach and graveyard reanimation with **Sanctifier en-Vec**, locks out multi-draw engines with **Spirit of the Labyrinth**, restricts tutoring with **Aven Mindcensor**, taxes noncreature spells with **Thalia, Guardian of Thraben**, and counters free interaction with **Boromir, Warden of the Tower**.
* Taps opposing artifacts and wipes cheap mana rocks with **Dauntless Dismantler**; taxes spells and abilities during your turn with **Tithe Taker**; punishes combat crackbacks with **Michiko Konda, Truth Seeker**.

### 4. Board Resilience & Combat Immunity
* **Dolmen Gate:** Attacking creatures take zero combat damage, allowing fragile non-Humans to attack into lethal blockers every turn for guaranteed Winota triggers.
* **Reconnaissance:** Untaps attackers post-damage or pulls blocked non-Humans out of combat before damage.
* **Bastion Protector:** Gives Winota +2/+2 and permanent indestructible right out of the command zone.
* **Selfless Spirit & Boromir:** Instant-speed sacrifice to make the entire board indestructible.
* **Guardian of Faith & Clever Concealment:** Instant-speed phasing (Clever Concealment convokes for 0 mana) that completely shields the board from non-destruction blowouts (*Farewell*, *Cyclonic Rift*, *Toxic Deluge*).

### 5. Deterministic Infinite Win Lines & Overrun Finishers
* **Deterministic Combo:** **Kiki-Jiki, Mirror Breaker** + **Combat Celebrant** $\rightarrow$ Tap Kiki-Jiki to clone Celebrant, attack and exert the token to untap Kiki-Jiki and grant an additional combat phase. Repeat infinitely for unbounded hasty combat steps and damage.
* **Recursive Token Exponential Growth:** **Silverwing Squadron** (creates 3 permanent 2/2 non-Human Knight tokens per attack) and **Sami, Ship's Engineer** (creates a permanent 2/2 non-Human Robot token at each end step) ensure you never run out of non-Human attackers.
* **Lethal Non-Combo Damage:** Cheating out **Blade Historian** (Double Strike) alongside **Angrath's Marauders** (Double Damage), **Goldnight Commander** (+1/+1 per entering creature), or **Erkenbrand, Lord of Westfold** (+1/+0 per Human) routinely closes the game on Turn 3 or 4 with 40–80+ unblockable combat damage.
