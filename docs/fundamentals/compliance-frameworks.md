---
title: Compliance & Standards
description: Major compliance frameworks — ISO 27001, SOC 2, PCI-DSS, HIPAA, GDPR, NIST 800-53 — what pentesters need to know for scope, reporting, and evidence
tags: [fundamentals, compliance, iso-27001, soc2, pci-dss, hipaa, gdpr, nist-800-53]
difficulty: beginner
time_estimate: "30 min"
prerequisites: ["fundamentals/security-models.md"]
---

# Compliance & Standards

> **TL;DR** — Compliance frameworks drive the *scope*, *methodology*, and *reporting format* of many engagements. You do not need to be an auditor, but you must know which controls map to which requirements so your findings speak the client's language.

## Why This Matters

A client says "We need a PCI-DSS penetration test." That means:
- Scope = Cardholder Data Environment (CDE) + connected systems
- Required tests = Specific requirement mapping (Req 11.3, 11.4, 6.5.x)
- Report format = Attestation of Compliance (AoC) + Report on Compliance (RoC)
- Evidence = Screenshots, tool output, chain of custody

If you deliver a generic "here are 15 vulnerabilities" report, the client cannot use it for their audit. You failed the engagement.

---

## Framework Comparison at a Glance

| Framework | Industry | Geography | Mandatory? | Pentest Frequency | Key Pentest Requirements |
|-----------|----------|-----------|------------|-------------------|--------------------------|
| **ISO 27001** | Any | Global | Voluntary (contractual) | Annual + after major changes | A.12.6.1, A.14.2.8, Annex A controls |
| **SOC 2** | SaaS, Service Orgs | US/Global | Contractual | Annual | CC6.1, CC7.1, CC7.2 (Trust Services Criteria) |
| **PCI-DSS** | Payment Cards | Global | Mandatory (card brands) | Annual + quarterly scans | Req 11.3, 11.4, 6.5.x, 6.6 |
| **HIPAA** | Healthcare (US) | US | Mandatory (federal) | Risk analysis (periodic) | 164.308(a)(1)(ii)(A), 164.312 |
| **GDPR** | Personal Data (EU) | EU/Global | Mandatory (law) | DPIA-triggered | Art 32, 33, 34 (security of processing) |
| **NIST 800-53** | US Federal + Contractors | US | Mandatory (federal) | Continuous / Annual | Control families (AC, AU, CM, IA, IR, SC, SI) |

---

## ISO 27001 / 27002 (International Standard)

### What It Is
Information Security Management System (ISMS) framework. Certifiable. Risk-based, not prescriptive.

### Structure
- **ISO 27001** — Requirements (clauses 4-10)
- **ISO 27002** — Control guidance (93 controls in 4 themes, 2022 version)

### Four Themes (2022)
| Theme | Controls | Pentest Relevance |
|-------|----------|-------------------|
| **Organizational** (A.5-A.8) | Policies, roles, assets, HR | Scope definition, asset inventory |
| **People** (A.6-A.7) | Screening, awareness, training | Social engineering scope, phishing tests |
| **Physical** (A.7-A.8) | Perimeter, entry, equipment | Physical pentest, tailgating, badge cloning |
| **Technological** (A.8-A.14) | Access, crypto, operations, network, app dev | **Core pentest scope** — network, web, API, code review |

### Key Annex A Controls for Pentesters
| Control | Title | What to Test |
|---------|-------|--------------|
| A.5.7 | Threat Intelligence | Threat modeling quality |
| A.8.8 | Technical Vulnerability Management | Vuln scanning, patching cadence |
| A.8.16 | Monitoring Activities | Logging, SIEM, alerting coverage |
| A.8.23 | Web Filtering | Proxy, DNS filtering bypass |
| A.8.28 | Secure Coding | SAST/DAST, code review |
| A.14.2.8 | Secure System Engineering | Architecture review, threat modeling |

### Engagement Flow
```
Scoping → ISMS Review → Asset Inventory → Risk Treatment Plan → Control Selection → Test Plan → Execute → Report → Remediation → Re-test → Surveillance Audit
```

---

## SOC 2 (Service Organization Control 2)

### What It Is
AICPA attestation standard for service organizations. Focus on **Trust Services Criteria (TSC)**. Not a certification — an independent auditor's opinion.

### Five Trust Services Criteria
| Criterion | Focus | Pentest Mapping |
|-----------|-------|-----------------|
| **Security (Common Criteria)** | Protection against unauthorized access | **Primary pentest scope** — network, app, physical |
| **Availability** | System uptime, resilience | DoS testing, failover validation |
| **Confidentiality** | Data protection, encryption | Data exfiltration attempts, crypto validation |
| **Processing Integrity** | Complete, accurate, timely processing | Logic flaw testing, race conditions |
| **Privacy** | PII collection, use, retention, disposal | PII discovery, data flow mapping |

