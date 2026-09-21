---
title: Interview Preparation Guide
description: Structured interview prep for cybersecurity roles — technical questions, practical challenges, behavioral, salary negotiation
tags: [fundamentals, interview, career, job-hunting, salary-negotiation]
difficulty: beginner
time_estimate: "45 min"
prerequisites: ["fundamentals/roles-careers.md"]
---

# Interview Preparation Guide

> **TL;DR** — Technical skill gets you the interview. Interview skill gets you the offer. This guide covers the question patterns, practical assessments, and negotiation strategies that separate candidates who get hired from candidates who keep interviewing.

## Why This Matters

You can hack a domain controller in your sleep. But if you cannot explain *why* you chose that technique, *how* you'd detect it, and *what* business risk it represents — you will not pass a senior interview.

Interviews test:
1. **Technical depth** — Can you do the work?
2. **Communication** — Can you explain it to a CISO?
3. **Judgment** — Do you prioritize correctly under pressure?
4. **Culture fit** — Will you break things responsibly?

---

## Interview Stages by Role

### Penetration Tester / Red Team
| Stage | Format | Duration | Focus |
|-------|--------|----------|-------|
| **Phone Screen** | Recruiter + hiring manager | 30-45 min | Background, certs, methodology, availability |
| **Technical Screen** | Senior pentester / team lead | 60-90 min | Scenario questions, tool knowledge, vulnerability classes |
| **Practical Assessment** | Live box / take-home / CTF | 2-4 hrs (live) / 1 week (take-home) | Real engagement simulation, report writing |
| **Panel / Culture** | Team + manager + maybe client-facing | 60 min | Soft skills, ethics, client communication |
| **Offer / Negotiation** | Recruiter / hiring manager | 30 min | Compensation, benefits, start date |

### SOC Analyst / Blue Team
| Stage | Format | Duration | Focus |
|-------|--------|----------|-------|
| **Phone Screen** | Recruiter + SOC lead | 30 min | Log analysis basics, SIEM experience, shift flexibility |
| **Technical Screen** | Senior analyst | 60 min | Alert triage exercise, MITRE mapping, detection logic |
| **Practical** | Live Splunk/Elastic / PCAP analysis | 60-90 min | "Here are logs — what happened?" |
| **Panel** | Team + manager | 45 min | Process adherence, escalation judgment, burnout resilience |

### Detection Engineer / Threat Hunter
| Stage | Format | Duration | Focus |
|-------|--------|----------|-------|
| **Phone Screen** | Recruiter + engineering lead | 30 min | Coding, Sigma, data pipelines, MITRE |
| **Technical** | Senior detection engineer | 90 min | Write detection for TTP, false positive tuning, coverage gaps |
| **Practical** | Take-home: build detection rule + test | 1 week | End-to-end: hypothesis → rule → test → documentation |
| **Architecture** | Staff engineer | 60 min | Pipeline design, scale, CI/CD for rules |

---

## Question Categories & Answer Frameworks

### 1. Methodology Questions (Every Role)

**Question:** "Walk me through your penetration testing methodology."

**Bad Answer:** "I run Nmap, then Nikto, then Metasploit."

**Strong Answer Framework:**
```
"Phase 1 — Reconnaissance: Passive (OSINT, cert transparency, DNS history) then active (port scan, service enum, tech fingerprint). Tools: Nmap, Amass, Subfinder, httpx.

Phase 2 — Threat Modeling: Map attack surface, identify high-value targets, prioritize based on client risk appetite.

Phase 3 — Vulnerability Analysis: Automated scanning (Nuclei, Nessus) + manual verification. Focus on business logic, auth, injection.

Phase 4 — Exploitation: Controlled, scoped, documented. Proof-of-concept only — no persistence unless authorized.

Phase 5 — Post-Exploitation: Privilege escalation, lateral movement simulation, data access validation — all mapped to MITRE ATT&CK.

Phase 6 — Reporting: Executive summary (business risk), technical findings (reproducible steps, evidence, CVSS, remediation), attestation letters.

Throughout: Constant communication, OpSec, evidence preservation, scope adherence."
```

**Why This Works:** Structured, references standards (MITRE, PTES), mentions communication and OpSec.

### 2. Scenario Questions (The "What Would You Do" Questions)

**Question:** "You find a critical RCE on an internet-facing server during an external pentest. The client has no WAF. What do you do?"

