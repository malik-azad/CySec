---
title: Roles & Career Paths
description: Cybersecurity career taxonomy — Red/Blue/Purple teams, SOC, pentester, red teamer, malware analyst, threat hunter, salaries, certifications
tags: [fundamentals, careers, roles, certifications, salary, job-hunting]
difficulty: beginner
time_estimate: "30 min"
prerequisites: ["fundamentals/terminology.md"]
---

# Roles & Career Paths

> **TL;DR** — Cybersecurity isn't one job. It's a spectrum of specializations. This page maps the landscape so you can choose your path, target the right certifications, and speak the language of hiring managers.

## Why This Matters

"Cybersecurity" job postings range from "monitor alerts for $60k" to "develop 0-day exploits for $300k+". The skills, tools, mindset, and career trajectory are completely different. Knowing where you fit — and where you *want* to fit — saves years of misdirected effort.

---

## The Color Wheel (Team Taxonomy)

| Team | Mission | Mindset | Typical Roles |
|------|---------|---------|---------------|
| **Red Team** | Adversary simulation — find gaps before real attackers | Offensive, creative, persistent, OpSec-obsessed | Red Team Operator, Penetration Tester, Exploit Developer |
| **Blue Team** | Detect, respond, harden — defend the enterprise | Defensive, analytical, process-driven, automation-focused | SOC Analyst, Threat Hunter, Detection Engineer, Incident Responder |
| **Purple Team** | Collaborative improvement — red teaches blue, blue teaches red | Bridge-building, feedback loops, continuous improvement | Purple Team Lead, Detection Engineer (with red experience) |
| **White Team** | Exercise management, scoring, refereeing | Neutral, organizational, process | CTF Organizer, Exercise Planner |

!!! note "Reality Check"
    Most "Red Team" job postings are actually **Penetration Testing** roles. True red teaming (long-term, stealthy, objective-based adversary simulation) is rare outside mature orgs, defense contractors, and Big Tech.

---

## Role Deep Dives

### 1. SOC Analyst (Tier 1 → Tier 2 → Tier 3)

| Tier | Focus | Skills | Certs | Salary (US, 2024) |
|------|-------|--------|-------|-------------------|
| **Tier 1** | Triage alerts, run playbooks, escalate | SIEM (Splunk/QRadar/Sentinel), basic networking, log analysis, ticketing | Security+, CySA+, Splunk Core Certified User | $60k-$85k |
| **Tier 2** | Investigate escalations, write detections, threat intel | MITRE ATT&CK, Sigma rules, malware basics, memory forensics basics | GCIA, GCFA, Splunk Enterprise Certified Admin | $85k-$115k |
| **Tier 3** | Lead incidents, hunt threats, mentor, architecture | Advanced forensics, malware analysis, threat hunting, purple teaming | GMON, GNFA, GREM, CISSP | $115k-$150k+ |

**Progression:** Tier 1 → Tier 2 (1-2 yrs) → Tier 3/Senior (3-5 yrs) → Lead/Manager or pivot to Threat Hunting/IR/Red Team

### 2. Penetration Tester (Consultant / Internal)

| Level | Scope | Skills | Certs | Salary (US, 2024) |
|-------|-------|--------|-------|-------------------|
| **Junior** | Web apps, networks, guided methodology | OWASP Top 10, Nmap, Burp, basic scripting, reporting | eJPT, PNPT, OSCP (studying) | $70k-$95k |
| **Mid** | Full scope: web, network, AD, cloud, mobile, API | AD attacks, privilege escalation, bypass techniques, custom tooling | OSCP, OSWA, OSEP (studying), CRTO | $95k-$135k |
| **Senior** | Complex environments, 0-day research, mentoring | Exploit dev, kernel exploitation, cloud/container escape, OpSec | OSEP, OSEE, CRTO, GPEN, GWAPT | $135k-$180k+ |
| **Principal / Staff** | Strategy, methodology, business development | All above + leadership, sales support, research | Multiple expert certs, conference speaking | $180k-$250k+ |

**Key Distinction:** **Consulting** = variety, travel, multiple clients, billable hours pressure. **Internal** = depth, single org, long-term projects, better WLB.

### 3. Red Team Operator

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Long-term stealthy simulation, custom tooling, OpSec, C2 dev, evasion | C/C++/Rust/Go, Windows internals, kernel, C2 frameworks (Cobalt Strike, Sliver, Brute Ratel), malleable profiles, AV/EDR evasion | CRTO, OSEP, OSEE, GXPN, OSCE (legacy), custom research | $130k-$220k+ |

**Reality:** Requires deep Windows internals, programming, and OpSec discipline. Often requires TS/SCI clearance for defense work.