### Common Criteria (CC) — Key for Pentesters
| CC | Description | Test Activity |
|----|-------------|---------------|
| CC6.1 | Logical/physical access controls | Network segmentation, ACLs, MFA, bastion hosts |
| CC6.2 | Credential management | Password policy, rotation, vault, MFA bypass |
| CC6.3 | Network segmentation | VLANs, firewall rules, micro-segmentation |
| CC6.6 | Vulnerability management | Scanning, patching, remediation SLAs |
| CC6.7 | Data transmission protection | TLS config, cert validation, downgrade attacks |
| CC7.1 | System monitoring | SIEM coverage, alert tuning, blind spots |
| CC7.2 | Incident detection/response | IR plan, forensic readiness, log retention |

### Report Types
| Type | Audience | Content |
|------|----------|---------|
| **Type 1** | Point-in-time design effectiveness | Control design only |
| **Type 2** | Period (6-12 months) operating effectiveness | Design + operating evidence |

**Pentester Role:** Usually feeds into Type 2 — tests operating effectiveness of security controls.

---

## PCI-DSS (Payment Card Industry Data Security Standard)

### What It Is
Mandatory for any entity that stores, processes, or transmits cardholder data. Enforced by card brands (Visa, Mastercard, Amex). Non-compliance = fines, loss of processing ability.

### Scope: The CDE (Cardholder Data Environment)
```
All systems that:
  ▸ Store, process, transmit CHD (Primary Account Number + any of: CVV, expiry, name)
  ▸ Connect to CDE systems (flat network, shared services, management interfaces)
  ▸ Impact CDE security (AD, DNS, NTP, logging, backup, monitoring)
```

**Scoping is everything.** Wrong scope = failed audit.

### Pentest Requirements (Req 11.3, 11.4)
| Requirement | Frequency | Scope | Methodology |
|-------------|-----------|-------|-------------|
| **11.3.1** External penetration test | Annual + after significant changes | Internet-facing CDE systems | NIST 800-115, PTES, OWASP |
| **11.3.2** Internal penetration test | Annual + after significant changes | Internal CDE + connected | Same + lateral movement, privilege escalation |
| **11.3.3** Segmentation test | Annual | Verify CDE isolation | Scan from non-CDE → CDE (must fail) |
| **11.4.1** Automated vulnerability scans | Quarterly | External + Internal CDE | ASV (Approved Scanning Vendor) |
| **11.4.2** Wireless scan | Quarterly | Wireless in/around CDE | Rogue AP detection, encryption validation |

### Requirement 6.5.x (Secure Coding) — Maps to OWASP Top 10
| 6.5.x | Vulnerability Class | Test Method |
|-------|---------------------|-------------|
| 6.5.1 | Injection (SQLi, OS command, LDAP) | DAST, SAST, manual |
| 6.5.2 | Buffer Overflow | Code review, fuzzing |
| 6.5.3 | Insecure Crypto | Cipher analysis, cert validation |
| 6.5.4 | Insecure Authentication/Session | Auth testing, session mgmt |
| 6.5.5 | Access Control (IDOR, forced browsing) | Authorization testing |
| 6.5.6 | XSS | Reflected, Stored, DOM |
| 6.5.7 | CSRF | Token validation, SameSite |
| 6.5.8 | Information Leakage | Error handling, headers, comments |
| 6.5.9 | Business Logic | Workflow bypass, race conditions |
| 6.5.10 | Other OWASP Top 10 | Comprehensive coverage |

### Deliverables
- **RoC (Report on Compliance)** — Full findings, evidence, risk ranking
- **AoC (Attestation of Compliance)** — Signed by QSA and client executive
- **Executive Summary** — Business risk, not technical detail

---

## HIPAA (Health Insurance Portability and Accountability Act)

### What It Is
US federal law protecting Protected Health Information (PHI). Applies to Covered Entities (providers, plans, clearinghouses) and Business Associates.

### Security Rule — Three Safeguard Categories
| Category | Standards | Implementation Specifications |
|----------|-----------|-------------------------------|
| **Administrative** | Risk analysis, workforce training, access management, incident procedures | **Required** (must implement) |
| **Physical** | Facility access, workstation security, device/media controls | **Addressable** (assess, implement or document alternative) |
| **Technical** | Access control, audit controls, integrity, transmission security | Mix of Required/Addressable |

