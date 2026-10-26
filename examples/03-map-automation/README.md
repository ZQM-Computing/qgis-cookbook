# 03 — Map automation: layouts and exports

## What it demonstrates

Automating a map export from Python: loading a layer, building a
print layout in code, adding a map item framed on the layer's
extent, and exporting the layout to a PDF and a PNG. The point is
repeatability — the same script re-exports the same layout every
time, instead of hand-building it in the Layout Manager for each
export.

This pattern covers layout construction and export automation
only. It does not cover expressions, styles, or QField guides —
those belong to qgis-resources, which this cookbook complements
rather than duplicates. (A style may be applied to the layer
beforehand; this pattern does not define one.)

## Prerequisites + versions

- QGIS 3.44.15 LTR on a Windows node (binary `qgis-ltr-bin.exe`,
  install path `C:\Program Files\QGIS 3.44.15`).
- GDAL 3.13.3 bundled with QGIS.
- The synthetic input in `inputs/demo_sites.geojson` (no real data,
  no real addresses).
- A writable output folder for the PDF and PNG.
- Layout class and method names for this build: to confirm at
  validation (the script uses the `QgsPrintLayout`,
  `QgsLayoutItemMap`, and `QgsLayoutExporter` classes as documented
  for the QGIS 3.x API).
- Python version bundled with this QGIS build: to confirm at validation.

## Steps

1. Open QGIS and open the Python console
   (Plugins → Python Console).
2. Open `export_demo_map.py` in the console editor, or paste its
   contents into the console.
3. Replace the placeholder paths at the top of the script: the
   input GeoJSON path, and the output PDF and PNG paths.
4. Run the script.
5. Check the printed messages, then open the exported PDF and PNG
   and confirm the three synthetic points appear inside the map
   frame.

Execution context, stated honestly: run from the QGIS Python console.
Headless / standalone execution is to confirm at validation — it is
not claimed here.

## Expected output

- A PDF at the output PDF path you set, containing one page with
  a map frame showing the synthetic points.
- A PNG at the output PNG path you set, showing the same map frame.
- Console output reporting the input feature count (3 with the
  supplied input), the layout name, and both export paths.
- Page size follows the layout defaults from `initializeDefaults()`
  (exact page-size setting for this build is to confirm at
  validation); PNG export uses 150 DPI. Exact rendered appearance
  depends on the layer's current symbology, which this pattern
  does not define.

## Failure behavior

- **Placeholder paths left in place:** the script stops before
  loading anything and prints which variable still holds a
  placeholder, so the fix is to set that path.
- **Invalid input (missing file, unreadable file, or a layer that
  fails `isValid()`):** the script stops with an error naming the
  input path and exports nothing. Fix the path or the input file
  and re-run.
- **No-result case (an input layer that loads but has zero
  features):** the script stops before building the layout,
  reports that the layer has zero features, and exports nothing.
  A blank map is never silently exported as a success.
- **Export failure (for example an unwritable output folder):**
  the script reports the exporter result for the failed format
  and names the path, so the failure is visible per format rather
  than masked by the other format's success.

## Evidence

Evidence: design-only, gate 1 target

This pattern has not been run and is not runtime-validated. It is a
design-only draft written for the gate 1 (Reproducible) target:
runnable example plus synthetic inputs plus stated expected and
failure outputs.

## Gate-3 proof

Gate 3 (Runtime-validated) would be proved by: running
`export_demo_map.py` from the QGIS Python console on one of the
three Windows nodes running QGIS 3.44.15 LTR
(`qgis-ltr-bin.exe`, `C:\Program Files\QGIS 3.44.15`, GDAL 3.13.3
bundled), using `inputs/demo_sites.geojson` as the input, and
recording (a) the console output, (b) both export paths, and
(c) a visual check that the exported PDF and PNG each show the
map frame with the three synthetic points. A separate headless /
standalone run, if it is to be claimed, must be run and recorded
separately — its command line and environment are to confirm at
validation. No gate 3 claim is made until that run exists.
