# 01 — PyQGIS basics: load layers, run processing, write outputs

## What it demonstrates

Loading a vector layer from a file, running a Processing algorithm
from Python, and writing the result to a new file — the three steps
almost every PyQGIS automation script needs. The example loads the
synthetic point layer in `inputs/`, buffers it, and writes the
buffered output to a GeoPackage.

This pattern covers PyQGIS automation and processing only. It does
not cover expressions, styles, or QField guides — those belong to
qgis-resources, which this cookbook complements rather than
duplicates.

## Prerequisites + versions

- QGIS 3.44.15 LTR on a Windows node (binary `qgis-ltr-bin.exe`,
  install path `C:\Program Files\QGIS 3.44.15`).
- GDAL 3.13.3 bundled with QGIS.
- The synthetic input in `inputs/demo_sites.geojson` (no real data,
  no real addresses).
- Python version bundled with this QGIS build: to confirm at validation.
- Headless / standalone execution details: to confirm at validation.

## Steps

1. Open QGIS and open the Python console
   (Plugins → Python Console).
2. Open `load_and_buffer.py` in the console editor, or paste its
   contents into the console.
3. Replace the placeholder paths at the top of the script with the
   real paths to your copy of `inputs/demo_sites.geojson` and to
   your chosen output location. Do not leave the `<...>` placeholders
   in place — the script stops with an actionable message if you do.
4. Run the script.
5. Check the printed messages: layer feature count, the Processing
   result path, and the output feature count.

Execution context, stated honestly: run from the QGIS Python console.
Headless / standalone execution is to confirm at validation — it is
not claimed here.

## Expected output

- A new GeoPackage at the output path you set, containing one
  buffered polygon per input point.
- With the supplied synthetic input (3 points), the output contains
  3 polygon features.
- Console output reporting the input feature count (3), the output
  path, and the output feature count (3). Exact wording is in the
  script's print statements; no timestamps or machine paths are
  asserted as part of the output.

## Failure behavior

- **Placeholder paths left in place:** the script stops before
  loading anything and prints which variable still holds a
  placeholder, so the fix is to set that path.
- **Invalid input (missing file, unreadable file, or a layer that
  fails `isValid()`):** the script stops with an error naming the
  input path and does not write an output file. Fix the path or the
  input file and re-run.
- **No-result case (an input layer that loads but has zero
  features):** the script stops before running Processing, reports
  that the layer has zero features, and writes no output file.
  An empty output is never silently produced.
- **Processing failure:** the script reports the algorithm name
  and stops without claiming an output was written. Check the
  QGIS message log for the algorithm's own error text.

## Evidence

Evidence: design-only, gate 1 target

This pattern has not been run and is not runtime-validated. It is a
design-only draft written for the gate 1 (Reproducible) target:
runnable example plus synthetic inputs plus stated expected and
failure outputs.

## Gate-3 proof

Gate 3 (Runtime-validated) would be proved by: running
`load_and_buffer.py` from the QGIS Python console on one of the
three Windows nodes running QGIS 3.44.15 LTR
(`qgis-ltr-bin.exe`, `C:\Program Files\QGIS 3.44.15`, GDAL 3.13.3
bundled), using `inputs/demo_sites.geojson` as the input, and
recording (a) the console output, (b) the output GeoPackage path,
and (c) an independent feature-count check of the output showing
3 polygon features. A separate headless / standalone run, if it is
to be claimed, must be run and recorded separately — its command
line and environment are to confirm at validation. No gate 3 claim
is made until that run exists.
