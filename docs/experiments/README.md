# Experimental Evaluation

## Overview

This directory documents the experimental evaluation of the 5G Digital Forensic Readiness Tool (5GDFRT) presented in Chapter 9 of the PhD thesis, A Digital Forensic Readiness Model for 5G Network Function Virtualisation (NFV) Environments.

The experiments demonstrate how the proposed prototype operationalises the Digital Forensic Readiness Model introduced in Chapter 6 and the prototype architecture presented in Chapters 7 and 8. Rather than focusing solely on intrusion detection, the evaluation demonstrates the complete forensic readiness lifecycle, including digital evidence collection, preservation, secure storage, machine learning-based analysis, and event reconstruction within a virtualised 5G Network Function Virtualisation (NFV) environment.

The experiments were conducted in a controlled OpenStack-based 5G testbed using OpenAirInterface (OAI), OpenStack Tacker, Zeek, Forensic Agents, the Elastic Stack (ELK), and a Random Forest machine learning classifier integrated into the prototype.

---

# Experimental Objectives

The evaluation was designed to validate the forensic readiness capabilities of the 5GDFRT. Specifically, the experiments aimed to:

- Evaluate the ability of the prototype to detect and log anomalous activities in near real time.
- Assess the effectiveness of the machine learning module in classifying different categories of cyber attacks.
- Verify that potential digital evidence is collected, preserved, transmitted and stored while maintaining forensic integrity.
- Demonstrate the reconstruction of complete forensic timelines by correlating evidence collected from multiple virtualised 5G Network Functions (VNFs).

---

# Experimental Environment

All experiments were performed using the prototype implementation described in Chapter 8.

The evaluation environment consisted of:

| Component | Purpose |
|----------|---------|
| OpenStack | NFV infrastructure |
| OpenStack Tacker | VNF orchestration |
| OpenAirInterface (OAI) | 5G Core Network |
| UERANSIM | Simulated User Equipment (UE) and Radio Access Network (RAN) |
| 5GDFRT | Network traffic monitoring |
| Elastic Stack (Elasticsearch, Logstash and Kibana) | Centralised forensic evidence collection and visualisation |
| FastAPI | Communication between the dashboard and backend services |
| Random Forest Classifier | Machine learning-based attack classification |
| Ostinato | Attack traffic generation |

Forensic agents were deployed within multiple 5G Network Functions, including the Access and Mobility Management Function (AMF), Session Management Function (SMF), User Plane Function (UPF), Network Repository Function (NRF), Authentication Server Function (AUSF), Unified Data Management (UDM), and other supporting components. These agents continuously monitored network activity and forwarded structured potential digital evidence (PDE) to the centralised Elastic Stack for analysis.

---

# Repository Structure

The experiments described in this directory utilise several components contained within this repository.

| Repository Directory | Description |
|----------------------|-------------|
| `deployment/` | Deployment scripts and supporting infrastructure |
| `vnfd/` | Virtual Network Function Descriptor packages |
| `requests/` | OpenStack Tacker deployment requests |
| `detection/` | Machine learning detection pipeline and dashboard |
| `config/` | Configuration files for Zeek, ELK Stack and supporting services |
| `docs/architecture/` | System architecture and deployment documentation |

---

# Experimental Scenarios

The experimental evaluation is organised into four documentation guides.

| Document | Description |
|----------|-------------|
| experiment1_ddos_ping_flood.md | Demonstrates forensic evidence collection during a distributed ICMP ping flood attack generated using Ostinato. |
| experiment2_ip_fragmentation.md | Evaluates the prototype's ability to detect protocol-level attacks involving Internet Protocol fragmentation. |
| machine_learning_analysis.md | Describes the feature extraction process, Random Forest classifier, explainability mechanisms, and machine learning dashboard used during evidence analysis. |
| experiment3_event_reconstruction.md | Demonstrates reconstruction of complete forensic timelines through correlation of control-plane, user-plane, and application logs collected from multiple VNFs. |

Together, these documents demonstrate the complete forensic workflow implemented by the prototype, from attack generation and evidence acquisition to automated analysis and forensic event reconstruction.

---

# Relationship to the Thesis

The documentation in this directory corresponds directly to Chapter 9 – Prototype Demonstration: Case Scenarios and Results.

