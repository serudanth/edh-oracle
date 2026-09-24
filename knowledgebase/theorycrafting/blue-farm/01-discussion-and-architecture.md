# Blue Farm (Tymna & Kraum) — Architectural Blueprint

**Author:** Charles (`fowlplays`)  
**Commanders:** **Tymna the Weaver** & **Kraum, Ludevic's Opus**  
**Color Identity:** Sans-Green / WUBR ({W}{U}{B}{R})  
**Format Target:** High-Power / Bracket 4 (Scalable to cEDH)  
**Core Constraint:** Strictly proxy only copies of cards already physically owned across the collection.

---

## 1. Executive Summary & Design Thesis

"Blue Farm" (Tymna + Kraum) is renowned in Commander as the pinnacle of midrange card advantage and combo assembly. Traditional cEDH builds demand thousands of dollars in Reserved List duals, fast mana (*Mox Diamond*, *Chrome Mox*, *Lion's Eye Diamond*), and premium free countermagic (*Force of Will*, *Fierce Guardianship*).

This theorycraft demonstrates that by adhering to **Charles's personal rule (proxying only copies of cards already owned)**, Charles can build a lethal, highly resilient 100-card Blue Farm deck for **literally $0.00 out-of-pocket**, with an optional **~$14 micro-upgrade** that adds two redundant infinite combo lines.

### The Foundation in Hand
Charles physically possesses the Final Fantasy prints of:
1. **Tymna the Weaver** (Command Zone engine #1)
2. **Kraum, Ludevic's Opus** (Command Zone engine #2)
3. **Thassa's Oracle** (Primary Wincon)
4. **Tainted Pact** (Primary Combo Piece)

By mirroring high-power staples already sitting in active decks—specifically **The Copied Factory** (Inalla), **The Rush** (Winota), **The Queen of Theft** (Tasha), and **The Crystal Braves** (Alisaie & Alphinaud)—the build inherits top-tier card draw (*Rhystic Study*), premium tutors (*Demonic Tutor*), uncounterable combo protection (*Silence*, *Ranger-Captain of Eos*, *Boromir*), and free countermagic (*Pact of Negation*).

---

## 2. The Two Architectural Variants

### Variant 1: The $0.00 Zero-Cost Blueprint (100% Owned / Proxied)
* **Out-of-Pocket Cost:** **$0.00**
* **Primary Win Condition:** **Thassa's Oracle + Tainted Pact**
* **The "Secret Tech" Tutor:** **Step Through** *(The Copied Factory)*.
  * *Step Through* has **Wizardcycling {2}** at instant speed. Because it is an activated ability rather than a spell, it cannot be countered by standard countermagic (*Counterspell*, *Dovin's Veto*, *Negate*, *Swan Song*).
  * *Thassa's Oracle* is a **Creature — Merfolk Wizard**.
  * For 2 generic mana at end of turn, *Step Through* uncounterably fetches *Thassa's Oracle* directly into hand.
* **Secondary Win Lines & Pressure:**
  * *Peer into the Abyss* + *Dark Ritual* / *Simian Spirit Guide* into an overwhelming hand of answers and combo pieces.
  * Rapid combat damage pressure with *Kraum* (4/4 flying haste) and evasive 1-drops fueling *Tymna* draw triggers across 3 opponents.
* **Stax & Pacing:** Employs Winota's premier hatebears (*Drannith Magistrate*, *Aven Mindcensor*, *Boromir, Warden of the Tower*, *Deafening Silence*) to drag turbo decks into the midgame where Blue Farm reigns supreme.

### Variant 2: The Expanded Combo Build (~$14.00 Out-of-Pocket)
* **Out-of-Pocket Cost:** **~$13.95 – $21.45 USD**
* **Upgrades Purchased as Real Cards:**
  1. **Twinflame** (~$0.76): Combines with the owned **Dualcaster Mage** *(The Copied Factory)* for infinite hasty 2/2 attackers.
  2. **Underworld Breach** (~$11.16): Combines with the owned **Brain Freeze** *(Bulk)* and rituals to mill the entire library, building storm and casting Oracle from the graveyard.
  3. **Wishclaw Talisman** (~$2.03): 2-mana Demonic Tutor to assemble any missing combo piece on the winning turn.
  4. *(Optional)* **Demonic Consultation** (~$7.50): Provides a 2nd 1-mana partner to *Thassa's Oracle*.

---

## 3. The Tainted Pact Singleton Land Geometry

To guarantee **Tainted Pact** never encounters two cards with the same name, the 33-land mana base is engineered with **100% unique names**, using lands Charles already owns:

| Land Category | Count | Card Selections | Source |
|---|:---:|---|---|
| **Rainbow & Fast** | 5 | *City of Brass, Command Tower, Exotic Orchard, Spire of Industry, Starting Town* | The Copied Factory / Bulk |
| **Pain Lands (Untapped)** | 4 | *Underground River, Caves of Koilos, Shivan Reef, Battlefield Forge* | The Queen of Theft / The Warrior of Darkness / Bulk / The Rush |
| **Check Lands** | 4 | *Glacial Fortress, Drowned Catacomb, Clifftop Retreat, Dragonskull Summit* | The Crystal Braves / The Queen of Theft / The Rush / The Copied Factory |
| **Filter Lands** | 3 | *Sunken Ruins, Fetid Heath, Rugged Prairie* | The Queen of Theft / The Warrior of Darkness / The Rush |
| **Horizon & Slow Lands** | 4 | *Silent Clearing, Shattered Sanctum, Sundown Pass, Stormcarved Coast* | The Warrior of Darkness / The Lorehold Redux / Bulk |
| **Duals & Reveals** | 4 | *Spirebluff Canal, Prairie Stream, Smoldering Marsh, Choked Estuary* | The Copied Factory / The Crystal Braves / The Queen of Theft |
| **Fetches & Utility** | 5 | *Prismatic Vista, Fabled Passage, Emergence Zone, Mystic Sanctuary, Great Hall of the Citadel* | The Copied Factory / Bulk / The Queen of Theft / The Warrior of Darkness |
| **Basics (Strictly 1 each)** | 4 | 1x *Plains*, 1x *Island*, 1x *Swamp*, 1x *Mountain* | Basic Lands |
| **Total Lands** | **33** | **Zero duplicate names; 28 enter untapped.** | |

---

## 4. Collection Salvage & Proxy Map

This table shows exactly where each physical card is sourced from, allowing immediate assembly:

```
[Physical In-Hand (FF Prints)]
  ├── Tymna the Weaver (Commander)
  ├── Kraum, Ludevic's Opus (Commander)
  ├── Thassa's Oracle (Wincon)
  └── Tainted Pact (Combo Piece)

[Proxied from: The Copied Factory (Inalla - UBR)]
  ├── Rhystic Study (Card Advantage)
  ├── Demonic Tutor (Tutor)
  ├── Pact of Negation (Free Interaction)
  ├── Gamble (Tutor)
  ├── Step Through (Wizardcycling Tutor for Thoracle)
  ├── Dualcaster Mage (Creature / Combo)
  ├── Dark Confidant (Card Advantage)
  ├── Mockingbird (1-drop Flying Clone)
  ├── Snapcaster Mage (Flashback Utility)
  ├── Fatal Push (Removal)
  ├── City of Brass, Spirebluff Canal, Prismatic Vista, Fabled Passage (Lands)
  └── Talisman of Creativity (Ramp)

[Proxied from: The Rush (Winota - WR)]
  ├── Silence (Combo Protection)
  ├── Ranger-Captain of Eos (Tutor + Walking Silence)
  ├── Boromir, Warden of the Tower (Free-Spell Hate + Indestructible Protection)
  ├── Drannith Magistrate (Commander / Exile Stax)
  ├── Aven Mindcensor (Flash Search Hate)
  ├── Loyal Apprentice (Tymna Token Engine)
  ├── Professional Face-Breaker (Treasure & Card Advantage)
  ├── Simian Spirit Guide (Fast Mana)
  ├── Cathar Commando & Deafening Silence (Removal & Stax)
  ├── Battlefield Forge, Clifftop Retreat, Rugged Prairie (Lands)
  └── Fellwar Stone, Talisman of Conviction (Ramp)

[Proxied from: The Queen of Theft (Tasha - UB)]
  ├── Cyclonic Rift (Asymmetric Board Wipe)
  ├── Toxic Deluge (Sweeper)
  ├── Baleful Strix (Tymna Cantrip Flyer)
  ├── Underground River, Drowned Catacomb, Sunken Ruins, Mystic Sanctuary (Lands)
  └── Talisman of Dominance, Countersquall, Drown in the Loch (Ramp & Interaction)

[Proxied from: The Crystal Braves (Alisaie & Alphinaud - WU)]
  ├── Ledger Shredder (Connive Engine)
  ├── Dovin's Veto (Uncounterable Noncreature Counter)
  ├── Rapid Hybridization, Stroke of Midnight (Removal)
  ├── Glacial Fortress, Prairie Stream (Lands)
  └── Talisman of Progress (Ramp)

[Proxied from: The Warrior of Darkness (Ardbert - WB)]
  ├── Caves of Koilos, Silent Clearing, Shattered Sanctum, Fetid Heath (Lands)
  └── Talisman of Hierarchy (Ramp)

[Sourced from Unused Bulk / Binders]
  ├── Brain Freeze (Bulk - Combo Engine for V2)
  ├── Diabolic Intent (Bulk - 2 copies available)
  ├── Spectral Sailor (Bulk - 2 copies available)
  ├── Changeling Outcast (Bulk - 1 copy available)
  ├── Dark Ritual (Bulk)
  ├── Sol Ring & Arcane Signet (Bulk)
  ├── Dimir Signet, Izzet Signet, Boros Signet, Mind Stone, Thought Vessel (Bulk)
  ├── Counterspell, An Offer You Can't Refuse, Spell Pierce, Negate, Abrade (Bulk)
  ├── Brainstorm, Preordain, Opt, Sleight of Hand, Faithless Looting (Bulk)
  └── Shivan Reef, Stormcarved Coast, Spire of Industry, Starting Town, Emergence Zone (Bulk)
```

---

## 5. Sequencing the Win Lines

### Line 1: Thassa's Oracle + Tainted Pact (Available in Both Variants)
* **Mana Cost:** {U}{B} + {1}{B} = {1}{U}{B}{B} (4 total mana, split across two spells).
* **Execution:**
  1. Cast **Silence** or activate **Ranger-Captain of Eos** during your upkeep/main phase to guarantee opponents cannot cast spells.
  2. Cast **Thassa's Oracle** for {U}{U}.
  3. When Oracle enters the battlefield and its triggered ability goes on the stack, cast **Tainted Pact** for {1}{B}.
  4. Exile cards from your library until 0 cards remain.
  5. The Oracle trigger resolves with an empty library: you win the game.

### Line 2: Dualcaster Mage + Twinflame (Variant 2)
* **Mana Cost:** {1}{R} + {1}{R}{R} = {2}{R}{R}{R} (5 total mana).
* **Execution:**
  1. Cast **Twinflame** targeting any creature you control; hold priority.
  2. Flash in **Dualcaster Mage**.
  3. Dualcaster's ETB triggers targeting Twinflame.
  4. The copy resolves, targeting Dualcaster Mage, creating a token copy of Dualcaster Mage with haste.
  5. Repeat infinitely to create infinite hasty Dualcaster Mages and attack for lethal.

### Line 3: Underworld Breach + Brain Freeze (Variant 2)
* **Mana Cost:** {1}{R} (Breach) + {1}{U} (Brain Freeze) + Mana Source.
* **Execution:**
  1. Resolve **Underworld Breach**.
  2. Escape **Dark Ritual** or **Lotus Petal** to generate mana.
  3. Escape **Brain Freeze** targeting yourself to mill 3 cards per storm count into the graveyard.
  4. Repeat until entire library is in graveyard.
  5. Escape **Thassa's Oracle** from the graveyard to win immediately.
