# System Architecture

## Overview

This directory contains the architectural diagrams that support the design, implementation, and deployment of the 5G Digital Forensic Readiness Tool (5GDFRT) developed during this PhD research.

The figures illustrate the evolution of the prototype, the interaction between the major software components, and the deployment topology used throughout the experimental evaluation.

The architecture was designed to enable forensic readiness within virtualised 5G Network Function Virtualisation (NFV) environments by integrating network monitoring, evidence collection, machine learning-based attack detection, and forensic reporting.

---

## Architecture Diagrams

| Figure | Description |
|--------|-------------|
| Figure 7.1 | Overall architecture of the proposed Digital Forensic Readiness Framework, illustrating the interaction between the 5G infrastructure, forensic collection components, evidence repository, and reporting modules. |
| Figure 7.2 | Prototype implementation architecture showing the software components that realise the proposed framework within the OpenStack NFV environment. |
| Figure 7.3 | End-to-end forensic workflow demonstrating how network traffic is captured, processed, analysed, and transformed into forensic evidence. |
| Figure 7.4 | Machine learning detection workflow illustrating feature extraction, classification, and attack identification within the detection pipeline. |
| Figure 7.5 | Integrated deployment architecture showing the interaction between OpenAirInterface, OpenStack Tacker, Zeek, ELK Stack, and the forensic readiness components. |
| compose_development.png | Docker Compose deployment architecture used during prototype implementation and integration testing. |
| RAN_UE_Simulation.png | Simulation environment used to emulate user equipment (UE) and radio access network (RAN) traffic during experimentation. |
| V6_Config_HL.png | High-level deployment topology of the final Version 6 prototype evaluated in the thesis. |

---

## Relationship to the Repository

The architectural components shown in these figures correspond directly to the repository structure:

| Repository Directory | Architectural Role |
|----------------------|--------------------|
| `deployment/` | Deployment and orchestration of prototype components |
| `vnfd/` | Virtual Network Function Descriptors used by OpenStack Tacker |
| `requests/` | Deployment requests submitted to Tacker |
| `detection/` | Machine learning detection engine and dashboard |
| `sample_logs/` | Example evidence collected during experimentation |
| `config/` | Configuration files for Zeek, ELK Stack, Filebeat, and related services |

---

## Relationship to the Thesis

The architectural diagrams contained within this directory correspond primarily to Chapter 7 (Prototype Design and Implementation) of the PhD thesis.

Together, they document the design decisions that support the implementation of the proposed Digital Forensic Readiness Framework and provide the architectural context for the experiments presented in the subsequent chapters.

---

## Purpose

These diagrams are intended to assist researchers in understanding the overall design of the prototype and to facilitate reproduction, extension, or adaptation of the forensic readiness framework in other virtualised 5G environments.