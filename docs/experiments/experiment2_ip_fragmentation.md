# Experiment 2 – Internet Protocol Fragmentation Attack

## Overview

This document describes the second experimental scenario used to evaluate the 5G Digital Forensic Readiness Tool (5GDFRT). The experiment demonstrates the prototype's ability to detect, collect, preserve, and analyse potential digital evidence generated during an Internet Protocol (IP) fragmentation attack within a virtualised 5G Network Function Virtualisation (NFV) environment.

Unlike volumetric Distributed Denial-of-Service (DDoS) attacks, fragmentation attacks exploit weaknesses in packet reassembly by transmitting malformed or overlapping IP fragments. Such attacks may evade conventional security mechanisms or disrupt network communication, making them particularly relevant in virtualised network environments.

This experiment evaluates the capability of the proposed forensic readiness architecture to capture evidence associated with protocol-level attacks while maintaining the integrity and availability of digital evidence for subsequent forensic investigation.

This experiment corresponds to Section 9.4 of the accompanying PhD thesis.

---

# Objective

The objectives of this experiment are to:

- demonstrate the generation of malicious fragmented IP traffic within the virtualised 5G environment;
- evaluate the ability of forensic agents to capture protocol-level anomalies associated with fragmented packets;
- verify that potential digital evidence (PDE) is preserved throughout the attack lifecycle;
- demonstrate automated detection using the integrated machine learning module; and
- provide investigators with sufficient forensic artefacts to reconstruct the attack sequence.

---

# Background

Internet Protocol fragmentation allows packets larger than the Maximum Transmission Unit (MTU) to be divided into smaller fragments for transmission across a network. Under normal operating conditions, these fragments are reassembled at the destination before being processed.

Attackers can exploit this mechanism by transmitting malformed, overlapping, or incomplete fragments designed to confuse packet reassembly, evade intrusion detection systems, or exhaust processing resources. Although modern operating systems have mitigated many historical fragmentation vulnerabilities, protocol fragmentation remains an important attack vector for evaluating forensic readiness because it generates distinctive network behaviours that should be captured as digital evidence.

Within the 5GDFRT, forensic agents continuously monitor network traffic to ensure that evidence relating to fragmented packets is collected and preserved regardless of whether the attack ultimately succeeds.

---

# Experimental Environment

The experiment was conducted using the same OpenStack-based virtualised 5G environment employed throughout the prototype evaluation.

## Infrastructure

| Component | Purpose |
|----------|---------|
| OpenStack | NFV Infrastructure |
| OpenStack Tacker | VNF orchestration |
| OpenAirInterface | 5G Core |
| UERANSIM | Simulated UE and RAN |
| Packet generation tools | Generation of fragmented IP traffic |
| Zeek | Network traffic monitoring |
| Elastic Stack | Evidence collection and visualisation |
| Random Forest | Machine learning attack classification |

---

# Repository Components

The following repository directories are used during this experiment.

| Directory | Purpose |
|----------|---------|
| deployment/ | Deployment scripts for the experimental environment |
| vnfd/ | Virtual Network Function Descriptor packages |
| requests/ | VNF deployment requests |
| detection/ | Machine learning detection pipeline |
| config/ | Configuration files for monitoring services |
| docs/architecture/ | Architecture documentation |

---

# Attack Generation

The attack is performed by generating intentionally fragmented IP packets containing malformed or overlapping fragment offsets. The fragmented traffic is transmitted through the virtualised 5G infrastructure towards selected network functions while legitimate user traffic continues to flow through the environment.

The objective is not to overwhelm the network with traffic volume but rather to trigger protocol-level anomalies that can be observed by the forensic monitoring infrastructure.

Throughout the experiment, forensic agents continue collecting network events while Zeek analyses protocol behaviour and forwards structured evidence to the Elastic Stack.

---

# Evidence Collection Workflow

During the experiment, the following workflow is executed:

1. Normal 5G communication is established using simulated user equipment.
2. Malicious fragmented IP packets are transmitted through the virtualised network.
3. Zeek analyses packet fragmentation behaviour.
4. Forensic agents collect protocol-related evidence.
5. Evidence is securely transmitted to Logstash.
6. Elasticsearch indexes the collected evidence.
7. Kibana visualises protocol anomalies.
8. The Random Forest classifier analyses extracted network features.
9. The dashboard presents detected attacks together with associated confidence scores.

---

# Expected Outputs

Successful execution of this experiment should produce:

- Zeek protocol analysis logs;
- fragmented packet metadata;
- Elastic Stack evidence records;
- machine learning classification results;
- dashboard alerts;
- preserved forensic evidence with associated metadata;
- cryptographic integrity information;
- exported forensic reports.

---

# Key Forensic Artefacts

Investigators should expect to obtain evidence including:

- IP fragment identifiers;
- fragment offsets;
- fragmentation flags;
- packet timestamps;
- source and destination IP addresses;
- protocol metadata;
- Zeek log entries;
- Elastic Stack records;
- machine learning prediction labels;
- confidence scores;
- event identifiers.

These artefacts collectively support reconstruction of protocol-level attack activity within the virtualised 5G environment.

---

# Reproducing the Experiment

To reproduce this experiment:

1. Deploy the prototype environment.
2. Instantiate the required VNFs.
3. Verify that forensic agents are operational.
4. Start the Elastic Stack.
5. Establish normal 5G communication using UERANSIM.
6. Generate fragmented IP traffic using the configured packet generation tool.
7. Monitor protocol events in Kibana.
8. Verify machine learning detection results.
9. Export forensic reports if required.

---

# Related Thesis Section

This experiment documents the implementation corresponding to:

- Chapter 9
- Section 9.4 – Experiment Scenario 2: Internet Protocol Fragmentation Attack

Readers interested in the detailed experimental methodology, results, and forensic interpretation should consult the corresponding section of the thesis.

---

# Repository References

- adeployment/`
- `vnfd/`
- `requests/`
- `detection/`
- `config/`
- `docs/architecture/`