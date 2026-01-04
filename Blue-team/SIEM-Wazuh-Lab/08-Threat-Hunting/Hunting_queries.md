# Threat Hunting Queries

## Overview

This document describes the threat hunting approach used in this SIEM project.  
Threat hunting focuses on proactively identifying suspicious behaviors that may bypass automated detections.

The hunting hypotheses and queries presented below are based on common attacker tradecraft and mapped to MITRE ATT&CK techniques.

---

## Hunting Methodology

The threat hunting process follows these steps:

1. Define a hunting hypothesis based on known attacker behaviors.
2. Identify relevant log sources.
3. Search for indicators and anomalies.
4. Validate findings through context and correlation.
5. Document results and lessons learned.

---

## Hunting Hypothesis 1: Suspicious PowerShell Usage

**Hypothesis:**  
Attackers may execute PowerShell from unusual locations or with obfuscated command-line arguments to evade detection.

**Log Sources:**  
- Sysmon Event ID 1 (Process Create)

**Indicators to Hunt:**  
- Execution of `powershell.exe` with encoded or obfuscated commands  
- PowerShell launched from non-standard directories  
- PowerShell executed by unexpected parent processes

**Example Hunting Query:**  
```text 
process_name:powershell.exe AND (command_line:*EncodedCommand* OR parent_process:*winword.exe* OR image_path:*AppData*)
```
```
```
---
## Hunting Hypothesis 2: Abnormal Process Execution from AppData

**Hypothesis:**
Malware often executes from user-writable directories such as AppData, Temp, or Downloads to evade security controls.

**Log Sources:**

Sysmon Event ID 1 (Process Create)

**Indicators to Hunt:**

Executables launched from AppData, Temp, or Downloads directories

Unsigned or unknown binaries running from user directories

```
```
## Hunting Hypothesis 3: Lateral Movement Indicators

**Hypothesis:**
Attackers may use administrative tools such as PsExec for lateral movement within the network.

**Log Sources:**

Sysmon Event ID 1 (Process Create)

Windows Service Creation Logs

**Indicators to Hunt:**

Execution of psexec.exe

Creation of the PSEXESVC service

```
```

## Hunting Hypothesis 4: Suspicious Authentication Activity

**Hypothesis:**
Repeated authentication failures from the same source may indicate brute force or password spraying attacks.

**Log Sources:**

Windows Security Event ID 4625 (Failed Logon)

**Indicators to Hunt:**

Multiple failed login attempts from the same IP address

Repeated failures targeting the same user account

Short time intervals between attempts

```
```

## Hunting Hypothesis 5: Persistence via Registry Modification

**Hypothesis:**
Attackers may modify registry autorun keys to maintain persistence after system reboot.

**Log Sources:**

Sysmon Event ID 13 (Registry Value Set)

**Indicators to Hunt:**

Modifications to Run or RunOnce registry keys

Unknown executables added to autorun locations