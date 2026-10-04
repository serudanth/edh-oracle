# The Apex Rush — Salvage Pool & Donor Architecture

This document catalogs every card in the optimized **Winota, Joiner of Forces** build (*The Apex Rush*), detailing its source within Charles's (`fowlplays`) physical card collection ([`manabox-collection.csv`](../../podlist/charles/inventory/manabox-collection.csv)) and active deck archive in `knowledgebase/podlist/charles/decks/`.

---

## 1. Executive Summary: 100% Owned Card Parity

* **Total Cards in Deck:** 100 (1 Commander, 99 Mainboard)
* **Missing / Unowned Cards:** 0 ($0.00 cash outlay required)
* **Core Base:** *The Rush* (70 cards retained from the existing active physical deck, including commander and basics)
* **Scavenged Upgrades:** 30 high-impact cards harvested across 6 active decks and the ManaBox bulk inventory
* **Creature Density:** 51 Total Creatures (27 Humans including Witch Enchanter MDFC, 24 Non-Humans)
* **Non-Creature Footprint:** Trimmed down to 16 absolute essential non-creatures (0 equipment, 0 non-creature token makers)

---

## 2. Donor Breakdown by Source

### A. Harvested from *The Lorehold Redux* (WR Graveyard) — 7 Cards
* **Selfless Spirit:** 2-CMC Spirit Cleric (Non-Human). Flying 2/1. Sacrifices to grant all creatures indestructible at instant speed against sweepers.
* **Remorseful Cleric:** 2-CMC Spirit Cleric (Non-Human). Flying 2/1. Sacrifices to exile target player's entire graveyard at instant speed (Breach/Reanimation hate).
* **Guardian of Faith:** 3-CMC Spirit Knight (Non-Human). Flash 3/2. Phases out target creatures to dodge non-destruction board wipes (*Farewell*, *Cyclonic Rift*, *Toxic Deluge*).
* **Drumbellower:** 3-CMC Spirit (Non-Human). Flying 3/2. Untaps all creatures during each opponent's untap step for total vigilance.
* **Fellwar Stone:** Untapped 2-CMC mana rock.
* **Sundown Pass:** Untapped Boros slowland ({R} or {W}) entering untapped on Turn 3+, replacing the artifact-conditional Spire of Industry.
* **Fabled Passage:** Untapped land fetch on turn 4+ to fix double-white and double-red requirements.

### B. Harvested from *The Gate of Babylon* / *The Armory* (WR Equipment) — 4 Cards
* **Arcane Signet:** Untapped 2-CMC Boros fixing rock.
* **Talisman of Conviction:** Untapped 2-CMC Boros fixing rock.
* **Tithe Taker:** 2-CMC Human Soldier. Opponents' spells and abilities on your turn cost {1} more (mini-Grand Abolisher). Leaves behind a 1/1 flying Spirit token (non-Human) upon death.
* **Clever Concealment:** 4-CMC instant with Convoke. Phases out any number of permanents at instant speed for 0 mana.

