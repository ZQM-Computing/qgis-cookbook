"""PyQGIS basics: load a layer, run Processing, write an output.

Execution context: run from the QGIS Python console. Headless /
standalone execution is to confirm at validation and is not claimed
here.

Replace the placeholder paths below before running. No credentials
are used anywhere in this script.
"""

from qgis.core import QgsApplication, QgsVectorLayer
import processing

# --- Placeholders: replace both before running ---------------------
INPUT_PATH = r"<YOUR_INPUT_GEOJSON_PATH>"   # e.g. path to inputs/demo_sites.geojson
OUTPUT_PATH = r"<YOUR_OUTPUT_GPKG_PATH>"    # e.g. path to buffered_sites.gpkg
BUFFER_DISTANCE = 0.01  # in the input layer's map units (degrees here,
# because the synthetic input is in CRS84); use a projected CRS and a
# metre distance for real-world work
# -------------------------------------------------------------------


def _is_placeholder(value):
    return value.startswith("<") or value.endswith(">")


def main():
    if _is_placeholder(INPUT_PATH):
        print("ERROR: INPUT_PATH still holds a placeholder. "
              "Set it to the path of inputs/demo_sites.geojson and re-run.")
        return
    if _is_placeholder(OUTPUT_PATH):
        print("ERROR: OUTPUT_PATH still holds a placeholder. "
              "Set it to an output GeoPackage path and re-run.")
        return

    layer = QgsVectorLayer(INPUT_PATH, "demo_sites", "ogr")
    if not layer.isValid():
        print(f"ERROR: input layer failed to load: {INPUT_PATH}")
        print("Check the path and that the file is a readable GeoJSON layer.")
        return

    count = layer.featureCount()
    print(f"Loaded input layer with {count} feature(s).")
    if count == 0:
        print("ERROR: input layer has zero features; "
              "no output will be written.")
        return

    result = processing.run(
        "native:buffer",
        {
            "INPUT": layer,
            "DISTANCE": BUFFER_DISTANCE,
            "SEGMENTS": 8,
            "END_CAP_STYLE": 0,
            "JOIN_STYLE": 0,
            "MITER_LIMIT": 2,
            "DISSOLVE": False,
            "OUTPUT": OUTPUT_PATH,
        },
    )
    output_path = result.get("OUTPUT", OUTPUT_PATH)
    print(f"Processing finished. Output written to: {output_path}")

    out_layer = QgsVectorLayer(output_path, "buffered_sites", "ogr")
    if not out_layer.isValid():
        print(f"ERROR: output layer failed to load for verification: {output_path}")
        return
    print(f"Output layer has {out_layer.featureCount()} feature(s).")


main()
