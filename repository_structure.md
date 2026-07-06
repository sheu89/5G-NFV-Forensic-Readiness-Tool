# Repository Structure

This repository contains the implementation artefacts supporting the proposed 5G NFV Digital Forensic Readiness Model.

## Top-Level Structure

| Directory | Description |
|------------|------------|
| `config/` | Consolidated configuration files for Zeek, Filebeat, Logstash, Elasticsearch and Kibana |
| `deployment/` | Docker Compose files and deployment artefacts for the prototype |
| `detection/` | Machine learning attack detection, forensic analysis API and dashboard |
| `docs/` | Architecture diagrams, deployment documentation and research artefacts |
| `requests/` | OpenStack Tacker VNF instantiation requests |
| `sample_logs/` | Example network evidence collected during experiments |
| `scripts/` | Utility and deployment scripts |
| `vnfd/` | Virtual Network Function Descriptors used in the prototype |

## Prototype Workflow

```
OpenStack
      │
      ▼
OpenStack Tacker
      │
      ▼
5G Network Functions
      │
      ▼
Zeek Network Monitor
      │
      ▼
Evidence Collection
      │
      ▼
Attack Detection
      │
      ▼
Digital Forensic Report
```

## Purpose

The repository is organised to support reproducibility of the proposed Digital Forensic Readiness Model and to accompany the PhD thesis implementation.