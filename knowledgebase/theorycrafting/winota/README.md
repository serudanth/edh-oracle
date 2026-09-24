# The Apex Rush (Winota, Joiner of Forces) — Theorycrafting & Architecture Archive

This directory serves as the centralized theorycrafting, architecture, and deckbuilding workspace for **Winota, Joiner of Forces**, titled **The Apex Rush**. 

This build synthesizes Charles's (`fowlplays`) physical card collection ([`manabox-collection.csv`](../../podlist/charles/inventory/manabox-collection.csv)) and active 13-deck archive to assemble the absolute highest-power, cEDH-adjacent Commander deck possible with 100% owned card parity ($0.00 acquisition spend).

---

## File Directory

| File | Type | Description | Status |
|---|---|---|:---:|
| **[01-salvage-pool.md](01-salvage-pool.md)** | Donor Inventory | Detailed audit of all 15 scavenged power cards from *The Copied Factory*, *The Gate of Babylon*, *The Best of Friends*, *The Last Ride*, *The Master Chef*, and ManaBox Bulk. | Ready |
| **[02-decklist.md](02-decklist.md)** | Complete Decklist | Complete 100-card decklist for *The Apex Rush* (Power Score 8.5 / 10.0, Archidekt Bracket 4). | Ready |
| **[archidekt-export.txt](archidekt-export.txt)** | Export | Formatted text file ready for direct 1-click import into Archidekt. | Ready |

---

## Core Strategy Overview

* **Commander:** **Winota, Joiner of Forces** ({2}{R}{W})
* **Identity:** Boros ({R}{W})
* **Archetype:** Stax-Aggro / Combo-Velocity
* **Target Power Score:** 8.5 / 10.0 (High-Power / cEDH-Fringe)

### Strategic Pillars

1. **Velocity Non-Human Curve (Turns 1–2):**
   * Drops 0-to-1 CMC evasive non-Humans (**Rograkh, Son of Rohgahh**, **Ornithopter**, **Gingerbrute**, **Phoenix Chick**, **Skrelv, Defector Mite**, **Freya Crescent**) or token generators (**Goblin Rabblemaster**, **Legion Warboss**, **Loyal Apprentice**).
   * Accelerates with **Sol Ring**, **Simian Spirit Guide**, **Talisman of Conviction**, **Arcane Signet**, and **Fellwar Stone** to reliably cast Winota on Turn 3.

2. **Asymmetric Stax Lockdown (Turns 2–3):**
   * Operates completely unhindered under Rule of Law effects (**Archon of Emeria**, **Eidolon of Rhetoric**, **Deafening Silence**, **High Noon**). While opponents are restricted to casting one spell per turn, Winota's triggered ability cheats multiple creatures directly onto the battlefield without casting.
   * Locks out opposing commanders with **Drannith Magistrate**, denies multi-draw engines with **Spirit of the Labyrinth**, restricts search lines with **Aven Mindcensor**, taxes interaction with **Thalia, Guardian of Thraben**, and counters free interaction with **Boromir, Warden of the Tower**.

3. **Combat Immunity & Spell Shielding:**
   * **Dolmen Gate:** Attacking creatures take zero combat damage, allowing fragile non-Humans to attack into any lethal blocker every turn for guaranteed Winota triggers.
   * **Conqueror's Flail:** Shuts off opponent spellcasting during your turns entirely, functioning as an uncounterable equipment Grand Abolisher.
   * **Reconnaissance:** Untaps attackers post-damage or pulls blocked non-Humans out of combat before damage.

4. **Deterministic Infinite Win Lines:**
   * **Line A (Primary):** **Kiki-Jiki, Mirror Breaker** + **Combat Celebrant** $\rightarrow$ Tap Kiki-Jiki to clone Celebrant, attack and exert the token to untap Kiki-Jiki and grant an additional combat phase. Repeat infinitely for unbounded hasty combat steps and damage.
   * **Line B (Secondary):** **Rionya, Fire Dancer** + **Combat Celebrant** $\rightarrow$ At the beginning of each combat phase, Rionya creates a token copy of Celebrant, which exerts to create another combat phase.
   * **Lethal Non-Combo Damage:** Cheating out **Blade Historian** (Double Strike) alongside **Angrath's Marauders** (Double Damage) or **Goldnight Commander** deals 30–50+ combat damage across multiple players on Turn 3.
