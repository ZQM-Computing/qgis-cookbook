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

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** QGIS patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

GIS developers who automate QGIS with Python.

## Prerequisites

- QGIS 3.44.15 LTR
- Python console and PyQGIS
- A sample project and layers

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-pyqgis-basics` | Loading layers, running processing algorithms, and writing outputs from Python |
| 02 | `02-processing-scripts` | Writing processing scripts with parameters and outputs |
| 03 | `03-map-automation` | Automating map exports and layouts |
| 04 | `04-plugin-pattern` | Structuring a minimal plugin from a working script |

## Repository layout

```text
qgis-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [gdal-cookbook](https://github.com/ZQM-Computing/gdal-cookbook) — GDAL/OGR conversion, reprojection, and raster/vector utilities
- [postgis-cookbook](https://github.com/ZQM-Computing/postgis-cookbook) — Spatial indexing, joins & KNN, SRID management, vector tiles