### Key Technical Specifications for Pentesters
| Spec | Requirement | Pentest Focus |
|------|-------------|---------------|
| **164.312(a)(1)** | Access Control (Unique User ID, Emergency Access, Auto Logoff, Encryption) | Account enumeration, session timeout, encryption at rest |
| **164.312(b)** | Audit Controls (Hardware, software, procedural mechanisms) | Log completeness, tamper protection, retention |
| **164.312(c)(1)** | Integrity (PHI not altered/destroyed improperly) | Hash validation, digital signatures, backup integrity |
| **164.312(d)** | Person/Entity Authentication | MFA, certificate-based auth, biometric |
| **164.312(e)(1)** | Transmission Security (Integrity, Encryption) | TLS 1.2+, VPN, email encryption, SFTP |

### Breach Notification Rule
- **Breach** = Unauthorized acquisition, access, use, disclosure of unsecured PHI
- **Notification** = 60 days max to individuals, HHS, media (if >500 affected)
- **Pentest Implication:** Any finding exposing PHI triggers simulated breach notification exercise

---

## GDPR (General Data Protection Regulation)

### What It Is
EU regulation on data protection and privacy. Extraterritorial — applies if you process EU residents' data, regardless of location.

### Key Articles for Security Testing
| Article | Requirement | Pentest Angle |
|---------|-------------|---------------|
| **Art 5** | Principles: Lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality | Data flow mapping, excessive collection, retention testing |
| **Art 25** | Data Protection by Design and Default | Architecture review, default configs, privacy settings |
| **Art 32** | Security of Processing (encryption, confidentiality, integrity, availability, resilience) | **Core pentest scope** — all technical controls |
| **Art 33** | Breach Notification to Supervisory Authority (72 hours) | IR readiness, detection capability, evidence preservation |
| **Art 34** | Communication to Data Subject (high risk) | Impact assessment, notification templates |
| **Art 35** | Data Protection Impact Assessment (DPIA) | High-risk processing = mandatory DPIA = pentest trigger |

### Lawful Basis (Must Have One)
Consent, Contract, Legal Obligation, Vital Interests, Public Task, Legitimate Interest

**Pentester View:** Test systems processing under each basis. Consent withdrawal = data deletion test. Legitimate interest = balancing test documentation.

---

## NIST SP 800-53 (Security and Privacy Controls)

### What It Is
Catalog of controls for US federal information systems. Mandatory for agencies, contractors (via DFARS, CMMC). Basis for FedRAMP, CMMC, StateRAMP.

### Control Families (20 in Rev 5)
| Family | ID | Pentest Relevance |
|--------|----|-------------------|
| Access Control | AC | AC-2, AC-3, AC-6, AC-17, AC-20 |
| Awareness & Training | AT | AT-2, AT-3 (phishing tests) |
| Audit & Accountability | AU | AU-2, AU-3, AU-6, AU-12 |
| Configuration Management | CM | CM-2, CM-6, CM-7, CM-8 |
| Identification & Authentication | IA | IA-2, IA-5, IA-8 (MFA, device auth) |
| Incident Response | IR | IR-4, IR-5, IR-6 (detection, handling) |
| Maintenance | MA | MA-4 (non-local maintenance) |
| Media Protection | MP | MP-6, MP-7 (media sanitization) |
| Physical & Environmental | PE | PE-2, PE-3, PE-6 (physical pentest) |
| Planning | PL | PL-2, PL-4 (threat modeling) |
| Personnel Security | PS | PS-3, PS-6 (insider threat) |
| Risk Assessment | RA | RA-5 (vulnerability scanning) |
| System & Services Acquisition | SA | SA-11, SA-15 (dev/sec/ops) |
| System & Comm Protection | SC | SC-7, SC-8, SC-13, SC-28 (boundary, crypto) |
| System & Info Integrity | SI | SI-2, SI-3, SI-4, SI-7 (flaw remediation, malicious code, monitoring) |

### Control Baselines
| Impact Level | Controls | Typical Use |
|--------------|----------|-------------|
| **Low** | ~130 | Public websites, non-sensitive |
| **Moderate** | ~260 | Most federal systems |
| **High** | ~300+ | Classified, critical infrastructure |

### Pentest Mapping (NIST 800-115)
```
Planning → Discovery → Attack → Reporting
   ↓           ↓          ↓         ↓
RA-5       SC-7        SI-3      IR-4, IR-5
CM-8       AC-3        IA-5      AU-6
```

---

## Mapping Findings to Frameworks (The Skill That Gets You Hired)

### Finding Template
```
Finding: SQL Injection in Customer Portal
CVSS: 9.1 Critical
Frameworks Affected:
  ▸ PCI-DSS: Req 6.5.1 (Injection), 6.5.6 (XSS), 11.3 (Penetration Test)
  ▸ ISO 27001: A.8.28 (Secure Coding), A.14.2.8 (Secure Engineering)
  ▸ SOC 2: CC6.1 (Logical Access), CC7.1 (Monitoring)
  ▸ NIST 800-53: SI-3 (Malicious Code Protection), SC-7 (Boundary Protection)
  ▸ GDPR: Art 32 (Security of Processing), Art 25 (Privacy by Design)
Remediation: Parameterized queries, WAF rule, input validation, code review
Evidence: Burp request/response, database error, data exfil PoC
```

