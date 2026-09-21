---
title: CySec — Cybersecurity Knowledge Base
description: Professional offensive security documentation for pentesters, red teamers, and security engineers
tags: [landing, overview]
difficulty: beginner
---

# CySec

> **Professional cybersecurity knowledge base** — Built for offensive security practitioners, by practitioners.
> Every page teaches *how to think*, not just *what to type*.

---

## 🎯 What Is This?

CySec is a structured, battle-tested reference for **offensive security** — penetration testing, red teaming, vulnerability research, and exploit development. It's designed to be:

| For Beginners | For Experts |
|---------------|-------------|
| Clear explanations with analogies | Deep technical detail & edge cases |
| Step-by-step methodologies | Real engagement workflows |
| Prerequisites linked inline | OpSec considerations & evasion |
| Hands-on lab references | Detection & blue team perspective |

---

## 🧭 Navigation

<div class="grid cards" markdown>

- :material-shield-key: **Fundamentals** — Terminology, roles, security models, compliance, interview prep
  [Start Learning →](fundamentals/index.md)

- :material-network: **Networking** — OSI/TCP-IP, subnetting, DNS/ARP/DHCP, scanning, MITM, packet analysis
  [View Networking →](networking/index.md)

- :material-console: **Linux** — Filesystem, permissions, users, processes, SSH, bash, privilege escalation, logs
  [View Linux →](linux/index.md)

- :material-magnify: **Recon & OSINT** — Methodology, passive/active recon, subdomain enum, infrastructure mapping, reporting
  [View Recon →](recon-osint/index.md)

- :material-web: **Web Application Security** — OWASP Top 10, auth, injection, SSRF/XXE, API testing, bypass techniques
  [View WebSec →](websec/index.md)

- :material-toolbox: **Tools Reference** — Nmap, Burp, Wireshark, Metasploit, BloodHound, Nuclei, Impacket, custom scripts
  [View Tools →](tools/index.md)

- :material-arrow-up-bold: **Privilege Escalation** — Linux & Windows: kernel, sudo/SUID, capabilities, tokens, DLL, UAC, Kerberos
  [View Privesc →](privesc/index.md)

- :material-domain: **Active Directory** — Kerberos, delegation, ACLs, AD CS, GPO, BloodHound, Azure AD, persistence
  [View AD →](active-directory/index.md)

- :material-lock: **Cryptography** — TLS/certs, JWT, padding oracle, weak crypto, crypto in malware, practical attacks
  [View Crypto →](cryptography/index.md)

- :material-bug: **Malware Analysis** — Static/dynamic analysis, memory forensics, YARA, sandbox evasion, C2, ransomware
  [View Malware →](malware/index.md)

- :material-flag: **CTF Writeups** — Methodology-focused writeups from HTB, THM, competitions
  [View CTF →](ctf/index.md)

- :material-cloud: **Cloud Security** — AWS, Azure, GCP, containers/K8s, serverless
  [View Cloud →](cloud/index.md)

- :material-wifi: **Wireless Security** — WPA2/3, evil twin, PMKID, Bluetooth, SDR
  [View Wireless →](wireless/index.md)

- :material-cellphone: **Mobile Security** — Android, iOS, Frida/Objection, bypassing controls
  [View Mobile →](mobile/index.md)

- :material-book-open-page-variant: **Appendices** — Ports, regex, file signatures, MITRE ATT&CK, glossary, certifications
  [View Appendices →](appendices/index.md)

</div>

---

## 📖 How to Use This Site

### Reading Paths

| Goal | Recommended Order |
|------|-------------------|
| **New to Cybersecurity** | Fundamentals → Networking → Linux → Recon → WebSec |
| **Pentest Prep (OSCP/CRTO)** | Networking → Linux → Recon → WebSec → Privesc → AD → Tools |
| **Red Team Focus** | Networking → Linux → AD → Privesc → Tools → Malware → C2 |
| **Web App Specialist** | Fundamentals → Networking → WebSec → Tools → Crypto |
| **Interview Prep** | Fundamentals → Appendices (Glossary, MITRE, Certifications) |

### Page Conventions

!!! tip "Pro Tip"
    Every page follows a consistent structure: **Why This Matters → Conceptual Foundation → Practical Methodology → Tool Reference → Pitfalls & Defenses → Hands-On Lab → Detection → MITRE Mapping → Checklist**

