"""Curve and velocity evaluator."""

from typing import Dict
from ..models import CurveMetrics, DeckInfo
from ..data.provider import CardDataProvider


class CurveEvaluator:
    """Calculates Average Mana Value (AMV), X-spell effective curve, and CMC distributions."""

    @staticmethod
    def evaluate(deck: DeckInfo, provider: CardDataProvider) -> CurveMetrics:
        total_non_lands = 0
        total_cmc = 0.0
        total_eff_cmc = 0.0
        cmc_le_2 = 0
        land_count = 0
        x_spell_count = 0
        cmc_distribution: Dict[int, int] = {}

        for card in deck.cards:
            qty = card.qty
            data = card.data or provider.get_card(card.name)
            card.data = data

            if not data:
                # If card not found in DB/cache, check user category
                if "land" in card.user_category.lower():
                    land_count += qty
                else:
                    total_non_lands += qty
                    total_cmc += 3.0 * qty
                    total_eff_cmc += 3.0 * qty
                continue

            type_line = data.get("type_line", "")
            mana_cost = data.get("mana_cost", "") or ""
            cmc = float(data.get("cmc", 0.0))

            if "Land" in type_line or "land" in card.user_category.lower():
                land_count += qty
                continue

            x_count = mana_cost.count("{X}")
            if x_count > 0:
                x_spell_count += qty

            eff_cmc = cmc + (x_count * 2.5 if x_count > 0 else 0.0)

            total_non_lands += qty
            total_cmc += cmc * qty
            total_eff_cmc += eff_cmc * qty

            if eff_cmc <= 2.0:
                cmc_le_2 += qty

            bucket = min(10, max(0, int(round(cmc))))
            cmc_distribution[bucket] = cmc_distribution.get(bucket, 0) + qty

        avg_cmc = (total_cmc / total_non_lands) if total_non_lands > 0 else 3.0
        avg_eff_cmc = (total_eff_cmc / total_non_lands) if total_non_lands > 0 else 3.0

        return CurveMetrics(
            avg_cmc=avg_cmc,
            effective_avg_cmc=avg_eff_cmc if x_spell_count >= 8 else None,
            x_spell_count=x_spell_count,
            total_non_lands=total_non_lands,
            land_count=land_count,
            cmc_le_2_count=cmc_le_2,
            cmc_distribution=cmc_distribution,
        )
