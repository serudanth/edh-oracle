# The Necrobloom — Theorycrafting & Architecture Archive

This directory serves as the strategic planning space and jumping-off point for designing an Abzan ($\text{W}\text{B}\text{G}$) deck centered around **The Necrobloom** (*Modern Horizons 3*).

---

## File Directory

| File | Type | Description | Status |
|---|---|---|:---:|
| **[01-salvage-pool.md](file:///media/Zodiark/Atelier/dev/edh-oracle/knowledgebase/theorycrafting/necrobloom/01-salvage-pool.md)** | Inventory | Donor cards salvaged from *The Dirt Kicker* (Mono-G) & *The Master Chef* (WG), plus owned *The Gitrog Monster* & *Dakmor Salvage*. | Ready |
| **[02-necrobloom-engine-blueprint.md](file:///media/Zodiark/Atelier/dev/edh-oracle/knowledgebase/theorycrafting/necrobloom/02-necrobloom-engine-blueprint.md)** | Decklist & Blueprint | Complete 100-card Budget-Lethal Abzan Engine decklist (Bracket 3 / 3.5), maximizing owned staples with a ~$13.90 upgrade spend. | Ready |
| **[archidekt-export.txt](file:///media/Zodiark/Atelier/dev/edh-oracle/knowledgebase/theorycrafting/necrobloom/archidekt-export.txt)** | Export | Formatted text file ready for direct 1-click import into Archidekt. | Ready |

---

## 1. Commander Analysis & Mechanical Pillars

| Characteristic | Detail |
|---|---|
| **Name** | **The Necrobloom** |
| **Mana Cost** | $\{1\}\{\text{W}\}\{\text{B}\}\{\text{G}\}$ (4 MV) |
| **Card Type** | Legendary Creature — Plant |
| **Base Stats** | 2/7 |
| **Static Ability** | Land cards in your graveyard have **dredge 2**. |
| **Triggered Ability** | Whenever a land enters the battlefield under your control, create a 0/1 green Plant creature token. If you control seven or more lands with different names, create a 2/2 black Zombie creature token instead. |

### The Core Operating Invariants

1. **Self-Fueling Land Recurser:**
   * Any card-draw event (draw step, cantrip, trigger) can be converted into bringing a land from the graveyard to your hand while milling 2 additional cards.
   * Cracked fetchlands and sacrificed utility lands return to hand unconditionally, ensuring you never miss a land drop while steadily loading the bin.
2. **"Field of the Dead" in the Command Zone:**
   * Early game provides defensive bodies (0/1 Plants) that double as free sacrifice fodder.
   * Late game pivots into lethal board presence (2/2 Zombies) once the 7-distinct-names threshold is met.
3. **Singleton Diversity Requirement:**
   * Demands a high ratio of named utility lands, split basics (regular + snow-covered), duals, and MDFCs to reliably activate 2/2 Zombies on curve.

---

## 2. Four Architectural Archetypes

```
                     ┌─────────────────────────────┐
                     │     The Necrobloom Engine    │
                     │  (Land Dredge 2 + Landfall)  │
                     └──────────────┬──────────────┘
                                    │
       ┌────────────────┬───────────┴────────────┬────────────────┐
       ▼                ▼                         ▼                ▼
[Archetype 1]    [Archetype 2]             [Archetype 3]    [Archetype 4]
 Aristocrats      Cycling Storm              Abzan Gates      The Gitrog
  Drain-Fall     & Turbo-Mill               & Maze's End     Discard Engine
 (Skullclamp +   (Fluctuator +             (12+ Gates in      (Skirge +
  Soultrader)    Syr Konrad)                Abzan + Gond)      Discard)
```

### Archetype 1: "Drain-Fall" Aristocrats & Token Velocity
* **Concept:** Pivot away from slow combat steps. Convert early 0/1 Plants and late 2/2 Zombies directly into cards, mana, and table-wide life drain.
* **Key Engine:**
  * **Skullclamp:** 0/1 Plants die on equip for $\{1\}$, drawing 2 cards. Each draw can be replaced with Dredge 2, putting 2 lands in hand and milling 4 cards.
  * **Warren Soultrader / Phyrexian Altar:** Converts landfall tokens into instant colored mana.
  * **Drain Package:** `Corpse Knight` (drains on enter), `Mirkwood Bats` (drains on token enter/leave), `Cruel Celebrant`, `Elas il-Kor, Sadistic Pilgrim`.
  * **Wight of the Reliquary:** Consumes Plant tokens to tutor any land straight to the battlefield untapped.
* **Target Bracket:** Bracket 3 (High Synergy / Mid-to-High Power).

### Archetype 2: Fluctuator / Cycling Storm (Turbo Self-Mill)
* **Concept:** Exploit the rules timing of cycling lands with universal dredge to churn through your deck at instant speed.
* **The Interaction:** Discarding a cycling land puts it into the graveyard as a cost *before* the cycling trigger resolves. You immediately replace that draw with Dredge 2 on *that same land*, recurring it to hand and milling 2.
* **Key Engine:**
  * **Fluctuator:** Reduces generic cycling costs to $\{0\}$. With 2-mana cyclers (`Drifting Meadow`, `Polluted Mire`, `Slippery Karst`, `Blasted Landscape`), mill your entire library for zero mana.
  * **Payoffs:** `Syr Konrad, the Grim` (game-ending burn), `Insidious Roots` (spawns an army of giant mana-dorks), `Songs of the Damned` into `Living Death` or mass reanimation.
* **Target Bracket:** Bracket 3.5 / 4 (Combo-Centric).

### Archetype 3: Abzan Gates & The Secret Maze
* **Concept:** An unconventional alt-wincon deck. Most pods expect Maze's End only in 4-5 color shells; Abzan quietly possesses 12+ legal Gates with built-in tutoring and graveyard protection.
* **Key Engine:**
  * **The Gates:** *Orzhov, Golgari, Selesnya Guildgates* + *Citadel, Black Dragon, Manor Gates* + *Heap Gate, Basilisk Gate, Baldur's Gate, Gond Gate, Gateway Plaza, Plaza of Harmony*.
  * **Gond Gate:** Crucial engine piece — allows all Gates to enter untapped.
  * **Baldur's Gate:** Generates explosive amounts of colorless/filtered mana.
  * **Necrobloom Synergy:** Land Dredge guarantees you can never be locked out by land destruction, while the diverse Gate names naturally turn on 2/2 Zombie generation.
* **Target Bracket:** Bracket 2.5 / 3 (Subversive Casual / Surprise Win).

### Archetype 4: The Abzan Gitrog & Discard Velocity
* **Concept:** Run `The Gitrog Monster` in the 99 with discard outlets. Because *every* land has dredge 2, you do not need Dakmor Salvage to loop draws.
* **Key Engine:**
  * Discard outlets: `Putrid Imp`, `Skirge Familiar`, `Zombie Infestation`, `Oblivion Crown`.
  * Pitching a land triggers Gitrog's draw $\rightarrow$ replace with Dredge 2 on that land $\rightarrow$ milling another land triggers Gitrog again.
  * Generates near-infinite black mana via `Skirge Familiar` and fills the graveyard for `Splendid Reclamation` / `Lumra, Bellow of the Woods`.
* **Target Bracket:** Bracket 3.5 / 4 (Engine / High Power).

---

## 3. High-Priority Tech & Donor Cards

### Cards Already Owned / In Donor Decks (e.g. *The Dirt Kicker*)
* `Azusa, Lost but Seeking` (Extra land drops)
* `Erinis, Gloom Stalker` (Attacks recur lands from graveyard)
* `Harrow` (Sacrifice a land to ramp 2 lands untapped $\rightarrow$ dredge the sacrificed land)
* `Traverse the Outlands` (Massive basic land fetch)
* `Abundance` (Guarantees land draws or nonland selection)
* `Spore Frog` (Fog lock when paired with creature recursion)
* `Rishkar's Expertise` / `Soul's Might` (Big draw/buff effects)

### Modern Standouts & Synergy MVPs
* **Six:** Nonland permanents in the graveyard gain Retrace. Dredging lands into hand turns your graveyard into your active spell-pool.
* **Shifting Woodland:** Delirium is trivial to achieve. Can copy any permanent in your graveyard (e.g., `Aftermath Analyst`, `Craterhoof Behemoth`, `Six`) for $\{4\}$ at instant speed.
* **Talon Gates of Madara:** Recurrable utility land that phases out opposing commanders, attackers, or protects Necrobloom from board wipes.
* **Aftermath Analyst / Lumra, Bellow of the Woods / Splendid Reclamation:** Mass-resurgence spells that put 15+ lands onto the board at once, generating 15–30 Zombies in a single burst.
* **Insidious Roots:** Whenever a land or creature leaves the graveyard via dredge, triggers plant growth and mana ramp.

---

## 4. Discussion Framework Before Construction

Before assembling the full 100-card list, consider the following decisions:

1. **Target Power Level & Playgroup Pod Alignment:**
   * Do we want a **combat/engine value deck** (Tokens + Aristocrats drain, Bracket 3), or an **accelerated combo list** (Fluctuator / Gitrog mill, Bracket 3.5/4)?
2. **Primary Win Condition:**
   * Token Overrun (`Craterhoof Behemoth`, `Moonshaker Cavalry`, `Beastmaster Ascension`)?
   * Aristocrats Drain (`Corpse Knight`, `Mirkwood Bats`, `Syr Konrad, the Grim`)?
   * Alt-Win / Landfall Combo (`Maze's End`, `Scapeshift` + `Ob Nixilis, the Fallen`)?
3. **Graveyard Reliance & Resilience:**
   * The Necrobloom leans heavily on the graveyard. How much protection (e.g., `Perpetual Timepiece`, `Boseiju, Who Endures`, instant-speed interaction) should be slotted against Rest in Peace / Bojuka Bog effects?
4. **Donor vs. Fresh Sourcing:**
   * Should we pull heavily from existing decks (e.g., *The Dirt Kicker*), or treat this as a standalone build?
