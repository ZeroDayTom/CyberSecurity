# UC02 – Brute Force Authentication Detection

## Use Case ID
UC02

## Title
Detection of Brute Force Authentication Attempts

## Description
This use case aims to detect brute force and password spraying attacks by identifying multiple failed authentication attempts within a short time window.  
Attackers commonly use this technique to gain initial access or escalate privileges by compromising user credentials.

---

## Objective
- Detect repeated authentication failures
- Identify potential brute force or password spraying activity
- Provide early warning of credential-based attacks

---

## MITRE ATT&CK Mapping

| Tactic            | Technique ID | Technique Name              |
|-------------------|--------------|-----------------------------|
| Credential Access | T1110        | Brute Force                 |

---

## Log Sources
- **Windows Security Logs**
  - Event ID 4625: Failed Logon

---

## Detection Logic

### Indicators of Compromise (IOCs)
- Multiple failed logon attempts
- Repeated failures from the same source IP
- Multiple failed attempts targeting the same user account
- Short time intervals between attempts

---

