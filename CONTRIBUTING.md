# Contributing to qgis-cookbook

This repository contains QGIS/PyQGIS reference patterns. Contributions must keep
the evidence level explicit: a syntactically valid script is not a QGIS runtime-
validated example.

## Before changing a pattern

- State the supported QGIS and bundled GDAL versions.
- Use synthetic fixtures; do not add real addresses, credentials, or personal data.
- Document the exact execution context: QGIS Python Console, Processing Toolbox,
  installed plugin, or a separately validated standalone environment.
- State CRS and units explicitly. Never present degrees as metres.
- Describe expected outputs and fail-closed behavior for missing, invalid, or
  empty inputs and unwritable destinations.
- Keep the example self-contained and avoid undocumented network downloads.

## Validation levels

- **Static:** Python parses; fixture and documentation contracts pass. This is
  what the repository CI currently checks.
- **Gate 1 — reproducible:** a contributor has run the documented steps in the
  stated environment and captured the command/UI steps, fixture, and outputs.
- **Gate 3 — runtime-validated:** the supported QGIS runtime executed the
  example; attach logs and output artifacts, independently verify feature
  counts/CRS/geometry, and include a visual check where the output is visual.

Do not upgrade an evidence label because CI is green. CI does not install or run
QGIS and cannot prove Processing algorithms, plugin lifecycle behavior, map
exports, or GUI interaction.

## Local checks

From the repository root:

```bash
python -m unittest discover -s tests -v
python -m compileall -q examples tests
```

## Pull requests

Include the affected pattern, QGIS/GDAL versions used, fixture details, exact
validation commands, observed results, output artifact paths, and any remaining
limitations. Keep unrelated patterns in separate changes. Do not claim a
runtime result that was not observed.

Report security issues privately to zqmcomputing@gmail.com; do not open a
public issue containing exploit details or credentials.
