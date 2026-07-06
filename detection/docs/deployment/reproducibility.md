# Reproducibility Guide

## Overview

This repository contains the implementation artefacts supporting the proposed **5G NFV Digital Forensic Readiness Model**.

The prototype integrates:

* OpenStack DevStack
* OpenStack Tacker
* OpenAirInterface (OAI) 5G Core
* UERANSIM
* Zeek Network Security Monitor
* Elastic Stack (ELK)
* Machine Learning Attack Detection

to demonstrate automated digital evidence collection and forensic readiness in virtualized 5G environments.

---

# Hardware Requirements

The complete prototype is computationally intensive and was designed for a dedicated research workstation or server.

## Minimum Recommended Specifications

| Component        | Specification    |
| ---------------- | ---------------- |
| CPU              | 16 logical cores |
| Memory           | 64 GB RAM        |
| Storage          | 500 GB SSD       |
| Operating System | Ubuntu 20.04 LTS |

## Recommended Specifications

| Component      | Specification    |
| -------------- | ---------------- |
| CPU            | 32 logical cores |
| Memory         | 128 GB RAM       |
| Storage        | 1 TB NVMe SSD    |
| Virtualization | KVM Enabled      |

---

# Software Components

| Component          | Purpose                     |
| ------------------ | --------------------------- |
| OpenStack DevStack | NFV Infrastructure          |
| OpenStack Tacker   | VNF Orchestration           |
| OpenAirInterface   | 5G Core Network             |
| UERANSIM           | User Equipment Simulation   |
| Forensic Agents    | Network Evidence Collection |
| Filebeat           | Log Forwarding              |
| Logstash           | Log Processing              |
| Elasticsearch      | Evidence Storage            |
| Kibana             | Evidence Visualization      |
| FastAPI            | Attack Detection API        |

---

# Repository Layout

The repository is organized into independent modules:

* `deployment/`
* `vnfd/`
* `requests/`
* `config/`
* `detection/`
* `docs/`

allowing individual components to be studied and reproduced independently.

---

# Notes

The complete prototype was validated within a dedicated research environment.

Researchers may execute individual components independently without deploying the full infrastructure.

This repository is intended to support reproducibility of the proposed Digital Forensic Readiness Model rather than provide a one-click deployment for production environments.
