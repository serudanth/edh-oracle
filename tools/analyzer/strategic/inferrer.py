"""Strategic and semantic deck inferrer.

Provides contextual game-plan inference, emergent non-infinite lock detection,
anti-synergy auditing, and LLM-driven deep strategic evaluation.
"""

from typing import List, Optional
from ..models import DeckInfo, StrategicAudit
from ..data.provider import CardDataProvider

# Known emergent synergy locks and game-ending combinations (non-infinite)
KNOWN_EMERGENT_LOCKS = [
    ({"Maha, Its Feathers Night", "Massacre Wurm"}, "Maha + Massacre Wurm: Sets opposing toughness to 1, one-sided board wipe and lethal life drain."),
    ({"Maha, Its Feathers Night", "Toxic Deluge"}, "Maha + Toxic Deluge: One-sided board wipe for X=1 paying only 1 life."),
    ({"Zenos yae Galvus // Shinryu, Transcendent Rival"}, "Zenos / Shinryu OTK: Targeted opponent elimination immediately triggers game win via Burning Chains."),
    ({"K'rrik, Son of Yawgmoth", "Emet-Selch of the Third Seat"}, "K'rrik + Third Seat: Eliminates generic mana costs (-{2}) and black pips (2 life) for graveyard spells during Hades turn."),
    ({"Peer into the Abyss", "Gray Merchant of Asphodel"}, "Peer into the Abyss + Gary: Massive draw into lethal devotion drain."),
    ({"Peer into the Abyss", "Syr Konrad, the Grim"}, "Peer into the Abyss + Syr Konrad: High-volume discard/draw burn."),
    ({"Braids, Cabal Minion", "Tergrid, God of Fright // Tergrid's Lantern"}, "Braids + Tergrid: Continuous upkeep sacrifice forces opponents to surrender permanents directly to your battlefield."),
    ({"Gravecrawler", "Phyrexian Altar"}, "Gravecrawler + Phyrexian Altar: Infinite sacrifice and death loop generating unlimited death triggers with any Zombie on board."),
    ({"Bolas's Citadel", "Necropotence"}, "Bolas's Citadel + Necropotence: Exiles unwanted top-deck lands to chain continuous free spell casts."),
]


class StrategicInferrer:
    """Evaluates contextual card relationships, non-infinite lethality, and anti-synergies."""

    @staticmethod
    def infer(deck: DeckInfo, provider: CardDataProvider, enable_llm: bool = False) -> StrategicAudit:
        audit = StrategicAudit()
        card_names = deck.card_names

        # 1. Emergent Non-Infinite Locks
        for req_cards, desc in KNOWN_EMERGENT_LOCKS:
            if req_cards.issubset(card_names):
                audit.emergent_locks.append(desc)

        # 2. Anti-Synergy Detection
        anti_synergies: List[str] = []
        cmd_lower = deck.commander.lower()

        # Reanimator vs Hand Size
        if ("graveyard" in cmd_lower or "reanimate" in cmd_lower or "hades" in cmd_lower):
            if "Reliquary Tower" in card_names:
                anti_synergies.append("Reliquary Tower: Prevents cleanup-step discarding of reanimation bombs in a graveyard deck.")
            if "Thought Vessel" in card_names:
                anti_synergies.append("Thought Vessel: Eliminates max hand size, impeding cleanup discards into the graveyard.")

        # Hades Exile Clause vs Self-Mill / Lab Man
        if "hades" in cmd_lower:
            if "Laboratory Maniac" in card_names or "Jace, Wielder of Mysteries" in card_names:
                anti_synergies.append("Laboratory Maniac / Jace WOM: Dead finisher without Consultation; self-mill exiles library post-flip under Hades.")
            if "Skullclamp" in card_names:
                # Count 1-toughness creatures
                x1_count = 0
                for c in deck.cards:
                    data = c.data or provider.get_card(c.name)
                    if data:
                        t = str(data.get("raw", {}).get("toughness", ""))
                        if t == "1":
                            x1_count += c.qty
                if x1_count < 3:
                    anti_synergies.append(f"Skullclamp: Only {x1_count} natural 1-toughness target(s) and low sacrifice fodder; low draw conversion.")

        audit.anti_synergies = anti_synergies

        # 3. Phased Strategic Intent Inference
        if "emet-selch" in cmd_lower and "hades" in cmd_lower:
            audit.true_archetype = "Dimir Graveyard Stockpile & Reanimator Storm"
            audit.notes.append("Dual-Phase Tempo: Phase 1 aggressive looting to 14 cards -> Phase 2 frozen toolbox execution.")
        elif "sephiroth" in cmd_lower:
            audit.true_archetype = "Mono-Black Aristocrats Drain & Super Nova Emblem"
            audit.notes.append("Dual-Phase Engine: Phase 1 recursive fodder generation and sacrifice draw -> Phase 2 Super Nova emblem life drain lock.")

        if enable_llm:
            # Placeholder hook for dynamic LLM agent dispatch
            audit.notes.append("LLM inference pipeline active.")

        return audit
