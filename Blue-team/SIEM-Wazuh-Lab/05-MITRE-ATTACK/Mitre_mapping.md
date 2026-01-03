# MITRE ATT&CK Mapping

## Overview

This document maps the detection use cases implemented in this SIEM project
to the MITRE ATT&CK framework. Each use case is designed to detect real-world
adversary behaviors and is validated through attack simulation.

The goal is to demonstrate a structured detection engineering approach aligned
with industry-standard threat modeling.

---

## ATT&CK Matrix Scope

- Platform: Windows
- Tactics covered:
  - Initial Access
  - Execution
  - Persistence
  - Privilege Escalation
  - Lateral Movement
  - Credential Access
  - Command and Control

---

## Detection Use Case Mapping

### T1059.001 – PowerShell Command Execution

- Tactic: Execution
- Description:
  Detects suspicious PowerShell execution using encoded commands, a common
  technique used to evade detection.
- Log Sources:
  - Sysmon Event ID 1 (Process Create)
- Detection Method:
  - Command-line analysis for `-EncodedCommand`
- Validation:
  - Simulated encoded PowerShell execution on the Windows endpoint

---

### T1569.002 – Service Execution (PsExec)

- Tactic: Lateral Movement
- Description:
  Detects the use of PsExec for remote command execution and lateral movement.
- Log Sources:
  - Sysmon Event ID 1 (Process Create)
  - Windows Service Creation Events
- Detection Method:
  - Detection of `psexec.exe`
  - Detection of `PSEXESVC` service creation
- Validation:
  - PsExec execution simulation

---

### T1078 – Valid Accounts

- Tactic: Persistence / Privilege Escalation
- Description:
  Detects suspicious creation of privileged accounts that may indicate
  compromised credentials or persistence.
- Log Sources:
  - Windows Security Event IDs 4720, 4672
- Detection Method:
  - Correlation of account creation and privilege assignment
- Validation:
  - Creation of a new administrator account

---

### T1547.001 – Registry Run Keys / Startup Folder

- Tactic: Persistence
- Description:
  Detects persistence mechanisms using Windows Run registry keys.
- Log Sources:
  - Sysmon Event ID 13 (Registry Modification)
- Detection Method:
  - Monitoring of autorun registry paths
- Validation:
  - Registry Run key modification simulation

---

### T1110 – Brute Force

- Tactic: Credential Access
- Description:
  Detects brute force authentication attempts based on repeated failed logins.
- Log Sources:
  - Windows Security Event ID 4625
  - Custom parsed authentication logs
- Detection Method:
  - Threshold-based detection using Python automation
- Validation:
  - Simulated multiple failed authentication attempts

---

## Automation-Based Detection Mapping

In addition to SIEM rules, certain detections are implemented using
custom Python scripts following a detection-as-code approach.

| Script            | Technique | Description                     |
|------------------|----------|---------------------------------|
| brute_force.py   | T1110    | Brute force detection logic     |
| linux_parser.py  | N/A      | Log normalization and parsing   |
| main.py          | N/A      | Detection pipeline orchestration|

---

## Coverage Summary

This project demonstrates detection coverage across multiple ATT&CK tactics
using both SIEM-based and custom detection logic. Each technique is validated
through controlled attack simulation to ensure detection effectiveness.

---

## Future Improvements

- Expand coverage to Linux ATT&CK techniques
- Add command and control (C2) detection use cases
- Integrate additional credential access techniques
- Automate MITRE coverage reporting