**Answer Framework (STAR + Ethics):**
```
Situation: Critical RCE found, no WAF, internet-facing.
Task: Prove impact without causing harm.
Action:
  1. Stop — verify scope, confirm rules of engagement allow exploitation.
  2. Document — screenshot, request/response, timestamp.
  3. Minimal PoC — execute harmless command (whoami, id) to confirm.
  4. Do NOT: pivot, install implants, access data, modify files.
  4. Immediately notify — primary contact + emergency contact per RoE.
  5. Provide temporary mitigation guidance (block IP, disable endpoint).
  6. Continue testing other areas while they remediate.
Result: Client patches same day. Finding reported as Critical with clear reproduction steps.
Ethics: Never exceed scope. Never access data not required for PoC. Protect client first.
```

### 3. Deep Technical Questions (Show Your Work)

**Question:** "Explain how Kerberoasting works end-to-end."

**Answer Structure:**
```
1. Prerequisites: Domain user account, SPN registered to service account.
2. Request: Attacker requests TGS for target SPN (kerberos TGS-REQ).
3. Response: KDC encrypts ticket with service account's NTLM hash (RC4_HMAC_MD5 or AES).
4. Offline: Attacker extracts ticket (TGS-REP), cracks hash offline (Hashcat, John).
5. Impact: Service account often has high privileges, password never rotates.
6. Detection: Event ID 4769 (Kerberos Service Ticket Request) with RC4 encryption type.
7. Mitigation: AES encryption, managed service accounts (gMSA), strong passwords, monitoring.
```

**Key Elements:** Protocol flow, crypto detail, impact, detection, mitigation.

### 4. "I Don't Know" Questions (Graceful Recovery)

