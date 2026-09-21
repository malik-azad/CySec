---
title: Security Models & Frameworks
description: Foundational security models — Bell-LaPadula, Biba, Clark-Wilson, Zero Trust, Defense in Depth, NIST CSF
tags: [fundamentals, security-models, bell-lapadula, biba, clark-wilson, zero-trust, defense-in-depth, nist]
difficulty: beginner
time_estimate: "30 min"
prerequisites: ["fundamentals/terminology.md"]
---

# Security Models & Frameworks

> **TL;DR** — Security models are the *theoretical foundations* behind every control you'll encounter. They explain **why** a control exists, **what** it protects, and **where** it fails. Understanding them lets you predict bypasses before you even touch a keyboard.

## Why This Matters

Every firewall rule, ACL, encryption requirement, and audit finding traces back to a security model. When you understand the model, you understand:
- The **assumptions** the control makes (and where they break)
- The **threat model** it addresses (and what it ignores)
- The **bypass strategies** that naturally emerge from its design

---

## Classic Confidentiality/Integrity Models

### Bell-LaPadula (BLP) — "No Read Up, No Write Down"

**Goal:** Confidentiality (prevent unauthorized disclosure)
**Context:** Military/government classified systems (1970s)

| Rule | Formal Name | Plain English |
|------|-------------|---------------|
| **Simple Security Property** | No Read Up | Subject at level L cannot read object at level > L |
| ***-Property (Star Property)** | No Write Down | Subject at level L cannot write to object at level < L |
| **Discretionary Security** | Need-to-know | DAC enforces additional restrictions |

```
CLEARANCE LEVELS (High → Low)
TOP SECRET  ◄── Can read SECRET, CONFIDENTIAL
SECRET      ◄── Can read CONFIDENTIAL
CONFIDENTIAL◄── Can read UNCLASSIFIED
UNCLASSIFIED
```

**Pentester View:**
- **Bypass:** Write up (exfiltrate via higher-clearance process), covert channels, mislabeled objects
- **Real-world:** Rarely implemented purely. Modern MAC (SELinux, AppArmor) uses similar principles.

### Biba — "No Read Down, No Write Up"

**Goal:** Integrity (prevent unauthorized modification)
**Context:** Commercial systems where data accuracy > secrecy

| Rule | Formal Name | Plain English |
|------|-------------|---------------|
| **Simple Integrity Axiom** | No Read Down | Subject at level L cannot read object at level < L |
| **Integrity *-Property** | No Write Up | Subject at level L cannot write to object at level > L |

```
INTEGRITY LEVELS (High → Low)
CRITICAL    ──▶ Can write to HIGH, MEDIUM, LOW
HIGH        ──▶ Can write to MEDIUM, LOW
MEDIUM      ──▶ Can write to LOW
LOW
```

**Pentester View:**
- **Bypass:** Read up (contaminate high-integrity process with low-integrity input), TOCTOU, supply chain
- **Real-world:** Windows Mandatory Integrity Control (MIC) — Low/Medium/High/System integrity levels

### Clark-Wilson — Commercial Integrity via Transactions

**Goal:** Integrity through **well-formed transactions** and **separation of duties**

**Core Concepts:**
| Concept | Description |
|---------|-------------|
| **Constrained Data Items (CDI)** | Data subject to integrity controls |
| **Unconstrained Data Items (UDI)** | Data not subject to controls (input/output) |
| **Transformation Procedures (TP)** | Only way to modify CDIs — must be certified |
| **Integrity Verification Procedures (IVP)** | Verify CDIs are in valid state |
| **Separation of Duties** | No single user can complete critical transaction alone |

**Rules:**
1. All TPs must be certified
2. IVPs must verify CDIs
3. Users can only execute TPs they're authorized for
4. Separation of duties enforced
5. Audit trail for all TP executions

**Pentester View:**
- **Bypass:** TP logic flaws, race conditions, authorization bypass, audit log tampering
- **Real-world:** Banking systems, ERP, any system with financial/regulatory integrity requirements

