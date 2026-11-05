# QGIS Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **QGIS cookbook** — PyQGIS automation, processing scripts, and plugin patterns. QGIS 3.44.15 LTR runs on all three Windows nodes. This cookbook covers PyQGIS automation and processing; it complements qgis-resources, which covers QGIS resources, rather than duplicating it. It is intended for GIS developers who automate QGIS with Python. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — four patterns are drafted at evidence gate 1 (design-only); none is runtime-validated. CI checks Python syntax, synthetic fixture structure, and documentation contracts only. It does not execute QGIS or certify the examples.

**What this repository is:** QGIS patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

GIS developers who automate QGIS with Python.

## Prerequisites

- QGIS 3.44.15 LTR
- Python console and PyQGIS
- A sample project and layers

## Patterns

| # | Example | Status | What it demonstrates |
|---|---------|--------|----------------------|
| 01 | [01-pyqgis-basics](examples/01-pyqgis-basics/README.md) | Written — design-only, gate 1 target | Loading layers, running processing algorithms, and writing outputs from Python |
| 02 | [02-processing-scripts](examples/02-processing-scripts/README.md) | Written — design-only, gate 1 target | Writing processing scripts with parameters and outputs |
| 03 | [03-map-automation](examples/03-map-automation/README.md) | Written — design-only, gate 1 target | Automating map exports and layouts |
| 04 | [04-plugin-pattern](examples/04-plugin-pattern/README.md) | Written — design-only, gate 1 target | Structuring a minimal plugin from a working script |

## Repository layout

```text
qgis-cookbook/
├── examples/
│   ├── 01-pyqgis-basics/
│   ├── 02-processing-scripts/
│   ├── 03-map-automation/
│   └── 04-plugin-pattern/
├── README.md
└── LICENSE
```

## Roadmap

- Complete gate-1 reproducibility for all four patterns: confirm paths, run instructions, synthetic fixtures, expected outputs, and failure behavior.
- Verify the plugin metadata and Processing Toolbox steps against the installed QGIS 3.44.15 LTR build.
- Promote patterns to gate 3 only after a recorded QGIS runtime run with output artifacts and independent feature-count / visual checks.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the example, fixture, validation, and evidence requirements. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [gdal-cookbook](https://github.com/ZQM-Computing/gdal-cookbook) — GDAL/OGR conversion, reprojection, and raster/vector utilities
- [postgis-cookbook](https://github.com/ZQM-Computing/postgis-cookbook) — Spatial indexing, joins & KNN, SRID management, vector tiles
