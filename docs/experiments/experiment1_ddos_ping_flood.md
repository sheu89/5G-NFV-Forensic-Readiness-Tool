# Experiment 1 – Distributed DoS Ping Flood Attack

## Overview

This document describes the first experimental scenario used to evaluate the 5G Digital Forensic Readiness Tool (5GDFRT). The experiment demonstrates the prototype's ability to detect, collect, preserve, and analyse potential digital evidence generated during a distributed Internet Control Message Protocol (ICMP) ping flood attack against a virtualised 5G network.

The experiment reproduces a common Distributed Denial-of-Service (DDoS) attack within the OpenStack-based 5G testbed. Rather than focusing solely on attack detection, the evaluation demonstrates how the proposed forensic readiness architecture continuously captures, preserves, and correlates digital evidence for subsequent forensic investigation.

This experiment corresponds to Section 9.3 of the accompanying PhD thesis.

---

# Objective

The objectives of this experiment are to:

- demonstrate the generation of a distributed ICMP ping flood attack within the virtualised 5G environment;
- evaluate the ability of the forensic agents to capture potential digital evidence (PDE) generated during the attack;
- verify that evidence is securely transported to the Elastic Stack without interruption;
- demonstrate automated attack detection using the integrated machine learning module; and
- provide investigators with sufficient artefacts to support subsequent forensic analysis.

---

# Background

Distributed Denial-of-Service (DDoS) attacks remain one of the most common threats against modern communication networks. A ping flood attack overwhelms a target by transmitting a large volume of ICMP Echo Request packets, consuming processing resources and degrading normal network operation.

Within the experimental environment, attack traffic is directed towards the User Plane Function (UPF), which is responsible for forwarding user traffic between the Radio Access Network (RAN) and external data networks. Because all user-plane traffic traverses the UPF, it provides an ideal observation point for forensic evidence collection.

Unlike conventional intrusion detection systems, the 5GDFRT continuously captures and preserves evidence throughout the attack lifecycle, ensuring that investigators can reconstruct events after the incident has occurred.

---

# Experimental Environment

The experiment uses the prototype environment described in Chapters 7 and 8 of the thesis.

## Infrastructure

| Component | Purpose |
|----------|---------|
| OpenStack | NFV Infrastructure |
| OpenStack Tacker | VNF orchestration |
| OpenAirInterface | 5G Core |
| UERANSIM | Simulated UE and RAN |
| Ostinato | Attack traffic generation |
| Zeek | Network monitoring |
| Elastic Stack | Evidence collection and visualisation |
| Random Forest | Machine learning attack classification |

---

# Repository Components

The following repository directories are used during this experiment.

| Directory | Purpose |
|----------|---------|
| deployment/ | Deploys the experimental environment |
| vnfd/ | Virtual Network Function Descriptors |
| requests/ | Tacker deployment requests |
| detection/ | Machine learning detection pipeline |
| config/ | Configuration files |
| docs/architecture/ | Architecture documentation |

---

# Attack Generation

The attack is generated using Ostinato, which transmits high-volume ICMP Echo Request packets through multiple simulated User Equipment (UE) instances created using UERANSIM.

Each simulated UE establishes a Packet Data Unit (PDU) session with the 5G Core before participating in the attack, creating a realistic traffic environment in which both legitimate and malicious traffic coexist.

The attack targets the User Plane Function (UPF), resulting in a substantial increase in packet-processing activity while forensic agents continuously monitor network events.

---

# Evidence Collection Workflow

During the experiment, the following workflow is executed:

1. UE and RAN simulation establish normal 5G communication.
2. Ostinato initiates the distributed ICMP ping flood.
3. Zeek monitors network traffic.
4. Forensic agents collect potential digital evidence.
5. Evidence is securely forwarded to Logstash.
6. Elasticsearch indexes the collected evidence.
7. Kibana visualises the captured events.
8. The Random Forest classifier analyses extracted network features.
9. The dashboard presents detected attacks and associated confidence scores.

---

# Expected Outputs

Successful execution of this experiment should produce:

- Forensic agent network logs;
- packet-processing statistics from the UPF;
- indexed Elastic Stack records;
- machine learning detection results;
- dashboard alerts;
- preserved forensic evidence with associated metadata;
- cryptographic integrity information;
- exported forensic reports.

---

# Key Forensic Artefacts

Investigators should expect to obtain evidence including:

- packet timestamps;
- source and destination IP addresses;
- ICMP protocol information;
- packet counts;
- traffic spikes;
- Zeek log files;
- Elastic Stack records;
- machine learning classification labels;
- confidence scores;
- event identifiers.

These artefacts collectively support subsequent event reconstruction and forensic investigation.

---

# Reproducing the Experiment

To reproduce this experiment:

1. Deploy the prototype environment.
2. Instantiate all required VNFs.
3. Verify that forensic agents are operational.
4. Start the Elastic Stack.
5. Launch UERANSIM.
6. Configure Ostinato packet streams.
7. Execute the ICMP ping flood.
8. Monitor evidence collection in Kibana.
9. Verify machine learning detection results.
10. Export forensic reports if required.

---

# Related Thesis Section

This experiment documents the implementation corresponding to:

- Chapter 9
- Section 9.3 – Experiment Scenario 1: Distributed Denial-of-Service Ping Flood Attack

Readers interested in the experimental results, discussion, and forensic interpretation should consult the corresponding section of the thesis.