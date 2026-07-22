# Virtual Network Function Descriptors (VNFDs)

## Overview

This directory contains the ETSI-compliant Virtual Network Function Descriptors (VNFDs) used to deploy the virtualised 5G core network within the OpenStack Tacker orchestration environment.

Each network function is packaged independently to enable flexible deployment and orchestration.

## Included VNFs

- AMF
- AUSF
- NRF
- UDM
- UDR
- SMF
- UPF
- ELK
- UERANSIM
- External Data Network
- All-in-One deployment

Each VNFD contains:

- TOSCA definitions
- HOT templates
- UserData scripts
- Package scripts

## Purpose

These descriptors form the infrastructure layer of the proposed Digital Forensic Readiness Framework by enabling automated deployment of evidence-producing virtual network functions.