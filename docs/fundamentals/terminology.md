---
title: Terminology & Core Concepts
description: Essential cybersecurity vocabulary — CIA, AAA, risk models, MITRE ATT&CK, kill chain, diamond model, CVE/CWE/CAPEC
tags: [fundamentals, terminology, cia, mitre, kill-chain, diamond-model]
difficulty: beginner
time_estimate: "45 min"
prerequisites: ["fundamentals/index.md"]
---

# Terminology & Core Concepts

> **TL;DR** — This is the vocabulary of cybersecurity. Every report, meeting, certification exam, and technical discussion uses these terms. Master them first — everything else builds on this foundation.

## Why This Matters

Terminology isn't pedantry — it's **precision**. When a client asks "What's the *impact* of this finding?" they mean something specific (CIA impact). When a blue teamer says "We detected *T1595.001*" they mean active scanning. When a compliance auditor asks for *evidence of control effectiveness* they want specific artifacts.

Misusing terms = miscommunicating risk = failed engagements.

---

## The CIA Triad (Foundation of All Security)

| Property | Definition | Pentester Question | Common Attacks | Key Defenses |
|----------|------------|-------------------|----------------|--------------|
| **Confidentiality** | Information accessible only to authorized entities | "Can I read data I shouldn't?" | Eavesdropping, data exfiltration, directory traversal, SSRF, broken access control | Encryption (at rest/in transit), access controls, DLP, classification |
| **Integrity** | Data is accurate, complete, and unmodified by unauthorized parties | "Can I change data I shouldn't?" | Injection (SQLi, command, LDAP), tampering, ransomware, rootkits, supply chain compromise | Hashes (SHA-256), digital signatures, WAF, code signing, immutable infrastructure |
| **Availability** | Systems/data accessible when needed by authorized users | "Can I break the service?" | DoS/DDoS, ransomware, wiper malware, resource exhaustion, logic bombs | Redundancy, load balancing, rate limiting, backups, disaster recovery |

!!! tip "Pro Tip: The Fourth Element — Non-Repudiation"
    Often added to CIA: **Non-Repudiation** — Proof of origin/delivery that cannot be denied. Critical for legal/forensic contexts. Achieved via digital signatures, audit logs, blockchain.

---

## AAA Framework (Access Control Foundation)

| Component | Question | Mechanisms | Pentest Relevance |
|-----------|----------|------------|-------------------|
| **Authentication** | Who are you? | Passwords, MFA (TOTP, push, hardware keys), certificates, biometrics, Kerberos, SAML, OAuth/OIDC | Credential stuffing, password spray, MFA bypass, session hijacking, Kerberoasting |
| **Authorization** | What can you do? | RBAC, ABAC, ACLs, capabilities, policies (OPA, Rego), PAM, sudo | Privilege escalation, IDOR, broken function-level auth, ACL bypass |
| **Accounting/Auditing** | What did you do? | Logging (syslog, Windows Event Log), SIEM, auditd, CloudTrail, CloudWatch | Log tampering, log evasion, timeline reconstruction, attribution |

---

## Risk, Threat, Vulnerability, Asset (The Risk Equation)

```
Risk = Likelihood × Impact
     = (Threat × Vulnerability) × Asset Value
```

| Term | Definition | Example | Pentester Role |
|------|------------|---------|----------------|
| **Asset** | Anything of value to the organization | Customer database, web server, reputation, revenue, IP | Identify critical assets during recon |
| **Threat** | Potential cause of unwanted incident | APT group, insider, script kiddie, hurricane, hardware failure | Emulate relevant threat actors (TTPs) |
| **Vulnerability** | Weakness that can be exploited | CVE-2021-44228, misconfigured S3 bucket, weak password policy | Discover, validate, exploit, report |
| **Exploit** | Code/technique that leverages a vulnerability | Public PoC, custom weaponized exploit, Metasploit module | Weaponize for proof-of-concept |
| **Payload** | Code that runs after exploitation | Reverse shell, meterpreter, ransomware, wiper | Deliver to demonstrate impact |
| **Risk** | Potential for loss/damage | High: RCE on internet-facing DB server | Quantify in report (CVSS + business context) |