---

## Modern Architectural Models

### Zero Trust — "Never Trust, Always Verify"

**Core Principle:** Trust is not granted by network location. Every request is authenticated, authorized, and encrypted.

**NIST 800-207 Zero Trust Architecture (ZTA) Tenets:**
1. **All data sources and computing services are resources**
2. **All communication is secured regardless of network location**
3. **Access to resources is granted on a per-session basis**
4. **Access policy is dynamic (based on observable state)**
5. **Enterprise monitors/measure integrity of all assets**
6. **Authentication/authorization dynamic and strictly enforced**
7. **Collect information to improve security posture**

**Logical Components:**
```
┌─────────────────────────────────────────────────────────────┐
│                    Policy Decision Point (PDP)              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Policy      │  │ Policy      │  │ Policy Information  │  │
│  │ Engine      │──▶│ Administrator│──▶│ Points (PIPs)       │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Policy Enforcement Point (PEP)                 │
│  (Proxies, Gateways, Agents, Sidecars — enforce decisions)  │
└─────────────────────────────────────────────────────────────┘
```

**Pentester View:**
| Traditional Perimeter | Zero Trust |
|----------------------|------------|
| VPN = trusted network | No VPN; identity-aware proxy |
| Lateral movement easy | Micro-segmentation, per-request auth |
| Compromise = broad access | Compromise = limited to session scope |
| **Bypass:** Token theft, session hijacking, PIP poisoning, policy misconfig | **Target:** Identity provider, policy engine, token issuance |

### Defense in Depth (Layered Security)

**Concept:** Multiple overlapping layers of defense. Failure of one layer ≠ total compromise.

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
1. **Identify layers** — What controls exist at each level?
2. **Find gaps** — Missing layer, misconfigured layer, bypassable layer
3. **Chain bypasses** — Perimeter → Network → Host → App → Data
4. **Measure depth** — How many layers did you cross? How long at each?

### NIST Cybersecurity Framework (CSF) 2.0

**Core Functions (Govern added in 2.0):**
```
GOVERN (GV) → IDENTIFY (ID) → PROTECT (PR) → DETECT (DE) → RESPOND (RS) → RECOVER (RC)
```

| Function | Key Categories | Pentest Relevance |
|----------|----------------|-------------------|
| **Govern** | Risk strategy, roles, policy, oversight | Understand org's risk appetite, reporting structure |
| **Identify** | Asset mgmt, business env, governance, risk assessment, supply chain | Recon scope, asset inventory, supply chain targets |
| **Protect** | Access control, awareness, data security, maintenance, protective tech | Controls you'll bypass: MFA, encryption, hardening |
| **Detect** | Anomalies, continuous monitoring, detection processes | Blue team capabilities you must evade/avoid |
| **Respond** | Response planning, communications, analysis, mitigation, improvements | Incident response timeline, evidence preservation |
| **Recover** | Recovery planning, improvements, communications | Business continuity, backup integrity, ransomware recovery |

**Pentest Mapping:**
- **Pre-engagement** → Govern/Identify (scope, rules, asset inventory)
- **Recon/Exploit** → Protect (bypass), Detect (evade)
- **Post-exploit** → Detect (avoid), Respond (simulate)
- **Reporting** → Respond/Recover (remediation, verification)

---

## Access Control Models

| Model | Basis | Decision Logic | Use Case |
|-------|-------|----------------|----------|
| **DAC** | Owner discretion | ACLs per object | File systems (Unix perms, Windows ACLs) |
| **MAC** | System policy | Labels (clearance + classification) | Military, high-security (SELinux, TrustedBSD) |
| **RBAC** | Organizational role | Role → Permissions → User | Enterprise apps, cloud IAM (AWS IAM roles) |
| **ABAC** | Attributes (user, resource, env) | Policy engine evaluates attributes | Fine-grained, dynamic (AWS IAM conditions, OPA) |
| **ReBAC** | Relationships | Graph-based (user → resource) | Social apps, file sharing (Google Zanzibar) |

---

## Trust Models