| Symbol | Meaning |
|--------|---------|
| `🔴` | Critical / High severity |
| `🟡` | Medium severity / Caution |
| `🟢` | Low severity / Informational |
| `💡` | Pro tip from real engagements |
| `⚠️` | Common mistake that breaks things |
| `🚨` | OpSec warning — gets you caught |
| `🧪` | Lab exercise with expected outcome |
| `🕵️` | Real engagement anecdote (anonymized) |

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `s` / `/` | Focus search |
| `Esc` | Close search / modals |
| `n` | Next page in section |
| `p` | Previous page in section |
| `g` + `h` | Go to home |
| `?` | Show help |

---

## 🔬 Philosophy

```
Theory without practice is sterile.
Practice without theory is blind.
— Immanuel Kant (adapted for infosec)
```

1. **Understand the *why*** — Every technique maps to a root cause (design flaw, implementation bug, misconfiguration)
2. **Master the fundamentals** — Networking, OS internals, protocols, crypto. Advanced attacks are just creative combinations of basics.
3. **Think like a defender** — Every attack page includes detection: logs, Sigma rules, mitigations. This makes you a better attacker.
4. **Document everything** — Your notes become your playbook. This repo *is* that playbook.
5. **Stay ethical** — Only test systems you own or have explicit written permission for. Unauthorized access is a crime.

---

## 🚀 Quick Start

### View Locally

```bash
# Clone the repo
git clone https://github.com/malik-azad/CySec.git
cd CySec

# Install dependencies
pip install -r requirements.txt

# Serve locally with live reload
mkdocs serve

# Open http://localhost:8000
```

### Contribute

See [CONTRIBUTING.md](https://github.com/malik-azad/CySec/blob/main/CONTRIBUTING.md) for guidelines.

### Report Issues

Found an error? [Open an issue](https://github.com/malik-azad/CySec/issues/new/choose) — we'll fix it.

---

## 📊 Project Status

| Module | Pages | Status | Last Updated |
|--------|-------|--------|--------------|
| Fundamentals | 6 | 🟡 In Progress | {{ git_last_modified('docs/fundamentals/index.md') }} |
| Networking | 8 | 🟢 Migrating | {{ git_last_modified('docs/networking/index.md') }} |
| Linux | 9 | 🟢 Migrating | {{ git_last_modified('docs/linux/index.md') }} |
| Recon & OSINT | 10 | 🔴 Planned | — |
| Web Application Security | 11 | 🔴 Planned | — |
| Tools Reference | 12 | 🔴 Planned | — |
| Privilege Escalation | 13 | 🔴 Planned | — |
| Active Directory | 11 | 🔴 Planned | — |
| Cryptography | 7 | 🔴 Planned | — |
| Malware Analysis | 8 | 🔴 Planned | — |
| CTF Writeups | 3+ | 🔴 Planned | — |
| Cloud Security | 6 | 🔴 Planned | — |
| Wireless Security | 6 | 🔴 Planned | — |
| Mobile Security | 5 | 🔴 Planned | — |
| Appendices | 8 | 🔴 Planned | — |

---

## 📜 License

This work is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

[View License →](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> You are free to: **Share** (copy/redistribute) and **Adapt** (remix/transform/build upon)
> Under terms: **Attribution**, **NonCommercial**, **ShareAlike**

---

## 🙏 Acknowledgments

Built on the shoulders of giants. Special thanks to the security community:

- **Offensive Security** — OSCP, OSWE, OSEP, EXP courses
- **PortSwigger** — Web Security Academy
- **Hack The Box** & **TryHackMe** — Hands-on labs
- **MITRE** — ATT&CK Framework
- **OWASP** — Top 10, ASVS, Testing Guide
- **SpecterOps** — BloodHound, AD research
- **ProjectDiscovery** — Nuclei, Subfinder, httpx
- **Carlospolop** — PEASS-ng (LinPEAS/WinPEAS)
- **GhostPack** — Rubeus, Certify, SharpDPAPI
- **Every CTF author & writeup writer** — You teach us how to think

---

## 📬 Connect

<div class="social-links" markdown>
[![GitHub](https://img.shields.io/badge/GitHub-malik--azad-181717?logo=github)](https://github.com/malik-azad)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-malikazad-0A66C2?logo=linkedin)](https://linkedin.com/in/malikazad)
[![Twitter](https://img.shields.io/badge/Twitter-@malikazad-1DA1F2?logo=twitter)](https://twitter.com/malikazad)
</div>

---

*Last updated: {{ current_year() }} | Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) | [View Source](https://github.com/malik-azad/CySec)*