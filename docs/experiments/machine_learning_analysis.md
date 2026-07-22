# Machine Learning-Based Digital Evidence Analysis

## Overview

This document describes the machine learning subsystem of the 5G Digital Forensic Readiness Tool (5GDFRT). The subsystem forms the analytical component of the proposed forensic readiness architecture by automatically classifying network events and assisting investigators in identifying malicious activities within a virtualised 5G Network Function Virtualisation (NFV) environment.

Unlike traditional intrusion detection systems that primarily focus on identifying attacks, the machine learning subsystem operates as part of a broader digital forensic readiness process. Following the acquisition and preservation of Potential Digital Evidence (PDE) from the virtualised 5G infrastructure, the subsystem analyses extracted network features, predicts the most probable attack category, and presents the results through the forensic dashboard for further investigation.

The implementation described in this document corresponds to Section 9.5 of the accompanying PhD thesis.

---

# Purpose

The machine learning subsystem was developed to support automated evidence analysis by:

- classifying captured network activity into predefined attack categories;
- assisting investigators in identifying suspicious behaviour;
- reducing the manual effort required to analyse large volumes of forensic evidence;
- providing confidence scores for each prediction; and
- integrating analytical results into the overall forensic readiness workflow.

Rather than replacing forensic investigators, the subsystem provides decision support by highlighting potentially malicious events that warrant further examination.

---

# Machine Learning Workflow

The analytical workflow consists of five primary stages.

1. Collection of Potential Digital Evidence (PDE)
2. Feature Extraction
3. Data Preprocessing
4. Random Forest Classification
5. Visualisation and Reporting

The workflow begins once forensic agents have collected and preserved digital evidence from the virtualised 5G environment. Relevant network features are extracted and supplied to the trained Random Forest classifier, which predicts the most likely attack category. The resulting predictions are stored and visualised through the dashboard to assist forensic investigations.

---

# Input Data

The machine learning subsystem operates on network evidence collected throughout the prototype.

Typical input data includes:

- Zeek network logs;
- packet metadata;
- protocol information;
- connection statistics;
- traffic flow characteristics;
- timestamps;
- source and destination addresses; and
- additional evidence attributes extracted during evidence acquisition.

The collected evidence is indexed within Elasticsearch before being processed by the analytical pipeline.

---

# Feature Extraction

Relevant features are extracted from the collected evidence to create a structured dataset suitable for machine learning analysis.

The extracted features represent observable network characteristics associated with both legitimate and malicious activities. Feature extraction standardises heterogeneous evidence collected from multiple network functions into a consistent format suitable for classification.

The exact feature set is described in the accompanying thesis.

---

# Data Preprocessing

Before classification, the extracted dataset undergoes preprocessing to improve model performance.

Preprocessing activities include:

- data cleaning;
- handling incomplete records where appropriate;
- feature preparation;
- formatting the dataset for model inference; and
- preparing evidence for prediction.

These steps ensure consistency between the collected forensic evidence and the data used during model training.

---

# Random Forest Classifier

The machine learning subsystem employs a Random Forest classifier to distinguish between normal network behaviour and multiple attack categories.

Random Forest was selected because it offers:

- high classification accuracy;
- robustness against overfitting;
- suitability for heterogeneous network datasets;
- efficient inference performance; and
- interpretability through confidence scores and feature importance measures.

Following prediction, each analysed event is assigned an attack label together with an associated confidence score.

---

# Dashboard Integration

Classification results are presented through the forensic dashboard, allowing investigators to monitor network activity in near real time.

The dashboard provides:

- detected attack categories;
- confidence scores;
- evidence summaries;
- indexed forensic records;
- visual analytics; and
- historical evidence available for subsequent investigation.

The dashboard serves as the primary interface between the analytical subsystem and the digital investigator.

---

# Repository Components

The following repository directories are directly related to the machine learning subsystem.

| Directory | Purpose |
|----------|---------|
| `detection/` | Machine learning implementation and inference pipeline |
| `config/` | Configuration files for supporting services |
| `deployment/` | Deployment resources |
| `docs/architecture/` | Prototype architecture documentation |

---

# Detection Module Structure

The machine learning subsystem is organised into several functional components that together implement the analytical stage of the forensic readiness workflow. Although the internal implementation may evolve over time, the overall processing pipeline remains consistent.

| Component | Responsibility |
|----------|----------------|
| Data Acquisition | Retrieves Potential Digital Evidence (PDE) collected by forensic agents from Elasticsearch. |
| Feature Extraction | Extracts relevant network and protocol features from the collected evidence to create structured input suitable for machine learning. |
| Data Preprocessing | Cleans, formats, and prepares extracted features for inference, ensuring compatibility with the trained model. |
| Random Forest Model | Performs attack classification by predicting the most probable attack category based on the extracted features. |
| Prediction Service | Coordinates the inference process and returns prediction results together with associated confidence scores. |
| Dashboard Integration | Publishes prediction results to the web dashboard for visualisation and investigator interaction. |
| Reporting Module | Generates forensic reports containing detected attacks, supporting evidence, and analytical summaries. |

---

## Processing Pipeline

The machine learning workflow implemented by the prototype follows the sequence illustrated below.


Potential Digital Evidence
          │
          ▼
 Data Acquisition
          │
          ▼
 Feature Extraction
          │
          ▼
 Data Preprocessing
          │
          ▼
 Random Forest Model
          │
          ▼
 Prediction Results
          │
          ▼
 Elasticsearch
          │
          ▼
 Dashboard
          │
          ▼
 Forensic Reports


Each component performs a distinct responsibility while collectively supporting automated digital evidence analysis within the 5GDFRT.

---

## Directory Organisation

The machine learning implementation is primarily contained within the `detection/` directory.

Typical contents include:

| Resource | Purpose |
|----------|---------|
| Machine learning models | Trained classification models used during inference. |
| Feature extraction utilities | Convert collected forensic evidence into structured feature vectors. |
| Prediction services | Execute model inference and return classification results. |
| REST API components | Provide communication between the dashboard and the analytical backend. |
| Supporting utilities | Logging, configuration management, and helper functions. |

Researchers extending the prototype should begin by examining the contents of the `detection/` directory, where the core analytical functionality of the 5GDFRT is implemented.

# Expected Outputs

Successful execution of the analytical pipeline should produce:

- predicted attack categories;
- confidence scores;
- indexed Elasticsearch records;
- dashboard visualisations;
- preserved evidence references;
- machine learning inference logs; and
- forensic reports generated from analysed evidence.

---

# Reproducing the Analysis

To reproduce the analytical workflow:

1. Deploy the prototype environment.
2. Ensure forensic agents are operational.
3. Start Elasticsearch and Kibana.
4. Collect network evidence using the supported monitoring infrastructure.
5. Execute the machine learning inference pipeline.
6. Review prediction results within the dashboard.
7. Analyse associated forensic evidence.
8. Export reports where required.

---

# Related Thesis Section

This document corresponds to:

- Chapter 9
- Section 9.5 – Machine-Learning-Based Digital Evidence Analysis

Readers interested in the model development, evaluation methodology, performance metrics, and experimental results should consult the corresponding section of the thesis.

---

# Repository References

- `detection/`
- `config/`
- `deployment/`
- `docs/architecture/`