| Model | Trust Assumption | Failure Mode |
|-------|------------------|--------------|
| **Perimeter** | Inside = trusted, Outside = untrusted | Insider threat, lateral movement, VPN compromise |
| **Zero Trust** | No implicit trust; verify every request | Identity provider compromise, token theft, policy gaps |
| **Software-Defined Perimeter** | App-level micro-perimeters | Controller compromise, misconfiguration |
| **BeyondCorp (Google)** | Device + user trust, no VPN | Device inventory gaps, certificate management |

---

## Hands-On Lab

!!! abstract "Lab Exercise: Map Controls to Models"
    **Objective:** Given a set of security controls, identify which model(s) they implement and predict bypasses.
    
    **Controls to Analyze:**
    1. Windows UAC (User Account Control)
    2. SELinux enforcing mode
    3. AWS IAM role with condition keys
    4. Network segmentation (VLANs, firewall rules)
    5. Code review requirement for production deployments
    6. MFA enforced via identity provider
    
    **For Each Control:**
    - Which model(s)? (BLP, Biba, Clark-Wilson, Zero Trust, Defense in Depth, DAC/MAC/RBAC/ABAC)
    - What threat does it mitigate?
    - What assumption does it make?
    - How would you bypass it?
    
    **Expected Outcome:** Completed analysis table with bypass strategies.

---

## Detection & Blue Team Perspective

| Model | Detection Focus | Key Data Sources |
|-------|-----------------|------------------|
| **BLP/MAC** | Label mismatches, unauthorized read/write attempts | Audit logs (SELinux AVC denials, Windows SACLs) |
| **Biba/Integrity** | Unauthorized modification of high-integrity objects | File integrity monitoring (FIM), registry monitoring |
| **Clark-Wilson** | TP execution without authorization, IVP failures | Application audit logs, transaction logs |
| **Zero Trust** | Policy decision anomalies, token reuse, geo-impossible auth | IdP logs, proxy logs, device posture data |
| **Defense in Depth** | Layer bypass detection, correlation across layers | SIEM correlation rules, attack path mapping |

---

## MITRE ATT&CK Mapping

| Tactic | Technique | ID | Model Relevance |
|--------|-----------|----|-----------------|
| Defense Evasion | Impair Defenses: Disable/Modify Security Tools | T1562.001 | Bypasses Protect layer |
| Defense Evasion | Modify Authentication Process | T1556 | Zero Trust / Identity |
| Privilege Escalation | Abuse Elevation Control Mechanism | T1548 | Biba / Integrity levels |
| Lateral Movement | Exploitation of Remote Services | T1210 | Network segmentation bypass |
| Persistence | Create Account | T1136 | DAC / RBAC misconfiguration |

---

## Checklist

- [ ] Explain BLP "No Read Up, No Write Down" with example
- [ ] Explain Biba "No Read Down, No Write Up" with example
- [ ] Describe Clark-Wilson's TP/IVP/CDI/UDI concepts
- [ ] List 7 Zero Trust tenets (NIST 800-207)
- [ ] Draw Defense in Depth layers from memory
- [ ] Map NIST CSF 2.0 functions to pentest phases
- [ ] Differentiate DAC, MAC, RBAC, ABAC, ReBAC
- [ ] Identify trust model for a given architecture diagram

---

## Further Reading

- [Bell-LaPadula Original Paper](https://csrc.nist.gov/CSRC/media/Presentations/Bell-LaPadula/images-media/Bell-LaPadula-Model.pdf)
- [Biba Integrity Model](https://www.cs.georgetown.edu/~denning/infosec/biba.html)
- [Clark-Wilson Paper](https://www.cs.umd.edu/~waa/414-F09/Clark-Wilson.pdf)
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [NIST CSF 2.0](https://www.nist.gov/cyberframework) — Latest framework
- [Google BeyondCorp](https://cloud.google.com/beyondcorp) — Zero Trust implementation
- [SELinux Notebook](https://github.com/SELinuxProject/selinux-notebook) — MAC implementation