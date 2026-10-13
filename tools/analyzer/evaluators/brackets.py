"""Official Commander Format Panel (CFP) 5-Bracket determination."""

from ..models import BracketResult, ComboMetrics, StaplesMetrics
from ..constants import BRACKET_DEFINITIONS


class BracketResolver:
    """Resolves the deck's official 5-Bracket format classification (Bracket 1 - 5)."""

    @staticmethod
    def resolve(
        power_score: float,
        staples: StaplesMetrics,
        combos: ComboMetrics,
    ) -> BracketResult:
        game_changers_count = len(staples.game_changers_found)
        stax_count = len(staples.stax_pieces_found)
        fast_mana_count = len(staples.fast_mana_found)
        tutor_count = staples.tutor_count
        combo_count = combos.combo_count

        # -------------------------------------------------------------
        # Bracket 5 (cEDH / Tournament Competitive)
        # -------------------------------------------------------------
        # High power (>= 8.5) with dense fast mana, tutors, or competitive combo lines
        is_bracket_5 = (
            (power_score >= 8.5 and (fast_mana_count >= 3 or combo_count >= 1 or game_changers_count >= 5))
            or (combo_count >= 1 and fast_mana_count >= 2 and tutor_count >= 2)
            or (combo_count >= 1 and stax_count >= 2 and power_score >= 8.0)
            or (game_changers_count >= 6 and power_score >= 8.0)
        )

        if is_bracket_5:
            b_def = BRACKET_DEFINITIONS[5]
            explanation = "cEDH tier: Meets tournament speed, hyper-dense fast mana/tutors, or competitive combo lock requirements."
            return BracketResult(bracket=5, label=b_def["label"], explanation=explanation)

        # -------------------------------------------------------------
        # Bracket 4 (Optimized / High-Power Casual)
        # -------------------------------------------------------------
        # CFP rule: 4+ Game Changers exceeds Bracket 3 cap of 3.
        # Alternatively, composite power >= 7.0 or high-power combo/stax integration.
        is_bracket_4 = (
            game_changers_count >= 4
            or power_score >= 7.0
            or (combo_count >= 1 and (fast_mana_count >= 1 or tutor_count >= 1))
            or (stax_count >= 2 and power_score >= 6.5)
        )

        if is_bracket_4:
            b_def = BRACKET_DEFINITIONS[4]
            reasons = []
            if game_changers_count >= 4:
                reasons.append(f"{game_changers_count} Game Changers (exceeds Bracket 3 cap of 3)")
            if power_score >= 7.0:
                reasons.append(f"Power score {power_score} >= 7.0")
            if combo_count >= 1:
                reasons.append("Infinite combo with active acceleration/tutors")
            if stax_count >= 2:
                reasons.append(f"{stax_count} Hard Stax pieces")

            explanation = f"Optimized High-Power Casual: {'; '.join(reasons)}."
            return BracketResult(bracket=4, label=b_def["label"], explanation=explanation)

        # -------------------------------------------------------------
        # Bracket 3 (Upgraded / Tuned Casual)
        # -------------------------------------------------------------
        # Permitted up to 3 Game Changers. Power score 5.5 - 6.9.
        is_bracket_3 = (
            (1 <= game_changers_count <= 3)
            or power_score >= 5.5
            or fast_mana_count >= 1
            or tutor_count >= 1
        )

        if is_bracket_3:
            b_def = BRACKET_DEFINITIONS[3]
            explanation = f"Upgraded Casual: Tuned synergy engine (Power {power_score}), {game_changers_count} Game Changer(s) (within <= 3 cap)."
            return BracketResult(bracket=3, label=b_def["label"], explanation=explanation)

        # -------------------------------------------------------------
        # Bracket 2 (Core / Precon Casual)
        # -------------------------------------------------------------
        if power_score >= 3.5:
            b_def = BRACKET_DEFINITIONS[2]
            explanation = f"Core Casual: Standard casual/precon performance (Power {power_score}), zero Game Changers, zero infinite combos."
            return BracketResult(bracket=2, label=b_def["label"], explanation=explanation)

        # -------------------------------------------------------------
        # Bracket 1 (Exhibition / Ultra-Casual / Theme)
        # -------------------------------------------------------------
        b_def = BRACKET_DEFINITIONS[1]
        explanation = f"Exhibition: Artistic, narrative, or low-synergy theme build (Power {power_score})."
        return BracketResult(bracket=1, label=b_def["label"], explanation=explanation)
