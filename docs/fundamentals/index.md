---
title: Cybersecurity Fundamentals
description: Core terminology, roles, security models, compliance frameworks, and interview preparation
tags: [fundamentals, overview, beginner]
difficulty: beginner
time_estimate: "2 hours"
---

# Cybersecurity Fundamentals

> **TL;DR** — This module covers the foundational knowledge every cybersecurity professional needs: terminology that appears in every report/meeting, career paths and certifications, security models that drive architecture decisions, compliance frameworks you'll encounter on engagements, and a structured interview preparation guide.

## Why This Matters

You can't hack what you don't understand. Every penetration test, red team engagement, vulnerability assessment, and security review builds on these fundamentals:

- **Terminology** is the universal language — CIAs, TTPs, IOCs, MITRE ATT&CK. If you can't speak it, you can't communicate findings.
- **Roles & Career Paths** define what skills to prioritize. A SOC analyst needs different depth than a red teamer.
- **Security Models** (Bell-LaPadula, Zero Trust, Defense in Depth) explain *why* controls exist — and where they fail.
- **Compliance Frameworks** (ISO 27001, SOC 2, PCI-DSS) dictate scope, reporting format, and evidence requirements on many engagements.
- **Interview Preparation** translates technical skill into career outcomes.

## Module Structure

| Page | Focus | Time |
|------|-------|------|
| [Terminology & Concepts](terminology.md) | CIA, AAA, risk/threat/vuln, MITRE, kill chain, diamond model, TTP, IOC, CVE/CWE/CAPEC | 45 min |
| [Roles & Career Paths](roles-careers.md) | Red/Blue/Purple, SOC, pentester, red teamer, malware analyst, threat hunter, salaries, certs | 30 min |
| [Security Models & Frameworks](security-models.md) | Bell-LaPadula, Biba, Clark-Wilson, Zero Trust, Defense in Depth, NIST CSF | 30 min |
| [Compliance & Standards](compliance-frameworks.md) | ISO 27001, SOC 2, PCI-DSS, HIPAA, GDPR, NIST 800-53 — what pentesters need to know | 30 min |
| [Interview Preparation](interview-guide.md) | Top 50 questions with answer frameworks, practical challenges, salary negotiation | 45 min |

## Prerequisites

- Basic computer literacy
- Familiarity with OS concepts (process, file, network)
- No prior security experience required

## Learning Path

```
Terminology → Roles → Security Models → Compliance → Interview Guide
     ↓           ↓           ↓              ↓              ↓
  Speak the   Choose your  Understand   Know the     Convert skills
  language    path         why controls   rules of     to offers
             exist        engagement
```

## How to Use This Module

1. **Read Terminology first** — Everything else references these terms
2. **Pick a role path** — Focus your learning on relevant certifications and skills
3. **Understand models** — They explain the "why" behind every control you'll bypass
4. **Know compliance** — Many engagements are compliance-driven; scope and reporting follow framework requirements
5. **Practice interviews** — Technical skill ≠ interview skill. Both are needed.

---

## Quick Reference: Core Concepts

### The CIA Triad
| Property | Definition | Example Attack | Example Defense |
|----------|------------|----------------|-----------------|
| **Confidentiality** | Only authorized access | Data exfiltration, sniffing | Encryption, access control |
| **Integrity** | Data unchanged by unauthorized | Tampering, injection, ransomware | Hashes, signatures, WAF |
| **Availability** | Systems accessible when needed | DoS, ransomware, wiper malware | Redundancy, backups, rate limiting |

### AAA Framework
| Component | Question | Example |
|-----------|----------|---------|
| **Authentication** | Who are you? | Password, MFA, certificate, biometric |
| **Authorization** | What can you do? | RBAC, ABAC, ACLs, capabilities |
| **Accounting** | What did you do? | Logging, audit trails, SIEM |

