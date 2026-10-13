"""Orchestrator pipeline for modular deck analysis."""

import datetime
import pathlib
from typing import Any, Dict, Optional

from .data.provider import CardDataProvider
from .evaluators.archetype import ArchetypeClassifier
from .evaluators.brackets import BracketResolver
from .evaluators.combos import ComboEvaluator
from .evaluators.curve import CurveEvaluator
from .evaluators.pillars import PillarEvaluator
from .evaluators.staples import StaplesEvaluator
from .formatters.json_formatter import JSONFormatter
from .models import DeckAnalysisResult, DeckInfo
from .parsers.markdown import parse_deck_markdown
from .strategic.inferrer import StrategicInferrer


class DeckAnalyzer:
    """The main analysis engine pipeline orchestrator."""

    def __init__(self, provider: Optional[CardDataProvider] = None):
        self.provider = provider or CardDataProvider()

    def analyze_deck(self, deck: DeckInfo, enable_llm: bool = False) -> DeckAnalysisResult:
        """Executes full evaluation pipeline on a parsed DeckInfo."""
        # 1. Curve and Velocity
        curve = CurveEvaluator.evaluate(deck, self.provider)

        # 2. Staples, Roles, Fast Mana, Stax
        staples = StaplesEvaluator.evaluate(deck, self.provider)

        # 3. Combos
        combos = ComboEvaluator.evaluate(deck)

        # 4. Archetype & Strategic Weighting
        archetype = ArchetypeClassifier.classify(deck, self.provider, x_spell_count=curve.x_spell_count)

        # 5. Sub-Pillar Metric Calculation & Composite Power Score
        pillars, power_score = PillarEvaluator.evaluate(deck, curve, staples, combos, archetype, self.provider)

        # 6. Strategic / Contextual Inference
        strategic = StrategicInferrer.infer(deck, self.provider, enable_llm=enable_llm)

        # 7. Official 5-Bracket Determination
        bracket = BracketResolver.resolve(power_score, staples, combos)

        now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        return DeckAnalysisResult(
            deck_name=deck.deck_name,
            commander=deck.commander,
            deck_url=deck.source_url,
            power_score=power_score,
            bracket=bracket,
            archetype=archetype,
            curve=curve,
            staples=staples,
            combos=combos,
            pillars=pillars,
            strategic=strategic,
            analysis_time=now_str,
        )

    def analyze_file(self, filepath: pathlib.Path, enable_llm: bool = False) -> DeckAnalysisResult:
        """Parses a markdown decklist file and runs the analysis pipeline."""
        deck = parse_deck_markdown(filepath)
        return self.analyze_deck(deck, enable_llm=enable_llm)

    def format_json(self, result: DeckAnalysisResult) -> Dict[str, Any]:
        """Converts DeckAnalysisResult to standardized JSON schema."""
        return JSONFormatter.format(result)
