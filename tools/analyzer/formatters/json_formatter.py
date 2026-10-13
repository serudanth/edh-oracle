"""Normalized JSON analysis schema formatter."""

from typing import Any, Dict
from ..models import DeckAnalysisResult


class JSONFormatter:
    """Formats DeckAnalysisResult into the standardized EDH Oracle JSON schema."""

    @staticmethod
    def format(result: DeckAnalysisResult) -> Dict[str, Any]:
        game_changers = result.staples.game_changers_found
        stax_pieces = result.staples.stax_pieces_found
        archetype_name = result.archetype.primary_archetype
        avg_cmc = result.curve.avg_cmc
        eff_cmc = result.curve.effective_avg_cmc
        x_spells = result.curve.x_spell_count

        strengths = [
            f"Game Changers: {len(game_changers)} ({', '.join(game_changers) if game_changers else 'None'})",
            *( [f"Stax / Lock pieces: {len(stax_pieces)} ({', '.join(stax_pieces)})"] if stax_pieces else [] ),
            f"Fast Mana acceleration: {len(result.staples.fast_mana_found)} source(s)",
            f"Tutor density: {result.staples.tutor_count} tutor(s)",
            f"Repeatable draw engines: {result.staples.repeatable_draw_count}"
        ]

        if result.strategic and result.strategic.emergent_locks:
            strengths.extend([f"Emergent Lock: {l}" for l in result.strategic.emergent_locks])

        weaknesses = [
            "Sensitive to targeted disruption if key engines are neutralized."
        ]
        if result.strategic and result.strategic.anti_synergies:
            weaknesses.extend(result.strategic.anti_synergies)

        summary_text = (
            f"{archetype_name} deck built around {result.commander}. Average CMC: {avg_cmc:.2f} (Effective: {eff_cmc:.2f} across {x_spells} X-spells)."
            if eff_cmc is not None else
            f"{archetype_name} deck built around {result.commander}. Average CMC: {avg_cmc:.2f}."
        )

        explanations = [
            f"Identified Piloting Archetype as '{archetype_name}'; applied adaptive strategic weighting profile.",
            result.bracket.explanation
        ]
        if result.strategic and result.strategic.notes:
            explanations.extend(result.strategic.notes)

        return {
            "deck_name": result.deck_name,
            "commander": result.commander,
            "sources": [
                {
                    "source": "EDHOracleLocalEngine",
                    "status": "success",
                    "error": None,
                    "metrics": {
                        "power_score": result.power_score,
                        "bracket": result.bracket.bracket,
                        "bracket_label": result.bracket.label,
                        "combo_score": round(result.pillars.closing / 10.0, 1),
                        "interaction_score": round(result.pillars.interaction / 10.0, 1),
                        "ramp_score": round(result.pillars.resource / 10.0, 1),
                        "consistency_score": round(result.pillars.engine / 10.0, 1),
                        "speed_score": round(result.pillars.velocity / 10.0, 1),
                        "tutor_count": result.staples.tutor_count,
                        "fast_mana_count": len(result.staples.fast_mana_found),
                        "combo_count": result.combos.combo_count,
                        "game_changers_count": len(game_changers),
                        "game_changers": game_changers,
                        "stax_count": len(stax_pieces),
                        "stax_pieces": stax_pieces,
                    },
                    "source_metrics": {
                        "piloting_archetype": archetype_name,
                        "average_cmc": f"{avg_cmc:.2f}",
                        "effective_average_cmc": f"{eff_cmc:.2f}" if eff_cmc is not None else None,
                        "x_spell_count": x_spells if x_spells > 0 else None,
                        "non_land_cards": result.curve.total_non_lands,
                        "land_cards": result.curve.land_count,
                    },
                    "text": {
                        "summary": summary_text,
                        "explanations": explanations,
                        "strengths": strengths,
                        "weaknesses": weaknesses,
                        "recommendations": [],
                        "suggested_changes": [],
                        "combo_lines": result.combos.combo_lines,
                        "mulligan_advice": [
                            "Keep hands with early mana acceleration and at least 2 lands."
                        ],
                    },
                    "raw_result": {
                        "engine_version": "2.0.0",
                        "sub_pillar_scores": {
                            "velocity": result.pillars.velocity,
                            "engine": result.pillars.engine,
                            "interaction": result.pillars.interaction,
                            "resource": result.pillars.resource,
                            "resilience": result.pillars.resilience,
                            "closing": result.pillars.closing,
                            "mana": result.pillars.mana,
                        },
                        "strategic_audit": {
                            "true_archetype": result.strategic.true_archetype if result.strategic else None,
                            "emergent_locks": result.strategic.emergent_locks if result.strategic else [],
                            "anti_synergies": result.strategic.anti_synergies if result.strategic else [],
                        } if result.strategic else None,
                    },
                }
            ],
            "metadata": {
                "deck_url": result.deck_url,
                "analysis_time": result.analysis_time,
                "successful_sources": ["EDHOracleLocalEngine"],
                "failed_sources": [],
            },
        }
