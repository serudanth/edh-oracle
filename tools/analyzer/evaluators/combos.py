"""Combo detection evaluator."""

from typing import List, Set
from ..models import ComboMetrics, DeckInfo
from ..constants import STAPLE_COMBOS


class ComboEvaluator:
    """Detects verified infinite combos from cards and commander."""

    @staticmethod
    def evaluate(deck: DeckInfo) -> ComboMetrics:
        all_cards: Set[str] = deck.card_names.copy()
        for cmd in deck.commander.split("//"):
            all_cards.add(cmd.strip())

        found_combos: List[str] = []
        for combo_set, desc in STAPLE_COMBOS:
            if combo_set.issubset(all_cards):
                found_combos.append(desc)

        return ComboMetrics(
            combo_count=len(found_combos),
            combo_lines=found_combos
        )
