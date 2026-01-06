# UC01 – Encoded PowerShell Execution

## Use Case ID
UC01

## Title
Detection of Encoded PowerShell Commands

## Description
This use case aims to detect suspicious executions of PowerShell using encoded or obfuscated command-line arguments.  
Attackers frequently abuse PowerShell with Base64-encoded commands to evade detection and execute malicious payloads in memory.

This behavior is commonly associated with initial access, execution, and post-exploitation phases.

---

## Objective
- Detect encoded or obfuscated PowerShell executions
- Identify abnormal PowerShell usage patterns
- Improve visibility into fileless and living-off-the-land attacks

---

## MITRE ATT&CK Mapping

| Tactic          | Technique ID | Technique Name                                |
|-----------------|--------------|-----------------------------------------------|
| Execution       | T1059.001    | Command and Scripting Interpreter: PowerShell |
| Defense Evasion | T1027        | Obfuscated / Encrypted Files or Information   |

---

## Log Sources
- **Sysmon**
  - Event ID 1: Process Create

---

## Detection Logic

### Indicators of Compromise (IOCs)
- PowerShell executed with `-EncodedCommand`
- Use of Base64-encoded strings
- PowerShell launched from unusual parent processes
- Execution from non-standard directories (AppData, Temp)

---
