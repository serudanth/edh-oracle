"""EDH Oracle Modular Deck Analyzer Package.

A modular, extensible evaluation pipeline for Commander / EDH decks combining
deterministic rules/curve math, 5-bracket format auditing, and strategic inference.
"""

from .models import (
    CardEntry,
    DeckInfo,
    DeckAnalysisResult,
    CurveMetrics,
    StaplesMetrics,
    SubPillars,
    BracketResult,
)
from .pipeline import DeckAnalyzer

__all__ = [
    "DeckAnalyzer",
    "CardEntry",
    "DeckInfo",
    "DeckAnalysisResult",
    "CurveMetrics",
    "StaplesMetrics",
    "SubPillars",
    "BracketResult",
]
