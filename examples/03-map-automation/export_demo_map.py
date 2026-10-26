"""Map automation: build a print layout in code and export it.

Execution context: run from the QGIS Python console. Headless /
standalone execution is to confirm at validation and is not claimed
here.

Replace the placeholder paths below before running. No credentials
are used anywhere in this script.
"""

from qgis.core import (
    QgsLayoutExporter,
    QgsLayoutItemMap,
    QgsPrintLayout,
    QgsProject,
    QgsVectorLayer,
)

# --- Placeholders: replace all three before running ----------------
INPUT_PATH = r"<YOUR_INPUT_GEOJSON_PATH>"  # e.g. path to inputs/demo_sites.geojson
OUTPUT_PDF = r"<YOUR_OUTPUT_PDF_PATH>"     # e.g. path to demo_map.pdf
OUTPUT_PNG = r"<YOUR_OUTPUT_PNG_PATH>"     # e.g. path to demo_map.png
# -------------------------------------------------------------------


def _is_placeholder(value):
    return value.startswith("<") or value.endswith(">")


def main():
    for name, value in [
        ("INPUT_PATH", INPUT_PATH),
        ("OUTPUT_PDF", OUTPUT_PDF),
        ("OUTPUT_PNG", OUTPUT_PNG),
    ]:
        if _is_placeholder(value):
            print(f"ERROR: {name} still holds a placeholder. "
                  f"Set it to a real path and re-run.")
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
              "no layout will be built and nothing will be exported.")
        return

    project = QgsProject.instance()
    if project.mapLayersByName("demo_sites"):
        print("Note: a layer named 'demo_sites' is already in the project; "
              "the new layer will be added alongside it.")
    project.addMapLayer(layer)

    layout = QgsPrintLayout(project)
    layout.initializeDefaults()
    layout.setName("demo_map")

    # Page size uses the layout defaults from initializeDefaults();
    # exact page-size API for this build is to confirm at validation.
    map_item = QgsLayoutItemMap(layout)
    map_item.setRect(20, 20, 257, 170)
    map_item.setExtent(layer.extent())
    # Frame the layer with a small margin around its extent.
    extent = layer.extent()
    extent.scale(1.2)
    map_item.setExtent(extent)
    map_item.setBackgroundColor(0xFFFFFF)
    layout.addLayoutItem(map_item)

    exporter = QgsLayoutExporter(layout)

    pdf_result = exporter.exportToPdf(
        OUTPUT_PDF, QgsLayoutExporter.PdfExportSettings()
    )
    if pdf_result != QgsLayoutExporter.Success:
        print(f"ERROR: PDF export failed (result {pdf_result}): {OUTPUT_PDF}")
    else:
        print(f"PDF exported to: {OUTPUT_PDF}")

    png_settings = QgsLayoutExporter.ImageExportSettings()
    png_settings.dpi = 150
    png_result = exporter.exportToImage(
        OUTPUT_PNG, png_settings
    )
    if png_result != QgsLayoutExporter.Success:
        print(f"ERROR: PNG export failed (result {png_result}): {OUTPUT_PNG}")
    else:
        print(f"PNG exported to: {OUTPUT_PNG}")


main()
