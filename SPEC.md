# CySec Master Specification

## Project Vision
A **world-class, practitioner-grade cybersecurity knowledge base** — built for offensive security professionals, pentesters, and red teamers. Beginner-accessible, expert-deep. Every page teaches *how to think*, not just *what to type*.

---

## Technology Stack

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Static Site Generator** | MkDocs + Material Theme | Best-in-class navigation, search, dark mode, responsive, versioning, PDF export, admonitions, tabs, code copy buttons |
| **Content Format** | Markdown + Mermaid diagrams + PlantUML | Version-controllable, diff-friendly, renders beautifully |
| **Search** | mkdocs-material built-in (lunr.js) | Instant client-side search, no external deps |
| **Diagrams** | Mermaid (sequences, flowcharts, graphs) + PlantUML (complex) | Native in MkDocs Material |
| **Hosting** | GitHub Pages (auto-deploy via Actions) | Free, custom domain, HTTPS, CDN |
| **CI/CD** | GitHub Actions | Lint (markdownlint), link check, spell check, build verification |

---

## Repository Structure

```
CySec/
├── .github/
│   └── workflows/
│       └── deploy.yml          # Build + deploy to GitHub Pages
├── docs/
│   ├── index.md                # Landing page
│   ├── fundamentals/           # 🎯 Cybersecurity Fundamentals (interview/job prep)
│   │   ├── index.md
│   │   ├── terminology.md
│   │   ├── roles-careers.md
│   │   ├── security-models.md
│   │   ├── compliance-frameworks.md
│   │   └── interview-guide.md
│   ├── networking/             # ✅ Existing - will enhance
│   │   ├── index.md
│   │   ├── osi-tcpip.md
│   │   ├── ip-subnetting.md
│   │   ├── dns-arp-dhcp.md
│   │   ├── scanning-enumeration.md
│   │   ├── mitm-attacks.md
│   │   ├── firewalls-vpn.md
│   │   └── packet-analysis.md
│   ├── linux/                  # ✅ Existing - will enhance
│   │   ├── index.md
│   │   ├── filesystem-permissions.md
│   │   ├── user-management.md
│   │   ├── process-network.md
│   │   ├── ssh-hardening.md
│   │   ├── bash-scripting.md
│   │   ├── privilege-escalation.md
│   │   ├── log-analysis.md
│   │   └── common-vulns.md
│   ├── recon-osint/            # 🔴 NEW - Priority 0
│   │   ├── index.md
│   │   ├── methodology.md
│   │   ├── passive-recon.md
│   │   ├── active-recon.md
│   │   ├── subdomain-enumeration.md
│   │   ├── osint-frameworks.md
│   │   ├── infrastructure-mapping.md
│   │   ├── people-osint.md
│   │   ├── reporting.md
│   │   └── automation.md
│   ├── websec/                 # 🔴 NEW - Priority 0
│   │   ├── index.md
│   │   ├── methodology.md
│   │   ├── owasp-top10.md
│   │   ├── authentication-authz.md
│   │   ├── injection-attacks.md
│   │   ├── client-side-attacks.md
│   │   ├── ssrf-xxe.md
│   │   ├── api-testing.md
│   │   ├── websocket-testing.md
│   │   ├── cms-frameworks.md
│   │   ├── bypass-techniques.md
│   │   └── reporting.md
│   ├── tools/                  # 🔴 NEW - Priority 1
│   │   ├── index.md
│   │   ├── nmap.md
│   │   ├── burp-suite.md
│   │   ├── wireshark.md
│   │   ├── metasploit.md
│   │   ├── bloodhound.md
│   │   ├── sqlmap.md
│   │   ├── ffuf-feroxbuster.md
│   │   ├── nuclei.md
│   │   ├── crackmapexec.md
│   │   ├── impacket.md
│   │   └── custom-scripts.md
│   ├── privesc/                # 🔴 NEW - Priority 1
│   │   ├── index.md
│   │   ├── linux-enumeration.md
│   │   ├── linux-kernel-exploits.md
│   │   ├── linux-sudo-suid.md
│   │   ├── linux-capabilities.md
│   │   ├── linux-cron-path.md
│   │   ├── linux-containers.md
│   │   ├── windows-enumeration.md
│   │   ├── windows-token-impersonation.md
│   │   ├── windows-dll-hijacking.md
│   │   ├── windows-services-registry.md
│   │   ├── windows-kerberos.md
│   │   ├── windows-uac-bypass.md
│   │   └── checklists.md
│   ├── active-directory/       # 🔴 NEW - Priority 1
│   │   ├── index.md
│   │   ├── fundamentals.md
│   │   ├── kerberos-attacks.md
│   │   ├── delegation-abuse.md
│   │   ├── acl-abuse.md
│   │   ├── adcs-attacks.md
│   │   ├── gpo-abuse.md
│   │   ├── bloodhound-queries.md
│   │   ├── trust-attacks.md
│   │   ├── azure-ad-hybrid.md
│   │   └── persistence.md
│   ├── cryptography/           # 🟡 NEW - Priority 2
│   │   ├── index.md
│   │   ├── tls-certificates.md
│   │   ├── jwt-attacks.md
│   │   ├── padding-oracle.md
│   │   ├── weak-crypto.md
│   │   ├── crypto-in-malware.md
│   │   └── practical-attacks.md
│   ├── malware/                # 🟡 NEW - Priority 2
│   │   ├── index.md
│   │   ├── static-analysis.md
│   │   ├── dynamic-analysis.md
│   │   ├── memory-forensics.md
│   │   ├── yara-rules.md
│   │   ├── sandbox-evasion.md
│   │   ├── c2-frameworks.md
│   │   └── ransomware.md
│   ├── ctf/                    # 🟡 NEW - Priority 2
│   │   ├── index.md
│   │   ├── methodology.md
│   │   ├── writeups/
│   │   │   ├── index.md
│   │   │   ├── htb-machine-name.md
│   │   │   └── ...
│   │   └── challenges/
│   ├── cloud/                  # 🟢 NEW - Priority 3
│   │   ├── index.md
│   │   ├── aws.md
│   │   ├── azure.md
│   │   ├── gcp.md
│   │   ├── containers-k8s.md
│   │   └── serverless.md
│   ├── wireless/               # 🟢 NEW - Priority 3
│   │   ├── index.md
│   │   ├── wpa2-wpa3.md
│   │   ├── evil-twin.md
│   │   ├── pmkid.md
│   │   ├── bluetooth.md
│   │   └── sdr-basics.md
│   ├── mobile/                 # 🟢 NEW - Priority 3
│   │   ├── index.md
│   │   ├── android.md
│   │   ├── ios.md
│   │   ├── frida-objection.md
│   │   └── bypassing-controls.md
│   ├── appendices/             # Reference
│   │   ├── index.md
│   │   ├── port-reference.md
│   │   ├── regex-cheatsheet.md
│   │   ├── file-signatures.md
│   │   ├── mitre-attack.md
│   │   ├── glossary.md
│   │   ├── certifications.md
│   │   └── resources.md
│   └── scripts/                # Automation (not rendered)
│       ├── enum/
│       ├── reporting/
│       └── lab-setup/
├── mkdocs.yml                  # Site configuration
├── requirements.txt            # Python deps
├── .markdownlint.json          # Lint rules
├── .cspell.json                # Spell check config
├── .gitignore
└── README.md                   # GitHub repo readme (points to site)
```

