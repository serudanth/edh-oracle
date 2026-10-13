"""Sub-pillar calculations and composite power scoring."""

from typing import Tuple
from ..models import (
    ArchetypeResult,
    ComboMetrics,
    CurveMetrics,
    DeckInfo,
    StaplesMetrics,
    SubPillars,
)
from ..data.provider import CardDataProvider


class PillarEvaluator:
    """Calculates quantifiable sub-pillar scores (0-100) and composite power score (1.0-10.0)."""

    @staticmethod
    def evaluate(
        deck: DeckInfo,
        curve: CurveMetrics,
        staples: StaplesMetrics,
        combos: ComboMetrics,
        archetype: ArchetypeResult,
        provider: CardDataProvider,
    ) -> Tuple[SubPillars, float]:
        weights = archetype.weights

        commander_oracle = ""
        for cmd_name in deck.commander.split("//"):
            cmd_data = provider.get_card(cmd_name.strip())
            if cmd_data:
                commander_oracle += " " + cmd_data.get("oracle_text", "")

        stax_count = len(staples.stax_pieces_found)
        fast_mana_count = len(staples.fast_mana_found)
        tutor_count = staples.tutor_count
        repeatable_draw_count = staples.repeatable_draw_count

        eval_cmc = curve.effective_avg_cmc if curve.effective_avg_cmc is not None else curve.avg_cmc
        cmc_le_2_ratio = curve.cmc_le_2_count / max(1, curve.total_non_lands)

        # 1. Velocity (0 - 100)
        s_velocity = min(100.0, max(0.0, 120.0 - 30.0 * (eval_cmc - 1.5) + 40.0 * cmc_le_2_ratio))

        # 2. Engine (0 - 100)
        s_engine = min(100.0, 12.0 * repeatable_draw_count + 6.0 * min(10, len(deck.cards) // 5))

        # 3. Interaction (0 - 100)
        s_interaction = min(100.0, 8.0 * (staples.interaction_count + staples.instant_interaction_count) + 12.0 * stax_count)

        # 4. Resource Acceleration (0 - 100)
        s_resource = min(100.0, 6.0 * staples.ramp_count + 20.0 * fast_mana_count + 18.0 * staples.cheat_engine_count)

        # 5. Resilience (0 - 100)
        has_emblem = "emblem" in commander_oracle.lower()
        s_resilience = min(100.0, 12.0 * staples.protection_count + 10.0 * staples.recursion_count + (25.0 if has_emblem else 0.0))

        # 6. Closing Vector (0 - 100)
        has_win_clause = "win" in commander_oracle.lower()
        s_closing = min(100.0, 25.0 * combos.combo_count + 12.0 * tutor_count + 10.0 * stax_count + (25.0 if has_emblem else 0.0) + (15.0 if has_win_clause else 5.0))

        # 7. Mana Base (0 - 100)
        s_mana = min(100.0, 85.0)

        # Composite Score Calculation
        raw_composite = (
            weights.get("w_vel", 0.15) * s_velocity +
            weights.get("w_eng", 0.20) * s_engine +
            weights.get("w_int", 0.15) * s_interaction +
            weights.get("w_res", 0.15) * s_resource +
            weights.get("w_resi", 0.10) * s_resilience +
            weights.get("w_clos", 0.15) * s_closing +
            weights.get("w_mana", 0.10) * s_mana
        ) / 10.0

        power_score = round(min(10.0, max(1.0, raw_composite)), 1)

        pillars = SubPillars(
            velocity=round(s_velocity, 1),
            engine=round(s_engine, 1),
            interaction=round(s_interaction, 1),
            resource=round(s_resource, 1),
            resilience=round(s_resilience, 1),
            closing=round(s_closing, 1),
            mana=round(s_mana, 1),
        )

        return pillars, power_score
