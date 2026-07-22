# Deployment

## Overview

The `deployment` directory contains the deployment configurations used to instantiate the experimental 5G Network Function Virtualisation (NFV) forensic readiness environment developed for this research.

The configurations support multiple deployment scenarios, ranging from lightweight testing environments to complete OpenAirInterface (OAI) deployments integrated with forensic monitoring components.

## Directory Structure

| Folder | Description |
|---------|-------------|
| elk | ELK stack deployment (Elasticsearch, Logstash and Kibana). |
| oai | OpenAirInterface deployment configuration. |
| user_plane_testing | Testbed used for validating user-plane traffic monitoring. |
| forensic_agent_testing | Environment for validating the 5GDFRT forensic agent. |
| openstack | Placeholder for OpenStack deployment documentation. |
| tacker | Placeholder for OpenStack Tacker orchestration documentation. |

## Purpose

These deployment configurations were developed to support the experimental evaluation described in the PhD thesis. They demonstrate how forensic evidence can be collected from virtualised 5G core network functions while maintaining a realistic NFV deployment architecture.