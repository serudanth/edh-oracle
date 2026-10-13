"""Staples, Game Changers, Hard Stax, and functional role evaluator."""

from typing import Set
from ..models import DeckInfo, StaplesMetrics
from ..constants import FAST_MANA_CARDS, GAME_CHANGERS, HARD_STAX_PIECES
from ..data.provider import CardDataProvider


class StaplesEvaluator:
    """Detects CFP Game Changers, Hard Stax, Fast Mana, and functional card roles."""

    @staticmethod
    def evaluate(deck: DeckInfo, provider: CardDataProvider) -> StaplesMetrics:
        metrics = StaplesMetrics()
        game_changers_found: Set[str] = set()
        stax_pieces_found: Set[str] = set()
        fast_mana_found: Set[str] = set()

        for card in deck.cards:
            name = card.name
            qty = card.qty
            cat = card.user_category.lower()
            data = card.data or provider.get_card(name)
            card.data = data

            front_name = name.split(" // ")[0].strip()

            # Format-defining checks
            if name in GAME_CHANGERS or front_name in GAME_CHANGERS:
                game_changers_found.add(name)
            if name in HARD_STAX_PIECES or front_name in HARD_STAX_PIECES:
                stax_pieces_found.add(name)
            if name in FAST_MANA_CARDS or front_name in FAST_MANA_CARDS:
                fast_mana_found.add(name)

            # User category source of truth
            if "ramp" in cat or "fast mana" in cat:
                metrics.ramp_count += qty
            if "draw" in cat or "card advantage" in cat:
                metrics.repeatable_draw_count += qty
            if "removal" in cat or "interaction" in cat or "counter" in cat:
                metrics.interaction_count += qty
            if "tutor" in cat:
                metrics.tutor_count += qty
            if "protection" in cat:
                metrics.protection_count += qty

            if not data:
                continue

            type_line = data.get("type_line", "")
            oracle = data.get("oracle_text", "").lower()

            # Fast mana fallback check
            if (name in FAST_MANA_CARDS or front_name in FAST_MANA_CARDS) and name not in fast_mana_found:
                fast_mana_found.add(name)

            # Ramp fallback when user categories are generic types
            if "ramp" not in cat and "fast mana" not in cat:
                if (
                    ("search your library for" in oracle and any(k in oracle for k in ["land", "forest", "plains", "island", "swamp", "mountain"]))
                    or ("land card" in oracle and "onto the battlefield" in oracle)
                    or (("add {" in oracle or "add one mana" in oracle or "add x mana" in oracle or "adds {" in oracle) and "land" not in type_line.lower())
                ):
                    metrics.ramp_count += qty

            # Oracle pattern checks
            if "search your library for" in oracle and "basic land" not in oracle:
                if "tutor" not in cat:
                    metrics.tutor_count += qty

            if ("whenever" in oracle or "at the beginning" in oracle) and "draw a card" in oracle:
                if "draw" not in cat and "card advantage" not in cat:
                    metrics.repeatable_draw_count += qty

            # Interaction fallback checks across all card types
            is_interaction = False
            if ("destroy target" in oracle or "exile target" in oracle or "destroy all" in oracle
                or "each opponent sacrifices" in oracle or "target opponent sacrifices" in oracle
                or "each player sacrifices" in oracle or "counter target" in oracle):
                is_interaction = True

            if "instant" in type_line.lower() and is_interaction:
                metrics.instant_interaction_count += qty

            if "removal" not in cat and "interaction" not in cat and "counter" not in cat:
                if is_interaction:
                    metrics.interaction_count += qty

            if "hexproof" in oracle or "indestructible" in oracle or "protection from" in oracle or "phase out" in oracle:
                if "protection" not in cat:
                    metrics.protection_count += qty

            if "return target" in oracle and ("graveyard" in oracle or "battlefield" in oracle):
                metrics.recursion_count += qty

            if "without paying its mana cost" in oracle or ("put" in oracle and "onto the battlefield" in oracle and "creature" in oracle):
                metrics.cheat_engine_count += qty

        metrics.game_changers_found = sorted(list(game_changers_found))
        metrics.stax_pieces_found = sorted(list(stax_pieces_found))
        metrics.fast_mana_found = sorted(list(fast_mana_found))

        return metrics
