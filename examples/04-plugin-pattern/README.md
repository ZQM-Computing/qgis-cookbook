# 04 — Plugin pattern: from a working script to a minimal plugin

## What it demonstrates

Structuring a minimal QGIS plugin from a working script: the
smallest file set that QGIS recognises as a plugin, and how the
script's logic moves into it unchanged. The example starts from
the buffer logic of patterns 01–02 and wraps it as a plugin with
a toolbar button that buffers the currently selected point layer
to a GeoPackage the user picks. The pattern is about plugin
structure — `metadata.txt`, the `classFactory` entry point, and
the plugin class lifecycle (`initGui` / `unload`) — not about new
geoprocessing logic.

This pattern covers plugin structure only. It does not cover
expressions, styles, or QField guides — those belong to
qgis-resources, which this cookbook complements rather than
duplicates.

## Prerequisites + versions

- QGIS 3.44.15 LTR on a Windows node (binary `qgis-ltr-bin.exe`,
  install path `C:\Program Files\QGIS 3.44.15`).
- GDAL 3.13.3 bundled with QGIS.
- The synthetic input in `inputs/demo_sites.geojson` (no real data,
  no real addresses) — load it into QGIS before using the plugin
  button, so there is a point layer to buffer.
- The plugin folder layout in this directory (`demo_buffer_plugin/`
  — see Steps).
- Plugin install path and minimum-QGIS-version metadata for this
  build: to confirm at validation (the plugin's `metadata.txt`
  uses placeholder version bounds that must be checked against
  the installed build before the gate 3 run).
- Python version bundled with this QGIS build: to confirm at validation.

## Steps

1. Copy the `demo_buffer_plugin/` folder into the QGIS plugins
   folder for your QGIS profile (exact profile-plugins path for
   this build is to confirm at validation), or install it via
   Plugin Manager → Install from ZIP after zipping the folder.
2. Restart QGIS (or reload plugins), then enable "Demo Buffer
   Plugin" in Plugin Manager → Installed.
3. Load `inputs/demo_sites.geojson` into QGIS and select that
   layer in the Layers panel.
4. Click the plugin's toolbar button ("Buffer demo layer").
5. In the file dialog, pick an output GeoPackage path. The plugin
   buffers the selected layer and adds the result to the project.
6. Check the message bar and the new layer's feature count.

Execution context, stated honestly: run as an installed plugin
inside QGIS (toolbar button). Headless / standalone execution is
to confirm at validation — it is not claimed here, and a plugin
is a GUI construct, so headless validation may not apply to this
pattern at all.

## Expected output

- A GeoPackage at the path picked in the file dialog, containing
  one buffered polygon per input point.
- With the supplied synthetic input (3 points) and the plugin's
  default distance, the output contains 3 polygon features.
- The output layer is added to the project, and the QGIS message
  bar reports success with the output path.
- The plugin appears in Plugin Manager as installed and enabled,
  and its toolbar button is present while it is enabled and gone
  after it is disabled (the `unload` check).

## Failure behavior

- **No layer selected, or the selected layer is not a point
  vector layer:** the plugin shows a warning in the message bar
  and writes nothing. Select a point layer and try again.
- **Invalid input (a selected layer that fails `isValid()`):**
  the plugin shows a critical message naming the layer and
  writes nothing.
- **No-result case (a selected layer that loads but has zero
  features):** the plugin shows a warning stating the layer has
  zero features and writes nothing. An empty output is never
  silently produced.
- **No output path chosen (file dialog cancelled):** the plugin
  stops silently with no output and no error — cancelling is not
  a failure.
- **Processing failure:** the plugin shows a critical message
  with the algorithm's error and does not add a layer to the
  project or claim success.

## Evidence

Evidence: design-only, gate 1 target

This pattern has not been run and is not runtime-validated. It is a
design-only draft written for the gate 1 (Reproducible) target:
runnable example plus synthetic inputs plus stated expected and
failure outputs.

## Gate-3 proof

Gate 3 (Runtime-validated) would be proved by: installing
`demo_buffer_plugin/` into QGIS 3.44.15 LTR (`qgis-ltr-bin.exe`,
`C:\Program Files\QGIS 3.44.15`, GDAL 3.13.3 bundled) on one of
the three Windows nodes, enabling it in Plugin Manager, loading
`inputs/demo_sites.geojson`, clicking its toolbar button, picking
an output GeoPackage path, and recording (a) the message-bar
success message with the output path, (b) an independent
feature-count check of the output showing 3 polygon features,
and (c) that disabling the plugin removes its toolbar button
(`unload` verified). A separate headless / standalone run is not
expected for this GUI pattern; if one is claimed, its method must
be run and recorded separately — it is to confirm at validation.
No gate 3 claim is made until that run exists.