### CVSS (Common Vulnerability Scoring System) — Quick Reference

| Metric | Values | What It Measures |
|--------|--------|------------------|
| **Attack Vector (AV)** | Network (N), Adjacent (A), Local (L), Physical (P) | How the vuln is exploited |
| **Attack Complexity (AC)** | Low (L), High (H) | Conditions beyond attacker control |
| **Privileges Required (PR)** | None (N), Low (L), High (H) | Access level needed |
| **User Interaction (UI)** | None (N), Required (R) | User action needed |
| **Scope (S)** | Unchanged (U), Changed (C) | Impact beyond vulnerable component |
| **Confidentiality (C)** | None (N), Low (L), High (H) | Data disclosure impact |
| **Integrity (I)** | None (N), Low (L), High (H) | Data modification impact |
| **Availability (A)** | None (N), Low (L), High (H) | Service disruption impact |

**Score Ranges:** None (0.0), Low (0.1-3.9), Medium (4.0-6.9), High (7.0-8.9), Critical (9.0-10.0)

---

## MITRE ATT&CK Framework (The Universal Language)

### Structure

```
Tactic (Why) 
  └── Technique (How) — T####
        └── Sub-technique (Variant) — T####.###
              └── Procedure (Real-world usage) — By Group/Software
```

### Core Tactics (Enterprise Matrix — 14 Tactics)

| Tactic | ID | Description | Example Techniques |
|--------|-----|-------------|-------------------|
| **Reconnaissance** | TA0043 | Gathering target information | T1590 Active Scanning, T1598 Phishing for Info |
| **Resource Development** | TA0042 | Building/buying capabilities | T1583 Acquire Infrastructure, T1587 Develop Capabilities |
| **Initial Access** | TA0001 | Getting into the environment | T1190 Exploit Public-Facing App, T1566 Phishing |
| **Execution** | TA0002 | Running malicious code | T1059 Command & Scripting, T1204 User Execution |
| **Persistence** | TA0003 | Maintaining access | T1505 Server Software Component, T1098 Account Manipulation |
| **Privilege Escalation** | TA0004 | Gaining higher permissions | T1068 Exploitation for Privilege Escalation, T1548 Abuse Elevation Control |
| **Defense Evasion** | TA0005 | Avoiding detection | T1027 Obfuscated Files, T1562 Impair Defenses |
| **Credential Access** | TA0006 | Stealing credentials | T1003 OS Credential Dumping, T1555 Credentials from Password Stores |
| **Discovery** | TA0007 | Learning about environment | T1082 System Info Discovery, T1018 Remote System Discovery |
| **Lateral Movement** | TA0008 | Moving through environment | T1021 Remote Services, T1570 Lateral Tool Transfer |
| **Collection** | TA0009 | Gathering data of interest | T1005 Data from Local System, T1560 Archive Collected Data |
| **Command & Control** | TA0011 | Communicating with compromised systems | T1071 Application Layer Protocol, T1573 Encrypted Channel |
| **Exfiltration** | TA0010 | Stealing data | T1041 Exfiltration Over C2 Channel, T1567 Exfiltration Over Web Service |
| **Impact** | TA0040 | Manipulating/destroying systems | T1486 Data Encrypted for Impact, T1491 Defacement |

!!! note "Key Distinction"
    - **Tactic** = Strategic goal (e.g., "Persistence")
    - **Technique** = Specific method (e.g., "T1505.003 Web Shell")
    - **Sub-technique** = Granular variant (e.g., "T1505.003 Web Shell" under "T1505 Server Software Component")
    - **Procedure** = Real-world implementation by a specific group (e.g., "APT29 uses custom ASP.NET web shell")

---

## Cyber Kill Chain (Lockheed Martin)

```
┌─────────────────┐   ┌──────────────────┐   ┌─────────────┐   ┌─────────────────┐
│ 1. Reconnaissance│──▶│ 2. Weaponization │──▶│ 3. Delivery │──▶│ 4. Exploitation │
└─────────────────┘   └──────────────────┘   └─────────────┘   └─────────────────┘
                                                                        │
┌─────────────────┐   ┌──────────────────┐   ┌────────────────────────┐
│ 7. Actions on   │◀──│ 6. Command &     │◀──│ 5. Installation        │
│    Objectives   │   │    Control (C2)  │   │                        │
└─────────────────┘   └──────────────────┘   └────────────────────────┘
```

