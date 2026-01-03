# Threat Hunting Queries

## Overview

This document describes the threat hunting approach used in this SIEM project.
Threat hunting focuses on proactively identifying suspicious behaviors that
may bypass automated detections.

The queries and hypotheses presented here are based on common attacker
tradecraft and mapped to MITRE ATT&CK techniques.

---

## Hunting Methodology

The threat hunting process follows these steps:

1. Define a hunting hypothesis based on known attacker behaviors
2. Identify relevant log sources
3. Analyze patterns and anomalies
4. Validate findings through context and correlation
5. Document results and improvements

---

## Hunting Hypothesis 1: Suspicious PowerShell Usage

### Hypothesis
Attackers may execute PowerShell from unusual locations or with obfuscated
command-line arguments to evade detection.

### Log Sources
- Sysmon Event ID 1 (Process Create)

### Indicators to Hunt
- Execution of `powershell.exe` with encoded or obfuscated commands
- PowerShell launched from non-standard directories
- PowerShell executed by unexpected parent processes

### Example Hunting Query
```text
process_name:powershell.exe AND
(command_line:*EncodedCommand* OR
 parent_process:*winword.exe* OR
 image_path:*AppData*)