---

## Content Standards

### 1. Page Template (Every Module Page)

```markdown
---
title: "Page Title"
description: "One-sentence summary for SEO/meta"
tags: [tag1, tag2, tag3]
difficulty: beginner|intermediate|advanced
time_estimate: "30 min"
prerequisites: ["link-to-prereq"]
---

# Page Title

> **TL;DR** — 2-3 bullet summary for quick scanning

## Why This Matters
*Real-world context: where this fits in a pentest/red team engagement, what you'll achieve*

## Conceptual Foundation
*Theory explained simply with analogies, diagrams (Mermaid), no jargon without definition*

## Practical Methodology
*Step-by-step workflow used in real engagements*

### Phase 1: [Name]
```bash
# Real commands with explanations
command --flag value  # What this does
```

### Phase 2: [Name]
...

## Tool Reference Table
| Tool | Purpose | Key Flags | Example |
|------|---------|-----------|---------|

## Common Pitfalls & Defenses
| Mistake | Impact | Detection | Mitigation |
|---------|--------|-----------|------------|

## Hands-On Lab
*Link to TryHackMe / HTB / VulnHub / local Docker lab + specific objectives*

## Detection & Blue Team Perspective
*How defenders see this: logs, SIEM rules, Sigma rules, mitigations*

## MITRE ATT&CK Mapping
| Technique | Tactic | ID |
|-----------|--------|----|

## Checklist
- [ ] Actionable item
- [ ] Another item

## Further Reading
- [Link](url) — Why it's valuable
```

### 2. Writing Principles