| Stage | Pentester Activity | Blue Team Detection |
|-------|-------------------|---------------------|
| **Recon** | OSINT, scanning, enum | CT log monitoring, honeypots, scan detection |
| **Weaponization** | Payload generation, exploit dev | Malware sandbox, YARA, threat intel |
| **Delivery** | Phishing, watering hole, drive-by | Email gateway, web proxy, EDR |
| **Exploitation** | Exploit execution, RCE | WAF, IPS, EDR behavior monitoring |
| **Installation** | Implant deployment, persistence | EDR, HIDS, file integrity monitoring |
| **C2** | Beaconing, tunneling, domain fronting | DNS monitoring, netflow, SSL inspection |
| **Objectives** | Data theft, destruction, ransomware | DLP, backup verification, anomaly detection |

---

## Diamond Model of Intrusion Analysis

```
                    ┌─────────────┐
                    │  Adversary  │
                    │  (Operator) │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌───────────┐ ┌───────────┐ ┌───────────┐
        │Capability │ │Infrastruct│ │  Victim   │
        │ (Tools,   │ │  (C2,     │ │ (Target,  │
        │  Malware) │ │  Hosting) │ │  Assets)  │
        └───────────┘ └───────────┘ └───────────┘
```

| Vertex | What to Analyze | Questions |
|--------|-----------------|-----------|
| **Adversary** | Operator, intent, sophistication | Who? Why? Skill level? Affiliation? |
| **Capability** | Tools, malware, exploits, techniques | What tools? Custom or public? Version? |
| **Infrastructure** | C2 domains, IPs, hosting, proxies | Where hosted? Bulletproof? Compromised? |
| **Victim** | Target org, systems, users, data | Why them? What access? What data? |

**Meta-features** (connect vertices): Timestamp, Phase, Result, Direction, Methodology, Resources

---

## Vulnerability Identification Standards

| Standard | Purpose | Format | Example |
|----------|---------|--------|---------|
| **CVE** | Unique ID for publicly known vulnerabilities | CVE-YYYY-NNNNN | CVE-2021-44228 (Log4Shell) |
| **CWE** | Classification of weakness *types* | CWE-NNN | CWE-77 (Command Injection), CWE-89 (SQLi) |
| **CAPEC** | Attack *patterns* (how weaknesses are exploited) | CAPEC-NNN | CAPEC-66 (SQL Injection), CAPEC-100 (Overflow) |

**Relationship:** CWE (root cause) → CVE (specific instance) → CAPEC (exploitation pattern)

---

## Common Acronyms Cheatsheet

| Acronym | Full Form | Context |
|---------|-----------|---------|
| **IoC** | Indicator of Compromise | Hash, IP, domain, registry key, mutex |
| **TTP** | Tactics, Techniques, Procedures | MITRE ATT&CK language |
| **C2 / C&C** | Command and Control | Attacker infrastructure |
| **RAT** | Remote Access Trojan | Malware category |
| **AV / NGAV** | Antivirus / Next-Gen AV | Endpoint protection |
| **EDR / XDR** | Endpoint Detection & Response / Extended | Advanced endpoint security |
| **SIEM** | Security Information & Event Management | Log aggregation + correlation |
| **SOAR** | Security Orchestration, Automation & Response | Automated playbooks |
| **DLP** | Data Loss Prevention | Data exfiltration prevention |
| **WAF** | Web Application Firewall | Layer 7 filtering |
| **IPS / IDS** | Intrusion Prevention / Detection System | Network monitoring |
| **NDR** | Network Detection & Response | Network traffic analysis |
| **SASE** | Secure Access Service Edge | Cloud-delivered security |
| **ZTNA** | Zero Trust Network Access | Identity-based access |
| **CSPM** | Cloud Security Posture Management | Cloud misconfig detection |
| **CWPP** | Cloud Workload Protection Platform | Runtime cloud protection |
| **ASM** | Attack Surface Management | External asset discovery |

---

