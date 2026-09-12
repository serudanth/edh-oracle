---
type: decklist
title: "The Necrobloom — Budget-Lethal Abzan Engine Blueprint"
commander: "The Necrobloom"
colors: [W, B, G]
power_level: 3.5
bracket: "Bracket 3 (Optimized Engine / Mid-to-High)"
target_upgrade_spend: "~$13.90"
tags: [#theorycrafting, #landfall, #dredge, #aristocrats, #gitrog, #budget-upgrade]
related: [README.md, 01-salvage-pool.md]
last_updated: 2026-09-11
---

# The Necrobloom — Budget-Lethal Abzan Engine Blueprint

A high-synergy, tournament-tested engine shell built around **The Necrobloom** that maximizes your existing collection and dismantled donor cards (*The Dirt Kicker*, *The Master Chef*, *Burgeoning*, *Sylvan Library*, *Skullclamp*, *The Gitrog Monster*, *Dakmor Salvage*, *Altar of Dementia*, *Morbid Opportunist*) while keeping the remaining card acquisition strictly budget-friendly (~$13.90 total upgrade spend).

---

## 1. Deck Architecture & Strategy

```
                          ┌─────────────────────────────┐
                          │     The Necrobloom Engine    │
                          │  (Land Dredge 2 + Landfall)  │
                          └──────────────┬──────────────┘
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
  [EARLY VELOCITY]               [MIDGAME ENGINE]                  [LETHAL FINISH]
- Burgeoning (T1/T2 drops)     - Skullclamp 0/1 Plant loops      - Altar + Beifong infinite loop
- Azusa + Selesnya bounce      - Gitrog + Discard outlets        - Corpse Knight / Mirkwood Bats drain
- Sylvan Library free dredge   - Planar Engineering (+4 basics)  - Summon: Titan (Ch. II mass lands)
- Land Dredge draw filtering   - Evolution Sage proliferate      - Zombie swarm beatdown
```

### The Four Winning Pillars:
1. **The Plant & Skullclamp Draw Engine:**
   * Before hitting 7 unique lands, Necrobloom produces 0/1 Plants.
   * Attach `Skullclamp` for $\{1\} \rightarrow$ Plant dies $\rightarrow$ draw 2 cards (or Dredge 4 cards, returning 2 lands).
   * Play a dredged land $\rightarrow$ make another Plant $\rightarrow$ repeat.
2. **The Gitrog / Discard Acceleration Loop:**
   * Pitch lands to free discard outlets (`Putrid Imp`, `Zombie Infestation`) $\rightarrow$ triggers `The Gitrog Monster` to draw $\rightarrow$ replace with Dredge 2.
   * Self-fuels mana and board presence without requiring high-dollar tutors.
3. **The Beifong + Altar of Dementia Infinite Loop:**
   * `Altar of Dementia` + `Beifong's Bounty Hunters` + `The Necrobloom`:
     * Sac a 2/2 Zombie to Altar (mills 2) $\rightarrow$ Beifong earthbends a land into a 2/2 creature.
     * Sac the 2/2 land creature to Altar (mills 2) $\rightarrow$ earthbend returns it tapped.
     * Land entering tapped triggers Necrobloom $\rightarrow$ creates a fresh 2/2 Zombie token.
     * Repeat infinitely to mill out the entire table, or drain the table with `Mirkwood Bats` / `Corpse Knight` / `Elas il-Kor` / `Syr Konrad` / `Bastion of Remembrance`.
4. **Mass Resurgence Landfall Burst:**
   * With 10–15 lands in the graveyard from Dredge and `Planar Engineering`, drop `Summon: Titan` (Chapter II) or `Splendid Reclamation`.
   * Triggers 10–15 simultaneous landfall triggers $\rightarrow$ instantly generates an army of 2/2 Zombies, proliferates with `Evolution Sage`, or drains the entire table.

---

## 2. Complete 100-Card Decklist

### Commander (1)
* 1x **The Necrobloom**

---

### Creatures (25)

#### Land Accelerators & Recursers
* 1x **The Gitrog Monster** *(OWNED — Collection)*
* 1x **Azusa, Lost but Seeking** *(OWNED — The Dirt Kicker)*
* 1x **Sakura-Tribe Elder** *(OWNED — The Master Chef)*
* 1x **Erinis, Gloom Stalker** *(OWNED — The Dirt Kicker)*
* 1x **Birds of Paradise** *(OWNED — The Dirt Kicker)*
* 1x **Stitcher's Supplier** *(OWNED — Collection)* — Premier 1-mana graveyard primer; mills 3 on ETB and 3 on death (6 total).
* 1x **Wight of the Reliquary** *(OWNED — Collection)* — Sacrifices 0/1 Plants to tutor any land straight to battlefield untapped.
* 1x **Aftermath Analyst** *(BUDGET UPGRADE — ~$0.50)* — Creature-based mass land reanimation.
* 1x **Tireless Provisioner** *(BUDGET UPGRADE — ~$1.50)* — Treasures / Food on every landfall.

#### Aristocrats & Table Drain
* 1x **Priest of Forgotten Gods** *(OWNED — Collection)* — Powerhouse sac engine: eats 2 tokens (triggering Bats twice) to force edicts, drain 2 life, add $\{B\}\{B\}$, and draw/dredge a card!
* 1x **Corpse Knight** *(BUDGET UPGRADE — ~$0.25)* — Drains each opponent for 1 whenever Plants/Zombies enter.
* 1x **Mirkwood Bats** *(OWNED — Collection)* — Drains on token creation and sacrifice.
* 1x **Elas il-Kor, Sadistic Pilgrim** *(BUDGET UPGRADE — ~$0.35)* — Life gain on enter, drain on death.
* 1x **Syr Konrad, the Grim** *(OWNED — Collection)* — Drains 1 to all opponents on creature mill, death, or leaving the graveyard.
* 1x **Vito, Thorn of the Dusk Rose** *(OWNED — Collection)* — Converts lifegain into targeted burn; 5-mana activated ability grants entire team lifelink.

#### Discard Enablers & Graveyard Engines
* 1x **Putrid Imp** *(BUDGET UPGRADE — ~$0.40)* — $\{0\}$ mana instant-speed discard outlet to fuel Gitrog / Dredge chains.
* 1x **Evolution Witness** *(OWNED — The Master Chef)* — Recurs key permanents from graveyard.
* 1x **Evolution Sage** *(OWNED — The Master Chef)* — Proliferates on every land drop (supercharges Sagas & counters).

#### Utility, Interaction & Finishers
* 1x **Summon: Titan** *(OWNED — The Dirt Kicker)* — Saga Giant: Chapter I mills 5; Chapter II returns all lands tapped; Chapter III lethal $+X/+X$ trample pump.
* 1x **Skyclave Apparition** *(OWNED — The Master Chef)*
* 1x **Haywire Mite** *(OWNED — The Dirt Kicker)*
* 1x **Spore Frog** *(OWNED — The Dirt Kicker)* — Repeatable fog defense.
* 1x **Morbid Opportunist** *(OWNED — Collection)* — Premier draw engine: triggers once on *each* player's turn whenever any creature dies (draws/dredges up to 4 cards per turn cycle!).
* 1x **Traveling Chocobo** *(OWNED — The Dirt Kicker)* — Plays lands from top of library; **doubles all landfall triggers** from lands and Birds!
* 1x **Beifong's Bounty Hunters** *(OWNED — Collection)* — Whenever a nonland creature dies, earthbends a land for X (turns land into an X/X haste creature that returns tapped if it dies, re-triggering Landfall!).

---

### Artifacts (6)
* 1x **Skullclamp** *(OWNED — Collection)* — Kills 0/1 Plants to draw 2 (or Dredge 4).
* 1x **Chocobo Racetrack** *(OWNED — The Dirt Kicker)* — Landfall token engine: creates 2/2 Birds that scale with future land drops (doubled by Traveling Chocobo).
* 1x **Sol Ring** *(OWNED — The Dirt Kicker)*
* 1x **Arcane Signet** *(OWNED — The Dirt Kicker)*
* 1x **Altar of Dementia** *(OWNED — Collection)* — Instant-speed sac outlet and self-mill engine; forms a deterministic infinite mill/drain combo with *Beifong's Bounty Hunters* and *The Necrobloom*.
* 1x **Idol of Oblivion** *(BUDGET UPGRADE — ~$0.40)* — $\{T\}$: Draw a card whenever you create a token (triggers on virtually every land drop).

---

### Enchantments (6)
* 1x **Burgeoning** *(OWNED — Collection)* — Explodes on turns 1–3, loops bounce lands off-turn.
* 1x **Sylvan Library** *(OWNED — Collection)* — Replaces draws with free Dredge 2 (zero life paid, zero cards returned).
* 1x **Abundance** *(OWNED — The Dirt Kicker)* — Guarantees land/nonland selection; prevents decking out.
* 1x **Insidious Roots** *(BUDGET UPGRADE — ~$1.50)* — Whenever a card leaves your graveyard, creates Plants and gives them mana-tapping counters.
* 1x **Zombie Infestation** *(BUDGET UPGRADE — ~$0.35)* — Free discard outlet: discard 2 lands $\rightarrow$ make a 2/2 Zombie $\rightarrow$ triggers Gitrog draws.
* 1x **Bastion of Remembrance** *(OWNED — Collection)* — Board-wipe insurance and aristocrat drain (drains each opponent for 1 and gains 1 life on any creature death).

---

### Sorceries (13)
* 1x **Reanimate** *(OWNED — Collection)* — Premier 1-mana reanimation: targets your milled bombs (The Gitrog Monster, Summon: Titan, Syr Konrad) or any opponent's graveyard threat.
* 1x **Planar Engineering** *(OWNED — Collection)* — Sac 2 lands (Dredge 2 / Gitrog triggers), fetch 4 basic lands tapped (4 landfall triggers!).
* 1x **Traverse the Outlands** *(OWNED — The Dirt Kicker)* — Fetches up to 6 basics with Gitrog out.
* 1x **Rishkar's Expertise** *(OWNED — The Dirt Kicker)* — Draws 6–7 cards and casts a free spell.
* 1x **Splendid Reclamation** *(BUDGET UPGRADE — ~$2.00)* — Redundancy for *Summon: Titan* to return all lands from GY tapped.
* 1x **Nature's Lore** *(OWNED — The Master Chef)*
* 1x **Cultivate** *(OWNED — The Master Chef)*
* 1x **Rampant Growth** *(OWNED — The Dirt Kicker)*
* 1x **Shamanic Revelation** *(BUDGET UPGRADE — ~$0.40)* — Burst draw: draws a card for each creature you control and gains life.
* 1x **Farewell** *(OWNED — The Master Chef)* — Emergency reset.
* 1x **Austere Command** *(OWNED — The Master Chef)* — Modular wipe that preserves your tokens or utility pieces.
* 1x **Victimize** *(BUDGET UPGRADE — ~$0.30)* — Sac a 0/1 Plant $\rightarrow$ reanimate 2 creatures from graveyard.
* 1x **Dread Return** *(BUDGET UPGRADE — ~$0.25)* — Flashback cost is free by sacrificing 3 Plant/Zombie tokens.

---

### Instants (11)
* 1x **Harrow** *(OWNED — The Dirt Kicker)* — Sacs a land (Dredge 2 / Gitrog draw) for 2 untapped lands.
* 1x **Elemental Teachings** *(OWNED — The Dirt Kicker)* — Instant *Realms Uncharted*: searches 4 named lands; opponent bins 2 (gain Dredge 2 & Gitrog draws!) and puts 2 onto battlefield tapped (2 landfall triggers!).
* 1x **Stroke of Midnight** *(OWNED — The Master Chef)* — Versatile nonland removal.
* 1x **Reprieve** *(OWNED — The Master Chef)* — White tempo pseudo-counter that draws a card.
* 1x **Your Temple Is Under Attack** *(OWNED — The Master Chef)* — Modal indestructible protection or draw 2.
* 1x **Gaea's Gift** *(OWNED — The Dirt Kicker)* — Hexproof, indestructible protection.
* 1x **Plumb the Forbidden** *(BUDGET UPGRADE — ~$0.50)* — Instant-speed sac outlet & burst draw: sacrifice any number of tokens to draw cards and dodge board wipes.
* 1x **Swords to Plowshares** *(OWNED — Collection)* — Premier 1-mana creature exile.
* 1x **Beast Within** *(BUDGET UPGRADE — ~$0.50)* — Hits any permanent.
* 1x **Crop Rotation** *(BUDGET UPGRADE — ~$1.50)* — Sacs a land to tutor *any* utility land (e.g. Bojuka Bog, Dakmor, Demolition Field) at instant speed.
* 1x **Golgari Charm** *(OWNED — Collection)* — Modal: regenerates all your creatures against wraths, kills opposing mana dorks, or destroys an enchantment.

---

### Lands (38) — Diversified Engine with 13 Basics

#### Basics (13) — 100% Owned, Fuels All Ramp & Untaps Snarls
* 7x **Forest** *(OWNED)*
* 3x **Plains** *(OWNED)*
* 3x **Swamp** *(OWNED)*

#### Engine & Dredge Lands (6)
* 1x **Dakmor Salvage** *(OWNED — Collection)* — Native Dredge 2.
* 1x **Ash Barrens** *(OWNED — The Master Chef)* — Cycling $\{1\}$ dredge loop.
* 1x **Scattered Groves** *(OWNED — The Master Chef)* — Cycling $\{2\}$ typed dual.
* 1x **Barren Moor** *(BUDGET UPGRADE — ~$0.25)* — Black cycling land.
* 1x **Tranquil Thicket** *(BUDGET UPGRADE — ~$0.25)* — Green cycling land.
* 1x **Secluded Steppe** *(BUDGET UPGRADE — ~$0.25)* — White cycling land.

#### Bounce Lands (3) — Burgeoning & Landfall Loopers
* 1x **Selesnya Sanctuary** *(OWNED — The Master Chef)*
* 1x **Golgari Rot Farm** *(BUDGET UPGRADE — ~$0.30)*
* 1x **Orzhov Basilica** *(BUDGET UPGRADE — ~$0.30)*

#### Land Destruction & Utility (3)
* 1x **Demolition Field** *(OWNED — The Dirt Kicker)* — Recurrable land destruction + basic tutor.
* 1x **Ghost Quarter** *(BUDGET UPGRADE — ~$0.75)* — Additional recurrable utility land kill.
* 1x **Bojuka Bog** *(OWNED — Collection)* — Graveyard hate on a land; can be crop-rotated or dredged.

#### Fetch / Shufflers (2)
* 1x **Evolving Wilds** *(OWNED — The Dirt Kicker)*
* 1x **Terramorphic Expanse** *(OWNED — The Dirt Kicker)*

#### Duals & Fast Fixers (11)
* 1x **Canopy Vista** *(OWNED — The Master Chef)*
* 1x **Brushland** *(OWNED — The Master Chef)*
* 1x **Sunpetal Grove** *(OWNED — The Master Chef)*
* 1x **Fortified Village** *(OWNED — The Master Chef)*
* 1x **Llanowar Wastes** *(OWNED — Collection)* — Golgari pain land.
* 1x **Caves of Koilos** *(BUDGET UPGRADE — ~$0.50)* — Orzhov pain land.
* 1x **Necroblossom Snarl** *(BUDGET UPGRADE — ~$0.30)*
* 1x **Shineshadow Snarl** *(BUDGET UPGRADE — ~$0.30)*
* 1x **Exotic Orchard** *(OWNED — Collection)*
* 1x **Command Tower** *(OWNED — The Master Chef)*
* 1x **Path of Ancestry** *(OWNED — The Master Chef)*

---

## 3. Budget Upgrade Cost Breakdown

| Category | Key Additions | Total Estimated Cost |
|---|---|:---:|
| **Creatures (5)** | Aftermath Analyst ($0.50), Tireless Provisioner ($1.50), Corpse Knight ($0.25), Elas il-Kor ($0.35), Putrid Imp ($0.40) | **~$3.00** |
| **Artifacts & Enchantments (3)** | Idol of Oblivion ($0.40), Insidious Roots ($1.50), Zombie Infestation ($0.35) | **~$2.25** |
| **Instants & Sorceries (7)** | Splendid Reclamation ($2.00), Victimize ($0.30), Dread Return ($0.25), Beast Within ($0.50), Crop Rotation ($1.50), Shamanic Revelation ($0.40), Plumb the Forbidden ($0.50) | **~$5.45** |
| **Lands (8)** | Ghost Quarter ($0.75), Golgari Rot Farm ($0.30), Orzhov Basilica ($0.30), Barren Moor/Tranquil/Secluded ($0.75), Caves of Koilos ($0.50), Snarls ($0.60) | **~$3.20** |
| **Total Upgrade Spend** | | **~$13.90** |

*(Note: Every expensive staple in the deck — Burgeoning, Sylvan Library, The Gitrog Monster, Azusa, Skullclamp, Altar of Dementia, Morbid Opportunist, Birds of Paradise, Farewell — is 100% covered by your owned cards!)*
