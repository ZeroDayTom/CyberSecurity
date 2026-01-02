# 🛡️ Project Blue Team – SOC Analyst Lab

## 🔵 Introduction
This project aims to develop and improve my skills as a **SOC (Security Operations Center) Analyst**.  
It allows me to understand how security monitoring works, how to detect attacks, analyze logs, and respond to security incidents.

This lab reproduces a realistic Blue Team environment used in professional SOC teams.

---

## 🎯 Project Objectives
- Install and configure a complete security monitoring environment  
- Collect logs from multiple endpoints  
- Create detection rules (use cases)  
- Use a SIEM like a real SOC analyst  
- Simulate attacks to validate detections  
- Practice threat hunting and incident investigation  
- Use the MITRE ATT&CK framework to understand adversary techniques  

---

## 🛠️ Technologies Used
### 🖥️ Virtualized Environment
- VirtualBox
- Windows 10 VM (Attack & monitored endpoint)
- Ubuntu 24.04.3-desktop VM (SIEM & monitoring stack)


### 🖥️ Endpoints & Logging
- Windows 10  
  - Sysmon (advanced Windows logging)  
  - Windows Event Logging  
  - PowerShell Logging
  - Event Viewer

### 📡 SIEM / Monitoring
- Wazuh Manager (hosted on Ubuntu)  
- Elastic Stack  
  - Elasticsearch
  - Logstash
  - Kibana
- Wazuh Dashboard  

### ⚙️ Blue Team Tools
- Sigma Rules  
- MITRE ATT&CK  
- VirusTotal / OSINT  
- PowerShell logging   

---

## 📘 Project Steps

### 1️⃣ SIEM Installation (Ubuntu VM)
- Deployment of **Wazuh Manager**  
- Deployment of **Elasticsearch & Kibana**  
- Configuration of the Wazuh dashboard  

---

### 2️⃣ Endpoint Configuration (Windows VM)
- Installation of the Wazuh Agent on Windows  
- Installation of Sysmon with the *SwiftOnSecurity* configuration  
- Forwarding Sysmon and Windows logs to the SIEM  

---

### 3️⃣ Threat Modeling
Identification of threats mapped to **MITRE ATT&CK**.  
Examples:

- **T1059.001** — PowerShell Command Execution  
- **T1547** — Persistence via Run Keys  
- **T1078** — Compromised Credentials  
- **T1569** — Remote Execution  

---

### 4️⃣ Use Case Creation (Detection Rules)

#### 🔥 Use Case 1: Encoded PowerShell Command
Detects PowerShell scripts executed with `-EncodedCommand`.

#### 🔥 Use Case 2: PsExec Installation (Lateral Movement)
Looks for:
- `psexec.exe`  
- `PSEXESVC` service  

#### 🔥 Use Case 3: Creation of a New Administrator Account
Detects Event ID **4720 + 4672**, indicating suspicious privilege escalation.

#### 🔥 Use Case 4: Run Key Persistence
Detects modification of autorun registry keys.

---

### 5️⃣ Attack Simulation
To validate the SIEM detections, several simulated attacks were executed:

- Suspicious PowerShell execution  
- PsExec lateral movement attempt  
- Creation of a new admin account  
- Simple network beaconing  

All logs were successfully collected and generated alerts in the SIEM.

---

## 6️⃣ Threat Hunting
Manual log analysis to identify suspicious behavior:

- Abnormal processes  
- Execution from AppData  
- Outbound connections to unknown IPs  
- Repetitive beaconing patterns  

---

## 📊 Project Results
- Complete log collection from Windows (Sysmon + event logs)  
- Successful detection of all simulated malicious activities  
- Clear visualization in Kibana (dashboards, graphs)  
- Custom detection rules with MITRE ATT&CK mapping  
- Full SOC analysis workflow practiced:
  - Detection  
  - Enrichment  
  - Analysis  
