# Techniques Used

## Overview

This document details the attacker techniques simulated and detected
throughout the SIEM project. Each technique represents a common adversary
behavior observed in real-world incidents and was selected to demonstrate
practical detection capabilities.

The techniques are aligned with the MITRE ATT&CK framework and validated
through controlled attack simulations.

---

## Execution Techniques

### PowerShell Encoded Command

- Technique ID: T1059.001
- Platform: Windows
- Description:
  Attackers frequently use encoded PowerShell commands to obfuscate
  malicious payloads and bypass security controls.
- Simulation Method:
  - PowerShell execution using the `-EncodedCommand` parameter
- Detection:
  - Sysmon Event ID 1
  - Command-line inspection
- Outcome:
  - Successful detection and alert generation

---

## Persistence Techniques

### Registry Run Keys

- Technique ID: T1547.001
- Platform: Windows
- Description:
  Registry Run keys are commonly used by attackers to maintain persistence
  across system reboots.
- Simulation Method:
  - Modification of autorun registry keys
- Detection:
  - Sysmon Event ID 13 (Registry modification)
- Outcome:
  - Persistence attempt detected

---

## Privilege Escalation & Persistence

### Valid Accounts

- Technique ID: T1078
- Platform: Windows
- Description:
  Attackers may create or abuse privileged accounts to maintain access
  and escalate privileges.
- Simulation Method:
  - Creation of a new administrator account
- Detection:
  - Windows Security Event IDs 4720 and 4672
- Outcome:
  - Suspicious account activity detected

---

## Lateral Movement Techniques

### PsExec Execution

- Technique ID: T1569.002
- Platform: Windows
- Description:
  PsExec is commonly abused by attackers for remote command execution
  and lateral movement.
- Simulation Method:
  - PsExec execution on target host
- Detection:
  - Sysmon Event ID 1
  - Windows service creation events
- Outcome:
  - Lateral movement activity detected

---

## Credential Access Techniques

### Brute Force Authentication

- Technique ID: T1110
- Platform: Windows
- Description:
  Brute force attacks attempt to guess credentials through repeated
  authentication failures.
- Simulation Method:
  - Multiple failed login attempts
- Detection:
  - Windows Security Event ID 4625
  - Threshold-based Python detection
- Outcome:
  - Brute force activity identified

---

## Detection Approach Summary

| Technique ID | Technique Name           | Log Source            | Detection Method              |
|-------------|--------------------------|-----------------------|-------------------------------|
| T1059.001   | PowerShell Execution     | Sysmon                | Command-line analysis         |
| T1547.001   | Run Key Persistence      | Sysmon                | Registry monitoring           |
| T1078       | Valid Accounts           | Windows Security      | Event correlation             |
| T1569.002   | PsExec Execution         | Sysmon / Windows      | Process & service detection  |
| T1110       | Brute Force              | Windows Security      | Threshold-based detection     |

---

## Key Takeaways

- All techniques are based on real adversary behavior
- Detections rely on behavioral indicators rather than signatures
- Each technique was validated through attack simulation
- The project demonstrates a realistic SOC detection workflow
