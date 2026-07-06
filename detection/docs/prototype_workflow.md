# Prototype Workflow

## Overview

The proposed 5G NFV Digital Forensic Readiness Tool (5GDFRT) implements a proactive approach to digital evidence collection and attack detection within a virtualized 5G environment.

The prototype integrates virtualized network functions, network monitoring, centralized evidence collection, machine learning-based attack detection, and automated forensic reporting into a single workflow.

---

# End-to-End Workflow

```
                    OpenStack DevStack
                            │
                            ▼
                  OpenStack Tacker (NFVO)
                            │
                            ▼
                 OpenAirInterface 5G Core
                            │
                            ▼
                     UERANSIM Traffic
                            │
                            ▼
                  Zeek Network Monitoring
                            │
                            ▼
                 Digital Evidence Collection
                            │
                            ▼
             Filebeat → Logstash → Elasticsearch
                            │
                            ▼
                Machine Learning Attack Detection
                            │
                            ▼
                  Automated Forensic Reporting
                            │
                            ▼
                  Kibana Investigation Dashboard
```

---

# Workflow Description

## Step 1 – Virtual Network Deployment

OpenStack DevStack provides the NFV Infrastructure (NFVI), while OpenStack Tacker orchestrates deployment of the Virtual Network Functions (VNFs) that form the OpenAirInterface 5G Core.

## Step 2 – Network Traffic Generation

UERANSIM simulates User Equipment (UE) and Radio Access Network (RAN) behaviour, generating realistic 5G traffic for experimentation.

## Step 3 – Digital Evidence Collection

Forensic agents continuously monitors network traffic and extracts metadata describing connections, protocols, services, and communication behaviour.

## Step 4 – Evidence Processing

Collected evidence is forwarded through Filebeat and Logstash before being indexed in Elasticsearch for centralized storage and retrieval.

## Step 5 – Attack Detection

The processed evidence is analysed using a machine learning attack detection component that classifies observed network activity into benign or malicious categories.

## Step 6 – Forensic Reporting

Detected events are transformed into structured forensic artefacts that include attack classifications, confidence values, supporting indicators, and recommended mitigation actions.

---

# Research Contribution

The proposed model demonstrates that digital forensic readiness can be integrated directly into a virtualized 5G NFV environment by combining proactive evidence collection, centralized evidence management, automated attack detection, and forensic report generation into a unified workflow.

The prototype serves as a proof-of-concept implementation of the proposed Digital Forensic Readiness Model.