### Risk Equation
```
Risk = Likelihood × Impact
     = (Threat × Vulnerability) × Asset Value
```
- **Threat** — Actor with intent/capability (APT, insider, script kiddie, nature)
- **Vulnerability** — Weakness that can be exploited (CVE, misconfig, logic flaw)
- **Asset** — What you're protecting (data, system, reputation, revenue)

### MITRE ATT&CK (Essential Framework)
| Concept | Description |
|---------|-------------|
| **Tactic** | *Why* — Adversary's tactical goal (e.g., Initial Access, Persistence) |
| **Technique** | *How* — Specific method to achieve tactic (e.g., Phishing, Valid Accounts) |
| **Sub-technique** | *Variant* — More specific implementation (e.g., Spearphishing Attachment) |
| **Procedure** | *Instance* — Real-world usage by a group (e.g., APT29's specific phishing template) |
| **Group** | Known threat actors (e.g., APT29, FIN7, Lazarus) |
| **Software** | Malware/tools used (e.g., Cobalt Strike, Mimikatz) |
| **Mitigation** | Defensive controls that reduce technique effectiveness |

### Cyber Kill Chain (Lockheed Martin)
```
1. Reconnaissance  →  2. Weaponization  →  3. Delivery  →  4. Exploitation
5. Installation    →  6. Command & Control (C2)  →  7. Actions on Objectives
```
*Pentester view: We simulate stages 1-7 to find gaps before real attackers do.*

### Diamond Model (Intrusion Analysis)
```
         Adversary
            │
     ┌──────┴──────┐
     ▼             ▼
Capability    Infrastructure
     ▲             ▲
     └──────┬──────┘
            ▼
         Victim
```
*Every intrusion has these four core features connected by relationships.*

---

## Hands-On Lab

!!! abstract "Lab Exercise: Map a Real CVE to MITRE ATT&CK"
    **Objective:** Take CVE-2021-44228 (Log4Shell) and map its exploitation chain to MITRE ATT&CK techniques.
    
    **Steps:**
    1. Read the [CVE description](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)
    2. Identify: Initial Access → Execution → Persistence → Privilege Escalation → Defense Evasion → Credential Access → Discovery → Lateral Movement → Collection → Command & Control → Exfiltration → Impact
    3. For each stage, find 1-2 relevant technique IDs
    4. Compare with [MITRE's official mapping](https://attack.mitre.org/software/S0656/)
    
    **Expected Outcome:** A completed matrix showing how one vulnerability enables multiple tactics.

---

## Detection & Blue Team Perspective

| Concept | Detection Approach | Sigma Rule Example |
|---------|-------------------|-------------------|
| Reconnaissance | Network scanning alerts, DNS query anomalies, certificate transparency monitoring | `title: Suspicious Port Scan` |
| Weaponization | Malware sandbox detonation, YARA matches on payloads | `title: Log4Shell Payload Detection` |
| Delivery | Email gateway analysis, web proxy URL categorization, EDR file reputation | `title: Phishing Email with Malicious Attachment` |
| Exploitation | WAF/IPS signatures, EDR behavior monitoring, application crash logs | `title: Log4Shell Exploitation Attempt` |

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

- [ ] Can define CIA, AAA, Risk, Threat, Vulnerability, Asset without notes
- [ ] Can explain MITRE ATT&CK structure: Tactic vs Technique vs Sub-technique vs Procedure
- [ ] Can walk through Cyber Kill Chain and Diamond Model for a given scenario
- [ ] Know the difference between CVE, CWE, and CAPEC
- [ ] Can name 5 threat actor groups and their typical TTPs
- [ ] Understand how compliance frameworks drive engagement scope

---

## Further Reading

- [MITRE ATT&CK Framework](https://attack.mitre.org/) — Primary reference
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) — CSF, 800-53, 800-171
- [OWASP Testing Guide](https://owasp.org/www-project-testing-guide/) — Web app methodology
- [PTES](http://www.pentest-standard.org/index.php/PTES_Main) — Penetration Testing Execution Standard
- [NIST Glossary](https://csrc.nist.gov/glossary) — Authoritative definitions
- [The Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — Original paper