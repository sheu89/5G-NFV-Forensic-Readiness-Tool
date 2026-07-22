# Deployment Requests

## Overview

This directory contains the JSON request files used to instantiate Virtual Network Functions (VNFs) using OpenStack Tacker.

Separate request sets are provided for multiple prototype versions developed during the research.

## Versions

| Version | Description |
|----------|-------------|
| v4 | Initial distributed deployment |
| v5 | Enhanced deployment including external data network |
| v6 | Final prototype evaluated in the PhD research |

Each request file defines the parameters required to instantiate a specific VNF through the Tacker API.

The accompanying shell scripts automate sequential deployment of the complete experimental environment.