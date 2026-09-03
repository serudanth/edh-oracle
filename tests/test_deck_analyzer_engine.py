import json
import pathlib
import sys
import tempfile
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import deck_analyzer_engine as dae


class TestDeckAnalyzerEngine(unittest.TestCase):
    def test_classify_piloting_archetype(self):
        types_spellslinger = {"Instant": 20, "Sorcery": 10, "Creature": 10}
        arch = dae.classify_piloting_archetype(
            commander_text="Feather, the Redeemed",
            card_types=types_spellslinger,
            user_cats=["Instant", "Sorcery"],
            cards_data=[],
        )
        self.assertEqual(arch, "Spellslinger / Storm")

        types_cheat = {"Creature": 30, "Land": 35}
        arch_cheat = dae.classify_piloting_archetype(
            commander_text="Winota, Joiner of Forces. Whenever a non-Human attacks, look at top 6 and put a Human onto battlefield.",
            card_types=types_cheat,
            user_cats=["Creature"],
            cards_data=[],
        )
        self.assertEqual(arch_cheat, "Cheat / Aggro Tempo")

    def test_detect_combos(self):
        commander = "Sephiroth, Fabled SOLDIER"
        cards = {"Sanguine Bond", "Exquisite Blood", "Sol Ring", "Swamp"}
        count, lines = dae.detect_combos(commander, cards)
        self.assertEqual(count, 1)
        self.assertIn("Sanguine Bond + Exquisite Blood", lines[0])

    def test_analyze_deck_structure(self):
        mock_deck_info = {
            "deck_name": "Sephiroth Pain is Love",
            "owner": "lto888",
            "commander": "Sephiroth, Fabled SOLDIER",
            "source_url": "https://archidekt.com/decks/13966160",
            "cards": [
                {"name": "Sol Ring", "qty": 1, "user_category": "Fast Mana"},
                {"name": "Demonic Tutor", "qty": 1, "user_category": "Tutor"},
                {"name": "Sanguine Bond", "qty": 1, "user_category": "Combo"},
                {"name": "Exquisite Blood", "qty": 1, "user_category": "Combo"},
                {"name": "Swamp", "qty": 34, "user_category": "Land"},
            ],
            "filepath": REPO_ROOT / "knowledgebase" / "podlist" / "lto888" / "decks" / "sephiroth-pain-is-love.md",
        }
        cache = {
            "Sol Ring": {"cmc": 1.0, "type_line": "Artifact", "oracle_text": "Tap: Add CC."},
            "Demonic Tutor": {"cmc": 2.0, "type_line": "Sorcery", "oracle_text": "Search your library for a card..."},
            "Sanguine Bond": {"cmc": 5.0, "type_line": "Enchantment", "oracle_text": "Whenever you gain life..."},
            "Exquisite Blood": {"cmc": 5.0, "type_line": "Enchantment", "oracle_text": "Whenever an opponent loses life..."},
            "Swamp": {"cmc": 0.0, "type_line": "Basic Land — Swamp", "oracle_text": ""},
        }

        res = dae.analyze_deck(mock_deck_info, cache)
        self.assertEqual(res["deck_name"], "Sephiroth Pain is Love")
        self.assertEqual(res["commander"], "Sephiroth, Fabled SOLDIER")

        source = res["sources"][0]
        self.assertEqual(source["source"], "EDHOracleLocalEngine")
        self.assertEqual(source["status"], "success")

        metrics = source["metrics"]
        self.assertEqual(metrics["fast_mana_count"], 1)
        self.assertEqual(metrics["tutor_count"], 1)
        self.assertEqual(metrics["combo_count"], 1)
        self.assertGreaterEqual(metrics["power_score"], 1.0)
        self.assertLessEqual(metrics["power_score"], 10.0)

    def test_write_analysis_to_kb(self):
        deck_path = REPO_ROOT / "knowledgebase" / "podlist" / "fowlplays" / "decks" / "the-best-of-friends.md"
        mock_data = {"deck_name": "The Best of Friends", "sources": []}
        out_path = dae.write_analysis_to_kb(deck_path, mock_data)

        self.assertTrue(out_path.exists())
        self.assertEqual(out_path.parent.name, "analysis")
        self.assertEqual(out_path.name, "the-best-of-friends.json")


if __name__ == "__main__":
    unittest.main()
