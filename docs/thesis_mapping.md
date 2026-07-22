# Thesis-to-Repository Mapping

## Overview

This repository accompanies the PhD thesis entitled:

> A Digital Forensic Readiness Model for 5G Network Function Virtualisation (NFV) Environments

The purpose of this document is to provide a clear mapping between the thesis and the implementation contained within this repository. While the thesis presents the research problem, proposed model, system architecture, implementation, and evaluation, this repository contains the prototype implementation, deployment artefacts, configuration files, and supporting documentation required to reproduce the work.

This mapping enables readers to quickly locate the implementation corresponding to a particular chapter, figure, experiment, or prototype component discussed in the thesis.

---

# Repository Structure

The repository is organised into logical components that reflect the architecture and implementation presented throughout the thesis.

| Repository Directory | Description |
|----------------------|-------------|
| `deployment/` | Deployment scripts and infrastructure resources used to instantiate the experimental environment. |
| `vnfd/` | Virtual Network Function Descriptor (VNFD) packages used by OpenStack Tacker. |
| `requests/` | Tacker deployment requests used to instantiate Virtual Network Functions (VNFs). |
| `detection/` | Machine learning detection subsystem, forensic dashboard, and analytical services. |
| `config/` | Configuration files for monitoring, logging, and supporting services. |
| `docs/` | Repository documentation, architecture descriptions, deployment guides, and experiment documentation. |

---

# Chapter Mapping

The following table maps each major chapter of the thesis to the corresponding repository components.

| Thesis Chapter | Repository Components |
|----------------|----------------------|
| Chapter 1 – Introduction | Project overview provided in the repository `README.md`. |
| Chapter 2 – Literature Review | No direct implementation. This chapter provides the theoretical foundation for the research. |
| Chapter 3 – Research Methodology | Reflected indirectly through the repository organisation and experimental documentation. |
| Chapter 4 – 5G NFV Digital Forensic Readiness Requirements | Implemented through the architectural design documented in `docs/architecture/`. |
| Chapter 5 – Existing Digital Forensic Readiness Models | No direct implementation. This chapter informs the design decisions adopted within the prototype. |
| Chapter 6 – Proposed Digital Forensic Readiness Model | Implemented through the overall prototype architecture and workflow documented throughout the repository. |
| Chapter 7 – Prototype Design | Corresponds to the architectural documentation contained within `docs/architecture/`. |
| Chapter 8 – Prototype Implementation | Implemented throughout the repository, particularly within `deployment/`, `vnfd/`, `requests/`, `config/`, and `detection/`. |
| Chapter 9 – Prototype Demonstration and Experimental Evaluation | Documented within `docs/experiments/`. |
| Chapter 10 – Conclusions and Future Work | Reflected in the repository roadmap and future enhancements described in the project documentation. |

---

# Prototype Component Mapping

The major prototype components described in the thesis correspond to the following repository locations.

| Prototype Component | Repository Location |
|---------------------|--------------------|
| 5G Testbed Deployment | `deployment/` |
| OpenStack Tacker Deployment Resources | `requests/` |
| Virtual Network Function Descriptors | `vnfd/` |
| Machine Learning Detection Module | `detection/` |
| Forensic Dashboard | `detection/` |
| Configuration Resources | `config/` |
| Experimental Documentation | `docs/experiments/` |
| Architecture Documentation | `docs/architecture/` |

---

# Experimental Evaluation Mapping

The experimental scenarios presented in Chapter 9 are documented separately to improve reproducibility.

| Thesis Section | Repository Document |
|----------------|---------------------|
| Section 9.3 – Distributed DoS Ping Flood Attack | `docs/experiments/experiment1_ddos_ping_flood.md` |
| Section 9.4 – Internet Protocol Fragmentation Attack | `docs/experiments/experiment2_ip_fragmentation.md` |
| Section 9.5 – Machine Learning-Based Digital Evidence Analysis | `docs/experiments/machine_learning_analysis.md` |
| Section 9.6 – Event Reconstruction | `docs/experiments/experiment3_event_reconstruction.md` |

---

# Architecture Documentation Mapping

The architectural descriptions presented within the thesis are supplemented by the documentation contained in the repository.

| Repository Document | Purpose |
|---------------------|---------|
| `docs/architecture/README.md` | Overview of the prototype architecture. |
| `docs/experiments/README.md` | Overview of the experimental evaluation. |
| Individual experiment guides | Detailed procedures for reproducing each experimental scenario. |

---

# Reproducibility Mapping

The repository contains the artefacts required to reproduce the prototype implementation and experimental evaluation.

| Repository Component | Supports |
|----------------------|----------|
| Deployment scripts | Infrastructure provisioning |
| VNFD packages | Network Function deployment |
| Configuration files | Service configuration |
| Detection module | Automated evidence analysis |
| Experiment documentation | Reproduction of Chapter 9 experiments |
| Architecture documentation | Understanding prototype design |

---

# Publications

This repository accompanies the research presented in:

> A Digital Forensic Readiness Model for 5G Network Function Virtualisation (NFV) Environments

Additional publications derived from this research may reference specific components of this repository.

---

# Citation

If you use this repository in your research, please cite the accompanying PhD thesis together with any associated journal or conference publications arising from this work.

---

# Contact

Questions regarding the implementation, prototype, or experimental evaluation may be directed through the GitHub Issues page for this repository.