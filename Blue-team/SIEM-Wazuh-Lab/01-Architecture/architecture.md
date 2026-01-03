# SIEM Architecture Overview

## 1. Overview

This project implements a Security Information and Event Management (SIEM)
laboratory using Wazuh to collect, analyze, and correlate security events
from Windows and Linux endpoints.

The objective is to simulate a real SOC environment by deploying a SIEM,
collecting endpoint telemetry, creating detection use cases mapped to
MITRE ATT&CK, and performing threat hunting and attack simulation.

---

## 2. Components

The architecture is composed of the following components:

### Ubuntu Server (SIEM)
- Hosts the Wazuh Manager, Indexer, and Dashboard
- Deployed using Docker and Docker Compose
- Centralizes log collection and alerting

### Windows 10 Endpoint
- Monitored endpoint generating security events
- Runs the Wazuh Agent
- Uses Sysmon with SwiftOnSecurity configuration for enhanced telemetry

### Automation Layer
- Custom Python scripts for log parsing and detection logic
- Implements a detection-as-code approach
- Enables testing detections outside of the SIEM

---

## 3. Network Architecture

The environment is deployed within a VirtualBox virtual network.

- Ubuntu SIEM VM IP: 192.168.1.137
- Windows 10 Endpoint: Same subnet (dynamic IP)

All communications between endpoints and the SIEM occur over the internal
virtual network to ensure isolation and security.

---

## 4. Log Collection Flow

1. Security-related activities occur on the Windows endpoint.
2. Sysmon logs detailed events such as:
   - Process creation
   - Network connections
   - Registry modifications
3. Windows Security logs capture authentication and privilege events.
4. The Wazuh Agent collects Sysmon and Windows Security logs.
5. Logs are forwarded to the Wazuh Manager on the Ubuntu server.
6. Events are indexed by the Wazuh Indexer.
7. Alerts and logs are visualized in the Wazuh Dashboard.

---

## 5. Detection and Analysis

Detection is performed at multiple layers:

- Built-in Wazuh detection rules
- Custom detection use cases mapped to MITRE ATT&CK
- Behavioral analysis based on endpoint telemetry

Each detection use case is validated through controlled attack simulations.

---

## 6. Automation and Detection Engineering

In addition to SIEM-based detections, an automation layer is implemented
using Python.

- Parsers normalize raw log data
- Detection modules apply custom logic (e.g., brute force detection)
- A main orchestrator simulates a SOC detection pipeline

This demonstrates a detection-engineering workflow similar to real SOC
environments.

---

## 7. Security Considerations

- The lab environment is isolated from production systems
- Communications between components use encrypted channels
- Attack simulations are executed in a controlled environment only
- Default credentials are changed after deployment

---

## 8. Architecture Diagram

An architecture diagram illustrating the components and log flow
is provided in the following file:

- architecture_diagram.png
