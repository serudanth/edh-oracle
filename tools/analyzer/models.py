"""Data models and type definitions for the EDH Oracle deck analyzer."""

from dataclasses import dataclass, field
import pathlib
from typing import Any, Dict, List, Optional, Set


@dataclass
class CardEntry:
    """Represents a single card entry in a decklist."""
    name: str
    qty: int = 1
    user_category: str = "Other"
    data: Optional[Dict[str, Any]] = None


@dataclass
class DeckInfo:
    """Represents an ingested decklist and its metadata."""
    deck_name: str
    owner: str
    commander: str
    source_url: str = ""
    status: str = "complete"
    cards: List[CardEntry] = field(default_factory=list)
    filepath: Optional[pathlib.Path] = None

    @property
    def card_names(self) -> Set[str]:
        return {c.name for c in self.cards}

    @property
    def total_cards(self) -> int:
        return sum(c.qty for c in self.cards)


@dataclass
class CurveMetrics:
    """Mana curve and velocity metrics."""
    avg_cmc: float
    effective_avg_cmc: Optional[float]
    x_spell_count: int
    total_non_lands: int
    land_count: int
    cmc_le_2_count: int
    cmc_distribution: Dict[int, int] = field(default_factory=dict)


@dataclass
class StaplesMetrics:
    """Format staples, game-changers, and mechanical role counters."""
    game_changers_found: List[str] = field(default_factory=list)
    stax_pieces_found: List[str] = field(default_factory=list)
    fast_mana_found: List[str] = field(default_factory=list)
    tutor_count: int = 0
    repeatable_draw_count: int = 0
    interaction_count: int = 0
    instant_interaction_count: int = 0
    ramp_count: int = 0
    protection_count: int = 0
    recursion_count: int = 0
    cheat_engine_count: int = 0


@dataclass
class ComboMetrics:
    """Infinite and deterministic combo detection results."""
    combo_count: int = 0
    combo_lines: List[str] = field(default_factory=list)


@dataclass
class ArchetypeResult:
    """Classified piloting archetype and associated strategic weights."""
    primary_archetype: str
    weights: Dict[str, float] = field(default_factory=dict)

    @property
    def archetype(self) -> str:
        return self.primary_archetype


@dataclass
class SubPillars:
    """The seven quantifiable sub-pillar dimension scores (0.0 - 100.0)."""
    velocity: float
    engine: float
    interaction: float
    resource: float
    resilience: float
    closing: float
    mana: float


@dataclass
class BracketResult:
    """Official 5-Bracket format classification (Bracket 1 - 5)."""
    bracket: int
    label: str
    explanation: str


@dataclass
class StrategicAudit:
    """Semantic / LLM contextual inference results."""
    true_archetype: Optional[str] = None
    synergy_coherence: Optional[float] = None
    anti_synergies: List[str] = field(default_factory=list)
    emergent_locks: List[str] = field(default_factory=list)
    calibration_delta: float = 0.0
    notes: List[str] = field(default_factory=list)


@dataclass
class DeckAnalysisResult:
    """Composite analysis report for a deck."""
    deck_name: str
    commander: str
    deck_url: str
    power_score: float
    bracket: BracketResult
    archetype: ArchetypeResult
    curve: CurveMetrics
    staples: StaplesMetrics
    combos: ComboMetrics
    pillars: SubPillars
    strategic: Optional[StrategicAudit] = None
    analysis_time: str = ""
