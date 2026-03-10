# 🌐 Networking for Cybersecurity

> This is not just a networking guide — this is the foundation of everything in offensive and defensive security.<br>
> Every attack, every tool, every exploit — it all maps back to networking.

---

## 📖 Table of Contents

1. [Network Fundamentals](#1-network-fundamentals)
2. [OSI Model](#2-osi-model)
3. [TCP/IP Model](#3-tcpip-model)
4. [IP Addressing & Subnetting](#4-ip-addressing--subnetting)
5. [Ports & Protocols](#5-ports--protocols)
6. [TCP vs UDP](#6-tcp-vs-udp)
7. [DNS](#7-dns)
8. [ARP](#8-arp)
9. [MAC Address](#9-mac-address)
10. [DHCP](#10-dhcp)
11. [NAT](#11-nat)
12. [Firewalls](#12-firewalls)
13. [VPN](#13-vpn)
14. [Network Scanning](#14-network-scanning)
15. [Packet Analysis](#15-packet-analysis)
16. [MITM Attacks](#16-mitm-attacks)
17. [Routing](#17-routing)
18. [VLAN](#18-vlan)
19. [Load Balancing](#19-load-balancing)
20. [Web Networking](#20-web-networking)
21. [Cloud Networking](#21-cloud-networking)
22. [Network Security Monitoring](#22-network-security-monitoring)
23. [Real Tools Used by Ethical Hackers](#23-real-tools-used-by-ethical-hackers)
24. [Recommended Resources](#24-recommended-resources)

---

## 1. Network Fundamentals

### What is a Network?

A **network** is simply a group of devices connected together so they can share data and resources. That's it. Your home Wi-Fi is a network. Your company's office is a network. The internet itself is just a massive, global network of networks.

As a cybersecurity professional, you need to understand how networks are built — because you'll be attacking them, defending them, or monitoring them.

---

### Types of Networks

| Type | Full Name | Coverage | Example |
|------|-----------|----------|---------|
| **PAN** | Personal Area Network | ~1–10 meters | Bluetooth headset, smartwatch |
| **LAN** | Local Area Network | Building / Campus | Home Wi-Fi, office network |
| **MAN** | Metropolitan Area Network | City-wide | City ISP network |
| **WAN** | Wide Area Network | Country / Global | The Internet, VPN connections |

- **LAN** — This is your typical home or office network. High speed, privately controlled. Most internal network attacks happen here.
- **WAN** — Connects multiple LANs across long distances. The Internet is the world's largest WAN.
- **MAN** — Covers a city or large campus, often managed by ISPs.
- **PAN** — Tiny personal network around a single person. Think Bluetooth or USB tethering.

---

### Internet vs Intranet vs Extranet

| Type | Who Can Access | Description | Example |
|------|----------------|-------------|---------|
| **Internet** | Everyone | Global public network | Browsing any website |
| **Intranet** | Employees only | Private internal network | Company HR portal |
| **Extranet** | Specific external users | Controlled access for partners | Vendor login to company system |

**Why it matters in pentesting:**
- Intranet-only systems are often assumed to be "safe" — they frequently have weaker security.
- Extranet portals are a common attack surface due to third-party access.

---

### Network Devices

These are the physical (or virtual) components that make a network work. You must understand what each one does because they determine how traffic flows — and how it can be intercepted or blocked.

| Device | Function | Pentest Relevance |
|--------|----------|--------------------|
| **Hub** | Broadcasts traffic to ALL devices on the network | Easy to sniff traffic — completely insecure |
| **Switch** | Forwards frames to the correct device using MAC address | MAC flooding, ARP spoofing attacks target switches |
| **Router** | Routes packets between different networks using IP | Gateway to the internet — critical target |
| **Bridge** | Connects two network segments at Layer 2 | Can be used to segment or join networks |
| **Repeater** | Amplifies and regenerates signals over long distances | Rarely attacked directly |
| **Gateway** | Translates between different network protocols | The "exit point" from your LAN |
| **Firewall** | Filters traffic based on rules | The main obstacle for attackers — must learn to bypass |
| **Load Balancer** | Distributes traffic across multiple servers | Can hide backend servers; bypass techniques exist |
| **IDS** | Intrusion Detection System — monitors and alerts on suspicious traffic | Attackers try to evade detection |
| **IPS** | Intrusion Prevention System — actively blocks malicious traffic | More aggressive than IDS; can block attacker tools |

> 💡 **IDS vs IPS:** IDS only detects and alerts. IPS actively blocks. Both are important to understand for evasion.

---

### Network Topologies

Topology = how devices are physically or logically connected.

| Topology | Description | Pros | Cons |
|----------|-------------|------|------|
| **Bus** | All devices share one cable | Simple, cheap | One cable failure = whole network down |
| **Star** | All devices connect to a central switch/hub | Easy to manage, failure isolated | Switch = single point of failure |
| **Ring** | Devices connected in a loop | Predictable traffic flow | One failure breaks the loop |
| **Mesh** | Every device connects to every other device | Highly redundant, fault-tolerant | Expensive, complex |
| **Hybrid** | Mix of two or more topologies | Flexible | Complex to manage |

> **Real-world note:** Most modern corporate networks use **Star** or **Hybrid** topologies. The internet backbone uses **Mesh**.

---

### Types of Network Communication

| Type | Description | Example | Attack Relevance |
|------|-------------|---------|-----------------|
| **Unicast** | One sender → One receiver | Browsing a website | Standard traffic; can be intercepted |
| **Broadcast** | One sender → All devices on the network | ARP request | Broadcast storms, ARP poisoning |
| **Multicast** | One sender → A group of receivers | Live video streaming | Multicast exploitation, group hijacking |
| **Anycast** | One sender → Nearest of multiple receivers | DNS root servers, CDNs | BGP hijacking can redirect anycast traffic |

---

## 2. OSI Model

The **OSI (Open Systems Interconnection)** model is one of the most important concepts in networking. Every cybersecurity professional must understand it deeply — not just memorize the layers, but understand what happens at each layer and what attacks target it.

Think of it as a blueprint for how data travels from one device to another across a network.

---

### The 7 Layers

| Layer | Name | What it does | Protocol Examples |
|-------|------|-------------|-------------------|
| 7 | **Application** | User-facing services; where apps interact with the network | HTTP, HTTPS, FTP, DNS, SMTP |
| 6 | **Presentation** | Data formatting, encryption, compression | SSL/TLS, JPEG, ASCII, Unicode |
| 5 | **Session** | Opens, manages, and closes sessions between devices | NetBIOS, RPC, PPTP |
| 4 | **Transport** | End-to-end delivery, segmentation, error recovery | TCP, UDP |
| 3 | **Network** | Logical addressing, routing between networks | IP, ICMP, IGMP |
| 2 | **Data Link** | MAC addressing, frames, error detection on local network | Ethernet, Wi-Fi (802.11), ARP |
| 1 | **Physical** | Actual transmission of raw bits over physical medium | Cables, fiber, radio waves, hubs |

> 💡 **Mnemonic (top to bottom):** *"All People Seem To Need Data Processing"*
> 💡 **Mnemonic (bottom to top):** *"Please Do Not Throw Sausage Pizza Away"*

---

### How Data Travels (Encapsulation)

When you send data, each layer **wraps** (encapsulates) the data with its own header:

```
Application → Data
Transport   → Segment  (adds TCP/UDP header)
Network     → Packet   (adds IP header)
Data Link   → Frame    (adds MAC header)
Physical    → Bits     (transmitted as signals)
```

At the receiving end, each layer **strips** its header (decapsulation) until the original data is recovered.

---

### Attack Map Per Layer

This is the most important part for pentesters. Every attack targets a specific layer.

| Layer | Attack | Description |
|-------|--------|-------------|
| 7 – Application | **SQL Injection** | Malicious SQL in input fields |
| 7 – Application | **XSS** | Injecting scripts into web pages |
| 7 – Application | **Directory Traversal** | Accessing restricted files via URL |
| 6 – Presentation | **SSL Stripping** | Downgrading HTTPS to HTTP |
| 5 – Session | **Session Hijacking** | Stealing a valid session token |
| 4 – Transport | **SYN Flood** | Flooding with SYN packets to exhaust connections |
| 4 – Transport | **TCP Hijacking** | Taking over an established TCP connection |
| 3 – Network | **IP Spoofing** | Forging source IP address |
| 3 – Network | **ICMP Flood (Ping Flood)** | Overwhelming with ICMP requests |
| 2 – Data Link | **ARP Poisoning** | Sending fake ARP replies to redirect traffic |
| 2 – Data Link | **MAC Spoofing** | Changing MAC address to impersonate another device |
| 2 – Data Link | **MAC Flooding** | Flooding switch's MAC table to cause it to broadcast |
| 1 – Physical | **Cable tapping** | Physically intercepting network cables |
| 1 – Physical | **Signal jamming** | Disrupting wireless signals |

> 💡 When you're doing a pentest, ask yourself: *"Which layer is this attack happening at?"* This helps you understand the root cause and the correct defense.

---

## 3. TCP/IP Model

The OSI model is a theoretical reference framework. The **TCP/IP model** is what the internet actually runs on.

### 4 Layers

| Layer | TCP/IP Name | Equivalent OSI Layers | Common Protocols |
|-------|-------------|----------------------|-----------------|
| 4 | **Application** | Application + Presentation + Session | HTTP, HTTPS, DNS, FTP, SMTP, SSH |
| 3 | **Transport** | Transport | TCP, UDP |
| 2 | **Internet** | Network | IP, ICMP, ARP |
| 1 | **Network Access** | Data Link + Physical | Ethernet, Wi-Fi, MAC |

### How a Packet Travels Across the Internet

1. Your browser requests `google.com`
2. DNS resolves it to an IP (e.g., `142.250.80.46`)
3. Your OS creates a TCP connection (3-way handshake)
4. Data is broken into packets with source/destination IPs
5. Your router sends packets to the next hop (gateway)
6. Packets travel through multiple routers on the internet
7. Google's server receives packets, reassembles them, responds
8. Response travels back through the same process

> This entire journey is what tools like **Wireshark** and **traceroute** let you see.

---

## 4. IP Addressing & Subnetting

### IPv4

IPv4 addresses are **32-bit** numbers written in dotted decimal notation.

```
192.168.1.1
```

Each of the 4 sections (octets) can be 0–255. That gives us about **4.3 billion** unique addresses.

### IP Classes (IPv4)

| Class | Range | Default Subnet Mask | Use |
|-------|-------|---------------------|-----|
| A | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 (/8) | Large organizations |
| B | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 (/16) | Medium organizations |
| C | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 (/24) | Small networks |
| D | 224.0.0.0 – 239.255.255.255 | — | Multicast |
| E | 240.0.0.0 – 255.255.255.255 | — | Reserved/Research |

> **Note:** 127.x.x.x is reserved for loopback (localhost). `127.0.0.1` always refers to your own machine.

---

### Private IP Ranges

These ranges are **not routable on the internet**. They're used inside private networks (homes, offices, data centers).

| Class | Private Range | Common Use |
|-------|--------------|------------|
| A | 10.0.0.0 – 10.255.255.255 | Large enterprise networks |
| B | 172.16.0.0 – 172.31.255.255 | Medium networks, Docker |
| C | 192.168.0.0 – 192.168.255.255 | Home routers, small offices |

**Memorize these.** When you're on a pentest and you see a `10.x.x.x` address, you know you're inside a large private network.

---

### Subnetting (Extremely Important)

Subnetting = dividing a large network into smaller sub-networks.

**Why it matters for pentesters:**
- Helps you map the internal network during reconnaissance
- Lets you calculate which hosts exist in a subnet
- Tools like Nmap use CIDR notation for scanning entire subnets

#### CIDR Notation

```
192.168.1.0/24
```

The `/24` means the first **24 bits** are the network portion. The remaining **8 bits** are for hosts.

| CIDR | Subnet Mask | Hosts Available |
|------|-------------|-----------------|
| /8 | 255.0.0.0 | 16,777,214 |
| /16 | 255.255.0.0 | 65,534 |
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /30 | 255.255.255.252 | 2 |

#### Key Terms

| Term | Description | Example |
|------|-------------|---------|
| **Network Address** | First address in the subnet — identifies the subnet | 192.168.1.0 |
| **Broadcast Address** | Last address — sent to all hosts in the subnet | 192.168.1.255 |
| **Usable Hosts** | All addresses between network and broadcast | 192.168.1.1 – 192.168.1.254 |
| **Subnet Mask** | Defines the network vs host portion | 255.255.255.0 |
| **Default Gateway** | Router address — usually first usable host | 192.168.1.1 |

#### VLSM (Variable Length Subnet Masking)

VLSM lets you assign different sized subnets to different parts of a network — so you don't waste IP addresses. For example, a /30 subnet for a point-to-point router link (only 2 hosts needed), and a /24 for a large office floor.

#### Quick Example

```
Target: 192.168.10.0/24

Network:    192.168.10.0
Broadcast:  192.168.10.255
First host: 192.168.10.1
Last host:  192.168.10.254
Total hosts: 254

Nmap scan: nmap -sn 192.168.10.0/24
```

---

### IPv6

IPv6 was created because IPv4 addresses were running out. It uses **128-bit** addresses.

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

Written in hexadecimal, separated by colons. Can be shortened — consecutive groups of zeros can be replaced with `::`.

**IPv6 in pentesting:** IPv6 is often misconfigured or ignored in security policies, making it a valuable attack vector. Many firewalls only filter IPv4 by default.

---

## 5. Ports & Protocols

Every service on a computer listens on a **port number**. Ports let a single machine run multiple services simultaneously.

- **Port range:** 0–65535
- **Well-known ports:** 0–1023 (reserved for standard services)
- **Registered ports:** 1024–49151
- **Dynamic/ephemeral ports:** 49152–65535 (used temporarily by clients)

### Ports You Must Memorize

| Port | Protocol | Service | Pentest Notes |
|------|----------|---------|---------------|
| 21 | TCP | **FTP** | Often allows anonymous login; credentials sent in cleartext |
| 22 | TCP | **SSH** | Brute force attacks; key-based auth is safer |
| 23 | TCP | **Telnet** | No encryption — credentials in cleartext; should never be open |
| 25 | TCP | **SMTP** | Email sending; SMTP relay attacks, spam |
| 53 | TCP/UDP | **DNS** | DNS enumeration, zone transfers, poisoning |
| 67/68 | UDP | **DHCP** | DHCP starvation, rogue DHCP server |
| 80 | TCP | **HTTP** | Web app attacks — XSS, SQLi, directory traversal |
| 110 | TCP | **POP3** | Email retrieval; cleartext credentials |
| 135 | TCP | **RPC** | Windows RPC — common exploit target |
| 139 | TCP | **NetBIOS** | Windows file sharing; enumeration |
| 143 | TCP | **IMAP** | Email access; brute force |
| 443 | TCP | **HTTPS** | Encrypted web — SSL/TLS attacks, cert issues |
| 445 | TCP | **SMB** | Critical — EternalBlue, WannaCry, ransomware target |
| 3306 | TCP | **MySQL** | Database — SQL injection, direct access attacks |
| 3389 | TCP | **RDP** | Remote Desktop — BlueKeep, brute force, credential theft |
| 8080 | TCP | **HTTP Proxy** | Common web proxy/dev port — often less secured |

> 💡 **During a pentest:** When you see port 445 open, think SMB exploitation. Port 3389 open? Think RDP attacks. Port 21 open? Try anonymous FTP login first.

---

## 6. TCP vs UDP

These are the two core transport layer protocols. You need to understand both deeply.

### TCP — Transmission Control Protocol

TCP is **connection-oriented**. Before any data is sent, a connection must be established.

#### The 3-Way Handshake

```
Client                  Server
  |------- SYN -------->|      (I want to connect)
  |<----- SYN-ACK ------|      (OK, I acknowledge)
  |------- ACK -------->|      (Connection established)
```

- **SYN** = Synchronize (client initiates)
- **SYN-ACK** = Server acknowledges and responds
- **ACK** = Client acknowledges — connection is now open

#### TCP Connection Teardown (4-Way)

```
Client                  Server
  |------- FIN -------->|
  |<------- ACK --------|
  |<------- FIN --------|
  |------- ACK -------->|
```

#### TCP Features

| Feature | Details |
|---------|---------|
| Reliability | Guarantees delivery — retransmits lost packets |
| Ordering | Packets are numbered and reassembled in order |
| Flow control | Prevents sender from overwhelming receiver |
| Error checking | Checksums detect corrupted data |
| Use cases | HTTP/HTTPS, SSH, FTP, SMTP, databases |

#### TCP Attacks

| Attack | How it Works |
|--------|-------------|
| **SYN Flood** | Attacker sends thousands of SYN packets but never completes the handshake. Server keeps half-open connections until resources are exhausted (DoS) |
| **TCP Hijacking** | Attacker inserts themselves into an established TCP session by predicting sequence numbers |
| **RST Attack** | Sending forged RST (reset) packets to terminate connections |

---

### UDP — User Datagram Protocol

UDP is **connectionless**. Data is sent without establishing a connection first — no handshake, no confirmation, no guaranteed delivery.

#### UDP Features

| Feature | Details |
|---------|---------|
| Speed | Much faster than TCP — no overhead |
| Reliability | No — packets can be lost, duplicated, or arrive out of order |
| Error checking | Minimal (optional checksum only) |
| Use cases | DNS, DHCP, VoIP, video streaming, gaming, TFTP |

#### UDP Attacks

| Attack | How it Works |
|--------|-------------|
| **UDP Flood** | Sending large volumes of UDP packets to random ports, forcing the target to check for listening services on each port |
| **UDP Amplification** | Using UDP services (DNS, NTP, SSDP) to amplify traffic — attacker sends small request with spoofed IP, server sends large response to victim |

---

### TCP vs UDP Summary

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented (handshake) | Connectionless |
| Reliability | Guaranteed delivery | Best effort, no guarantee |
| Speed | Slower (overhead) | Faster (no overhead) |
| Ordering | In-order delivery | No ordering |
| Header Size | 20+ bytes | 8 bytes |
| Use Case | Web, email, file transfer, SSH | DNS, streaming, VoIP, gaming |
| Attack Types | SYN flood, TCP hijacking | UDP flood, amplification |

---

## 7. DNS

DNS = **Domain Name System** — it translates human-readable domain names into IP addresses.

```
google.com  →  142.250.80.46
```

Without DNS, you'd have to memorize IP addresses for every website. DNS is essentially the phonebook of the internet.

### How DNS Resolution Works

```
1. You type google.com in your browser
2. Your computer checks its local DNS cache
3. If not cached, asks your ISP's DNS resolver
4. Resolver queries a Root DNS server (.)
5. Root server directs to .com TLD nameserver
6. TLD nameserver directs to google.com's nameserver
7. Google's nameserver returns the IP
8. Your browser connects to that IP
```

### DNS Record Types

| Record | Purpose | Example |
|--------|---------|---------|
| **A** | Maps domain to IPv4 address | google.com → 142.250.80.46 |
| **AAAA** | Maps domain to IPv6 address | google.com → 2607:f8b0:... |
| **MX** | Mail exchange server | smtp.google.com |
| **NS** | Authoritative nameserver for the domain | ns1.google.com |
| **CNAME** | Alias pointing to another domain | www → google.com |
| **TXT** | Text records — SPF, DKIM, verification | v=spf1 include:... |
| **PTR** | Reverse DNS — IP to domain | 46.80.250.142.in-addr.arpa |
| **SOA** | Start of authority — zone info | Serial, refresh, retry, expire |

### DNS Attacks

| Attack | Description | Impact |
|--------|-------------|--------|
| **DNS Poisoning (Cache Poisoning)** | Injecting fake DNS records into a resolver's cache | Users redirected to attacker-controlled servers |
| **DNS Spoofing** | Sending forged DNS responses to a client | Same result as poisoning but targeted at one client |
| **DNS Enumeration** | Querying DNS to discover all subdomains/records | Maps the target's infrastructure |
| **Zone Transfer Attack** | Exploiting misconfigured DNS to download entire zone file | Complete domain map of the target |
| **Subdomain Takeover** | Claiming an abandoned subdomain pointing to unclaimed resources | Host malicious content under target's domain |
| **DNS Tunneling** | Using DNS queries/responses to smuggle data | Data exfiltration, C2 communication bypasses firewalls |

### DNS Tools

- `nslookup` — Basic DNS queries
- `dig` — Detailed DNS lookups (preferred on Linux)
- `host` — Simple DNS resolver
- `dnsenum` — DNS enumeration
- `subfinder` / `amass` — Subdomain discovery

---

## 8. ARP

ARP = **Address Resolution Protocol** — maps IP addresses to MAC addresses on a local network.

### How ARP Works

When your computer wants to send data to `192.168.1.5`:

```
1. Your PC broadcasts: "Who has 192.168.1.5? Tell 192.168.1.10"
   (ARP Request — sent to FF:FF:FF:FF:FF:FF)
2. The device with 192.168.1.5 replies:
   "192.168.1.5 is at AA:BB:CC:DD:EE:FF"
   (ARP Reply — unicast back)
3. Your PC stores this in its ARP cache
4. Data is now sent to that MAC address
```

> View your ARP cache: `arp -a` on Windows/Linux/Mac

### ARP Spoofing (ARP Poisoning)

This is one of the most important attacks for internal network pentesting.

**How it works:**
1. Attacker sends **fake ARP replies** to both the victim and the router
2. Victim's ARP cache now maps the router's IP to the attacker's MAC
3. Router's ARP cache now maps the victim's IP to the attacker's MAC
4. All traffic between victim and router now flows through the attacker
5. **Attacker is now the Man-in-the-Middle (MITM)**

```
Normal:  Victim  ←→  Router
Attacked: Victim ←→  Attacker  ←→  Router
```

**Tools for ARP Spoofing:**

| Tool | Usage |
|------|-------|
| `arpspoof` | `arpspoof -i eth0 -t [victim] [gateway]` |
| `Bettercap` | All-in-one MITM framework |
| `Ettercap` | GUI-based MITM tool |

**Defense against ARP Spoofing:**
- Dynamic ARP Inspection (DAI) on managed switches
- Static ARP entries for critical devices
- Using encrypted protocols (HTTPS, SSH) — even if MITM'd, traffic is unreadable

---

## 9. MAC Address

A **MAC (Media Access Control) address** is a unique hardware identifier assigned to every network interface card (NIC).

```
Example: 00:1A:2B:3C:4D:5E
Format:  OUI (first 3 bytes) : Device ID (last 3 bytes)
```

- 48 bits (6 bytes), written in hexadecimal
- First 3 bytes = **OUI (Organizationally Unique Identifier)** — identifies the manufacturer
- Last 3 bytes = **device-specific identifier**
- Operates at **Layer 2 (Data Link)**
- Only relevant within the same local network (not routed)

### MAC-Based Attacks

| Attack | Description | Impact |
|--------|-------------|--------|
| **MAC Spoofing** | Changing your MAC address to impersonate another device | Bypass MAC-based access control, network authentication |
| **MAC Flooding** | Flooding a switch's MAC address table with fake entries until it overflows | Switch enters "fail-open" mode and broadcasts all traffic — enables sniffing |

**MAC Spoofing on Linux:**
```bash
ip link set dev eth0 down
ip link set dev eth0 address AA:BB:CC:DD:EE:FF
ip link set dev eth0 up
```

> **Real-world use:** Some networks restrict access by MAC address (MAC filtering). MAC spoofing trivially bypasses this — it is NOT a reliable security control.

---

## 10. DHCP

DHCP = **Dynamic Host Configuration Protocol** — automatically assigns IP addresses and network configuration to devices when they join a network.

### DORA Process

When a device joins a network, it follows the **DORA** process:

```
1. DISCOVER  — Client broadcasts: "Is there a DHCP server here?"
2. OFFER     — DHCP server responds: "Here, take IP 192.168.1.50"
3. REQUEST   — Client broadcasts: "I'd like to accept that IP"
4. ACK       — Server confirms: "IP 192.168.1.50 is yours for [lease time]"
```

### What DHCP Assigns

- IP address
- Subnet mask
- Default gateway
- DNS server addresses
- Lease time

### DHCP Attacks

| Attack | Description | Impact |
|--------|-------------|--------|
| **DHCP Starvation** | Attacker sends thousands of DHCP requests with spoofed MACs, exhausting the available IP pool | Legitimate devices can't get an IP — denial of service |
| **Rogue DHCP Server** | After starvation, attacker sets up their own DHCP server | Assigns attacker-controlled gateway/DNS to victims — full MITM |

> **Tools:** Yersinia is commonly used for DHCP starvation attacks.

---

## 11. NAT

NAT = **Network Address Translation** — allows multiple devices on a private network to share a single public IP address.

### Why NAT Exists

IPv4 only has ~4.3 billion addresses. There are billions of devices. NAT was the solution — internal devices use private IPs, and the router translates them to one public IP when communicating on the internet.

### How NAT Works

```
Internal device: 192.168.1.5:54321
Router (NAT):    203.0.113.1:12345   ← This is what the internet sees
Destination:     8.8.8.8:53
```

The router maintains a **NAT translation table** to track which internal device corresponds to each external connection.

### Types of NAT

| Type | Description |
|------|-------------|
| **Static NAT** | One private IP permanently maps to one public IP — used for servers |
| **Dynamic NAT** | Private IPs mapped to a pool of public IPs — dynamic assignment |
| **PAT (Port Address Translation)** | Multiple private IPs share one public IP, differentiated by port numbers — most common (used in home routers) |

### NAT and Pentesting

- Attackers hiding behind NAT are harder to trace back to their origin
- Internal services behind NAT are generally not directly reachable from the internet (unless port forwarding is configured)
- Misconfigured port forwarding can expose internal services to the internet

---

## 12. Firewalls

A **firewall** is a security system that monitors and controls incoming and outgoing network traffic based on predefined rules.

### Firewall Types

| Type | How it Works | Pros | Cons |
|------|-------------|------|------|
| **Packet Filtering** | Inspects each packet individually (source/dest IP, port, protocol) — stateless | Fast, low overhead | Doesn't understand context; easy to evade |
| **Stateful Firewall** | Tracks connection states — knows if a packet is part of an established connection | Better than packet filtering | Can still be bypassed |
| **Next-Generation Firewall (NGFW)** | Deep packet inspection, application awareness, IDS/IPS integration | Very thorough | Expensive, complex |
| **Web Application Firewall (WAF)** | Specifically protects web applications — filters HTTP traffic | Stops common web attacks (SQLi, XSS) | Only for Layer 7; can be bypassed |

### Firewall Evasion Techniques (Pentesting)

| Technique | Description |
|-----------|-------------|
| **Fragmentation** | Splitting packets so firewall can't reassemble and inspect them |
| **Source Port Manipulation** | Using allowed source ports (e.g., 80, 443) to trick packet filters |
| **Decoy Scanning** | Sending scans from multiple fake IPs to confuse IDS/firewall |
| **Protocol Tunneling** | Hiding traffic inside allowed protocols (e.g., DNS tunneling, ICMP tunneling) |
| **Slow Scanning** | Scanning very slowly to avoid triggering rate-based detection |

> 💡 **Nmap firewall evasion flags:** `-f` (fragment), `-D` (decoy), `--source-port`, `-T0` (slow scan)

---

## 13. VPN

VPN = **Virtual Private Network** — creates an encrypted tunnel between two points over an untrusted network (like the internet).

### How VPN Works

```
Your Device  →  [Encrypted Tunnel]  →  VPN Server  →  Internet
```

All traffic from your device is encrypted before leaving, sent to the VPN server, decrypted there, and forwarded to the destination. The destination sees the VPN server's IP, not yours.

### VPN Protocols

| Protocol | Description | Security | Use Case |
|----------|-------------|----------|---------|
| **IPsec** | Suite of protocols for securing IP communications | Strong | Site-to-site VPNs, corporate |
| **OpenVPN** | Open-source, uses SSL/TLS | Strong | Remote access, flexible |
| **WireGuard** | Modern, fast, minimal codebase | Very Strong | Modern VPN deployments |
| **L2TP/IPsec** | Layer 2 tunneling + IPsec encryption | Medium | Legacy systems |
| **PPTP** | Old protocol — **do not use** | Weak (broken) | Legacy — avoid |

### VPN Security Issues

| Issue | Description |
|-------|-------------|
| **VPN Misconfiguration** | Weak ciphers, outdated protocols, or split tunneling leaks |
| **Credential Theft** | Compromising VPN credentials gives attacker direct network access |
| **VPN Exploitation** | Vulnerabilities in VPN software (e.g., Pulse Secure, Fortinet CVEs) |
| **DNS Leak** | VPN fails to route DNS queries through tunnel — real IP exposed |
| **Split Tunneling Abuse** | Only some traffic goes through VPN — bypass of security controls |

---

## 14. Network Scanning

Network scanning is the process of discovering hosts, open ports, and services on a network. **This is one of the first steps in any penetration test.**

### Why It Matters

Before you can attack anything, you need to know:
- What hosts are alive?
- What ports are open?
- What services are running?
- What OS is the target running?
- What version of the service is running?

### Tools

| Tool | Purpose |
|------|---------|
| **Nmap** | The most powerful and widely used network scanner |
| **Masscan** | Extremely fast port scanner (internet-scale) |
| **Netdiscover** | ARP-based host discovery for local networks |
| **Angry IP Scanner** | GUI-based scanner, beginner friendly |

### Nmap Scan Types

| Scan Type | Flag | Description |
|-----------|------|-------------|
| **Host Discovery (Ping Sweep)** | `-sn` | Find live hosts without port scanning |
| **TCP Connect Scan** | `-sT` | Full 3-way handshake — noisy, logged |
| **SYN Scan (Stealth)** | `-sS` | Half-open scan — faster, less detectable |
| **UDP Scan** | `-sU` | Scans UDP ports — slower |
| **OS Detection** | `-O` | Attempts to identify OS |
| **Service/Version Detection** | `-sV` | Identify service versions |
| **Script Scan** | `-sC` | Runs default NSE scripts |
| **Aggressive Scan** | `-A` | OS, version, scripts, traceroute |

### Common Nmap Commands

```bash
# Discover live hosts on a subnet
nmap -sn 192.168.1.0/24

# Basic port scan
nmap 192.168.1.1

# Full scan — OS, version, scripts
nmap -A 192.168.1.1

# Scan specific ports
nmap -p 22,80,443 192.168.1.1

# Scan all 65535 ports
nmap -p- 192.168.1.1

# SYN stealth scan
nmap -sS 192.168.1.1

# Save output to file
nmap -A 192.168.1.0/24 -oN scan_results.txt
```

---

## 15. Packet Analysis

Packet analysis = capturing and inspecting actual network traffic at the packet level. Essential for both offensive (capturing credentials, extracting data) and defensive (incident response, anomaly detection) work.

### Tools

| Tool | Type | Use |
|------|------|-----|
| **Wireshark** | GUI | Full packet capture and analysis with filters |
| **Tcpdump** | CLI | Lightweight capture tool, great for remote systems |
| **Tshark** | CLI | Command-line version of Wireshark |

### Key Wireshark Skills

| Skill | Example Filter |
|-------|---------------|
| Filter by protocol | `http`, `dns`, `tcp`, `udp`, `icmp` |
| Filter by IP | `ip.addr == 192.168.1.5` |
| Filter by port | `tcp.port == 80` |
| Follow TCP stream | Right-click → Follow → TCP Stream |
| Find credentials in cleartext | Filter `http`, look for POST requests |
| Filter by keyword | `frame contains "password"` |

### Common Tcpdump Commands

```bash
# Capture all traffic on interface
tcpdump -i eth0

# Save capture to file
tcpdump -i eth0 -w capture.pcap

# Filter by host
tcpdump -i eth0 host 192.168.1.5

# Filter by port
tcpdump -i eth0 port 80

# Read from file
tcpdump -r capture.pcap
```

### What to Look For

- **Cleartext credentials** (FTP, HTTP, Telnet, POP3)
- **Interesting HTTP traffic** — cookies, tokens, form data
- **ARP traffic** — detect ARP poisoning
- **DNS queries** — detect DNS enumeration or C2 traffic
- **Unusual port activity** — potential backdoors or C2 channels
- **Large data transfers** — potential exfiltration

---

## 16. MITM Attacks

MITM = **Man-in-the-Middle** — the attacker secretly positions themselves between two communicating parties, intercepting and potentially altering traffic.

### Attack Flow

```
Normal:   Alice  ←→  Bob
MITM:     Alice  ←→  Attacker  ←→  Bob
```

Alice thinks she's talking to Bob. Bob thinks he's talking to Alice. The attacker reads (and can modify) everything.

### MITM Techniques

| Technique | How | Layer |
|-----------|-----|-------|
| **ARP Spoofing** | Fake ARP replies redirect traffic through attacker | Layer 2 |
| **DNS Spoofing** | Fake DNS responses redirect user to attacker's server | Layer 3/7 |
| **SSL Stripping** | Downgrades HTTPS connection to HTTP — decrypts traffic | Layer 7 |
| **DHCP Spoofing** | Rogue DHCP server gives attacker as gateway | Layer 3 |
| **ICMP Redirect** | Sending fake ICMP redirect messages to reroute traffic | Layer 3 |
| **BGP Hijacking** | Announcing false routes to redirect internet traffic | Layer 3 |

### MITM Tools

| Tool | Description |
|------|-------------|
| **Bettercap** | Modern, powerful MITM framework — ARP, DNS, SSL stripping, credential capture |
| **Ettercap** | Classic MITM tool with GUI — ARP poisoning, sniffing |
| **MITMf** | Man-in-the-Middle Framework with multiple attack modules |
| **Responder** | LLMNR/NBT-NS/MDNS poisoning — captures NTLMv2 hashes on Windows networks |

### Defense

- Use encrypted protocols (HTTPS, SSH, encrypted DNS)
- HSTS (HTTP Strict Transport Security) — prevents SSL stripping
- Certificate pinning — prevents fake certificate attacks
- Dynamic ARP Inspection on switches
- Use VPNs on untrusted networks

---

## 17. Routing

Routing is the process of determining the best path for packets to travel from source to destination across multiple networks.

### Types of Routing

| Type | Description |
|------|-------------|
| **Static Routing** | Routes manually configured by an admin — no automatic updates |
| **Dynamic Routing** | Routers automatically share and update routing information using routing protocols |
| **Default Route** | The fallback route when no specific route matches — `0.0.0.0/0` |

### Routing Protocols

| Protocol | Type | Use Case | Details |
|----------|------|---------|---------|
| **RIP** (Routing Information Protocol) | Interior | Small networks | Distance-vector; max 15 hops; slow convergence |
| **OSPF** (Open Shortest Path First) | Interior | Enterprise networks | Link-state; fast convergence; uses Dijkstra's algorithm |
| **EIGRP** (Enhanced Interior Gateway Routing Protocol) | Interior | Cisco networks | Cisco proprietary; hybrid distance-vector/link-state |
| **BGP** (Border Gateway Protocol) | Exterior | Internet backbone | The protocol that runs the internet — routes between ASes |

### Routing and Pentesting

| Attack | Description |
|--------|-------------|
| **BGP Hijacking** | Announcing false routes to redirect internet traffic — can hijack entire IP blocks |
| **OSPF Injection** | Injecting false OSPF routes to reroute internal traffic |
| **Route Poisoning** | Deliberately advertising bad routes to disrupt routing |
| **Traceroute for Recon** | `traceroute`/`tracert` reveals the path packets take — maps network infrastructure |

---

## 18. VLAN

VLAN = **Virtual Local Area Network** — a logical segmentation of a physical network into separate broadcast domains.

### Why VLANs Exist

Without VLANs, every device on a network receives every broadcast. VLANs allow network admins to:
- Separate departments (HR, Finance, IT)
- Improve security (prevent HR from seeing Finance traffic)
- Reduce broadcast traffic
- Apply different security policies per segment

### Example

```
Physical Network: One switch, 24 ports

VLAN 10 → Ports 1-8   → HR Department
VLAN 20 → Ports 9-16  → Finance Department
VLAN 30 → Ports 17-24 → IT Department

HR can't communicate directly with Finance, even though they're on the same switch.
```

### VLAN Concepts

| Term | Description |
|------|-------------|
| **Access Port** | A port assigned to one VLAN — connects end devices |
| **Trunk Port** | Carries traffic for multiple VLANs between switches — uses 802.1Q tagging |
| **802.1Q** | The standard for VLAN tagging on trunk links |
| **Native VLAN** | Untagged VLAN on a trunk port — misconfiguration here leads to attacks |

### VLAN Hopping

VLAN hopping is an attack that allows an attacker in one VLAN to access another VLAN — bypassing segmentation.

**Methods:**

1. **Switch Spoofing** — Attacker's port negotiates as a trunk port, receiving traffic from all VLANs
2. **Double Tagging** — Attacker sends a frame with two 802.1Q tags. The outer tag matches the native VLAN and gets stripped by the first switch. The inner tag routes the frame to the target VLAN.

**Defense:**
- Disable DTP (Dynamic Trunking Protocol) on access ports
- Set a dedicated unused VLAN as the native VLAN
- Manually configure trunk/access ports — don't use auto-negotiation

---

## 19. Load Balancing

A **load balancer** distributes incoming network traffic across multiple servers to prevent any single server from becoming overwhelmed.

### Load Balancing Methods

| Method | Description |
|--------|-------------|
| **Round Robin** | Requests distributed sequentially across servers |
| **Least Connection** | New request goes to server with fewest active connections |
| **IP Hash** | Client IP determines which server handles the request (session persistence) |
| **Weighted** | Servers with more capacity receive more requests |

### Load Balancers and Pentesting

| Issue | Description |
|-------|-------------|
| **Backend Discovery** | Load balancer hides backend servers — sometimes misconfigured to reveal them |
| **Load Balancer Bypass** | Directly targeting backend server IPs instead of going through the load balancer |
| **Session Persistence Issues** | If sessions aren't properly shared between backend servers, session fixation or confusion is possible |
| **Health Check Exploitation** | Health check endpoints sometimes expose internal details |

---

## 20. Web Networking

Understanding HTTP is fundamental for web application pentesting (WAPT) and OWASP Top 10 attacks.

### HTTP Protocol

HTTP = **HyperText Transfer Protocol** — the foundation of data communication on the web.

#### HTTP Methods

| Method | Purpose | Pentest Relevance |
|--------|---------|-------------------|
| **GET** | Retrieve a resource | Parameter tampering in URL |
| **POST** | Submit data to server | Login forms, data submission — SQLi, brute force |
| **PUT** | Replace a resource entirely | File upload vulnerabilities |
| **DELETE** | Remove a resource | Unauthorized deletion |
| **PATCH** | Partially update a resource | Mass assignment vulnerabilities |
| **HEAD** | GET without response body | Information gathering |
| **OPTIONS** | Returns allowed methods | CORS misconfigurations, enumeration |

#### HTTP Status Codes

| Code | Meaning | Pentest Relevance |
|------|---------|-------------------|
| 200 | OK | Request succeeded |
| 301/302 | Redirect | Possible open redirect vulnerability |
| 400 | Bad Request | Input validation errors |
| 401 | Unauthorized | Auth required — try bypass |
| 403 | Forbidden | Access denied — look for bypass |
| 404 | Not Found | Directory enumeration |
| 500 | Internal Server Error | Error handling — may reveal stack traces |
| 503 | Service Unavailable | Potential DoS condition |

#### Important HTTP Headers

| Header | Purpose | Pentest Relevance |
|--------|---------|-------------------|
| `Authorization` | Carries auth tokens/credentials | JWT attacks, token leakage |
| `Cookie` | Session management | Session hijacking, CSRF |
| `User-Agent` | Identifies client browser | User-agent spoofing |
| `Host` | Target domain | Host header injection |
| `X-Forwarded-For` | Client IP behind proxy | IP spoofing, bypass IP restrictions |
| `Content-Type` | Type of data being sent | MIME type confusion attacks |
| `Referer` | Previous page URL | Information leakage |

---

### Cookies

Cookies are small pieces of data stored on the client, used primarily for session management.

| Type | Description |
|------|-------------|
| **Session Cookie** | No expiry — deleted when browser closes. Contains session ID |
| **Persistent Cookie** | Has expiry date — survives browser restart |
| **Secure Cookie** | Only sent over HTTPS — flag: `Secure` |
| **HttpOnly Cookie** | Cannot be accessed by JavaScript — flag: `HttpOnly` — protects against XSS stealing cookies |
| **SameSite Cookie** | Controls cross-site cookie sending — protects against CSRF |

#### Cookie-Based Attacks

| Attack | Description |
|--------|-------------|
| **Session Hijacking** | Stealing a valid session cookie to impersonate the user |
| **Session Fixation** | Forcing a victim to use a specific session ID chosen by the attacker |
| **XSS Cookie Theft** | Using XSS to steal HttpOnly-less cookies via `document.cookie` |
| **CSRF** | Tricking user's browser into making unauthorized requests using their cookies |

---

### HTTPS and SSL/TLS

HTTPS = HTTP + TLS encryption. All data is encrypted in transit.

**TLS Handshake (simplified):**
```
1. Client Hello (TLS version, cipher suites)
2. Server Hello (chosen cipher, certificate)
3. Client verifies certificate
4. Key exchange
5. Encrypted communication begins
```

#### SSL/TLS Attacks

| Attack | Description |
|--------|-------------|
| **SSL Stripping** | Downgrading HTTPS to HTTP by intercepting redirects |
| **Downgrade Attack** | Forcing use of older, weaker TLS version (SSLv3, TLS 1.0) |
| **POODLE** | Exploit in SSLv3 — reason SSLv3 was deprecated |
| **BEAST** | Attack on TLS 1.0 CBC mode |
| **Certificate Spoofing** | Presenting a fake cert — defeated by cert pinning and HSTS |
| **Expired Certificate** | Browsers warn users — misconfiguration |

---

## 21. Cloud Networking

Most modern companies run infrastructure on the cloud. You must understand cloud networking basics.

### Key Cloud Networking Concepts

| Concept | Description |
|---------|-------------|
| **VPC (Virtual Private Cloud)** | Isolated virtual network within a cloud provider. Your own private network in the cloud |
| **Subnets** | VPCs are divided into public (internet-facing) and private (internal) subnets |
| **Security Groups** | Virtual firewalls controlling inbound/outbound traffic to cloud instances |
| **NACLs (Network ACLs)** | Stateless firewall rules at the subnet level |
| **Internet Gateway** | Allows public subnet instances to communicate with the internet |
| **NAT Gateway** | Allows private subnet instances to access the internet without being directly accessible |
| **Peering** | Connecting two VPCs together |
| **Load Balancers** | AWS ALB/NLB — distribute traffic across EC2 instances |

### Cloud Security Issues

| Issue | Description |
|-------|-------------|
| **Overly permissive Security Groups** | Port `0.0.0.0/0` open to any IP — common misconfiguration |
| **Public S3 buckets** | Storage buckets accidentally exposed to the internet |
| **SSRF (Server-Side Request Forgery)** | Attacking cloud metadata endpoint (`169.254.169.254`) to steal IAM credentials |
| **Misconfigured IAM** | Overly permissive roles/policies — privilege escalation |
| **Exposed cloud dashboards** | Kubernetes dashboards, Elasticsearch, etc. left open |

---

## 22. Network Security Monitoring

NSM = collecting, detecting, and analyzing network traffic for suspicious activity.

### Core Skills

| Skill | Description |
|-------|-------------|
| **Traffic Analysis** | Identifying normal vs. abnormal traffic patterns |
| **Anomaly Detection** | Finding deviations from baseline behavior |
| **Log Analysis** | Reading and interpreting firewall, DNS, DHCP, and system logs |
| **Threat Hunting** | Proactively searching for signs of compromise |
| **Alert Triage** | Sorting through IDS/IPS alerts to find real threats |

### NSM Tools

| Tool | Type | Purpose |
|------|------|---------|
| **Zeek (formerly Bro)** | NSM | Deep protocol analysis, log generation |
| **Suricata** | IDS/IPS | Signature and anomaly-based detection; can also capture packets |
| **Snort** | IDS/IPS | Rule-based detection; one of the oldest and most widely used |
| **Security Onion** | Platform | All-in-one NSM platform combining Zeek, Suricata, Elasticsearch, Kibana |
| **Splunk** | SIEM | Log aggregation, correlation, and visualization |
| **ELK Stack** | SIEM | Elasticsearch + Logstash + Kibana — open-source SIEM |

### What to Monitor

- **Unusual outbound connections** — possible C2 communication
- **Large data transfers** — possible exfiltration
- **Port scanning activity** — reconnaissance
- **Multiple failed login attempts** — brute force
- **DNS queries to unknown domains** — possible DNS tunneling
- **ARP traffic anomalies** — ARP spoofing

---

## 23. Real Tools Used by Ethical Hackers

These are the core networking tools you will use on every engagement. Learn each one.

| Tool | Category | What it Does | Why You Need It |
|------|----------|-------------|-----------------|
| **Nmap** | Scanner | Network discovery, port scanning, OS/service detection | First tool on every pentest |
| **Wireshark** | Packet Analyzer | GUI traffic capture and analysis | Understand what's actually on the wire |
| **Tcpdump** | Packet Analyzer | CLI traffic capture | Remote systems, scripting, lightweight capture |
| **Netcat (nc)** | Swiss Army Knife | Port scanning, banners, reverse shells, file transfer | Extremely versatile — called the "Swiss Army Knife" |
| **Burp Suite** | Web Proxy | Intercept and modify HTTP/HTTPS requests | Essential for web app pentesting |
| **Bettercap** | MITM | ARP/DNS spoofing, SSL stripping, credential capture | Modern replacement for Ettercap |
| **Ettercap** | MITM | ARP poisoning, sniffing | Classic MITM tool |
| **Responder** | LLMNR Poisoner | Captures NTLMv2 hashes on Windows networks | Critical for internal Windows network attacks |
| **Metasploit** | Exploitation | Exploit framework with extensive module library | Industry-standard exploitation framework |
| **Masscan** | Scanner | Internet-scale port scanner | Very fast scanning of large ranges |
| **Netdiscover** | Discovery | ARP-based host discovery | Quick LAN host discovery |

### Quick Reference Commands

```bash
# Nmap — Find all hosts and open ports
nmap -sV -sC -O 192.168.1.0/24

# Netcat — Banner grabbing
nc -v 192.168.1.1 22

# Netcat — Simple listener (for reverse shells)
nc -lvnp 4444

# Tcpdump — Capture traffic on interface
tcpdump -i eth0

# Netdiscover — Find live hosts on local network
netdiscover -r 192.168.1.0/24

# Responder — Start LLMNR/NBT-NS poisoning
responder -I eth0 -rdwv
```

---

## 24. Recommended Resources

### Free Beginner-Friendly Platforms

| Resource | Link | Why |
|----------|------|-----|
| **TryHackMe — Pre-Security Path** | [tryhackme.com/path/outline/presecurity](https://tryhackme.com/path/outline/presecurity) | Best structured beginner path — covers all fundamentals interactively |
| **TryHackMe — Network Fundamentals Module** | [tryhackme.com/module/network-fundamentals](https://tryhackme.com/module/network-fundamentals) | Directly covers everything in this guide with hands-on labs |
| **Professor Messer — CompTIA Network+** | [professormesser.com](https://www.professormesser.com/) | Free, deep, high-quality video content covering networking from scratch |
| **Cisco Networking Academy (Packet Tracer)** | [netacad.com](https://www.netacad.com/) | Free courses + Packet Tracer simulator for practicing routing, VLANs, subnetting |

### Practice Subnetting

| Resource | Link |
|----------|------|
| **Subnet Practice** | [subnettingpractice.com](https://subnettingpractice.com/) |
| **Subnetting Questions** | [subnetting.org](https://www.subnetting.org/) |

### Books

- **"Computer Networking: A Top-Down Approach"** — Kurose & Ross (gold standard textbook)
- **"The TCP/IP Guide"** — Charles M. Kozierok (free online at tcpipguide.com)
- **"Hacking: The Art of Exploitation"** — Jon Erickson (covers networking from an offensive angle)

---

> *"To hack a network, you must first think like the network."*