| Principle | Application |
|-----------|-------------|
| **No AI fluff** | No "In today's digital landscape", "crucial", "delve", "tapestry", "unlock", "master", "comprehensive guide" |
| **Show, don't just tell** | Every concept → command + output example + explanation of *why* |
| **Beginner → Expert progression** | Start with "what/why", build to "how", end with "edge cases/evasion" |
| **Pentester's lens** | Always ask: "How do I exploit this? How do I detect this? How do I defend this?" |
| **Cross-reference aggressively** | `See [[networking/dns-arp-dhcp#dns-attacks|DNS Attacks]] for exploitation` |
| **Version control friendly** | One concept per file, descriptive commit messages |
| **Accessibility** | Alt text for diagrams, semantic headings, color-blind safe diagrams |

### 3. Admonition Types (Use Consistently)

```markdown
!!! note "Key Concept"
    Essential understanding

!!! tip "Pro Tip"
    Real-world trick from experience

!!! warning "Common Mistake"
    What breaks engagements

!!! danger "OpSec Warning"
    Actions that get you caught/banned

!!! example "Real Engagement"
    Anonymized story from actual pentest

!!! abstract "Lab Exercise"
    Hands-on practice with expected outcome
```

### 4. Diagram Standards

- **Mermaid** for: attack flows, network topologies, auth sequences, enumeration trees
- **PlantUML** for: complex AD trust maps, Kerberos flows, cloud architectures
- Always include `title` and meaningful node names
- Use consistent color scheme: 🔴 Attacker, 🔵 Target, 🟢 Defender, 🟡 Data

---

## Navigation & UX

### Main Nav (mkdocs.yml)
```
- Fundamentals
- Networking
- Linux
- Recon & OSINT
- Web Application Security
- Tools Reference
- Privilege Escalation
- Active Directory
- Cryptography
- Malware Analysis
- CTF Writeups
- Cloud Security
- Wireless Security
- Mobile Security
- Appendices
```

### Side Nav (per section)
Auto-generated from folder structure with `nav:` in mkdocs.yml for custom ordering.

### Search Enhancements
- Tags in front matter for faceted search
- Synonyms in `.cspell.json` for common typos

---

## Quality Gates (CI Pipeline)

```yaml
# .github/workflows/ci.yml
jobs:
  lint:
    - markdownlint (strict)
    - cspell (custom dictionary)
    - lychee (link check, ignore localhost)
    - yamllint (mkdocs.yml)
  build:
    - mkdocs build --strict
  test:
    - python -m pytest tests/ (if any)
  deploy:
    - mkdocs gh-deploy --force
```

---

## Contribution Model (Future-Proof)

### Current: Solo Author
- Direct commits to `main`
- PRs only for external contributors
- You review every change

### Future: Community
- `CONTRIBUTING.md` with:
  - Content style guide
  - PR template with checklist
  - Issue templates (typo, new topic, lab request)
  - Code of Conduct
- Maintainers: You + 1-2 trusted peers
- Release tags: `v1.0-fundamentals`, `v2.0-websec`, etc.

---

## Content Creation Workflow (Our Process)

```
1. RESEARCH
   ├─ Read 3-5 authoritative sources (RFCs, vendor docs, conference talks, CTF writeups)
   ├─ Test every command in lab environment
   ├─ Document edge cases, version differences, OpSec considerations

2. DRAFT (in feature branch)
   ├─ Follow page template exactly
   ├─ Write for "me 6 months ago" — explain prerequisites inline
   ├─ Include failed attempts + why they failed

3. REVIEW (you + me)
   ├─ Technical accuracy
   ├─ Completeness (checklist vs spec)
   ├─ Clarity for beginner
   ├─ Cross-links to existing pages

4. POLISH
   ├─ Add diagrams
   ├─ Verify all commands run
   ├─ Add lab references
   ├─ Spell check, link check

5. MERGE & DEPLOY
   ├─ Squash commits with conventional message
   ├─ GitHub Action builds + deploys
   ├─ Verify live site
```

---

## Module Specifications (High-Level)

### Fundamentals (Interview/Job Prep)
| Page | Focus |
|------|-------|
| Terminology | CIA, AAA, risk/threat/vuln, MITRE, kill chain, diamond model, TTP, IOC, CVE/CWE/CAPEC |
| Roles & Careers | Red/Blue/Purple, SOC analyst, pentester, red teamer, malware analyst, threat hunter, salaries, certs |
| Security Models | Bell-LaPadula, Biba, Clark-Wilson, Zero Trust, Defense in Depth |
| Compliance | ISO 27001, SOC2, PCI-DSS, HIPAA, GDPR, NIST CSF — what pentesters need to know |
| Interview Guide | Top 50 questions with answer frameworks, practical challenges, salary negotiation |