### C. Harvested from *The Crystal Braves* (WU Knights/Legends) — 2 Cards
* **Silverwing Squadron:** 6-CMC Human Knight. Flying, vigilance, */* equal to creature count. Enters as an enormous indestructible threat off Winota; attacks to permanently create three 2/2 non-Human Knight tokens with vigilance.
* **Michiko Konda, Truth Seeker:** 4-CMC Human Advisor. Unconditional stax deterrent: whenever an opponent deals damage to you, that player must sacrifice a permanent of their choice.

### D. Harvested from *The Master Chef* (WG Counters) — 3 Cards
* **Oltec Matterweaver:** 3-CMC Human Artificer. Whenever you cast a creature spell of MV <= 3, creates a 1/1 Gnome artifact creature token (Non-Human) to fuel Winota triggers.
* **Reprieve:** 2-CMC white spell delay that bypasses uncounterable clauses, bounces spells, and cantrips.
* **Soul Warden:** 1-CMC Human Cleric. Generates massive continuous life cushion off creature swarms; serves as a 1-drop Human tutor target for Ranger-Captain of Eos.

### E. Harvested from *The Copied Factory* (UBR Wizards) — 3 Cards
* **Gamble:** 1-CMC instant tutor to locate Kiki-Jiki, Mirror Breaker, Combat Celebrant, or Silence.
* **Prismatic Vista:** Premium untapped fetchland that fetches either basic Mountain or basic Plains untapped.
* **City of Brass:** Untapped 5-color land providing unconditional Boros fixing on Turn 1.

### F. Harvested from *The Last Ride* (RG Vehicles) — 2 Cards
* **Dolmen Gate:** 2-CMC artifact. Attacking creatures take zero combat damage, allowing fragile non-Humans to attack into lethal blockers for guaranteed Winota triggers.
* **Magda, Brazen Outlaw:** 2-CMC Dwarf Berserker (Non-Human). Generates Treasure tokens whenever tapped (attacking or tapping for abilities).

### G. Harvested from ManaBox Physical Bulk — 9 Cards
* **Sanctifier en-Vec:** 2-CMC Human Cleric (`MH2 #444`). Protection from black and red. Shuts down Underworld Breach, Dockside loops, and graveyard strategies.
* **Bastion Protector:** 3-CMC Human Soldier (`FIC #233`). Commander creatures you control get +2/+2 and have indestructible.
* **Abdel Adrian, Gorion's Ward:** 5-CMC Human Warrior (`CLB #2`). Exiles nonland permanents to create a swarm of 1/1 non-Human Soldier tokens.
* **Sami, Ship's Engineer:** 4-CMC Human Artificer (`EOE #225`). At your end step, if you control two or more tapped creatures (guaranteed on any attack turn), creates a permanent 2/2 non-Human Robot token to continuously supply Winota triggers.
* **Momo, Friendly Flier:** 1-CMC Lemur Bat Ally (`TLA #29`). 1/1 Flying Non-Human for Turn 3 Winota triggers.
* **Momo, Playful Pet:** 1-CMC Lemur Bat Ally (`TLA #30`). 1/1 Flying & Vigilance Non-Human; attacks for Winota and stays back to block.
* **Topplegeist:** 1-CMC Spirit (`SOI #45`). 1/1 Flying Non-Human; taps opposing blocker on entry.
* **Senu, Keen-Eyed Protector:** 2-CMC Bird Scout (`ACR #8`). 2/1 Flying/Vigilance Non-Human; recurs from exile tapped and attacking when a legendary creature attacks.
* **Grenzo, Havoc Raiser:** 2-CMC Goblin Rogue (`TDC #216`). Goads opponents or impulse draws from combat damage.

---

## 3. Cards Cut from Deck & Architectural Rationale

| Cut Card | Type | Rationale for Cut |
|---|---|---|
| **Rionya, Fire Dancer** | Creature (Human) | Playtest cut: with non-creatures trimmed to 8 total instants/sorceries, Rionya cannot scale and only ever creates 1 temporary token for 5 mana. Replaced by **Sami, Ship's Engineer** (permanent 2/2 Robot token generation on a 4-CMC body). |
| **Harried Dronesmith** | Creature (Human) | Identified low-yield engine: creates a temporary 1/1 Thopter that is sacrificed at end step, yielding only +1 temporary trigger for 4 mana. Replaced by **Silverwing Squadron** (creates permanent 2/2 non-Human Knight tokens for each opponent on attack). |
| **Zack Fair** | Creature (Human) | Dead equipment attachment clause; {1} to sacrifice for indestructible is outclassed by **Selfless Spirit**, **Guardian of Faith**, and **Bastion Protector**. Replaced by **Soul Warden** (continuous lifegain + 1-drop Human tutor target for Ranger-Captain). |
| **Freya Crescent** | Creature (Non-Human) | Dead equipment mana clause; vanilla 1/1 flyer on your turn. Replaced by **Momo, Playful Pet** (1-CMC with both Flying AND Vigilance). |
| **Swiftblade Vindicator** | Creature (Human) | Without equipment to pump power, it is a vanilla 1/1 double striker dealing 2 damage. Replaced by stax deterrent **Michiko Konda, Truth Seeker**. |
| **Spire of Industry** | Land | Artifact requirement makes it unreliable as colored mana with equipment purged (only 5 artifacts remaining). Replaced by unconditional untapped dual **Sundown Pass**. |
| **Conqueror's Flail** | Artifact (Equipment) | Dropped equipment package. Slower setup; replaced by **Tithe Taker**, **Boromir**, and **Silence**. |
| **Lightning Greaves** | Artifact (Equipment) | Shroud prevents targeting; replaced by haste from creatures and zero-cost board protection. |
| **Skullclamp** | Artifact (Equipment) | 1-mana equip is mana-intensive during setup; replaced by creature card engines (**Professional Face-Breaker**, **Grenzo, Havoc Raiser**). |
| **Umezawa's Jitte** | Artifact (Equipment) | Slow reactive value engine that slows down proactive aggro velocity. |
| **Cloud, Midgar Mercenary** | Creature (Human) | Without Equipment cards to tutor, Cloud is an empty 2-CMC vanilla 2/1. |
| **Mind Stone** | Artifact | Colorless 2-CMC rock; does not fix Boros colors and whiffs on Winota triggers. |
| **Raise the Alarm** | Instant | Non-creature token maker. Whiffs on Winota triggers. Replaced by 1-CMC evasive non-Humans (**Momo**, **Topplegeist**). |
| **Secure the Wastes** | Instant | Non-creature mana sink that whiffs on Winota triggers. Replaced by token-generating Humans (**Oltec Matterweaver**, **Silverwing Squadron**). |
| **Hordeling Outburst** | Sorcery | 3-CMC sorcery speed non-creature that whiffs on Winota. Replaced by recurring creature token engines (**Goblin Rabblemaster**, **Legion Warboss**). |
| **Warleader's Call** | Enchantment | 3-CMC non-creature anthem. Whiffs on Winota. Replaced by creature-based anthems (**Goldnight Commander**, **Erkenbrand, Lord of Westfold**, **Blade Historian**). |
| **Relentless Assault** | Sorcery | 4-CMC sorcery speed extra combat. Whiffs on Winota. Replaced by creature combo piece (**Combat Celebrant** + **Kiki-Jiki**). |
| **Requisition Raid** | Sorcery | Sorcery speed non-creature removal. Replaced by creature-based removal (**Cathar Commando**, **Skyclave Apparition**, **Dauntless Dismantler**, **Witch Enchanter**). |
| **Loran's Escape** | Instant | Single-target reactive protection. Replaced by team protection on bodies (**Selfless Spirit**, **Guardian of Faith**, **Bastion Protector**). |
| **Unbreakable Formation** | Instant | 3-CMC instant protection. Replaced by free convoke protection (**Clever Concealment**) and on-board sacrifice protection (**Selfless Spirit**, **Boromir**). |
| **Chaos Warp** | Instant | 3-CMC non-creature removal. Replaced by creature density. |
| **Generous Gift** | Instant | 3-CMC non-creature removal. Replaced by creature density. |
| **Return the Favor** | Instant | Reactive spree spell that causes Winota whiffs. |
| **Abrade** | Instant | Narrow removal spell that causes Winota whiffs. |
| **Plains (1x)** | Basic Land | Land count trimmed to 33 (including Witch Enchanter MDFC) to match lean 2.50 average non-land CMC. |
