# UC03 – PsExec Lateral Movement Detection

## Use Case ID
UC03

## Title
Detection of Lateral Movement Using PsExec

## Description
This use case focuses on detecting lateral movement activity performed using **PsExec**, a legitimate administrative tool frequently abused by attackers to execute commands remotely on other systems within a network.

PsExec abuse is commonly observed during post-exploitation phases after initial access has been achieved.

---

## Objective
- Detect lateral movement attempts using PsExec
- Identify misuse of legitimate administrative tools
- Improve visibility into internal network compromise

---

## MITRE ATT&CK Mapping

| Tactic           | Technique ID | Technique Name                              |
|------------------|--------------|---------------------------------------------|
| Lateral Movement | T1569.002    | System Services: Service Execution          |
| Lateral Movement | T1021        | Remote Services                             |

---

## Log Sources
- **Sysmon**
  - Event ID 1: Process Create
- **Windows System Logs**
  - Service creation events (PSEXESVC)

---

## Detection Logic

### Indicators of Compromise (IOCs)
- Execution of `psexec.exe`
- Creation of the `PSEXESVC` service
- Remote command execution using PsExec
- PsExec executed by unexpected users or hosts

---