# Windows Endpoint Configuration

## Overview

This document describes the configuration of the Windows endpoint monitored within the SIEM lab.  
The endpoint simulates a corporate workstation and serves as the primary source of security telemetry for detection and threat hunting activities.

---

## Endpoint Purpose

The Windows endpoint is designed to:

- Generate realistic security events
- Simulate attacker techniques and user behavior
- Provide telemetry for detection use cases
- Support threat hunting and MITRE ATT&CK mapping

It represents a typical user workstation in a SOC monitoring scenario.

---

## Operating System

- Windows 10 (Workstation)
- Local user and administrative accounts configured
- System hardened only at baseline level to allow attack simulation

---

## Installed Security Components

### Wazuh Agent
- Installed and registered with the Wazuh Manager
- Responsible for forwarding endpoint logs and telemetry

### Sysmon
- Installed with a custom configuration file
- Provides detailed visibility into system activity

Sysmon enables advanced detections such as:
- Process creation tracking
- Parent-child process relationships
- Command-line analysis
- Registry persistence mechanisms

---

## Logging Configuration

The following log sources are enabled and collected:

### Windows Event Logs
- Security
- System
- Application

### Sysmon Event Log
- Microsoft-Windows-Sysmon/Operational

Logging is configured to ensure sufficient visibility without excessive noise.

---

## Attack Simulation Readiness

The endpoint is intentionally configured to allow the simulation of:

- Encoded PowerShell execution
- Brute force authentication attempts
- Lateral movement using administrative tools
- Persistence via registry autorun keys

These simulations support the development and validation of detection use cases.

---

## Role in Detection & Threat Hunting

The Windows endpoint provides the raw telemetry required for:

- Detection rule development
- Correlation across log sources
- Hypothesis-driven threat hunting
- Validation of MITRE ATT&CK techniques

Without endpoint visibility, behavioral detections would not be possible.

---

## Conclusion

The Windows endpoint is a foundational component of the SIEM lab.  
It enables realistic monitoring, detection engineering, and SOC analyst workflows by generating high-quality security data.
