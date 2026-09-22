# 📚 Cybersecurity Fundamentals

> This is not just a basics guide — this is the foundation every security professional builds on.  
> Whether you're hunting bugs, defending networks, or explaining risk to executives, these concepts are your daily language.

---

## 📖 Table of Contents

1. [Core Concepts & Terminology](#1-core-concepts--terminology)
2. [The CIA Triad](#2-the-cia-triad)
3. [AAA Framework](#3-aaa-framework)
4. [Risk, Threats & Vulnerabilities](#4-risk-threats--vulnerabilities)
5. [CVSS Scoring](#5-cvss-scoring)
6. [MITRE ATT&CK Framework](#6-mitre-attck-framework)
7. [Cyber Kill Chain](#7-cyber-kill-chain)
8. [Diamond Model](#8-diamond-model)
9. [Security Models](#9-security-models)
10. [Zero Trust Architecture](#10-zero-trust-architecture)
11. [Defense in Depth](#11-defense-in-depth)
12. [Access Control Models](#12-access-control-models)
13. [Compliance Frameworks](#13-compliance-frameworks)
14. [Security Roles & Career Paths](#14-security-roles--career-paths)
15. [Certifications Roadmap](#15-certifications-roadmap)
16. [Interview Preparation](#16-interview-preparation)
17. [Essential Resources](#17-essential-resources)

---

## 1. Core Concepts & Terminology

Before diving into tools and techniques, you need to speak the language. These terms appear in every report, meeting, certification exam, and job description.

### Essential Vocabulary

| Term | Definition | Why It Matters |
|------|------------|----------------|
| **Asset** | Anything of value — data, systems, people, reputation | You protect assets, not just servers |
| **Threat** | Any potential cause of an unwanted incident | APT group, insider, malware, natural disaster |
| **Vulnerability** | A weakness that can be exploited | CVE-2021-44228, misconfigured S3 bucket, weak password |
| **Exploit** | Code or technique that leverages a vulnerability | Public PoC, Metasploit module, custom weaponized code |
| **Payload** | Code that runs after successful exploitation | Reverse shell, meterpreter, ransomware encryptor |
| **Risk** | Likelihood × Impact of a threat exploiting a vulnerability | Drives prioritization and budget decisions |
| **Control** | Measure that reduces risk | Firewall, MFA, encryption, policy, training |
| **IoC** | Indicator of Compromise — forensic artifact | Hash, IP, domain, registry key, mutex |
| **TTP** | Tactics, Techniques, Procedures — how attackers operate | MITRE ATT&CK language |
| **C2 / C&C** | Command and Control — attacker infrastructure | Beaconing, domain fronting, encrypted channels |
| **ATP** | Advanced Persistent Threat — sophisticated, targeted | Nation-state actors, organized crime |
| **RCE** | Remote Code Execution — highest severity vuln class | Full system takeover |
| **LPE / Privesc** | Local Privilege Escalation | User → root / SYSTEM |
| **IDOR** | Insecure Direct Object Reference | Accessing objects by manipulating IDs |
| **BOLA** | Broken Object Level Authorization | API-specific IDOR |
| **SSRF** | Server-Side Request Forgery | Server makes requests to unintended destinations |
| **XXE** | XML External Entity Injection | Parsing malicious XML input |
| **SSTI** | Server-Side Template Injection | Template engine code execution |

---

## 2. The CIA Triad

The foundation of information security. Every control, every finding, every risk assessment maps back to these three.

| Property | Definition | Attacker Goal | Defender Goal | Example Attacks | Key Controls |
|----------|------------|---------------|---------------|-----------------|--------------|
| **Confidentiality** | Only authorized access to information | Read data they shouldn't | Prevent unauthorized disclosure | Sniffing, data exfiltration, directory traversal, SSRF | Encryption (at rest/in transit), access controls, DLP, classification |
| **Integrity** | Data is accurate and unmodified by unauthorized parties | Modify data they shouldn't | Prevent unauthorized modification | SQL injection, command injection, ransomware, rootkits, supply chain | Hashes (SHA-256), digital signatures, WAF, code signing, immutable infra |
| **Availability** | Systems accessible when needed | Deny access to legitimate users | Ensure continuous operation | DoS/DDoS, ransomware, wiper malware, resource exhaustion | Redundancy, load balancing, rate limiting, backups, disaster recovery |

### The Fourth Element: Non-Repudiation
Proof of origin/delivery that cannot be denied. Critical for legal and forensic contexts. Achieved via digital signatures, audit logs, blockchain.

---

## 3. AAA Framework

Access control foundation — every authentication and authorization decision uses this.

| Component | Question | Mechanisms | Pentest Focus |
|-----------|----------|------------|---------------|
| **Authentication** | Who are you? | Passwords, MFA (TOTP, push, hardware keys), certificates, biometrics, Kerberos, SAML, OAuth/OIDC | Credential stuffing, password spray, MFA bypass, session hijacking, Kerberoasting |
| **Authorization** | What can you do? | RBAC, ABAC, ACLs, capabilities, policies (OPA/Rego), PAM, sudo | Privilege escalation, IDOR, broken function-level auth, ACL bypass |
| **Accounting** | What did you do? | Logging (syslog, Windows Event Log), SIEM, auditd, CloudTrail, CloudWatch | Log tampering, log evasion, timeline reconstruction, attribution |

---

## 4. Risk, Threats & Vulnerabilities

### The Risk Equation

```
Risk = Likelihood × Impact
     = (Threat × Vulnerability) × Asset Value
```

| Element | Description | Example |
|---------|-------------|---------|
| **Asset** | What you're protecting | Customer database, web server, reputation, revenue |
| **Threat** | Actor with intent and capability | APT29, malicious insider, script kiddie, hurricane |
| **Vulnerability** | Weakness that can be exploited | CVE-2021-44228, misconfigured S3, weak password policy |
| **Exploit** | Code/technique using the vuln | Public PoC, custom weaponized exploit |
| **Impact** | Business consequence | Data breach, downtime, regulatory fine, reputation loss |

### Threat Actor Taxonomy

| Category | Motivation | Capability | Examples |
|----------|------------|------------|----------|
| **Nation-State / APT** | Espionage, sabotage, influence | High (0-days, custom malware, supply chain) | APT29, Lazarus, Equation Group |
| **Cybercrime / Ransomware** | Financial gain | Medium-High (RaaS, commodity tools, affiliates) | LockBit, Conti, REvil |
| **Hacktivist** | Ideological/political | Low-Medium (DDoS, defacement, leaks) | Anonymous, GhostSec |
| **Insider** | Revenge, greed, coercion | High (legitimate access) | Malicious admin, compromised employee |
| **Script Kiddie** | Notoriety, curiosity | Low (public tools, no understanding) | Random scanner, skid |

---

## 5. CVSS Scoring

Common Vulnerability Scoring System — standardized severity rating.

### Base Metrics (v3.1)

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

### Severity Ranges
- **None:** 0.0
- **Low:** 0.1 – 3.9
- **Medium:** 4.0 – 6.9
- **High:** 7.0 – 8.9
- **Critical:** 9.0 – 10.0

> **Pentester Tip:** CVSS is a starting point. Always add business context — a Medium vuln on a payment server is often more critical than a High vuln on a dev box.

---

## 6. MITRE ATT&CK Framework

The universal language for describing adversary behavior. Learn this inside out.

### Structure

```
Tactic (Why) 
  └── Technique (How) — T####
        └── Sub-technique (Variant) — T####.###
              └── Procedure (Real-world usage) — By Group/Software
```

### Enterprise Tactics (14)

| Tactic | ID | Description | Example Techniques |
|--------|-----|-------------|-------------------|
| **Reconnaissance** | TA0043 | Gathering target information | T1590 Active Scanning, T1598 Phishing for Info |
| **Resource Development** | TA0042 | Building/buying capabilities | T1583 Acquire Infrastructure, T1587 Develop Capabilities |
| **Initial Access** | TA0001 | Getting into the environment | T1190 Exploit Public-Facing App, T1566 Phishing |
| **Execution** | TA0002 | Running malicious code | T1059 Command & Scripting, T1204 User Execution |
| **Persistence** | TA0003 | Maintaining access | T1505 Server Software Component, T1098 Account Manipulation |
| **Privilege Escalation** | TA0004 | Gaining higher permissions | T1068 Exploitation for Privesc, T1548 Abuse Elevation Control |
| **Defense Evasion** | TA0005 | Avoiding detection | T1027 Obfuscated Files, T1562 Impair Defenses |
| **Credential Access** | TA0006 | Stealing credentials | T1003 OS Credential Dumping, T1555 Credentials from Password Stores |
| **Discovery** | TA0007 | Learning about environment | T1082 System Info Discovery, T1018 Remote System Discovery |
| **Lateral Movement** | TA0008 | Moving through environment | T1021 Remote Services, T1570 Lateral Tool Transfer |
| **Collection** | TA0009 | Gathering data of interest | T1005 Data from Local System, T1560 Archive Collected Data |
| **Command & Control** | TA0011 | Communicating with compromised systems | T1071 Application Layer Protocol, T1573 Encrypted Channel |
| **Exfiltration** | TA0010 | Stealing data | T1041 Exfiltration Over C2 Channel, T1567 Exfiltration Over Web Service |
| **Impact** | TA0040 | Manipulating/destroying systems | T1486 Data Encrypted for Impact, T1491 Defacement |

### Key Distinctions
- **Tactic** = Strategic goal (e.g., "Persistence")
- **Technique** = Specific method (e.g., "T1505.003 Web Shell")
- **Sub-technique** = Granular variant
- **Procedure** = Real-world implementation by a specific group (e.g., "APT29 uses custom ASP.NET web shell")

---

## 7. Cyber Kill Chain

Lockheed Martin's model for attack lifecycle. Use it to map your testing and identify detection gaps.

```
1. Reconnaissance  →  2. Weaponization  →  3. Delivery  →  4. Exploitation
5. Installation    →  6. Command & Control (C2)  →  7. Actions on Objectives
```

| Stage | Pentester Activity | Blue Team Detection |
|-------|-------------------|---------------------|
| **Recon** | OSINT, scanning, enumeration | CT log monitoring, honeypots, scan detection |
| **Weaponization** | Payload generation, exploit development | Malware sandbox, YARA, threat intel |
| **Delivery** | Phishing, watering hole, drive-by | Email gateway, web proxy, EDR |
| **Exploitation** | Exploit execution, RCE | WAF, IPS, EDR behavior monitoring |
| **Installation** | Implant deployment, persistence | EDR, HIDS, file integrity monitoring |
| **C2** | Beaconing, tunneling, domain fronting | DNS monitoring, netflow, SSL inspection |
| **Objectives** | Data theft, destruction, ransomware | DLP, backup verification, anomaly detection |

---

## 8. Diamond Model

Intrusion analysis framework — every intrusion has four core features.

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

---

## 9. Security Models

Theoretical foundations behind every control you'll encounter.

### Bell-LaPadula (Confidentiality)
**"No Read Up, No Write Down"**
- **Simple Security Property:** No Read Up — subject at level L cannot read object at level > L
- ***-Property:** No Write Down — subject at level L cannot write to object at level < L
- Used in: Military/government classified systems, SELinux MLS

### Biba (Integrity)
**"No Read Down, No Write Up"**
- **Simple Integrity Axiom:** No Read Down — subject at level L cannot read object at level < L
- **Integrity *-Property:** No Write Up — subject at level L cannot write to object at level > L
- Used in: Windows Mandatory Integrity Control (Low/Medium/High/System)

### Clark-Wilson (Commercial Integrity)
Integrity through **well-formed transactions** and **separation of duties**.
- **Constrained Data Items (CDI):** Data subject to integrity controls
- **Transformation Procedures (TP):** Only way to modify CDIs — must be certified
- **Integrity Verification Procedures (IVP):** Verify CDIs are in valid state
- Used in: Banking systems, ERP, financial/regulatory systems

---

## 10. Zero Trust Architecture

**Core Principle:** Trust is not granted by network location. Every request is authenticated, authorized, and encrypted.

### NIST 800-207 Tenets
1. All data sources and computing services are resources
2. All communication is secured regardless of network location
3. Access to resources is granted on a per-session basis
4. Access policy is dynamic (based on observable state)
5. Enterprise monitors/measure integrity of all assets
6. Authentication/authorization dynamic and strictly enforced
7. Collect information to improve security posture

### Logical Components
```
Policy Decision Point (PDP) → Policy Enforcement Point (PEP)
    │                              │
    ├── Policy Engine              ├── Proxies, Gateways
    ├── Policy Administrator       ├── Agents, Sidecars
    └── Policy Information Points  └── (enforce decisions)
```

### Pentester View
| Traditional Perimeter | Zero Trust |
|----------------------|------------|
| VPN = trusted network | No VPN; identity-aware proxy |
| Lateral movement easy | Micro-segmentation, per-request auth |
| Compromise = broad access | Compromise = limited to session scope |
| **Target:** VPN, firewall | **Target:** Identity provider, policy engine, token issuance |

---

## 11. Defense in Depth

Multiple overlapping layers. Failure of one layer ≠ total compromise.

```
┌──────────────────────────────────────────────────────────────┐
│                        DATA (Core Asset)                      │
├──────────────────────────────────────────────────────────────┤
│  Application Security (WAF, secure code, input validation)   │
├──────────────────────────────────────────────────────────────┤
│  Host Security (EDR, HIPS, patching, hardening, logging)     │
├──────────────────────────────────────────────────────────────┤
│  Network Security (Segmentation, firewall, IDS/IPS, ZTNA)    │
├──────────────────────────────────────────────────────────────┤
│  Perimeter Security (Border FW, DDoS protection, email gate) │
├──────────────────────────────────────────────────────────────┤
│  Physical Security (Guards, cameras, badge access, cages)    │
├──────────────────────────────────────────────────────────────┤
│  Policies & Awareness (Training, procedures, governance)     │
└──────────────────────────────────────────────────────────────┘
```

**Pentester Strategy:**
1. Identify layers — What controls exist at each level?
2. Find gaps — Missing layer, misconfigured layer, bypassable layer
3. Chain bypasses — Perimeter → Network → Host → App → Data
4. Measure depth — How many layers did you cross? How long at each?

---

## 12. Access Control Models

| Model | Basis | Decision Logic | Use Case |
|-------|-------|----------------|----------|
| **DAC** | Owner discretion | ACLs per object | File systems (Unix perms, Windows ACLs) |
| **MAC** | System policy | Labels (clearance + classification) | Military, high-security (SELinux, TrustedBSD) |
| **RBAC** | Organizational role | Role → Permissions → User | Enterprise apps, cloud IAM (AWS IAM roles) |
| **ABAC** | Attributes (user, resource, env) | Policy engine evaluates attributes | Fine-grained, dynamic (AWS IAM conditions, OPA) |
| **ReBAC** | Relationships | Graph-based (user → resource) | Social apps, file sharing (Google Zanzibar) |

---

## 13. Compliance Frameworks

Drives scope, methodology, and reporting for many engagements.

| Framework | Industry | Mandatory? | Key Pentest Requirements |
|-----------|----------|------------|--------------------------|
| **ISO 27001** | Any | Voluntary (contractual) | A.12.6.1, A.14.2.8, Annex A controls |
| **SOC 2** | SaaS, Service Orgs | Contractual | CC6.1, CC7.1, CC7.2 (Trust Services Criteria) |
| **PCI-DSS** | Payment Cards | Mandatory (card brands) | Req 11.3, 11.4, 6.5.x, 6.6 — CDE scoping critical |
| **HIPAA** | Healthcare (US) | Mandatory (federal) | 164.308(a)(1)(ii)(A), 164.312 — PHI protection |
| **GDPR** | Personal Data (EU) | Mandatory (law) | Art 32, 33, 34 — security of processing, breach notification |
| **NIST 800-53** | US Federal + Contractors | Mandatory (federal) | Control families (AC, AU, CM, IA, IR, SC, SI) |

### PCI-DSS CDE Scoping (Critical)
**Cardholder Data Environment** = All systems that:
- Store, process, transmit CHD (PAN + CVV/expiry/name)
- Connect to CDE systems (flat network, shared services, management)
- Impact CDE security (AD, DNS, NTP, logging, backup, monitoring)

**Required Tests:**
- 11.3.1 External penetration test (annual + after changes)
- 11.3.2 Internal penetration test (annual + after changes)
- 11.3.3 Segmentation test (verify CDE isolation)
- 11.4 Quarterly vulnerability scans (ASV)
- 6.5.x Secure coding (maps to OWASP Top 10)

---

## 14. Security Roles & Career Paths

Cybersecurity isn't one job. Know the landscape to pick your path.

### Role Breakdown

| Role | Mission | Key Skills | Entry Certs | Senior Certs | US Salary (2024) |
|------|---------|------------|-------------|--------------|------------------|
| **SOC Analyst** | Monitor, triage, escalate | SIEM, log analysis, MITRE, basic forensics | Security+, CySA+ | GMON, GCFA, CISSP | $60k–$150k |
| **Penetration Tester** | Find and exploit vulnerabilities | OWASP, network/AD/web, reporting | eJPT, OSCP | OSEP, CRTO, GPEN | $70k–$250k+ |
| **Red Team Operator** | Long-term adversary simulation | C2 dev, evasion, Windows internals, OpSec | CRTO (after OSCP) | OSEP, OSEE, GXPN | $130k–$300k+ |
| **Malware Analyst** | Static/dynamic analysis, reverse engineering | Assembly, IDA/Ghidra, Volatility, YARA | GREM | GMRE, OSED, CREA | $110k–$180k+ |
| **Threat Hunter** | Proactive threat search | MITRE, Sigma/KQL, threat intel, analytics | GMON | GCTI, GCFA | $120k–$170k+ |
| **Detection Engineer** | Build/maintain detections | Sigma, Splunk/Elastic, CI/CD for rules | GMON | Splunk certs, coding | $110k–$160k+ |
| **Incident Responder** | Breach response, forensics | Disk/memory forensics, timeline, malware triage | GCFA, GCFE | GNFA, GREM | $110k–$170k+ |
| **Cloud Security** | Secure cloud infra (AWS/Azure/GCP) | Cloud services, Terraform, K8s, CSPM | Cloud provider certs | AWS Sec Spec, AZ-500, CKS | $120k–$180k+ |
| **AppSec Engineer** | Secure SDLC, code review, SAST/DAST | OWASP ASVS, CodeQL, threat modeling | GWAPT | OSWA, CSSLP | $110k–$170k+ |
| **GRC/Compliance** | Policy, risk, audit, frameworks | ISO 27001, SOC 2, NIST, communication | CISA | CISM, CRISC | $80k–$140k+ |

### Skill Transfer Matrix
| From \ To | SOC | Pentest | Red Team | Malware | Threat Hunt | Detection | DFIR | Cloud | AppSec |
|-----------|-----|---------|----------|---------|-------------|-----------|------|-------|--------|
| **SOC** | — | ★★☆ | ★☆☆ | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ | ★★☆ |
| **Pentest** | ★★☆ | — | ★★★ | ★★☆ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| **Red Team** | ★☆☆ | ★★★ | — | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |

---

## 15. Certifications Roadmap

```
ENTRY LEVEL (0-1 year)
├── CompTIA Security+ (baseline for ALL roles)
├── CompTIA Network+ (if networking is weak)
├── (ISC)² CC (entry, no experience required)
└── eJPT / PNPT (hands-on pentest entry)

SPECIALIZATION (1-3 years)
├── SOC/Blue:     CySA+ → GCIA/GCFA → GMON/GNFA
├── Pentest:      OSCP → OSWA/OSEP → CRTO → OSEE
├── Red Team:     CRTO → OSEP/OSEE → Custom research
├── Malware:      GREM → GMRE → OSED
├── Cloud:        AWS Sec Spec / AZ-500 / GCP Sec Eng
├── AppSec:       GWAPT → OSWA → CodeQL/Semgrep mastery
├── DFIR:         GCFA/GCFE → GNFA → GREM
├── GRC:          CISA → CISM → CRISC

EXPERT / LEADERSHIP (5+ years)
├── CISSP (management track, 5 yrs exp)
├── CCISO (executive)
├── GSE (GIAC Expert — multiple expert certs)
└── Original research, conference speaking
```

> **Cert Strategy:** Certs get interviews. Skills get jobs. **Projects get better jobs.**
> - Pick 1-2 target certs per year max
> - Build a public project for each (GitHub repo, blog writeup, tool)
> - OSCP > 10 theory certs for pentesting roles

---

## 16. Interview Preparation

### Stage Breakdown (Pentest Example)
| Stage | Format | Duration | Focus |
|-------|--------|----------|-------|
| **Phone Screen** | Recruiter + hiring manager | 30-45 min | Background, certs, methodology, availability |
| **Technical Screen** | Senior pentester | 60-90 min | Scenario questions, tool knowledge, vuln classes |
| **Practical** | Live box / take-home / CTF | 2-4 hrs / 1 week | Real engagement simulation, report writing |
| **Panel/Culture** | Team + manager | 60 min | Soft skills, ethics, client communication |

### Answer Frameworks

**Methodology Question ("Walk me through your pentest methodology"):**
```
Phase 1 — Recon: Passive (OSINT, cert transparency, DNS) then active (port scan, service enum, tech fingerprint).
Phase 2 — Threat Modeling: Map attack surface, identify high-value targets, prioritize by client risk.
Phase 3 — Vulnerability Analysis: Automated (Nuclei, Nessus) + manual verification. Focus on business logic, auth, injection.
Phase 4 — Exploitation: Controlled, scoped, documented. PoC only — no persistence unless authorized.
Phase 5 — Post-Exploitation: Privesc, lateral movement sim, data access validation — all mapped to MITRE.
Phase 6 — Reporting: Exec summary (business risk), technical findings (repro steps, evidence, CVSS, remediation).
Throughout: Communication, OpSec, evidence preservation, scope adherence.
```

**Scenario Question ("Critical RCE found on internet-facing server, no WAF"):**
```
1. Stop — verify scope, confirm RoE allows exploitation
2. Document — screenshot, request/response, timestamp
3. Minimal PoC — harmless command (whoami, id) to confirm
4. Do NOT pivot, install implants, access data, modify files
5. Immediately notify — primary + emergency contact per RoE
6. Provide temporary mitigation (block IP, disable endpoint)
7. Continue testing other areas while they remediate
Ethics: Never exceed scope. Never access data not required for PoC. Protect client first.
```

**Deep Technical ("Explain Kerberoasting end-to-end"):**
```
1. Prereqs: Domain user, SPN registered to service account
2. Request: Attacker requests TGS for target SPN (TGS-REQ)
3. Response: KDC encrypts ticket with service account's NTLM hash (RC4_HMAC_MD5 or AES)
4. Offline: Extract ticket (TGS-REP), crack hash (Hashcat, John)
5. Impact: Service accounts often have high privs, passwords never rotate
6. Detection: Event 4769 with RC4 encryption type
7. Mitigation: AES encryption, gMSA, strong passwords, monitoring
```

### Top 20 Technical Questions to Master
1. TCP 3-way handshake and teardown — flags at each step
2. DNS resolution flow — recursive vs iterative, record types
3. ARP poisoning — how it works, detection, prevention
4. TLS handshake — 1.2 vs 1.3, cipher suites, cert validation
5. SQL injection types — error-based, union, blind (boolean, time), stacked
6. XSS — reflected, stored, DOM — payload examples
7. SSRF — blind vs full, cloud metadata, filter bypass
8. Kerberos auth flow — AS-REQ, AS-REP, TGS-REQ, TGS-REP
9. Kerberoasting vs AS-REP Roasting — prerequisites, differences
10. Delegation — unconstrained, constrained, resource-based — abuse paths
11. ACL abuse — GenericAll, GenericWrite, WriteDacl, WriteOwner, AllExtendedRights
12. AD CS — ESC1-ESC13, NTLM relay to HTTP enrollment
13. SUID/SGID — finding, exploiting (GTFOBins), detection
14. Sudo misconfigs — NOPASSWD, env_keep, command injection
15. Capabilities — cap_dac_override, cap_setuid, cap_sys_admin exploitation
16. Kernel exploits — DirtyCow, DirtyPipe, CVE-2021-4034 — version matching
17. Container escape — privileged, hostPID, hostNetwork, cgroup release_agent
18. JWT vulnerabilities — alg:none, key confusion, kid injection, weak secrets
19. CORS misconfigs — null origin, wildcard with credentials
20. File upload bypasses — extension, MIME, magic bytes, polyglots

### Questions YOU Should Ask
- "What methodology does the team follow? PTES? OSSTMM? Custom?"
- "What % web vs network vs cloud vs AD? Red team vs pentest?"
- "Solo or paired? Senior/junior pairing? Mentorship program?"
- "Report template? QA process? Client presentation involvement?"
- "Conference budget? Training budget? Cert support? Research time?"
- "Travel %? On-call? Weekend work? Remote policy?"
- "How does the team handle a finding that delays a client launch?"

---

## 17. Essential Resources

### Frameworks & Standards
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/) — Interactive matrix
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) — CSF, 800-53, 800-171
- [OWASP Testing Guide](https://owasp.org/www-project-testing-guide/) — Web app methodology
- [PTES](http://www.pentest-standard.org/index.php/PTES_Main) — Penetration Testing Execution Standard
- [NIST Glossary](https://csrc.nist.gov/glossary) — Authoritative definitions

### Practice Platforms
- [Hack The Box](https://www.hackthebox.com/) — Realistic boxes, retired machines free
- [TryHackMe](https://tryhackme.com/) — Guided learning paths, beginner-friendly
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — Best free web app training
- [VulnHub](https://www.vulnhub.com/) — Downloadable VMs
- [PicoCTF](https://picoctf.org/) — CTF for learning
- [AttackDefense](https://attackdefense.com/) — Lab environments

### Reference Sites
- [GTFOBins](https://gtfobins.github.io/) — Unix binary exploitation
- [LOLBAS](https://lolbas-project.github.io/) — Windows living-off-the-land
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) — Cheat sheets
- [HackTricks](https://book.hacktricks.xyz/) — Comprehensive pentest notes
- [Exploit-DB](https://www.exploit-db.com/) — Public exploits

### Communities
- [r/netsec](https://www.reddit.com/r/netsec/) — Technical security discussion
- [r/AskNetsec](https://www.reddit.com/r/AskNetsec/) — Career and technical questions
- [Infosec Twitter](https://twitter.com/i/lists/123456) — Follow researchers, vendors, practitioners
- Local OWASP/ISACA/ISSA chapters — Meet people in your area

---

> *"The quieter you become, the more you can hear."* — Master the fundamentals, then the advanced topics make sense.