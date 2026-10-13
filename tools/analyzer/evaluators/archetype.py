"""Piloting archetype classifier and weight assignment."""

from typing import Dict
from ..models import ArchetypeResult, DeckInfo
from ..constants import ARCHETYPE_WEIGHTS
from ..data.provider import CardDataProvider


class ArchetypeClassifier:
    """Classifies primary piloting intent and assigns dynamic weighting matrix."""

    @staticmethod
    def classify(deck: DeckInfo, provider: CardDataProvider, x_spell_count: int = 0) -> ArchetypeResult:
        user_cats = [c.user_category for c in deck.cards]

        commander_oracle = ""
        for cmd_name in deck.commander.split("//"):
            cmd_data = provider.get_card(cmd_name.strip())
            if cmd_data:
                commander_oracle += " " + cmd_data.get("oracle_text", "")

        cmd_lower = (deck.commander + " " + commander_oracle).lower()

        card_types: Dict[str, int] = {}
        for card in deck.cards:
            data = card.data or provider.get_card(card.name)
            if data:
                type_line = data.get("type_line", "")
                for t in ["Creature", "Instant", "Sorcery", "Artifact", "Enchantment", "Planeswalker", "Land"]:
                    if t in type_line:
                        card_types[t] = card_types.get(t, 0) + card.qty

        instants_sorceries = card_types.get("Instant", 0) + card_types.get("Sorcery", 0)
        artifacts = card_types.get("Artifact", 0)

        archetype = "Midrange / Engine Value"

        # 1. Cheat / Aggro Tempo
        if "whenever" in cmd_lower and ("attack" in cmd_lower or "combat" in cmd_lower) and ("cheat" in cmd_lower or "put onto the battlefield" in cmd_lower or "without paying" in cmd_lower):
            archetype = "Cheat / Aggro Tempo"
        elif "winota" in cmd_lower or "kaalia" in cmd_lower or "kinnan" in cmd_lower:
            archetype = "Cheat / Aggro Tempo"

        # 2. Big Mana / Landfall
        elif x_spell_count >= 15 or "zimone" in cmd_lower or "x in its mana cost" in cmd_lower or "hydra" in cmd_lower:
            archetype = "Big Mana / Landfall"
        elif card_types.get("Land", 0) >= 42 or "landfall" in cmd_lower or "gladiolus" in cmd_lower or "omnath" in cmd_lower:
            archetype = "Big Mana / Landfall"

        # 3. Aristocrats / Sacrifice
        elif "sac" in cmd_lower or "dies" in cmd_lower or "death" in cmd_lower or "sephiroth" in cmd_lower or any("sac" in c.lower() for c in user_cats):
            archetype = "Aristocrats / Sacrifice"

        # 4. Spellslinger / Storm
        elif (instants_sorceries >= 28 and instants_sorceries > card_types.get("Creature", 0)) or "feather" in cmd_lower or "inalla" in cmd_lower or "stella lee" in cmd_lower:
            archetype = "Spellslinger / Storm"

        # 5. Voltron / Equipment
        elif "equipment" in cmd_lower or "aura" in cmd_lower or (artifacts >= 12 and any("equipment" in c.lower() for c in user_cats)):
            archetype = "Voltron / Equipment"

        # 6. Control / Stax
        elif card_types.get("Instant", 0) >= 15 and ("counter" in cmd_lower or "destroy" in cmd_lower or "y'shtola" in cmd_lower):
            archetype = "Control / Stax"

        weights = ARCHETYPE_WEIGHTS.get(archetype, ARCHETYPE_WEIGHTS["Midrange / Engine Value"])
        return ArchetypeResult(primary_archetype=archetype, weights=weights)
