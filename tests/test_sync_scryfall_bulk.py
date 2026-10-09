import json
import pathlib
import sys
import tempfile
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import scryfall_cache
import sync_scryfall_bulk as sync


class TestScryfallBulkSync(unittest.TestCase):
    def setUp(self):
        self.sample_cards = [
            {
                "name": "Sol Ring",
                "cmc": 1.0,
                "mana_cost": "{1}",
                "type_line": "Artifact",
                "oracle_text": "{T}: Add {C}{C}.",
                "colors": [],
                "color_identity": [],
                "keywords": [],
                "legalities": {"commander": "legal"},
                "edhrec_rank": 1,
                "prices": {"usd": "1.50", "usd_foil": "3.00"},
                "layout": "normal",
            },
            {
                "name": "Blightstep Pathway // Searstep Pathway",
                "cmc": 0.0,
                "mana_cost": "",
                "type_line": "Land // Land",
                "oracle_text": "",
                "colors": [],
                "color_identity": ["B", "R"],
                "keywords": [],
                "legalities": {"commander": "legal"},
                "edhrec_rank": 120,
                "prices": {"usd": "5.50"},
                "layout": "modal_dfc",
                "card_faces": [
                    {
                        "name": "Blightstep Pathway",
                        "type_line": "Land",
                        "mana_cost": "",
                        "oracle_text": "{T}: Add {B}.",
                        "colors": [],
                    },
                    {
                        "name": "Searstep Pathway",
                        "type_line": "Land",
                        "mana_cost": "",
                        "oracle_text": "{T}: Add {R}.",
                        "colors": [],
                    },
                ],
            },
        ]

    def test_normalize_card_entry_normal(self):
        norm, aliases = sync.normalize_card_entry(self.sample_cards[0], "2026-10-09")
        self.assertEqual(norm["cmc"], 1.0)
        self.assertEqual(norm["mana_cost"], "{1}")
        self.assertEqual(norm["oracle_text"], "{T}: Add {C}{C}.")
        self.assertEqual(norm["legal_commander"], "legal")
        self.assertEqual(norm["prices_usd"], "1.50")
        self.assertEqual(norm["prices_usd_foil"], "3.00")
        self.assertEqual(aliases, [])

    def test_normalize_card_entry_mdfc(self):
        norm, aliases = sync.normalize_card_entry(self.sample_cards[1], "2026-10-09")
        self.assertEqual(norm["color_identity"], ["B", "R"])
        self.assertIn("{T}: Add {B}.", norm["oracle_text"])
        self.assertIn("{T}: Add {R}.", norm["oracle_text"])
        self.assertIn("Blightstep Pathway", aliases)
        self.assertIn("Searstep Pathway", aliases)

    def test_build_and_query_sqlite_cache(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            json_file = pathlib.Path(tmpdir) / "test_bulk.json"
            db_file = pathlib.Path(tmpdir) / "test_scryfall.db"

            json_file.write_text(json.dumps(self.sample_cards), encoding="utf-8")

            count = sync.build_sqlite_cache(json_file, db_file)
            self.assertEqual(count, 2)
            self.assertTrue(db_file.exists())

            db = scryfall_cache.ScryfallDatabase(db_file)
            self.assertTrue(db.is_available())
            self.assertEqual(db.count(), 2)

            # 1. Exact match lookup
            sol_ring = db.get_card("Sol Ring")
            self.assertIsNotNone(sol_ring)
            self.assertEqual(sol_ring["cmc"], 1.0)

            # 2. Case-insensitive lookup
            sol_ring_lower = db.get_card("sol ring")
            self.assertIsNotNone(sol_ring_lower)
            self.assertEqual(sol_ring_lower["type_line"], "Artifact")

            # 3. Alias lookup (front face of MDFC)
            blightstep = db.get_card("Blightstep Pathway")
            self.assertIsNotNone(blightstep)
            self.assertEqual(blightstep["color_identity"], ["B", "R"])

            # 4. Back face lookup
            searstep = db.get_card("Searstep Pathway")
            self.assertIsNotNone(searstep)

            # 5. Full-text search (FTS5)
            fts_results = db.search_fts("mana")
            self.assertGreaterEqual(len(fts_results), 0)

            db.close()

    def test_build_and_query_sqlite_cache_gzipped_jsonl(self):
        import gzip
        with tempfile.TemporaryDirectory() as tmpdir:
            gz_file = pathlib.Path(tmpdir) / "test_bulk.jsonl.gz"
            db_file = pathlib.Path(tmpdir) / "test_scryfall.db"

            with gzip.open(gz_file, "wt", encoding="utf-8") as gz_out:
                for card in self.sample_cards:
                    gz_out.write(json.dumps(card) + "\n")

            count = sync.build_sqlite_cache(gz_file, db_file)
            self.assertEqual(count, 2)
            self.assertTrue(db_file.exists())

            db = scryfall_cache.ScryfallDatabase(db_file)
            self.assertTrue(db.is_available())
            self.assertEqual(db.count(), 2)
            card = db.get_card("Sol Ring")
            self.assertIsNotNone(card)
            self.assertEqual(card["cmc"], 1.0)
            db.close()

    def test_unified_scryfall_cache_fallback(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            json_file = pathlib.Path(tmpdir) / "scryfall-cards.json"
            db_file = pathlib.Path(tmpdir) / "scryfall.db"

            # Put Sol Ring only in JSON
            json_file.write_text(
                json.dumps({
                    "Sol Ring": {"cmc": 1.0, "type_line": "Artifact"}
                }),
                encoding="utf-8",
            )

            # Put MDFC in DB
            raw_json = pathlib.Path(tmpdir) / "raw.json"
            raw_json.write_text(json.dumps([self.sample_cards[1]]), encoding="utf-8")
            sync.build_sqlite_cache(raw_json, db_file)

            cache = scryfall_cache.UnifiedScryfallCache(json_path=json_file, db_path=db_file)

            # Both should be seamlessly accessible
            self.assertIn("Sol Ring", cache)
            self.assertIn("Blightstep Pathway // Searstep Pathway", cache)
            self.assertIn("Blightstep Pathway", cache)  # via DB alias
            self.assertNotIn("Black Lotus", cache)

            self.assertEqual(cache["Sol Ring"]["cmc"], 1.0)
            self.assertEqual(cache["Blightstep Pathway"]["color_identity"], ["B", "R"])
            self.assertIsNone(cache.get("Nonexistent Card"))


if __name__ == "__main__":
    unittest.main()
