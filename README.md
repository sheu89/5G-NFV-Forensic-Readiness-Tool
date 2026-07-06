# 5G Digital Forensic Readiness Tool (5GDFRT)

A research prototype implementing a Digital Forensic Readiness Model for 5G Network Function Virtualization (NFV) Environments.

The prototype demonstrates proactive digital evidence collection, preservation, storage, analysis, and automated attack detection within a virtualized 5G infrastructures.

---

## Overview

The 5G Digital Forensic Readiness Tool (5GDFRT) integrates Network Function Virtualization (NFV), Software Defined Networking (SDN), centralized logging, and machine learning to support forensic readiness in 5G core networks.

The repository accompanies the implementation of the proposed Digital Forensic Readiness Model and provides the deployment artefacts, configuration files, and supporting documentation required to reproduce the research prototype.

---

## Prototype Components

* OpenStack DevStack
* OpenStack Tacker
* OpenAirInterface (OAI) 5G Core
* UERANSIM
* Forensic Agents
* Elasticsearch
* Logstash
* Kibana
* Machine Learning Attack Detection API

---

## Key Features

* Proactive Digital Evidence Collection
* Digital Evidence Preservation
* Digital Evidence Storage
* Digital Evidence Analysis
* Machine Learning-based Attack Detection
* Automated Forensic Report Generation

---

## Repository Structure

```text
config/         Consolidated configuration files
deployment/     Deployment artefacts and Docker Compose files
detection/      Attack detection API, dashboard and forensic pipeline
docs/           Architecture and deployment documentation
requests/       OpenStack Tacker VNF instantiation requests
sample_logs/    Sample network evidence
scripts/        Deployment and utility scripts
vnfd/           Virtual Network Function Descriptors
```

---

## Installation

### Prerequisites

The complete prototype was developed and evaluated on Ubuntu 22.04 LTS.

Recommended minimum specifications:

* 16 CPU cores
* 64 GB RAM
* 500 GB SSD
* KVM Virtualization enabled

---

### Clone the Repository

```bash
git clone https://github.com/sheu89/5G-NFV-Forensic-Readiness-Tool.git

cd 5G-NFV-Forensic-Readiness-Tool
```

---

### Deploy the Prototype

The deployment process consists of the following stages:

1. Deploy the OpenStack DevStack environment.
2. Install and configure OpenStack Tacker.
3. Deploy the OpenAirInterface (OAI) 5G Core VNFs.
4. Deploy the Elastic Stack (Elasticsearch, Logstash and Kibana).
5. Configure Forensic agents for evidence collection.
6. Start the Machine Learning Attack Detection API.
7. Generate network traffic using UERANSIM.
8. Analyse collected evidence using Kibana and the forensic reporting pipeline.

Detailed deployment instructions are provided in:

```
docs/deployment/
```

---

### Running the Attack Detection API

```bash
cd detection/api

pip install -r requirements.txt

uvicorn main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

The interactive API documentation can be accessed at:

```
http://localhost:8000/docs
```

---

## Documentation

Additional documentation is available in the `docs/` directory, including:

* Architecture Overview
* Prototype Workflow
* Repository Structure
* Reproducibility Guide
* Deployment Documentation

---

## Research Purpose

This repository serves as the implementation artefact accompanying the proposed 5G NFV Digital Forensic Readiness Model. It is intended to support reproducibility of the research and provide a reference implementation for researchers working in digital forensics, 5G networks, and Network Function Virtualization.

---

## License

This project is released for academic and research purposes.