| Thesis Section | Repository Document |
|---------------|---------------------|
| Section 9.3 | experiment1_ddos_ping_flood.md |
| Section 9.4 | experiment2_ip_fragmentation.md |
| Section 9.5 | machine_learning_analysis.md |
| Section 9.6 | experiment3_event_reconstruction.md |

Readers interested in the detailed methodology, experimental results, performance analysis, and discussion should consult the corresponding sections of the thesis.

---

# Reproducing the Experiments

To reproduce the experimental evaluation:

1. Deploy the virtualised 5G environment using the deployment resources contained in this repository.
2. Instantiate the required VNFs using the supplied VNFD packages and deployment requests.
3. Deploy the forensic agents within the network functions.
4. Configure 5GDFRT forensic agents and the Elastic Stack for evidence collection.
5. Generate attack traffic using Ostinato or legitimate user traffic using UERANSIM.
6. Execute the machine learning detection pipeline.
7. Analyse the collected evidence using Kibana and the forensic dashboard.
8. Correlate collected evidence to reconstruct the sequence of events.

Detailed instructions for each scenario are provided in the corresponding experiment documentation.

---

# Purpose

The documentation contained within this directory serves as a practical companion to the PhD thesis. It enables researchers, practitioners, and students to understand how the prototype was evaluated, reproduce the experimental scenarios, and extend the work in future research on digital forensic readiness within virtualised 5G environments.


# Prerequisites

The experimental scenarios documented in this directory assume that the prototype has already been deployed and configured. Before attempting to reproduce the experiments, ensure that the following prerequisites have been satisfied.

## Hardware Requirements

The prototype was evaluated using commodity server hardware capable of supporting multiple virtual machines simultaneously. A system with the following minimum specifications is recommended:

| Component | Recommended Specification |
|----------|----------------------------|
| Processor | Multi-core 64-bit CPU with hardware virtualisation support (Intel VT-x or AMD-V) |
| Memory | Minimum 32 GB RAM (64 GB recommended for improved performance) |
| Storage | Minimum 500 GB available disk space (SSD recommended) |
| Network | Gigabit Ethernet connectivity |

> Note: The prototype can be deployed on systems with fewer resources; however, reducing available CPU cores or memory may limit the number of simultaneously instantiated Virtual Network Functions (VNFs) and affect experimental performance.

---

## Software Requirements

The prototype was implemented entirely using open-source technologies.

| Software | Purpose |
|----------|---------|
| Ubuntu Server | Host operating system |
| OpenStack | Network Function Virtualisation Infrastructure (NFVI) |
| OpenStack Tacker | VNF lifecycle management and orchestration |
| OpenAirInterface (OAI) | 5G Core implementation |
| UERANSIM | Simulated User Equipment (UE) and Radio Access Network (RAN) |
| Docker | Containerised deployment of selected services |
| Zeek | Network monitoring and protocol analysis |
| Elasticsearch | Centralised evidence storage |
| Logstash | Log ingestion and processing |
| Kibana | Evidence visualisation and analysis |
| Python | Machine learning services and backend processing |
| FastAPI | RESTful API services |
| React | Web-based dashboard |
| Git | Repository management |

---

## Prototype Components

The following repository directories are required to reproduce the experiments described in this directory.

| Directory | Purpose |
|----------|---------|
| `deployment/` | Infrastructure deployment scripts |
| `vnfd/` | Virtual Network Function Descriptor packages |
| `requests/` | OpenStack Tacker deployment requests |
| `detection/` | Machine learning detection module |
| `config/` | Configuration files |
| `docs/architecture/` | Prototype architecture documentation |

---

## Services Required

Before executing any experimental scenario, verify that the following services are operational:

- OpenStack cloud
- OpenStack Tacker
- OpenAirInterface 5G Core
- UERANSIM
- Zeek monitoring services
- Elastic Stack (Elasticsearch, Logstash and Kibana)
- Machine learning detection service
- FastAPI backend
- React dashboard

---

## Experimental Assumptions

The experiments documented in this directory assume that:

- the 5G Core Network has been successfully deployed;
- all required VNFs have been instantiated;
- forensic agents have been deployed within the selected network functions;
- Forensic agents are actively monitoring the required network interfaces;
- Elastic Stack is receiving and indexing Potential Digital Evidence (PDE);
- the machine learning detection module is connected to Elasticsearch through the REST API; and
- the dashboard is operational and capable of displaying detection results.

Once these prerequisites have been satisfied, the experimental scenarios described in this directory can be reproduced by following the individual experiment guides.