### Recon-OSINT
| Page | Focus |
|------|-------|
| Methodology | Passive → Active → Validation → Reporting (structured workflow) |
| Passive Recon | Certificate transparency, DNS history, Wayback, search engines, Shodan, Censys, Grayhat Warfare |
| Active Recon | Port scanning strategies, service enumeration, banner grabbing, technology fingerprinting |
| Subdomain Enum | Sources (CT logs, DNS brute, permutations, APIs), tools, validation, takeover detection |
| OSINT Frameworks | SpiderFoot, theHarvester, Recon-ng, Maltego, custom automation |
| Infrastructure Mapping | ASN, netblocks, CDN detection, cloud asset discovery, shadow IT |
| People OSINT | LinkedIn, GitHub, email harvesting, breach data, social media, phishing prep |
| Reporting | Executive summary, technical findings, risk rating, remediation, evidence packaging |

### WebSec
| Page | Focus |
|------|-------|
| Methodology | Map → Analyze → Attack → Prove → Report (consistent across all vuln classes) |
| OWASP Top 10 | Each: theory → detection → exploitation → bypass WAF → detection → remediation |
| Auth/Authr | Broken auth, session mgmt, JWT flaws, OAuth/OIDC, SSO, MFA bypass |
| Injection | SQLi (all types), NoSQLi, LDAPi, Command, XPATH, template — unified methodology |
| Client-Side | XSS (reflected/stored/DOM), CSRF, clickjacking, CORS, postMessage, CSP bypass |
| SSRF/XXE | Blind/out-of-band, cloud metadata, filter bypass, PDF/upload vectors |
| API Testing | REST/GraphQL/gRPC — authz, rate limit, mass assignment, BOLA, schema analysis |
| WebSocket | Handshake, auth, message tampering, race conditions |
| CMS/Frameworks | WordPress, Drupal, Joomla, Laravel, Django, Spring, .NET — common vulns |
| Bypass Techniques | WAF evasion, filter bypass, encoding, polyglots, race conditions |

### Tools Reference
Each tool page: **Install → Config → Core Workflows → Advanced Features → Cheat Sheet → Real Scenarios → Alternatives**

### PrivEsc (Linux + Windows)
| Category | Techniques Covered |
|----------|-------------------|
| Enumeration | LinPEAS/WinPEAS, manual checks, automated scripts |
| Kernel Exploits | DirtyCow, DirtyPipe, CVE-2021-4034, version matching |
| Sudo/SUID | GTFOBins, sudo -l parsing, LD_PRELOAD, env vars |
| Capabilities | cap_dac_override, cap_setuid, cap_sys_admin — exploitation |
| Cron/Path | Wildcards, PATH hijacking, writable scripts |
| Containers | Escape to host, privileged pods, cgroup release_agent |
| Windows Token | Impersonation, primary vs impersonation, RottenPotato, PrintSpoofer |
| DLL Hijacking | Search order, known DLLs, phantom DLLs, side-loading |
| Services/Registry | Unquoted paths, weak permissions, AlwaysInstallElevated |
| Kerberos | AS-REP roasting, Kerberoasting, delegation, silver/golden tickets |
| UAC Bypass | Fodhelper, eventvwr, sdclt, COM hijacking, mock directories |

### Active Directory
Deep coverage of every major attack path with BloodHound queries, SharpHound collection, mitigation detection.

---

## Metrics for Success

| Metric | Target |
|--------|--------|
| Page load time | < 2s |
| Search relevance | Top 3 results answer query |
| Beginner comprehension | Can follow any page without external tabs |
| Expert depth | Covers 90% of OSCP/OSWE/CRTO syllabus |
| Cross-link density | > 3 internal links per page |
| Command accuracy | 100% tested in lab |
| Update frequency | Quarterly major, monthly minor |

---

## Next Steps (Immediate)

1. **Approve this spec** — confirm structure, templates, standards
2. **I'll create** `mkdocs.yml`, `requirements.txt`, GitHub Actions workflow
3. **You verify** local build works (`mkdocs serve`)
4. **We migrate** existing Networking/Linux content to new structure (split into focused pages)
5. **We build** Fundamentals module first (interview value + foundation for all else)
6. **Then** Recon-OSINT, WebSec in parallel priority

---

**Your call**: Approve spec as-is, or request changes before I generate the site scaffold?