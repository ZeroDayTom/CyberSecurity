# Attack Simulation

## Overview

This document describes the attack simulations performed in the SIEM lab.  
These simulations are used to generate realistic malicious activity in order to validate detections, threat hunting hypotheses, and MITRE ATT&CK mappings.

All attacks are executed in a controlled lab environment for educational purposes only.

---

## Objectives

The main objectives of attack simulation are to:

- Generate realistic attacker behaviors
- Validate detection use cases
- Test log visibility and coverage
- Support threat hunting activities
- Map observed behavior to MITRE ATT&CK techniques

---

## Attack Simulation Environment

- Attacker Machine: Windows / Linux (local lab)
- Victim Endpoint: Windows 10 with Wazuh Agent and Sysmon
- SIEM Platform: Wazuh (Single-node deployment)
- Log Collection: Windows Event Logs + Sysmon

---

## Simulated Attack Scenarios

### Attack 1: Encoded PowerShell Execution

**Description:**  
PowerShell is executed using encoded commands to evade basic detection mechanisms.

**Technique:**  
- MITRE ATT&CK: T1059.001 – PowerShell

**Simulation Method:**  
- PowerShell launched with `-EncodedCommand`
- Obfuscated command line

**Expected Telemetry:**  
- Sysmon Event ID 1 (Process Create)
- PowerShell command-line arguments

**Related Use Case:**  
- UC01 – Encoded PowerShell Execution

---

### Attack 2: Brute Force Authentication Attempts

**Description:**  
Multiple failed authentication attempts are generated to simulate a brute force or password spraying attack.

**Technique:**  
- MITRE ATT&CK: T1110 – Brute Force

**Simulation Method:**  
- Repeated invalid login attempts
- Targeting a single or multiple user accounts

**Expected Telemetry:**  
- Windows Security Event ID 4625 (Failed Logon)

**Related Use Case:**  
- UC04 – Brute Force Detection

---

### Attack 3: Lateral Movement Using PsExec

**Description:**  
PsExec is used to simulate lateral movement within a network environment.

**Technique:**  
- MITRE ATT&CK: T1021.002 – SMB/Windows Admin Shares

**Simulation Method:**  
- Execution of `psexec.exe`
- Creation of the PSEXESVC service

**Expected Telemetry:**  
- Sysmon Event ID 1 (Process Create)
- Windows Service Creation Logs

**Related Use Case:**  
- UC03 – Lateral Movement Detection

---

## Validation Process

Each attack simulation is validated by:

1. Verifying log ingestion in Wazuh
2. Confirming event visibility in dashboards
3. Testing detection rules
4. Performing manual threat hunting queries
5. Mapping activity to MITRE ATT&CK

---

## Conclusion

Attack simulation is a critical component of this SIEM lab.  
It ensures that detections are behavior-based, validated, and aligned with real-world attacker techniques.
