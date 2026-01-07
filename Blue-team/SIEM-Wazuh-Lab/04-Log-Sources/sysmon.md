# Sysmon Configuration and Usage

## Overview

Sysmon (System Monitor) is a Windows system service and device driver developed by Microsoft Sysinternals.  
It provides detailed telemetry about system activity, which is essential for threat detection and incident investigation in a SIEM environment.

In this project, Sysmon is used to enhance Windows logging and provide high-fidelity events to the Wazuh SIEM.

---

## Why Sysmon is Used in This Project

Default Windows logs often lack the level of detail required for effective security monitoring.  
Sysmon complements native logs by providing:

- Detailed process creation events
- Full command-line arguments
- Parent-child process relationships
- File hash values
- Network connection visibility
- Registry modification tracking

This data enables behavioral-based detection and advanced threat hunting.

---

## Sysmon Installation

Sysmon was installed on the Windows endpoint with a hardened configuration based on the **SwiftOnSecurity** Sysmon configuration.

### Installation Command

```powershell

