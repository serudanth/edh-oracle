# Magic: The Gathering Comprehensive Rules Archive

This directory maintains the official, authoritative plaintext reference of the **Magic: The Gathering Comprehensive Rules** for EDH Oracle rules lookup, color identity verification, and engine validation.

---

## Metadata

| Property | Value |
| :--- | :--- |
| **Document** | Magic: The Gathering Comprehensive Rules |
| **Effective Date** | August 7, 2026 |
| **WotC CDN Published** | August 19, 2026 |
| **Archive Date** | September 17, 2026 |
| **Source URL** | [`https://media.wizards.com/2026/downloads/MagicCompRules%2020260819.txt`](https://media.wizards.com/2026/downloads/MagicCompRules%2020260819.txt) |
| **Official Portal** | [`https://magic.wizards.com/en/rules`](https://magic.wizards.com/en/rules) |
| **Local File** | [`MagicCompRules.txt`](MagicCompRules.txt) |
| **File Size** | 977,819 bytes (~955 KB) |
| **Line Count** | 9,397 lines |
| **Total Numbered Rules** | 1,988 rules (`100.1` through `905.7`) |

---

## Document Structure

The Comprehensive Rules consist of an introduction, 9 major chapters covering 142 distinct sections, followed by an exhaustive glossary and credits:

1. **Section 1: Game Concepts** (`100`–`123`)
   - Core foundations: Golden Rules, Players, Starting/Ending the Game, Colors, Mana, Numbers/Symbols, Cards, Objects, Permanents, Tokens, Spells, Abilities, Emblems, Targets, Special Actions, Timing & Priority, Costs, Life, Damage, Drawing, Counters, Stickers.
2. **Section 2: Parts of a Card** (`200`–`213`)
   - Card anatomy: Name, Mana Cost & Color, Illustration, Color Indicator, Type Line, Expansion Symbol, Text Box, Power/Toughness, Loyalty, Defense, Hand/Life Modifiers.
3. **Section 3: Card Types** (`300`–`315`)
   - Types and subtypes: Artifacts, Creatures, Enchantments, Instants, Lands, Planeswalkers, Sorceries, Kindreds, Dungeons, Battles, Planes, Phenomena, Vanguards, Schemes, Conspiracies.
4. **Section 4: Zones** (`400`–`408`)
   - Spatial zones: Library, Hand, Battlefield, Graveyard, Stack, Exile, Ante, Command.
5. **Section 5: Turn Structure** (`500`–`514`)
   - Phases and steps: Beginning Phase (Untap, Upkeep, Draw), Main Phase, Combat Phase (Beginning, Attackers, Blockers, Combat Damage, End of Combat), Ending Phase (End Step, Cleanup Step).
6. **Section 6: Spells, Abilities, and Effects** (`600`–`616`)
   - Mechanics and priority: Casting Spells, Activated/Triggered/Static Abilities, Mana Abilities, Loyalty Abilities, Linked Abilities, Resolution, One-Shot/Continuous/Text-Changing/Replacement/Prevention Effects, Layer System (`613`).
7. **Section 7: Additional Rules** (`700`–`733`)
   - Advanced mechanics: Keyword Actions (`701`), Keyword Abilities (`702`), Turn-Based/State-Based Actions (`703`, `704`), Coin Flipping/Die Rolling, Copying, Face-Down, Double-Faced Cards, Sagas, Classes, Cases, Attractions, Spacecraft, Day/Night, Shortcuts, Illegal Actions.
8. **Section 8: Multiplayer Rules** (`800`–`811`)
   - Multiplayer formats: Range of Influence, Attack Multiple Players, Shared Turns, Free-for-All (`806`), Two-Headed Giant (`810`), Emperor, Grand Melee.
9. **Section 9: Casual Variants** (`900`–`905`)
   - Alternative formats: Planechase (`901`), Vanguard (`902`), **Commander (`903`)**, Archenemy (`904`), Conspiracy Draft (`905`).
10. **Glossary**
    - Complete alphabetical definitions from *Abandon* to *Zone-Change Triggers*.
11. **Credits & Legal**
    - Design, development, rules management credits, and trademark/licensing acknowledgments.

---

## EDH / Commander Critical Rules

For EDH Oracle, the primary rule references are:

- **Rule 903 (Commander Variant):**
  - `903.3`: Commander eligibility (legendary creature, Vehicle, or Spacecraft with P/T, or cards with explicit commander abilities).
  - `903.4`: Color identity determination (colors in mana cost, rules text, characteristic-defining abilities, or color indicators).
  - `903.5`: Deck construction rules (singleton 99 + commander, color identity restriction).
  - `903.8`: Commander tax ({2} per previous cast from command zone).
  - `903.10`: Commander damage lethal state-based action (21 combat damage from a single commander).
- **Rule 613 (Interaction of Continuous Effects / Layers):**
  - Essential for evaluating power/toughness modifiers, type changing, ability adding/removing, and control alterations.
- **Rule 105 & 106 (Colors & Mana):**
  - Mana generation and color identity evaluation constraints.

---

## Maintenance & Ingestion Note

Wizards of the Coast releases updated Comprehensive Rules concurrently with premier card set releases. When updating:
1. Verify the current download URL on [`https://magic.wizards.com/en/rules`](https://magic.wizards.com/en/rules).
2. If egress is restricted by proxy (HTTP 403), route through Jina reader (`https://r.jina.ai/https://media.wizards.com/...`) with header `X-Return-Format: text`.
3. Overwrite [`MagicCompRules.txt`](MagicCompRules.txt) and update this README metadata and effective date.
