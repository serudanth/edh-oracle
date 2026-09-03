---
type: lesson
title: "Product Design Document (PDD) — Automated EDH Deck Analyzer Engine"
domain: tooling
tags: [#pdd, #deck-analyzer, #architecture, #scoring-engine]
related: [2026-08-25-external-analysis-extract]
source: internal-design
---

# Product Design Document (PDD)
## Automated EDH Deck Analyzer & Metric Calculation Engine

**Author:** EDH Oracle System Architect  
**Status:** Proposed / Design Specification  
**Version:** 1.1.0  
**Target Repository:** `edh-oracle`  
**Date:** 2026-08-25  

---

## 1. Executive Summary & Product Vision

### 1.1 Objective
The **EDH Deck Analyzer Engine** is a deterministic, offline-capable analysis subsystem designed to calculate objective performance metrics, power levels, curve evaluations, fast mana counts, tutor counts, and infinite combo configurations for Magic: The Gathering Commander (EDH) decklists.

### 1.2 Problem Statement
Traditional rating systems treat all EDH decks identically by applying uniform card counts and static weights. A *Winota, Joiner of Forces* deck does not require traditional land ramp because its core engine cheats high-CMC creatures directly onto the battlefield via attack triggers. Static formulas penalize cheat/tempo engines for low ramp while over-rewarding goodstuff piles. Furthermore, relying on external web scrapers (e.g. CommanderSalt, EDHCheck, ScryCheck) introduces Cloudflare HTTP 403 blocks, SPA rendering delays, and UI breakage.

### 1.3 Proposed Solution
Implement a **local, 100% deterministic evaluation engine** inside `tools/` featuring:
1. **First-Pass Piloting Intent Classification**: Evaluates the commander(s) and 99 to determine how the deck wants to be piloted (Cheat/Tempo, Spellslinger, Aristocrats, Landfall, Control, Voltron, Midrange).
2. **Strategy-Adaptive Dynamic Weight Profiles**: Dynamically re-weights assessment pillars based on the deck's identified strategic intent.
3. **Quantifiable Sub-Pillar Formulas**: Computes mathematical sub-scores for Velocity, Engine Synergy, Interaction, Resource Acceleration, Resilience, Closing Vector, and Mana Base Health.

---

## 2. System Architecture & Workflow

```
+-----------------------------------------------------------------------------------+
|                                  INPUT SOURCES                                    |
|   Archidekt URL / ID  |  Moxfield URL / ID  |  Local KB File  |  Raw Text Decklist    |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                        1. DECKLIST EXTRACTION & NORMALIZER                        |
|   Extracts title, owner, commander, color identity, and normalized card list       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                        2. CARD ATTRIBUTE ENRICHMENT MODULE                        |
|   Queries local scryfall-cards.json cache (fallback to Scryfall API via proxy)    |
|   Resolves: CMC, mana cost, type line, oracle text, keywords, color identity     |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|               3. FIRST-PASS PILOTING PATTERN & INTENT CLASSIFICATION              |
|   Analyzes Commander + 99 composition to identify strategic archetype:            |
|   - Cheat / Aggro Tempo (Winota, Kaalia, Kinnan)                                  |
|   - Spellslinger / Cantrip Storm (Feather, Inalla, Stella Lee)                    |
|   - Aristocrats / Sac-Loop (Sephiroth, Ayara, Teysa)                             |
|   - Big Mana / Landfall (Gladiolus/Forresta, Omnath)                              |
|   - Control / Stax (Y'shtola, Grand Arbiter)                                      |
|   - Voltron / Equipment (Cloud, Bruenor, Light-Paws)                              |
|   - Midrange / Engine Value (Minsc & Boo, Miirym)                                 |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                     4. STRATEGY-ADAPTIVE WEIGHT PROFILE ASSIGNMENT                 |
|   Selects archetype weight matrix W_archetype adjusting pillar importance          |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                     5. COMBO RESOLVER (Commander Spellbook API)                    |
|   POST find-my-combos with commander + deck mainboard                             |
|   Extracts: Exact combos, step counts, prerequisites, produces, almost-included  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                  6. QUANTIFIABLE SUB-PILLAR METRIC CALCULATION                    |
|   Calculates: S_velocity, S_engine, S_interaction, S_resource, S_resilience,       |
|               S_closing, S_mana.                                                  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                           7. STANDARDIZED JSON OUTPUT                             |
|   Strict adherence to external_analysis_extract.py schema                         |
+-----------------------------------------------------------------------------------+
```

---

## 3. Quantifiable Sub-Dimension Formulas

Each dimension $S_k \in [0, 100]$ is computed deterministically from card metrics:

### 3.1 Velocity & Curve Efficiency ($S_{\text{velocity}}$)
Evaluates how efficiently the deck converts mana into early game actions.
$$S_{\text{velocity}} = \min\left(100, \; \max\left(0, \; 120 - 30 \times (\text{AMV} - 1.5) + 40 \times \frac{N_{\text{CMC}\le 2}}{N_{\text{total}}}\right)\right)$$
- $\text{AMV}$: Average Mana Value of non-land cards.
- $N_{\text{CMC}\le 2}$: Count of non-land cards with $\text{CMC} \le 2$.

### 3.2 Engine Synergy & Repeatable Advantage ($S_{\text{engine}}$)
Measures the density of ongoing value engines vs. single-use spells.
$$S_{\text{engine}} = \min\left(100, \; 12 \times N_{\text{rep\_draw}} + 6 \times N_{\text{syn}} + 15 \times N_{\text{mult}}\right)$$
- $N_{\text{rep\_draw}}$: Count of repeatable draw engines (*Rhystic Study*, *Skullclamp*, *Beast Whisperer*).
- $N_{\text{syn}}$: Cards directly triggering or benefiting from the commander's primary mechanic.
- $N_{\text{mult}}$: Exponential engine multipliers (*Doubling Season*, *Drivnod*, *Panharmonicon*).

### 3.3 Interaction Efficiency & Coverage ($S_{\text{interaction}}$)
Evaluates answer speed, cost efficiency, and breadth of threat coverage.
$$S_{\text{interaction}} = \min\left(100, \; \left(6 \times N_{\text{inst}} + 15 \times C_{\text{types}}\right) \times \max\left(0.5, \; 2.0 - 0.3 \times \overline{\text{CMC}}_{\text{int}}\right)\right)$$
- $N_{\text{inst}}$: Instant-speed answers.
- $C_{\text{types}} \in [0.0, 1.0]$: Coverage ratio across 5 threat types (Creature, Artifact, Enchantment, Graveyard, Stack/Spell).
- $\overline{\text{CMC}}_{\text{int}}$: Average mana cost of interaction spells.

### 3.4 Resource Acceleration & Cheat Velocity ($S_{\text{resource}}$)
Measures how quickly the deck ramps mana **or cheats deployment costs**.
$$S_{\text{resource}} = \min\left(100, \; 6 \times N_{\text{ramp}} + 20 \times N_{\text{fast}} + 18 \times N_{\text{cheat}}\right)$$
- $N_{\text{ramp}}$: Standard land/rock ramp spells.
- $N_{\text{fast}}$: Net-positive fast mana sources (*Sol Ring*, *Mana Crypt*, *Lotus Petal*).
- $N_{\text{cheat}}$: Free deployment / cheat engines (*Winota*, *Kaalia*, *Sneak Attack*, *Aetherial Armor*).

### 3.5 Resilience & Recovery ($S_{\text{resilience}}$)
Measures ability to withstand and recover from board wipes, removal, and disruption.
$$S_{\text{resilience}} = \min\left(100, \; 12 \times N_{\text{prot}} + 10 \times N_{\text{rec}} + 8 \times N_{\text{indest}}\right)$$
- $N_{\text{prot}}$: Instant protection spells (*Heroic Intervention*, *Teferi's Protection*, *Deflecting Swat*).
- $N_{\text{rec}}$: Recursion engines (*Reanimate*, *Sun Titan*, *Underworld Breach*).
- $N_{\text{indest}}$: Persistent protection/indestructible/hexproof enablers.

### 3.6 Closing Vector & Inevitability ($S_{\text{closing}}$)
Evaluates table-killing capability and win-condition speed.
$$S_{\text{closing}} = \min\left(100, \; 25 \times N_{\text{combo}} + 12 \times N_{\text{tutor}} + 15 \times N_{\text{kill}}\right)$$
- $N_{\text{combo}}$: Verified infinite combo lines (via Commander Spellbook).
- $N_{\text{tutor}}$: Unconditional/typed tutors that fetch win conditions.
- $N_{\text{kill}}$: Non-combo table-kill finishers (*Craterhoof*, *Gray Merchant*, *Triumph of the Hordes*).

### 3.7 Mana Base Health ($S_{\text{mana}}$)
$$S_{\text{mana}} = 60 \times R_{\text{untapped}} + 40 \times A_{\text{color}}$$
- $R_{\text{untapped}}$: Ratio of lands entering untapped.
- $A_{\text{color}}$: Color fixing alignment score (matching land mana production to 99 card cost requirements).

---

## 4. Piloting Pattern Analysis & Strategy-Adaptive Dynamic Weights

### 4.1 First-Pass Intent Classification
Before computing the final composite score, the engine inspects the 99 + Commander to classify the primary **Piloting Archetype**:

1. **Cheat / Aggro Tempo**: High density of low-cost enablers (e.g. non-Human tokens) + high-CMC cheat targets (e.g. Humans/Demons/Angels) + cheat-attack commanders (*Winota*, *Kaalia*).
2. **Spellslinger / Cantrip Storm**: High instant/sorcery ratio ($>30\%$) + low AMV + magecraft/prowess payoffs (*Feather*, *Stella Lee*).
3. **Aristocrats / Sacrifice**: High sacrifice outlet count + death-trigger payoffs + recursive bodies (*Sephiroth*, *Ayara*).
4. **Big Mana / Landfall**: High land count ($>38$) + extra land drop enablers + landfall triggers (*Gladiolus/Forresta*, *Omnath*).
5. **Control / Stax**: High instant interaction ($>15$) + sweepers + stax/tax pieces (*Y'shtola*).
6. **Voltron / Equipment**: High Equipment/Aura count ($>12$) + equipment cost reducers (*Cloud*, *Bruenor*).
7. **Midrange / Engine Value**: Balanced creature/spell distribution building progressive board control (*Minsc & Boo*).

### 4.2 Strategy-Adaptive Weight Matrix ($W_{\text{archetype}}$)

The Composite Deck Score $S_{\text{deck}}$ applies the identified archetype's dynamic weight profile:

$$S_{\text{deck}} = \sum_{k=1}^{7} w_k \cdot S_k \quad \text{where} \quad \sum_{k=1}^{7} w_k = 1.0$$

| Strategic Archetype | $w_{\text{velocity}}$ | $w_{\text{engine}}$ | $w_{\text{interaction}}$ | $w_{\text{resource}}$ | $w_{\text{resilience}}$ | $w_{\text{closing}}$ | $w_{\text{mana}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cheat / Aggro Tempo** | **0.25** | **0.25** | 0.10 | **0.05** *(low ramp)* | 0.10 | **0.15** | 0.10 |
| **Spellslinger / Storm** | **0.25** | 0.20 | **0.20** | 0.05 | 0.05 | **0.15** | 0.10 |
| **Aristocrats / Sac** | 0.10 | **0.30** | 0.10 | 0.10 | **0.15** | **0.15** | 0.10 |
| **Big Mana / Landfall** | 0.10 | 0.15 | 0.10 | **0.35** *(high ramp)* | 0.05 | 0.15 | 0.10 |
| **Control / Stax** | 0.10 | 0.20 | **0.30** | 0.10 | 0.15 | 0.05 | 0.10 |
| **Voltron / Equipment** | 0.15 | **0.25** | 0.10 | 0.10 | **0.15** | 0.15 | 0.10 |
| **Default / Midrange** | 0.15 | 0.20 | 0.15 | 0.15 | 0.10 | 0.15 | 0.10 |

---

## 5. Output Data Schema & API Contract

The output generated by the engine strictly conforms to the JSON schema defined in `tools/external_analysis_extract.py`:

```json
{
  "deck_name": "Sephiroth Pain is Love",
  "commander": "Sephiroth, Fabled SOLDIER // Sephiroth, One-Winged Angel",
  "sources": [
    {
      "source": "EDHOracleLocalEngine",
      "status": "success",
      "error": null,
      "metrics": {
        "power_score": 8.8,
        "bracket": 4,
        "combo_score": 9.0,
        "interaction_score": 7.5,
        "ramp_score": 8.0,
        "consistency_score": 8.5,
        "speed_score": 8.2,
        "tutor_count": 4,
        "fast_mana_count": 3,
        "combo_count": 1
      },
      "source_metrics": {
        "piloting_archetype": "Aristocrats / Sacrifice",
        "average_cmc": "2.34",
        "land_count": 34,
        "salt_score": "48.5"
      },
      "text": {
        "summary": "Deterministic Mono-Black aristocrats control deck featuring the Sanguine Bond + Exquisite Blood combo, high tutor density, and fast mana.",
        "explanations": [
          "Piloting Archetype identified as Aristocrats / Sacrifice; applied dedicated Sac-Engine weight matrix.",
          "Calculated via local Scryfall oracle engine and Commander Spellbook combo API."
        ],
        "strengths": [
          "High tutor density (4 tutors)",
          "Fast mana acceleration (3 sources)",
          "Deterministic infinite life-drain win condition"
        ],
        "weaknesses": [
          "Vulnerable to instant-speed enchantment removal and graveyard hate"
        ],
        "recommendations": [
          "Consider Imp's Mischief or Defense Grid for stack protection"
        ],
        "suggested_changes": [],
        "combo_lines": [
          "Sanguine Bond + Exquisite Blood -> Infinite life drain and infinite life gain"
        ],
        "mulligan_advice": [
          "Prioritize hands with early ramp/fast mana and at least 2 lands."
        ]
      },
      "raw_result": {
        "engine_version": "1.1.0",
        "rule_set": "Standard EDH 2026"
      }
    }
  ],
  "metadata": {
    "deck_url": "https://archidekt.com/decks/13966160",
    "analysis_time": "2026-08-25T18:06:00Z",
    "successful_sources": ["EDHOracleLocalEngine"],
    "failed_sources": []
  }
}
```

---

## 6. Implementation Roadmap & Verification

- **Phase 1**: Implement `tools/deck_analyzer_engine.py` (First-pass piloting pattern classifier, dynamic weight selector, sub-pillar mathematical formulas).
- **Phase 2**: Integrate Commander Spellbook API combo detection.
- **Phase 3**: Add unit test suite `tests/test_deck_analyzer_engine.py`.
- **Phase 4**: Run batch analysis across all 48 eligible pod decks in `knowledgebase/podlist/`.
