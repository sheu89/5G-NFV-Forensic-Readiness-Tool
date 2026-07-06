# Machine Learning Models

This directory contains machine learning artefacts used by the 5G NFV Digital Forensic Readiness Tool.

## Included

- `label_encoder.joblib`

## Excluded

The trained Random Forest model (`rf_model.joblib`) is intentionally excluded from this repository because of its size (>4 GB).

To use the detection API:

1. Train the model using the provided training pipeline, or
2. Place `rf_model.joblib` into this directory.



```
detection/
└── models/
    ├── rf_model.joblib
    └── label_encoder.joblib
```