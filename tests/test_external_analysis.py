import json
import pathlib
import sys
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import external_analysis_extract as eae


class TestExternalAnalysisExtract(unittest.TestCase):
    def test_schema_field_presence(self):
        entry = eae.create_source_entry("ScryCheck", status="success")
        self.assertEqual(entry["source"], "ScryCheck")
        self.assertEqual(entry["status"], "success")
        self.assertIsNone(entry["error"])

        # Metrics keys check
        metrics = entry["metrics"]
        for key in eae.STANDARD_METRICS:
            self.assertIn(key, metrics)
            self.assertIsNone(metrics[key])

        # Text keys check
        text = entry["text"]
        self.assertIn("summary", text)
        self.assertIsNone(text["summary"])
        for text_key in ["explanations", "strengths", "weaknesses", "recommendations", "suggested_changes", "combo_lines", "mulligan_advice"]:
            self.assertIn(text_key, text)
            self.assertEqual(text[text_key], [])

    def test_metric_and_text_population(self):
        metrics_input = {
            "power_score": 7.5,
            "bracket": "High",
            "combo_score": 3,
            "unknown_metric": "ignore_me",
        }
        text_input = {
            "summary": "Solid midrange deck",
            "strengths": ["Fast ramp", "Good interaction"],
            "weaknesses": "Board wipes",  # string converted to list
        }
        source_metrics_input = {"salt_score": 42}
        raw_result_input = {"raw_field_x": 123}

        entry = eae.create_source_entry(
            source_name="EDHCheck",
            status="partial",
            error="Missing cast_probability",
            metrics=metrics_input,
            source_metrics=source_metrics_input,
            text=text_input,
            raw_result=raw_result_input,
        )

        self.assertEqual(entry["status"], "partial")
        self.assertEqual(entry["error"], "Missing cast_probability")
        self.assertEqual(entry["metrics"]["power_score"], 7.5)
        self.assertEqual(entry["metrics"]["bracket"], "High")
        self.assertNotIn("unknown_metric", entry["metrics"])
        self.assertEqual(entry["source_metrics"], {"salt_score": 42})
        self.assertEqual(entry["text"]["summary"], "Solid midrange deck")
        self.assertEqual(entry["text"]["strengths"], ["Fast ramp", "Good interaction"])
        self.assertEqual(entry["text"]["weaknesses"], ["Board wipes"])
        self.assertEqual(entry["raw_result"], {"raw_field_x": 123})

    def test_normalize_extraction_request_defaults(self):
        req = {"deck_url": "https://archidekt.com/decks/123456", "requested_sources": None}
        out = eae.normalize_extraction_request(req)

        self.assertIn("deck_name", out)
        self.assertIn("commander", out)
        self.assertEqual(len(out["sources"]), 6)

        source_names = [s["source"] for s in out["sources"]]
        for expected in eae.SUPPORTED_SOURCES:
            self.assertIn(expected, source_names)

        metadata = out["metadata"]
        self.assertEqual(metadata["deck_url"], "https://archidekt.com/decks/123456")
        self.assertIn("analysis_time", metadata)
        self.assertIsInstance(metadata["successful_sources"], list)
        self.assertIsInstance(metadata["failed_sources"], list)

    def test_normalize_extraction_request_with_raw_sources(self):
        input_data = {
            "deck_url": "https://moxfield.com/decks/abcde",
            "requested_sources": ["RateMyDecks", "PowerDeckAI"],
            "deck_name": "Test Deck",
            "commander": "Atraxa, Praetors' Voice",
            "raw_sources": {
                "RateMyDecks": {
                    "status": "success",
                    "metrics": {"power_score": 8.0, "bracket": "cEDH"},
                    "text": {"recommendations": ["Add Sol Ring"]},
                },
                "PowerDeckAI": {
                    "status": "access_blocked",
                    "error": "HTTP 403 Forbidden",
                },
            },
        }

        out = eae.normalize_extraction_request(input_data)
        self.assertEqual(out["deck_name"], "Test Deck")
        self.assertEqual(out["commander"], "Atraxa, Praetors' Voice")
        self.assertEqual(len(out["sources"]), 2)

        rate_my_decks = next(s for s in out["sources"] if s["source"] == "RateMyDecks")
        self.assertEqual(rate_my_decks["status"], "success")
        self.assertEqual(rate_my_decks["metrics"]["power_score"], 8.0)
        self.assertEqual(rate_my_decks["text"]["recommendations"], ["Add Sol Ring"])

        power_deck_ai = next(s for s in out["sources"] if s["source"] == "PowerDeckAI")
        self.assertEqual(power_deck_ai["status"], "access_blocked")
        self.assertEqual(power_deck_ai["error"], "HTTP 403 Forbidden")

        self.assertEqual(out["metadata"]["successful_sources"], ["RateMyDecks"])
        self.assertEqual(out["metadata"]["failed_sources"], ["PowerDeckAI"])


if __name__ == "__main__":
    unittest.main()