**Question:** "How does CVE-2023-XXXX exploitation work?" (Something you haven't seen)

**Good Response:**
```
"I haven't analyzed that specific CVE yet. Here is how I would approach it:
1. Read the advisory and affected versions.
2. Check for public PoC or analysis (GitHub, Exploit-DB, vendor blog).
3. Set up vulnerable version in lab.
4. Diff the patch to understand root cause.
5. Build reliable exploit with proper error handling.
6. Test detection opportunities.
7. Document for team knowledge base.

For similar vuln class [X], I have done [Y]. The principles transfer."
```

**Why This Works:** Shows process, honesty, learning ability, related experience.

---

## Top 50 Technical Questions (Categorized)

### Networking & Protocols
1. TCP 3-way handshake and teardown — what flags at each step?
2. UDP vs TCP — when does each matter for an attacker?
3. DNS resolution flow — recursive vs iterative, record types.
4. ARP poisoning — how it works, detection, prevention.
5. TLS handshake — 1.2 vs 1.3 differences, cipher suites, cert validation.
6. DHCP starvation and rogue DHCP — attack and mitigation.
7. VLAN hopping — switch spoofing vs double tagging.
8. BGP hijacking — how it works, real-world examples.
9. IPv6 security implications — neighbor discovery, RA guard.
10. MTU and fragmentation attacks — overlapping fragments, IDS evasion.

### Web Application Security
11. OWASP Top 10 2021 — rank them by prevalence in your experience.
12. SQL injection types — error-based, union, blind (boolean, time), stacked.
13. XSS — reflected, stored, DOM — payload examples for each.
14. CSRF — same-site cookies, token patterns, bypass techniques.
15. SSRF — blind vs semi-blind vs full, cloud metadata, filter bypass.
16. XXE — payload variations, out-of-band, blind XXE.
17. IDOR / BOLA — testing methodology, automation.
18. JWT vulnerabilities — alg:none, key confusion, kid injection, weak secrets.
19. CORS misconfigurations — null origin, wildcard with credentials.
20. File upload bypasses — extension, MIME, magic bytes, polyglots.
21. Deserialization — Java, .NET, PHP, Python — gadget chains.
22. Template injection (SSTI) — detection, payload construction.
23. Business logic flaws — examples from real engagements.
24. API security — GraphQL introspection, batching, depth limits.
25. WebSocket testing — handshake, message tampering, auth.

### Active Directory / Windows
26. Kerberos authentication flow — AS-REQ, AS-REP, TGS-REQ, TGS-REP.
27. Kerberoasting vs AS-REP Roasting — prerequisites, differences.
28. Delegation — unconstrained, constrained, resource-based — abuse paths.
29. ACL abuse — GenericAll, GenericWrite, WriteDacl, WriteOwner, AllExtendedRights.
30. AD CS (Certificate Services) — ESC1-ESC13, NTLM relay to HTTP enrollment.
31. GPO abuse — immediate tasks, startup scripts, registry, permissions.
32. DCSync / DCShadow — prerequisites, detection (Event 4662, 4742).
33. Silver / Golden tickets — krbtgt hash, PAC, lifetime, detection.
34. Password spray vs credential stuffing — tools, detection, lockout policies.
35. LAPS — misconfigurations, clear-text passwords in AD.
36. BloodHound — SharpHound collectors, key queries, attack paths.
37. Privilege escalation — token impersonation (RottenPotato, PrintSpoofer).
38. UAC bypass — fodhelper, eventvwr, sdclt, COM hijacking.
39. DLL hijacking — search order, known DLLs, phantom DLLs.
40. Windows event logs — 4624, 4625, 4672, 4688, 4698, 5140, 5145.

### Linux / Privilege Escalation
41. SUID/SGID — finding, exploiting (GTFOBins), detection.
42. Sudo misconfigurations — NOPASSWD, env_keep, command injection.
43. Capabilities — cap_dac_override, cap_setuid, cap_sys_admin exploitation.
44. Cron jobs — wildcards, PATH, writable scripts.
45. Kernel exploits — DirtyCow, DirtyPipe, CVE-2021-4034 — version matching.
46. Container escape — privileged, hostPID, hostNetwork, cgroup release_agent.
47. SSH keys — agent forwarding, key reuse, authorized_keys injection.
48. LD_PRELOAD / LD_LIBRARY_PATH — hijacking, detection.
49. /proc / /sys / /dev — information disclosure, exploitation.
50. Auditd / Sysmon for Linux — rule writing, detection coverage.

---

## Practical Assessment Preparation

### Live Box Test (2-4 Hours)
| What They Watch | How to Excel |
|-----------------|--------------|
| **Methodology** | Narrate: "I am doing X because Y" |
| **Tool Usage** | Right tool, right flags, interpret output |
| **Note Taking** | Real-time documentation (CherryTree, Obsidian, OneNote) |
| **Scope Adherence** | Ask before pivoting, document authorization |
| **Communication** | Slack/Teams updates every 30-60 min |
| **Report Quality** | Executive summary + technical details + evidence |
| **Cleanup** | Remove tools, restore state, document |

**Prep:** Practice on HTB/THM/VulnHub with a timer. Write full report afterward. Get feedback.

### Take-Home Assessment (1 Week)
| Deliverable | Expectation |
|-------------|-------------|
| **Methodology Doc** | 1-2 pages: approach, tools, scope interpretation |
| **Findings** | 3-5 vulnerabilities with reproduction steps |
| **Report** | Professional template: exec summary, findings, remediation |
| **Code/Tools** | Any custom scripts used (clean, commented) |
| **Time Log** | Hours spent per phase (honest) |

**Prep:** Build a template repo. Practice on 3-4 boxes. Time yourself.

### Detection Engineering Take-Home
| Deliverable | Expectation |
|-------------|-------------|
| **Hypothesis** | "I believe technique X is detectable via data source Y" |
| **Sigma Rule** | Valid YAML, tested against test data |
| **Test Data** | Generated or sourced (Atomic Red Team, custom) |
| **False Positive Analysis** | Legitimate triggers, tuning strategy |
| **Coverage Map** | MITRE tactic/technique coverage before/after |
| **Documentation** | Runbook for analysts |

---

## Behavioral Questions (STAR Method)

| Question | What They Want |
|----------|----------------|
| "Tell me about a time you found a critical vulnerability." | Impact, communication, remediation follow-through |
| "Describe a situation where you disagreed with a client/manager." | Professional conflict resolution, evidence-based |
| "When did you make a mistake during an engagement?" | Accountability, learning, process improvement |
| "How do you handle burnout / high-pressure periods?" | Self-awareness, boundaries, sustainability |
| "Tell me about a time you had to explain technical risk to non-technical stakeholders." | Translation skill, business alignment |

**STAR Template:**
```
Situation: Brief context (1-2 sentences)
Task: Your responsibility (1 sentence)
Action: What YOU did — specific, detailed (3-5 sentences)
Result: Quantified outcome + what you learned (2-3 sentences)
```

---

## Questions YOU Should Ask

| Category | Questions |
|----------|-----------|
| **Methodology** | "What methodology does the team follow? PTES? OSSTMM? Custom?" |
| **Tooling** | "What tools are standard? Budget for licenses (Burp Pro, Cobalt Strike)?" |
| **Engagement Type** | "What % web vs network vs cloud vs AD? Red team vs pentest?" |
| **Team Structure** | "Solo or paired? Senior/junior pairing? Mentorship program?" |
| **Reporting** | "Report template? QA process? Client presentation involvement?" |
| **Professional Development** | "Conference budget? Training budget? Cert support? Research time?" |
| **Work Life** | "Travel %? On-call? Weekend work? Remote policy?" |
| **Culture** | "How does the team handle a finding that delays a client launch?" |
| **Business** | "Client retention rate? Average engagement size? Growth areas?" |

---

## Salary Negotiation Framework

### Know Your Numbers
| Component | Research Sources |
|-----------|------------------|
| **Base Salary** | Levels.fyi, Glassdoor, Blind, Paysa, Robert Half, Dice |
| **Bonus** | Target %, actual payout history, clawback clauses |
| **Equity** | RSUs vs options, vesting schedule, 409A valuation, liquidity |
| **Benefits** | 401k match, HSA, insurance, PTO, education budget, equipment |
| **Total Comp** | Base + Bonus + Equity (annualized) + Benefits value |

### Negotiation Script
```
"Thank you for the offer. I am excited about the role and the team.

Based on my research and the value I bring — [specific: OSCP + 3 years consulting + custom tooling + detection engineering] — I was targeting a total compensation of $X.

The offer at $Y is close. Could we explore:
1. Base salary of $Z (market 75th percentile for this role/geo)
2. Sign-on bonus of $A (bridges equity vesting cliff)
3. Professional development budget of $B/year
4. One additional week PTO

I want to make this work. What flexibility exists?"
```

### Leverage Points
- **Competing offers** (strongest)
- **Unique skills** (rare certs, niche expertise, published research)
- **Immediate availability** (they need someone now)
- **Referral** (internal champion)

---

## Red Flags (Decline If You See These)

| Red Flag | Why It Matters |
|----------|----------------|
| No methodology, "wing it" culture | Inconsistent quality, burnout, legal risk |
| No QA on reports | Your name on bad work |
| Unlimited scope creep without change orders | Unpaid labor, missed deadlines |
| No training budget / cert support | Stagnation, market value drops |
| High turnover (>30%/yr) | Toxic culture, bad management |
| "We don't do written reports" | Unprofessional, unusable for compliance |
| Recruiter cannot explain the role | Disorganized hiring = disorganized org |
| Pressure to accept immediately | Desperation, hidden problems |

---

## Hands-On Lab

!!! abstract "Lab Exercise: Mock Interview Loop"
    **Objective:** Simulate full interview process for target role.
    
    **Setup:**
    1. Find a peer/mentor (or record yourself)
    2. Pick target role
    3. Run: Phone screen → Technical → Practical → Behavioral
    4. Time each stage
    5. Debrief: What felt weak? What questions stumped you?
    
    **Deliverables to Practice:**
    - 2-minute "tell me about yourself" tailored to role
    - 5-minute methodology walkthrough
    - 3 scenario responses (STAR)
    - 3 questions for them
    - Salary negotiation script
    
    **Expected Outcome:** 3 things to improve, 3 strengths to highlight, confident delivery.

---

## Checklist

- [ ] Can explain your methodology in 3 minutes without notes
- [ ] Have 5 STAR stories ready (critical finding, mistake, conflict, pressure, translation)
- [ ] Can answer 80% of the Top 50 technical questions
- [ ] Completed 2 timed practical assessments with written reports
- [ ] Resume tailored to target role (keywords from job description)
- [ ] GitHub has 3+ relevant projects with READMEs
- [ ] LinkedIn profile matches resume, keywords optimized
- [ ] Researched salary bands for role/geo/experience
- [ ] Prepared 5 questions for each interview stage
- [ ] Practiced negotiation script with a peer

---

## Further Reading

- [Cracking the Coding Interview](https://www.crackingthecodinginterview.com/) — Behavioral framework
- [Never Split the Difference](https://www.neversplitthedifference.com/) — Negotiation (Chris Voss)
- [Staff Engineer](https://staffeng.com/) — Senior IC career path
- [The Holloway Guide to Technical Recruiting](https://www.holloway.com/g/technical-recruiting) — Employer perspective
- [Red Team Interview Questions](https://github.com/redteam-archives/redteam-interview-questions) — Community list
- [Detection Engineering Interview Prep](https://github.com/ detection-engineering/interview-prep) — Community resources