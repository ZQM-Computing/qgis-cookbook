"""Static quality gates for the QGIS cookbook.

These tests intentionally do not import QGIS or claim runtime validation.
They validate Python syntax, synthetic fixtures, plugin metadata, and the
evidence statements in the example documentation.
"""
import ast
import json
import math
import configparser
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"

class StaticContractTests(unittest.TestCase):
    def test_all_python_examples_parse_without_importing_qgis(self):
        files = sorted(EXAMPLES.rglob("*.py"))
        self.assertGreaterEqual(len(files), 5)
        for path in files:
            with self.subTest(path=path.relative_to(ROOT)):
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    def test_each_pattern_has_a_three_point_crs84_fixture(self):
        pattern_dirs = [
            "01-pyqgis-basics",
            "02-processing-scripts",
            "03-map-automation",
            "04-plugin-pattern",
        ]
        for name in pattern_dirs:
            path = EXAMPLES / name / "inputs" / "demo_sites.geojson"
            with self.subTest(pattern=name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(data.get("type"), "FeatureCollection")
                self.assertEqual(len(data.get("features", [])), 3)
                self.assertIn("CRS84", data.get("crs", {}).get("properties", {}).get("name", ""))
                ids = set()
                for feature in data["features"]:
                    self.assertEqual(feature.get("geometry", {}).get("type"), "Point")
                    coords = feature["geometry"]["coordinates"]
                    self.assertEqual(len(coords), 2)
                    self.assertTrue(all(math.isfinite(float(v)) for v in coords))
                    ids.add(feature.get("properties", {}).get("site_id"))
                self.assertEqual(len(ids), 3)
                self.assertNotIn(None, ids)

    def test_user_path_scripts_guard_placeholders_before_processing(self):
        for rel in [
            "01-pyqgis-basics/load_and_buffer.py",
            "03-map-automation/export_demo_map.py",
        ]:
            source = (EXAMPLES / rel).read_text(encoding="utf-8")
            with self.subTest(script=rel):
                self.assertIn("def _is_placeholder", source)
                self.assertIn("still holds a placeholder", source)
                self.assertIn("def main()", source)

    def test_processing_algorithm_exposes_qgis_contract_methods(self):
        source = (EXAMPLES / "02-processing-scripts" / "buffer_points_algorithm.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        cls = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "BufferDemoPointsAlgorithm")
        methods = {node.name for node in cls.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
        self.assertTrue({"name", "displayName", "group", "groupId", "createInstance", "initAlgorithm", "processAlgorithm"} <= methods)

    def test_plugin_metadata_and_entrypoint_are_present(self):
        metadata = configparser.ConfigParser()
        metadata.read(EXAMPLES / "04-plugin-pattern" / "demo_buffer_plugin" / "metadata.txt", encoding="utf-8")
        self.assertTrue(metadata.has_section("general"))
        for key in ("name", "version", "qgisMinimumVersion", "author", "description"):
            self.assertTrue(metadata.has_option("general", key), key)
        init_source = (EXAMPLES / "04-plugin-pattern" / "demo_buffer_plugin" / "__init__.py").read_text(encoding="utf-8")
        self.assertIn("def classFactory(iface):", init_source)
        plugin_tree = ast.parse((EXAMPLES / "04-plugin-pattern" / "demo_buffer_plugin" / "plugin.py").read_text(encoding="utf-8"))
        plugin = next(node for node in plugin_tree.body if isinstance(node, ast.ClassDef) and node.name == "DemoBufferPlugin")
        methods = {node.name for node in plugin.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"initGui", "unload", "run"} <= methods)

    def test_all_patterns_disclose_design_only_evidence(self):
        for name in ("01-pyqgis-basics", "02-processing-scripts", "03-map-automation", "04-plugin-pattern"):
            doc = (EXAMPLES / name / "README.md").read_text(encoding="utf-8")
            with self.subTest(pattern=name):
                self.assertIn("Evidence: design-only, gate 1 target", doc)
                self.assertIn("No gate 3 claim", doc)

if __name__ == "__main__":
    unittest.main()
