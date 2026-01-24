# Wazuh Agent Configuration

## Overview

The Wazuh agent is installed on the Windows endpoint to collect, monitor, and forward security-relevant telemetry to the Wazuh SIEM platform.  
It acts as the primary data collector on the endpoint and enables real-time detection and threat hunting.

---

## Agent Role in the SIEM Architecture

The Wazuh agent is responsible for:

- Collecting Windows Security, System, and Application logs
- Forwarding Sysmon events for advanced process-level visibility
- Monitoring file integrity and system activity
- Sending events securely to the Wazuh Manager for analysis and correlation

This agent-based approach ensures reliable and structured log collection from the endpoint.

---

## Installation

The Wazuh agent was installed on a Windows workstation using the official Wazuh installer.

Key steps:
- Installation of the Windows agent package
- Registration of the agent with the Wazuh Manager
- Assignment of a unique agent ID
- Verification of secure communication with the manager

---

## Log Collection Configuration

The agent is configured to collect the following log sources:

### Windows Event Logs
- Security
- System
- Application

### Sysmon Logs
- Microsoft-Windows-Sysmon/Operational

Sysmon events provide enhanced visibility into:
- Process creation (Event ID 1)
- Network connections
- Registry modifications
- Image loading and process relationships

---

## Communication with Wazuh Manager

- The agent communicates with the Wazuh Manager deployed on an Ubuntu server
- Events are sent over a secure channel
- The manager performs decoding, rule matching, and alert generation

This separation ensures scalability and centralized security monitoring.

---

## Detection Enablement

By forwarding enriched endpoint telemetry, the Wazuh agent enables:

- Behavioral detections (PowerShell abuse, lateral movement, persistence)
- Correlation between multiple log sources
- Mapping of alerts to MITRE ATT&CK techniques
- Manual threat hunting and hypothesis-driven analysis

---

## Limitations and Considerations

- Detection quality depends on endpoint configuration (Sysmon rules, logging level)
- High verbosity may increase log volume
- False positives must be tuned at the SIEM level

These considerations are addressed through detection tuning and iterative improvement.

---

## Conclusion

The Wazuh agent is a critical component of the SIEM architecture, bridging the endpoint and the detection engine.  
Proper configuration of the agent ensures high-quality telemetry and effective security monitoring.