### 4. Malware Analyst / Reverse Engineer

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Static/dynamic analysis, unpacking, C2 extraction, attribution, YARA | Assembly (x86/x64/ARM), IDA/Ghidra, debuggers, Volatility, YARA, Python, C | GREM, GMRE, OSED, CREA | $110k-$180k+ |

### 5. Threat Hunter

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Proactive search for undetected threats, hypothesis-driven, analytics | MITRE ATT&CK, Sigma/KQL/Splunk SPL, threat intel, data science basics, MITRE D3FEND | GMON, GCTI, GCFA, OSCP (for attacker perspective) | $120k-$170k+ |

### 6. Detection Engineer

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Build/maintain detections, rule lifecycle, false positive reduction, coverage mapping | Sigma, Splunk/KQL/Elastic, MITRE ATT&CK, CI/CD for rules, testing frameworks | GMON, Splunk certs, coding (Python/Go) | $110k-$160k+ |

### 7. Incident Responder / DFIR

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Breach response, forensics, timeline, root cause, eradication, recovery | Disk/memory forensics, Volatility, KAPE, Timeline Explorer, log analysis, malware triage | GCFA, GCFE, GNFA, GREM, CFCE | $110k-$170k+ |

### 8. Cloud Security Engineer

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Secure cloud infra (AWS/Azure/GCP), IaC scanning, CSPM, CI/CD security | Cloud provider services, Terraform, Kubernetes, CSPM tools, container security | AWS Security Specialty, AZ-500, GCP Security Engineer, CKS | $120k-$180k+ |

### 9. Application Security Engineer

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Secure SDLC, SAST/DAST/IAST/SCA, code review, developer enablement | Code review, OWASP ASVS, SAST tools (Semgrep, CodeQL), secure coding, threat modeling | GWAPT, CSSLP, OSWA, application security certs | $110k-$170k+ |

### 10. GRC / Compliance / Security Analyst (Non-Technical Track)

| Focus | Skills | Certs | Salary (US, 2024) |
|-------|--------|-------|-------------------|
| Policy, risk assessment, audit, compliance frameworks, vendor risk | ISO 27001, SOC 2, NIST CSF, PCI-DSS, HIPAA, risk frameworks, communication | CISA, CISM, CRISC, ISO 27001 LA | $80k-$140k+ |

---

## Certification Roadmap by Role

```
ENTRY LEVEL
├── CompTIA Security+ (Baseline for ALL roles)
├── CompTIA Network+ (If weak on networking)
├── (ISC)² CC (Entry cert, no experience req)
└── eJPT / PNPT (Hands-on pentest entry)

SPECIALIZATION
├── SOC/Blue:  CySA+ → GCIA/GCFA → GMON/GNFA
├── Pentest:   OSCP → OSWA/OSEP → CRTO → OSEE
├── Red Team:  CRTO → OSEP/OSEE → Custom Research
├── Malware:   GREM → GMRE → OSED
├── Cloud:     AWS Sec Spec / AZ-500 / GCP Sec Eng
├── AppSec:    GWAPT → OSWA → CodeQL/Semgrep mastery
├── DFIR:      GCFA/GCFE → GNFA → GREM
├── GRC:       CISA → CISM → CRISC

EXPERT / LEADERSHIP
├── CISSP (Management track, 5 yrs exp)
├── CCISO (Executive)
├── GSE (GIAC Expert, multiple expert certs)
└── PhD / Original Research
```

!!! tip "Cert Strategy"
    **Certs get you interviews. Skills get you jobs. Projects get you *better* jobs.**
    - Pick 1-2 target certs per year max
    - Build a public project for each cert (GitHub repo, blog writeup, tool)
    - OSCP > 10 theory certs for pentesting roles

---

## Salary Benchmarks (US, 2024 — Total Comp including bonus/equity)

| Role | Entry (0-2 yr) | Mid (3-5 yr) | Senior (6-10 yr) | Staff/Principal (10+ yr) |
|------|----------------|--------------|------------------|--------------------------|
| SOC Analyst | $60k-$85k | $85k-$115k | $115k-$150k | $150k-$180k |
| Penetration Tester | $70k-$95k | $95k-$135k | $135k-$180k | $180k-$250k |
| Red Team Operator | — | $130k-$160k | $160k-$220k | $220k-$300k+ |
| Malware Analyst | $80k-$100k | $110k-$140k | $140k-$180k | $180k-$230k |
| Threat Hunter | $90k-$110k | $120k-$150k | $150k-$180k | $180k-$220k |
| Detection Engineer | $90k-$110k | $110k-$140k | $140k-$170k | $170k-$210k |
| Incident Responder | $80k-$100k | $110k-$140k | $140k-$170k | $170k-$210k |
| Cloud Security | $90k-$115k | $120k-$150k | $150k-$190k | $190k-$240k |
| AppSec Engineer | $90k-$115k | $110k-$145k | $145k-$180k | $180k-$230k |
| GRC/Compliance | $70k-$90k | $90k-$120k | $120k-$150k | $150k-$180k |

