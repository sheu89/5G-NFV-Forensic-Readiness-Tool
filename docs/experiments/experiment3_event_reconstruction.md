# Experiment 3 – Event Reconstruction

## Overview

This document describes the third experimental scenario used to evaluate the 5G Digital Forensic Readiness Tool (5GDFRT). The experiment demonstrates the prototype's ability to reconstruct complete forensic timelines by correlating Potential Digital Evidence (PDE) collected from multiple Virtual Network Functions (VNFs) within a virtualised 5G Network Function Virtualisation (NFV) environment.

Unlike the previous experiments, which focus primarily on attack generation and automated detection, this experiment demonstrates how the collected evidence can be analysed collectively to reconstruct the sequence of events leading to a security incident. By correlating network events, application logs, signalling messages, and user activity, investigators are provided with a comprehensive timeline that supports digital forensic investigations.

This experiment corresponds to Section 9.6 of the accompanying PhD thesis.

---

# Objective

The objectives of this experiment are to:

- demonstrate the reconstruction of forensic timelines using evidence collected throughout the prototype;
- correlate evidence originating from multiple 5G Network Functions (VNFs);
- validate that the forensic readiness architecture preserves sufficient evidence for post-incident investigation;
- demonstrate how machine learning predictions complement traditional forensic analysis; and
- provide investigators with a unified view of events occurring throughout the attack lifecycle.

---

# Background

Digital forensic investigations rarely rely on a single source of evidence. Instead, investigators reconstruct incidents by correlating evidence collected from multiple systems, network devices, applications, and communication protocols.

Within virtualised 5G environments, this process becomes considerably more complex because subscriber activity, signalling traffic, user-plane communication, authentication procedures, and service interactions are distributed across numerous virtual network functions.

The 5GDFRT addresses this challenge by continuously collecting and preserving Potential Digital Evidence (PDE) from multiple monitoring points, enabling investigators to reconstruct complex attack scenarios after an incident has occurred.

---

# Experimental Environment

The experiment uses the same OpenStack-based virtualised 5G infrastructure employed throughout the prototype evaluation.

## Infrastructure

| Component | Purpose |
|----------|---------|
| OpenStack | NFV Infrastructure |
| OpenStack Tacker | VNF orchestration |
| OpenAirInterface | 5G Core |
| UERANSIM | Simulated UE and RAN |
| Zeek | Network monitoring |
| Elastic Stack | Centralised evidence repository |
| Random Forest | Automated attack classification |
| Forensic Dashboard | Evidence visualisation and investigation |

---

# Repository Components

The following repository directories are utilised during this experiment.

| Directory | Purpose |
|----------|---------|
| `deployment/` | Prototype deployment resources |
| `vnfd/` | VNF descriptors |
| `requests/` | Deployment requests |
| `detection/` | Machine learning detection module |
| `config/` | Configuration files |
| `docs/architecture/` | Architecture documentation |

---

# Evidence Sources

The forensic timeline is reconstructed by correlating evidence collected from multiple sources throughout the virtualised 5G environment.

Primary evidence sources include:

- Zeek network monitoring logs;
- HTTP/2 signalling traffic;
- OpenAirInterface service logs;
- AMF events;
- SMF events;
- UPF traffic records;
- NRF registration events;
- AUSF authentication logs;
- UDM subscriber information;
- Machine learning prediction results; and
- Dashboard event records.

Each evidence source contributes a different perspective of the incident, allowing investigators to reconstruct the complete sequence of events.

---

# Event Correlation Workflow

The reconstruction process follows the workflow below.

1. Potential Digital Evidence (PDE) is collected from multiple VNFs.
2. Evidence is securely forwarded to the Elastic Stack.
3. Records are indexed and timestamped.
4. Machine learning predictions are associated with relevant evidence.
5. Related events are correlated using shared identifiers and timestamps.
6. The reconstructed timeline is presented through the forensic dashboard.
7. Investigators analyse the timeline to determine the progression of the incident.

---

# Timeline Reconstruction

The reconstructed timeline enables investigators to observe the progression of an incident from its initial stages through to its conclusion.

Typical events represented within the timeline include:

- UE registration;
- authentication procedures;
- network function registration;
- PDU session establishment;
- signalling exchanges;
- application requests;
- malicious activity;
- machine learning detections;
- evidence preservation; and
- post-incident analysis.

By correlating these events chronologically, investigators can determine how an attack developed and identify the network functions involved.

---

# Expected Outputs

Successful execution of this experiment should produce:

- reconstructed forensic timelines;
- correlated network events;
- subscriber activity records;
- machine learning predictions;
- indexed Elasticsearch evidence;
- dashboard visualisations;
- chronological event sequences; and
- forensic investigation reports.

---

# Key Forensic Artefacts

Investigators should expect to obtain artefacts including:

- timestamps;
- subscriber identifiers (e.g., IMSI where applicable);
- session identifiers;
- HTTP/2 transaction records;
- signalling messages;
- authentication events;
- network function identifiers;
- protocol metadata;
- machine learning prediction labels;
- confidence scores; and
- correlated event identifiers.

These artefacts collectively enable investigators to reconstruct complex incidents occurring within the virtualised 5G environment.

---

# Reproducing the Experiment

To reproduce this experiment:

1. Deploy the prototype environment.
2. Instantiate the required 5G Network Functions.
3. Verify that forensic agents are operational.
4. Generate network activity or execute one of the supported attack scenarios.
5. Allow evidence to be collected by the monitoring infrastructure.
6. Verify that evidence is indexed within Elasticsearch.
7. Execute the machine learning analysis.
8. Open the forensic dashboard.
9. Analyse the reconstructed timeline.
10. Export forensic reports where required.

---

# Related Thesis Section

This document corresponds to:

- Chapter 9
- Section 9.6 – Experiment Scenario 3: Event Reconstruction

Readers interested in the detailed experimental methodology, reconstructed timelines, and forensic interpretation should consult the corresponding section of the thesis.

---

# Repository References

- `deployment/`
- `vnfd/`
- `requests/`
- `detection/`
- `config/`
- `docs/architecture/`
- `docs/architecture/`