### Why This Matters
- **Auditors** check checkboxes against requirements
- **Clients** need to show auditors "we tested X and fixed Y"
- **You** become a partner, not just a vendor

---

## Hands-On Lab

!!! abstract "Lab Exercise: Framework Scoping Exercise"
    **Scenario:** Client is a US-based SaaS company processing credit cards for EU healthcare providers. They store PHI and CHD.
    
    **Task:** Determine which frameworks apply and define pentest scope for each.
    
    **Questions:**
    1. Which frameworks are mandatory vs contractual?
    2. What is the CDE boundary? What connects to it?
    3. Which SOC 2 TSCs apply? (Hint: all five)
    4. What HIPAA safeguards are in scope?
    5. Does GDPR apply? Under what lawful basis?
    6. Create a unified test plan covering all frameworks efficiently.
    
    **Expected Outcome:** Scoping document with framework matrix, unified methodology, and deliverable list per framework.

---

## Detection & Blue Team Perspective

| Framework | Continuous Monitoring Requirements | Key Metrics for Dashboards |
|-----------|-----------------------------------|---------------------------|
| **ISO 27001** | A.8.16 Monitoring, A.12.4 Logging | Log coverage %, alert mean time to detect |
| **SOC 2** | CC7.1, CC7.2 System Monitoring | Detection coverage by MITRE tactic, false positive rate |
| **PCI-DSS** | Req 10 (Logging), 11.4 (Scans), 11.5 (FIM) | Scan completion %, critical vuln aging, FIM alerts |
| **HIPAA** | 164.312(b) Audit Controls | PHI access audit log completeness, anomaly detection |
| **GDPR** | Art 32 Resilience, Art 33 Breach Detection | Breach detection time, DPIA completion rate |
| **NIST 800-53** | SI-4 Monitoring, AU-6 Audit Review | Control implementation %, POA&M aging |

---

## MITRE ATT&CK Mapping

| Tactic | Technique | ID | Framework Driver |
|--------|-----------|----|------------------|
| Reconnaissance | Active Scanning | T1595 | PCI 11.4, ISO A.8.8, NIST RA-5 |
| Initial Access | Exploit Public-Facing App | T1190 | PCI 6.5.x, SOC 2 CC6.1, NIST SC-7 |
| Execution | Command & Scripting Interpreter | T1059 | PCI 6.5.1, NIST SI-3 |
| Persistence | Server Software Component | T1505 | PCI 10.7, NIST CM-7 |
| Defense Evasion | Impair Defenses | T1562 | SOC 2 CC7.1, NIST SI-4 |
| Credential Access | OS Credential Dumping | T1003 | PCI 8.2, NIST IA-5 |
| Discovery | System Network Config Discovery | T1016 | PCI 11.3.3, NIST SC-7 |
| Lateral Movement | Remote Services | T1021 | PCI 1.2, NIST AC-4 |
| Collection | Data from Information Repositories | T1213 | HIPAA 164.312, GDPR Art 32 |
| Exfiltration | Exfiltration Over C2 Channel | T1041 | PCI 12.10, GDPR Art 33 |

---

## Checklist

- [ ] Can explain the difference between ISO 27001 (certifiable) and SOC 2 (attestation)
- [ ] Know PCI-DSS CDE scoping rules and the 4 pentest requirements (11.3.1-11.3.3, 11.4)
- [ ] Can map a SQLi finding to PCI 6.5.1, ISO A.8.28, SOC 2 CC6.1, NIST SI-3
- [ ] Understand HIPAA Required vs Addressable implementation specifications
- [ ] Know GDPR Art 32 (security of processing) and Art 33 (72-hour breach notification)
- [ ] Can name 5 NIST 800-53 control families relevant to pentesting
- [ ] Have a finding template that includes framework mappings

---

## Further Reading

- [PCI-DSS v4.0 Official](https://www.pcisecuritystandards.org/document_library) — Current standard
- [ISO 27001:2022 Transition](https://www.iso.org/standard/27001) — Latest version
- [SOC 2 Trust Services Criteria](https://www.aicpa.org/interestareas/frc/assurance/downloadabledocuments/tscs-update-2017.pdf) — 2017 update
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html) — HHS guidance
- [GDPR Text](https://gdpr.eu/article-32-security-of-processing/) — Article 32 focus
- [NIST 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — Full catalog
- [NIST 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final) — Technical guide for pentesting