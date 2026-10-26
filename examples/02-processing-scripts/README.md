# 02 — Processing scripts: parameters and outputs

## What it demonstrates

Writing a QGIS Processing script — a script that declares its own
parameters and outputs so it appears in the Processing Toolbox and
can be re-run with different inputs without editing code. The
example script takes a point layer and a buffer distance, buffers
the points, and returns a polygon layer. It follows the standard
Processing script structure: a class extending
`QgsProcessingAlgorithm`, `initAlgorithm`, `processAlgorithm`,
and the metadata methods (`name`, `displayName`, `group`,
`groupId`, `createInstance`).

This pattern covers Processing scripting structure only. It does
not cover expressions, styles, or QField guides — those belong to
qgis-resources, which this cookbook complements rather than
duplicates.

## Prerequisites + versions

- QGIS 3.44.15 LTR on a Windows node (binary `qgis-ltr-bin.exe`,
  install path `C:\Program Files\QGIS 3.44.15`).
- GDAL 3.13.3 bundled with QGIS.
- The synthetic input in `inputs/demo_sites.geojson` (no real data,
  no real addresses).
- How to add a script to the Processing Toolbox (Scripts → Add
  script to Toolbox, or placing the file in the scripts folder):
  exact menu wording for this build is to confirm at validation.
- Python version bundled with this QGIS build: to confirm at validation.

## Steps

1. Open QGIS and open the Processing Toolbox.
2. Add `buffer_points_algorithm.py` as a Processing script (see
   Prerequisites for the route to confirm at validation).
3. Run the new "Buffer demo points" algorithm from the Toolbox.
4. Set the parameters: Input point layer =
   `inputs/demo_sites.geojson`; Buffer distance = `0.01`
   (degrees, matching the synthetic input's CRS84 coordinates —
   use a projected CRS and a metre distance for real-world work);
   Output = a GeoPackage path of your choice.
5. Run it and check the log and the output layer.

Execution context, stated honestly: run as a Processing script from
inside QGIS (via the Processing Toolbox). Headless / standalone
execution is to confirm at validation — it is not claimed here.

## Expected output

- A polygon layer at the output path you set, with one buffered
  polygon per input point.
- With the supplied synthetic input (3 points) and distance `0.01`,
  the output contains 3 polygon features, each carrying the input
  point's attributes (`site_id`, `site_name`, `category`).
- The algorithm log reports successful completion. The output
  feature count is the check, not any log wording.

## Failure behavior

- **Invalid input (missing file, unreadable file, or a layer that
  fails `isValid()`):** Processing reports the algorithm as failed
  and no output file is written. Fix the input path or file and
  re-run; do not treat a partial file as a result.
- **No-result case (an input layer that loads but has zero
  features):** the script raises a `QgsProcessingException`
  stating the input has zero features, the algorithm fails
  cleanly, and no output file is written. An empty output is never
  silently produced.
- **Invalid parameter (for example a negative buffer distance):**
  the script raises a `QgsProcessingException` naming the
  parameter before running the buffer, so no output is written.
- **Processing failure inside the buffer step:** the exception
  propagates and Processing reports the failure; no success
  message is printed.

## Evidence

Evidence: design-only, gate 1 target

This pattern has not been run and is not runtime-validated. It is a
design-only draft written for the gate 1 (Reproducible) target:
runnable example plus synthetic inputs plus stated expected and
failure outputs.

## Gate-3 proof

Gate 3 (Runtime-validated) would be proved by: adding
`buffer_points_algorithm.py` to the Processing Toolbox in QGIS
3.44.15 LTR (`qgis-ltr-bin.exe`, `C:\Program Files\QGIS 3.44.15`,
GDAL 3.13.3 bundled) on one of the three Windows nodes, running
it on `inputs/demo_sites.geojson` with distance `0.01` and an
explicit output path, and recording (a) the Toolbox log showing
successful completion, (b) the output path, and (c) an independent
feature-count check of the output showing 3 polygon features with
the input attributes retained. A separate headless / standalone run,
if it is to be claimed, must be run and recorded separately — its
command line and environment are to confirm at validation. No gate
3 claim is made until that run exists.
