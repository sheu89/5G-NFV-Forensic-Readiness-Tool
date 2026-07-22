# Attack Detection Module

## Overview

The attack detection module provides machine learning capabilities for identifying malicious activities captured from the 5G NFV environment.

The implementation combines:

- 5GDFRT network monitoring
- Feature extraction
- Machine learning inference
- Web dashboard
- Report generation

## Components

| Folder | Purpose |
|---------|----------|
| api | FastAPI detection service |
| dashboard | React-based visual dashboard |
| models | Machine learning models |
| pipelines | Zeek parsing and feature extraction |
| reports | Generated forensic reports |
| simulation | Traffic generation scripts |

## Workflow

Network traffic is captured by Zeek before being parsed and transformed into feature vectors. These features are submitted to the detection API where the trained Random Forest model performs attack classification. The results are presented through the dashboard and incorporated into the generated forensic report.

## Note

The trained Random Forest model used during experimentation is intentionally excluded from this repository because of its size. The repository includes the supporting code and label encoder required to reproduce the detection pipeline.