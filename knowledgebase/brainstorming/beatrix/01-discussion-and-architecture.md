# Beatrix, Loyal General — Discussion & Architectural Blueprint

**Deck:** The Alexandria Armory  
**Commander:** [Beatrix, Loyal General](https://scryfall.com/card/fic/12/beatrix-loyal-general) ({4}{W}{W})  
**Format:** Commander / EDH  
**Color Identity:** Mono-White ({W})  
**Archetype:** Equipment Voltron / Heavy Armory / Combat Control  
**Target Power Bracket:** Bracket 3 (High-Synergy Mid-Power Engine)  
**Date:** 2026-09-11  

---

## 1. Context & The "Boros Fatigue" Problem

### The Pod Saturation
Within the local playgroup, the equipment design space has become heavily saturated in Red-White (Boros) and its supersets:
* **LTO888:** Running *Lightning, Army of One* (Boros RW — extra attacks & equipment).
* **reimaru:** Running *Syr Gwyn, Hero of Ashvale* (Mardu WBR — Knight tribal equipment).
* **mjznoozer:** Running *Cloud, Ex-SOLDIER* (Naya RGW — Soldier equipment).
* **fowlplays (previous):** Ran *Bruenor Battlehammer* (*The Gate of Babylon* — Boros RW).

### The Boros Equipment Template
Most Boros and Boros-superset equipment lists collapse into an identical mechanical loop:
1. Tutor a signature weapon ([Colossus Hammer](https://scryfall.com/card/afc/202/colossus-hammer), [Sunforger](https://scryfall.com/card/cmr/473/sunforger), or Swords of X and Y).
2. Cheat equip costs using standard white/red cheat engines ([Puresteel Paladin](https://scryfall.com/card/cmm/51/puresteel-paladin), [Sigarda's Aid](https://scryfall.com/card/cmr/384/sigardas-aid), [Ardenn](https://scryfall.com/card/cmr/10/ardenn-intrepid-archaeologist), [Bruenor](https://scryfall.com/card/afr/219/bruenor-battlehammer)).
3. Swing a tall double-striking beatstick or take extra combats.

### The Objective
Design a fresh equipment deck that:
1. **Breaks the color mold:** Retains at most one of the two Boros colors (settling firmly on **White**) and completely cuts **Red**.
2. **Avoids Boros supersets:** No Naya, Mardu, Jeskai, 4-color, or 5-color hulls.
3. **Pivots the gameplay axis:** Instead of aggressive extra combats and hasty alpha strikes, build around **tactical combat control, free simultaneous equipment attachment, and resilient defense**.

---

## 2. Commander Selection: Beatrix, Loyal General

```
Beatrix, Loyal General
{4}{W}{W}
Legendary Creature — Human Soldier
4/4
Vigilance
At the beginning of combat on your turn, you may attach any number of Equipment you control to target creature you control.
```

### Why Beatrix Changes the Equation
1. **Free Simultaneous Attachment:** Unlike Bruenor Battlehammer (who cheats *one* equip cost of {0} per turn), Beatrix attaches **every piece of equipment on your board simultaneously** to target creature for {0} mana at the start of combat. 
2. **Breaks High-Equip Artillery:** Weapons with crippling equip costs (e.g., [Ultima Weapon](https://scryfall.com/card/fic/159/ultima-weapon) {7}, [Colossus Hammer](https://scryfall.com/card/afc/202/colossus-hammer) {8}, [Aettir and Priwen](https://scryfall.com/card/fic/142/aettir-and-priwen) {5}, [Wrecking Ball Arm](https://scryfall.com/card/fic/161/wrecking-ball-arm) {7}) become immediate zero-mana payloads.
3. **Flexibility on Targets:** Beatrix does not have to target herself. She can equip [Adelbert Steiner](https://scryfall.com/card/fic/1/adelbert-steiner) to gain 30+ life via lifelink, an unblockable token, or a protected squire.
4. **Natural Vigilance & Defense:** A 4/4 vigilant body allows Beatrix to swing for lethal commander damage while remaining untapped to block opposing commanders (Lightning, Syr Gwyn, Cloud).
5. **Thematic Vibe:** Fits the Alexandria knight flavor from *Final Fantasy IX* (Beatrix + Steiner leading the charge), mirroring the pod's Universes Beyond theme.

---

## 3. Card Sourcing & Salvage Architecture

The decklist is constructed primarily from cards already owned across:
1. **The Salvage of *The Gate of Babylon* (Bruenor Battlehammer):**
   * Retained all premier white creatures ([Puresteel Paladin](https://scryfall.com/card/cmm/51/puresteel-paladin), [Cloud, Midgar Mercenary](https://scryfall.com/card/fic/14/cloud-midgar-mercenary), [Danitha Capashen, Paragon](https://scryfall.com/card/cmm/23/danitha-capashen-paragon), [Cid, Freeflier Pilot](https://scryfall.com/card/fic/13/cid-freeflier-pilot), [Ashe, Princess of Dalmasca](https://scryfall.com/card/fic/4/ashe-princess-of-dalmasca), [Zack Fair](https://scryfall.com/card/fic/38/zack-fair), [Skyclave Apparition](https://scryfall.com/card/znr/39/skyclave-apparition), [Tithe Taker](https://scryfall.com/card/rna/27/tithe-taker)).
   * Retained core colorless and white equipment ([Colossus Hammer](https://scryfall.com/card/afc/202/colossus-hammer), [Ultima Weapon](https://scryfall.com/card/fic/159/ultima-weapon), [Genji Glove](https://scryfall.com/card/fic/149/genji-glove), [Buster Sword](https://scryfall.com/card/fic/144/buster-sword), [Aettir and Priwen](https://scryfall.com/card/fic/142/aettir-and-priwen), [Leyline Axe](https://scryfall.com/card/fic/151/leyline-axe), [Sword of Vengeance](https://scryfall.com/card/c17/228/sword-of-vengeance), [Brotherhood Regalia](https://scryfall.com/card/acr/71/brotherhood-regalia), [Darksteel Plate](https://scryfall.com/card/2xm/251/darksteel-plate), [Kusari-Gama](https://scryfall.com/card/chk/260/kusari-gama), [Quietus Spike](https://scryfall.com/card/ncc/377/quietus-spike), [Umezawa's Jitte](https://scryfall.com/card/bok/163/umezawas-jitte), [Sword of the Animist](https://scryfall.com/card/cmm/413/sword-of-the-animist), [Crystal Fragments](https://scryfall.com/card/fic/147/crystal-fragments-summon-alexander)).
   * Retained white interaction & enchantments ([Sigarda's Aid](https://scryfall.com/card/cmr/384/sigardas-aid), [Reconnaissance](https://scryfall.com/card/dom/26/reconnaissance), [Clever Concealment](https://scryfall.com/card/onc/5/clever-concealment), [Swords to Plowshares](https://scryfall.com/card/mkc/88/swords-to-plowshares), [Dispatch](https://scryfall.com/card/nec/83/dispatch), [Bovine Intervention](https://scryfall.com/card/otj/6/bovine-intervention), [Ultimate Magic: Holy](https://scryfall.com/card/fic/35/ultimate-magic-holy), [Unfinished Business](https://scryfall.com/card/onc/27/unfinished-business), [Austere Command](https://scryfall.com/card/mkc/56/austere-command)).
   * Retained high-utility ramp artifacts: [White Auracite](https://scryfall.com/card/fic/160/white-auracite), [Inspiring Statuary](https://scryfall.com/card/mkc/230/inspiring-statuary), [Arcane Signet](https://scryfall.com/card/otc/252/arcane-signet), [Sol Ring](https://scryfall.com/card/pip/234/sol-ring).
2. **Final Fantasy Set Pulls:**
   * **[Beatrix, Loyal General](https://scryfall.com/card/fic/12/beatrix-loyal-general)** (Commander)
   * **[Adelbert Steiner](https://scryfall.com/card/fic/1/adelbert-steiner)** (Primary lieutenant / lifelink beatstick)
   * **[Elena, Turk Recruit](https://scryfall.com/card/fic/20/elena-turk-recruit)** (Historic recursion & counter scaling)
3. **Player Collection & Binders:**
   * **[Bastion Protector](https://scryfall.com/card/c20/80/bastion-protector)** (Commander +2/+2 and Indestructible)
   * **[Archaeomancer's Map](https://scryfall.com/card/c21/12/archaeomancers-map)** (Plains tutoring and catch-up ramp)
   * **[Knight of the White Orchid](https://scryfall.com/card/moc/193/knight-of-the-white-orchid)** (Plains ramp body)
   * **[Fomori Vault](https://scryfall.com/card/big/29/fomori-vault)** (Instant-speed impulse card selection on a land)
   * **[Swiftfoot Boots](https://scryfall.com/card/otc/268/swiftfoot-boots)** (Haste and hexproof)
4. **Secrets of Strixhaven (SOS / SOC / SOA) Synergies:**
   * **[Bitterthorn, Nissa's Animus](https://scryfall.com/card/moc/45/bitterthorn-nissas-animus)** (Living Weapon ramp)
   * **[Tocasia's Welcome](https://scryfall.com/card/soc/29/tocasias-welcome)** (Steady draw on low-mana creature / token entry)
   * **[Mangara, the Diplomat](https://scryfall.com/card/soc/18/mangara-the-diplomat)** & **[Teshar, Ancestor's Apostle](https://scryfall.com/card/soc/28/teshar-ancestors-apostle)** (Card draw & historic reanimation)
   * **[Akroma's Will](https://scryfall.com/card/soa/1/akromas-will)** & **[Reprieve](https://scryfall.com/card/soa/10/reprieve)** (Lethal finisher & tempo counter)
   * **[War Room](https://scryfall.com/card/soc/53/war-room)** & **[Emeria, the Sky Ruin](https://scryfall.com/card/soc/40/emeria-the-sky-ruin)** (Repeatable card draw & late-game reanimation on lands)

---

## 4. Solving the Three Mono-White Bottlenecks

### Bottleneck A: The 6-Mana Ramp Curve
A 6-mana commander in Mono-White cannot wait until turn 6. The deck runs an aggressive suite of 12 ramp and cost-reduction pieces:
* **The Weapon Rampers:** [Sword of the Animist](https://scryfall.com/card/cmm/413/sword-of-the-animist) and [Bitterthorn, Nissa's Animus](https://scryfall.com/card/moc/45/bitterthorn-nissas-animus) trigger on combat to pull basic Plains straight to the board.
* **Catch-up Land Acceleration:** [Archaeomancer's Map](https://scryfall.com/card/c21/12/archaeomancers-map) and [Knight of the White Orchid](https://scryfall.com/card/moc/193/knight-of-the-white-orchid).
* **Rocks & Cost Reducers:** [Sol Ring](https://scryfall.com/card/pip/234/sol-ring), [Arcane Signet](https://scryfall.com/card/otc/252/arcane-signet), [Mind Stone](https://scryfall.com/card/mkc/232/mind-stone), [Thought Vessel](https://scryfall.com/card/mkc/245/thought-vessel), [Danitha Capashen, Paragon](https://scryfall.com/card/cmm/23/danitha-capashen-paragon), and [Cid, Freeflier Pilot](https://scryfall.com/card/fic/13/cid-freeflier-pilot).
* **The Secret MVP — [Inspiring Statuary](https://scryfall.com/card/mkc/230/inspiring-statuary):** Equipment does not need to be untapped to grant abilities. With 3–4 equipment in play, Inspiring Statuary allows you to tap your weapons to improvise Beatrix onto the board as early as Turn 4!
* **Dual-Duty [White Auracite](https://scryfall.com/card/fic/160/white-auracite):** Serves as an untapped mana rock while temporarily exiling the most dangerous threat at the table.

### Bottleneck B: Card Velocity Without Sram / Esper Sentinel
Rather than relying on expensive staples not in the collection, card advantage is distributed across multiple engines:
* **[Puresteel Paladin](https://scryfall.com/card/cmm/51/puresteel-paladin):** Draws on every equipment cast; provides backup {0} equip metalcraft.
* **[Cloud, Midgar Mercenary](https://scryfall.com/card/fic/14/cloud-midgar-mercenary):** Tutors equipment on ETB; doubles all equipment triggers (doubles Buster Sword, Animist, Bitterthorn, Ultima Weapon!).
* **[Ashe, Princess of Dalmasca](https://scryfall.com/card/fic/4/ashe-princess-of-dalmasca):** Attacks to dig 5 cards deep for an artifact.
* **[Buster Sword](https://scryfall.com/card/fic/144/buster-sword):** On combat damage, draws a card and free-casts a spell with mana value $\le$ damage dealt.
* **[Fomori Vault](https://scryfall.com/card/big/29/fomori-vault):** Instant-speed impulse digging on a land, scaling directly with equipment count.
* **[War Room](https://scryfall.com/card/soc/53/war-room):** Tap, pay 1 life, draw a card.
* **[Tocasia's Welcome](https://scryfall.com/card/soc/29/tocasias-welcome)** & **[Secret Rendezvous](https://scryfall.com/card/stx/26/secret-rendezvous):** Reliable burst and turn-by-turn card draw.

### Bottleneck C: Protecting the Investment
High-equip targets invite spot removal. The deck runs comprehensive layers of defense:
* **Passive Protection:** [Bastion Protector](https://scryfall.com/card/c20/80/bastion-protector) (passive indestructible), [Darksteel Plate](https://scryfall.com/card/2xm/251/darksteel-plate), [Swiftfoot Boots](https://scryfall.com/card/otc/268/swiftfoot-boots) (hexproof/haste), and [Brotherhood Regalia](https://scryfall.com/card/acr/71/brotherhood-regalia) (unblockable + Ward {2}).
* **Selfless Bodyguards:** [Zack Fair](https://scryfall.com/card/fic/38/zack-fair) sacrifices for {1} to give indestructible and transfer equipment/counters.
* **Instant Board Shields:** [Ultimate Magic: Holy](https://scryfall.com/card/fic/35/ultimate-magic-holy) (team indestructible + damage prevention), [Clever Concealment](https://scryfall.com/card/onc/5/clever-concealment) (convoke phasing out against Farewell/Rift), and [Make a Stand](https://scryfall.com/card/cmr/32/make-a-stand).
* **Recursion:** [Unfinished Business](https://scryfall.com/card/onc/27/unfinished-business) returns Beatrix with two heavy weapons attached; [Elena, Turk Recruit](https://scryfall.com/card/fic/20/elena-turk-recruit), [Cid, Freeflier Pilot](https://scryfall.com/card/fic/13/cid-freeflier-pilot), and [Sevinne's Reclamation](https://scryfall.com/card/soc/23/sevinnes-reclamation) recover lost artifacts.