## Threat Actor Taxonomy

| Category | Motivation | Typical Capability | Examples |
|----------|------------|-------------------|----------|
| **Nation-State / APT** | Espionage, sabotage, influence | High (0-days, custom malware, supply chain) | APT29, Lazarus, Equation Group |
| **Cybercrime / Ransomware** | Financial gain | Medium-High (RaaS, commodity tools, affiliates) | LockBit, Conti, REvil |
| **Hacktivist** | Ideological/political | Low-Medium (DDoS, defacement, leaks) | Anonymous, GhostSec |
| **Insider** | Revenge, greed, coercion | High (legitimate access) | Malicious admin, compromised employee |
| **Script Kiddie** | Notoriety, curiosity | Low (public tools, no understanding) | Random scanner, skid |
| **Red Teamer** | Authorized simulation | High (custom tooling, OpSec) | You (eventually) |

---

## Hands-On Lab

!!! abstract "Lab Exercise: Build Your Terminology Flashcards"
    **Objective:** Create Anki/Quizlet deck with 50 core terms from this page.
    
    **Cards to Create:**
    - Front: "CIA Triad" → Back: "Confidentiality, Integrity, Availability — with one attack/defense each"
    - Front: "Difference between CVE, CWE, CAPEC" → Back: "CVE=specific vuln, CWE=weakness class, CAPEC=attack pattern"
    - Front: "MITRE Tactic vs Technique" → Back: "Tactic=why (goal), Technique=how (method), e.g., Persistence vs T1505"
    - Front: "Kill Chain Stage 3" → Back: "Delivery — getting weapon to target (phishing, drive-by, USB)"
    - Front: "Diamond Model Vertices" → Back: "Adversary, Capability, Infrastructure, Victim"
    
    **Expected Outcome:** 80%+ recall after 1 week spaced repetition.

---

## Detection & Blue Team Perspective

| Term | What Analysts Look For | Common Data Sources |
|------|------------------------|---------------------|
| IoC | Matching hashes, IPs, domains in logs | SIEM, EDR, proxy, DNS logs |
| TTP | Behavioral patterns (not just IoCs) | MITRE ATT&CK mapping, Sigma rules |
| C2 Beaconing | Regular intervals, uniform packet sizes, specific UA | Zeek, Suricata, netflow, DNS logs |
| Lateral Movement | SMB/RPC/WinRM connections, pass-the-hash | Windows Security Log (4624), Sysmon |
| Privilege Escalation | Token manipulation, service install, scheduled tasks | Sysmon (Event ID 1, 12, 13), 4672, 4673 |

---

## MITRE ATT&CK Mapping

| Tactic | Technique | ID |
|--------|-----------|----|
| Reconnaissance | Active Scanning | T1595 |
| Reconnaissance | Gather Victim Host Information | T1592 |
| Resource Development | Develop Capabilities | T1587 |
| Resource Development | Obtain Capabilities | T1588 |

---

## Checklist

- [ ] Define CIA triad with one attack/defense per element
- [ ] Explain AAA and give pentest example for each
- [ ] Write the risk equation from memory
- [ ] Explain CVSS metrics AV, AC, PR, UI, S, C, I, A
- [ ] List all 14 MITRE ATT&CK Enterprise tactics
- [ ] Distinguish Tactic vs Technique vs Sub-technique vs Procedure
- [ ] Walk through all 7 Kill Chain stages with pentester/defender view
- [ ] Draw Diamond Model from memory with 2 questions per vertex
- [ ] Define CVE, CWE, CAPEC and their relationship
- [ ] Identify 20 acronyms from the cheatsheet without looking

---

## Further Reading

- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/) — Interactive matrix
- [NIST Glossary](https://csrc.nist.gov/glossary) — Authoritative definitions
- [CVSS v3.1 Specification](https://www.first.org/cvss/v3.1/specification-document) — Official scoring guide
- [The Diamond Model Paper](https://apps.dtic.mil/sti/pdfs/ADA586960.pdf) — Original 2013 paper
- [Lockheed Martin Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — Official page
- [CWE Top 25](https://cwe.mitre.org/top25/archive/2023/2023_cwe_top25.html) — Most dangerous weaknesses