**Non-US Adjustment:** Multiply by ~0.6-0.8 for Western Europe, ~0.3-0.5 for Eastern Europe/Asia/LATAM. Remote US roles changing this.

---

## Skill Overlap Matrix (What Transfers)

| From \ To | SOC | Pentest | Red Team | Malware | Threat Hunt | Detection Eng | DFIR | Cloud Sec | AppSec |
|-----------|-----|---------|----------|---------|-------------|---------------|------|-----------|--------|
| **SOC** | — | ★★☆ | ★☆☆ | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ | ★★☆ |
| **Pentest** | ★★☆ | — | ★★★ | ★★☆ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| **Red Team** | ★☆☆ | ★★★ | — | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| **Malware** | ★☆☆ | ★★☆ | ★★★ | — | ★★☆ | ★★☆ | ★★★ | ★★☆ | ★★☆ |
| **DFIR** | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | — | ★★☆ | ★★☆ |

★★★ = High transfer, ★★☆ = Medium, ★☆☆ = Low

---

## Building Your Portfolio (What Hiring Managers Actually Look At)

| Asset | Pentest/Red Team | Blue Team/Detection | Malware/DFIR | Cloud/AppSec |
|-------|------------------|---------------------|--------------|--------------|
| **GitHub** | Custom tools, exploit PoCs, automation scripts | Sigma rules, detection logic, parser scripts | YARA rules, unpacking scripts, Volatility plugins | Terraform modules, SAST rules, threat models |
| **Blog** | Engagement writeups (sanitized), technique deep-dives | Detection engineering posts, hunt hypotheses | Malware analysis reports, unpacking tutorials | Secure code reviews, vuln class explanations |
| **CTF** | HTB/THM profile, competition writeups | Blue team CTFs, detection challenges | RE challenges, forensics challenges | Web challenges, crypto challenges |
| **Certs** | OSCP, CRTO, OSEP | GMON, GCIA, GCFA | GREM, GMRE, OSED | Cloud provider expert certs |

---

## Interview Preparation by Role

| Role | Technical Screen | Practical Assessment | Soft Skills |
|------|------------------|---------------------|-------------|
| **SOC** | Log analysis exercise, alert triage scenario | "Here's a PCAP/Splunk query — what happened?" | Communication, process adherence, escalation judgment |
| **Pentest** | Methodology walkthrough, vuln identification, exploit chain | Live/box test (HTB-style), report writing sample | Client communication, risk articulation, prioritization |
| **Red Team** | OpSec scenario, C2 design, evasion technique discussion | Multi-stage engagement simulation (rare) | Long-term thinking, tradecraft discipline, ethics |
| **Malware** | Static analysis of sample, unpacking steps, C2 extraction | Live analysis (time-boxed) | Documentation, attribution caution, legal awareness |
| **Detection Eng** | Write Sigma rule for technique, explain false positive tuning | Rule review, coverage gap analysis | Collaboration with analysts, iterative improvement |

---

## Hands-On Lab

!!! abstract "Lab Exercise: Role Self-Assessment"
    **Objective:** Map your current skills to target role requirements.
    
    **Steps:**
    1. Pick 2 target roles from above
    2. For each, list: Required certs, required tools, required knowledge areas
    3. Rate yourself 1-5 on each (1=never heard, 5=teach others)
    4. Identify top 3 gaps per role
    5. Create 90-day learning plan for #1 gap
    
    **Expected Outcome:** Concrete, prioritized learning plan with measurable milestones.

---

## Checklist

- [ ] Can name 10 distinct cybersecurity roles and their primary mission
- [ ] Know the difference between Penetration Testing and Red Teaming
- [ ] Can map 5 certifications to their target roles
- [ ] Understand salary ranges for your target role in your geography
- [ ] Have a GitHub with at least 3 relevant projects for your target role
- [ ] Can articulate your 90-day learning plan for top skill gap

---

## Further Reading

- [NIST NICE Framework](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center) — Official role taxonomy
- [CyberSeek](https://www.cyberseek.org/) — Interactive career pathway & salary data
- [Red Team vs Pentest](https://www.specterops.io/assets/resources/SpecterOps_Red_Team_vs_Pentest.pdf) — SpecterOps whitepaper
- [Certification Comparison](https://pauljerimy.com/security-certification-roadmap/) — Interactive cert roadmap
- [Hiring Manager Perspectives](https://www.reddit.com/r/netsec/comments/hiring_manager_ama/) — Reddit AMAs