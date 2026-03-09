# 🌐 Networking Fundamentals

> A comprehensive guide to networking concepts essential for cybersecurity professionals.

---

## 📌 What is a Computer Network?

A **computer network** is a collection of interconnected devices that communicate and exchange data using standardized communication protocols.

### 🔑 Key Components of a Network

| Component | Description |
|-----------|-------------|
| **Devices** | Computers, routers, switches, servers, smartphones |
| **Transmission Medium** | Copper cables, fiber optic, wireless (Wi-Fi, Bluetooth) |
| **Protocols** | Standardized rules that govern how data is sent and received |
| **Network Interface Card (NIC)** | Hardware that connects a device to the network |
| **IP Address** | Unique identifier assigned to each device on a network |

---

## 📦 Packet Switching

Data in networks is transmitted using **packet switching** — data is broken into smaller units called **packets** for efficient transmission.

### How It Works:
1. A large piece of data is divided into smaller packets.
2. Each packet is sent independently through the network.
3. Packets may take different routes to the destination.
4. At the destination, packets are **reassembled** in the correct order.

### Each Packet Contains:
- **Source IP Address** — where the packet came from
- **Destination IP Address** — where the packet is going
- **Payload** — the actual data being transferred
- **Sequence Number** — for correct reassembly
- **Control Information** — error detection and routing info

---

## 🖧 Types of Networks

| Type | Full Name | Coverage | Example |
|------|-----------|----------|---------|
| **PAN** | Personal Area Network | ~1–10 meters | Bluetooth headset, smartwatch |
| **LAN** | Local Area Network | Building / Campus | Home Wi-Fi, office network |
| **MAN** | Metropolitan Area Network | City-wide | City ISP network, university campus |
| **WAN** | Wide Area Network | Countries / Continents | The Internet, VPN connections |

### Details:

#### 🏠 LAN — Local Area Network
- Covers homes, offices, or universities.
- High speed (usually 100 Mbps to 10 Gbps).
- Privately owned and managed.
- Uses Ethernet (wired) or Wi-Fi (wireless).

#### 🌍 WAN — Wide Area Network
- Connects multiple LANs across cities or countries.
- Lower speed than LAN due to distance.
- The **Internet** is the largest WAN.
- Uses leased lines, fiber, or satellite links.

#### 🏙️ MAN — Metropolitan Area Network
- Covers a city or large campus.
- Larger than LAN but smaller than WAN.
- Often used by ISPs or city governments.

#### 📱 PAN — Personal Area Network
- Very small, personal network around a single user.
- Examples: Bluetooth devices, USB tethering, AirDrop.
- Range is typically under 10 meters.

---

## 🌐 Internet vs Intranet vs Extranet

| Type | Access | Description | Example |
|------|--------|-------------|---------|
| **Internet** | Public | Global network accessible to everyone | Browsing websites |
| **Intranet** | Private (Internal) | Internal network within an organization | Company internal portal |
| **Extranet** | Limited External | Controlled access for partners or clients | Vendor login to company system |

### Key Differences:
- **Internet** = Open to all, no ownership.
- **Intranet** = Closed network, requires employee credentials.
- **Extranet** = Bridge between Intranet and Internet — selective external access.

---

## 🔢 IP Addressing

Every device on a network needs a unique **IP (Internet Protocol) address**.

### IPv4
- Format: `192.168.1.1` (4 octets, each 0–255)
- 32-bit address → ~4.3 billion unique addresses
- Classes: A, B, C, D, E

### IPv6
- Format: `2001:0db8:85a3::8a2e:0370:7334`
- 128-bit address → virtually unlimited addresses
- Designed to replace IPv4 due to address exhaustion

### Private IP Ranges (IPv4):
| Class | Range | Common Use |
|-------|-------|------------|
| A | 10.0.0.0 – 10.255.255.255 | Large networks |
| B | 172.16.0.0 – 172.31.255.255 | Medium networks |
| C | 192.168.0.0 – 192.168.255.255 | Home/small office |

---

## 🧱 OSI Model (7 Layers)

The **OSI (Open Systems Interconnection)** model defines how data travels across a network.

| Layer | Name | Function | Protocol Examples |
|-------|------|----------|-------------------|
| 7 | **Application** | User interface, network services | HTTP, FTP, DNS, SMTP |
| 6 | **Presentation** | Data formatting, encryption | SSL/TLS, JPEG, ASCII |
| 5 | **Session** | Manages sessions/connections | NetBIOS, RPC |
| 4 | **Transport** | Reliable/unreliable delivery | TCP, UDP |
| 3 | **Network** | Routing, logical addressing | IP, ICMP, ARP |
| 2 | **Data Link** | MAC addressing, error detection | Ethernet, Wi-Fi (802.11) |
| 1 | **Physical** | Bits over physical medium | Cables, radio waves |

> 💡 **Mnemonic:** *"All People Seem To Need Data Processing"* (top to bottom)

---

## 📡 TCP/IP Model (4 Layers)

A simplified, practical model used by the modern Internet.

| Layer | Name | Equivalent OSI Layers |
|-------|------|-----------------------|
| 4 | **Application** | Application + Presentation + Session |
| 3 | **Transport** | Transport |
| 2 | **Internet** | Network |
| 1 | **Network Access** | Data Link + Physical |

---

## 🔄 Key Protocols

| Protocol | Port | Purpose |
|----------|------|---------|
| **HTTP** | 80 | Web browsing (unencrypted) |
| **HTTPS** | 443 | Web browsing (encrypted) |
| **FTP** | 21 | File transfer |
| **SSH** | 22 | Secure remote access |
| **DNS** | 53 | Domain name resolution |
| **DHCP** | 67/68 | Automatic IP assignment |
| **SMTP** | 25 | Sending emails |
| **POP3** | 110 | Receiving emails |
| **IMAP** | 143 | Email access (server-side) |
| **Telnet** | 23 | Remote access (unencrypted — avoid!) |

---

## ⚔️ TCP vs UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable (acknowledgements) | Unreliable (no ACKs) |
| Speed | Slower | Faster |
| Order | Packets delivered in order | No guaranteed order |
| Use Case | Web, Email, File Transfer | DNS, Video Streaming, Gaming |

---

## 🔧 Common Network Devices

| Device | Function |
|--------|----------|
| **Hub** | Broadcasts data to all devices (dumb, outdated) |
| **Switch** | Forwards data to specific device using MAC address |
| **Router** | Routes packets between networks using IP address |
| **Firewall** | Filters traffic based on rules (security) |
| **Modem** | Converts digital↔analog signals for ISP connection |
| **Access Point** | Provides wireless connectivity |
| **Proxy Server** | Acts as intermediary between client and internet |

---

## 🔐 Cybersecurity Relevance

Understanding networking is the **foundation of cybersecurity**. Key concepts used in attacks and defense:

- **Port Scanning** — Attackers use tools like `nmap` to find open ports.
- **Packet Sniffing** — Capturing network traffic using tools like `Wireshark`.
- **Man-in-the-Middle (MitM)** — Intercepting communication between two parties.
- **DNS Spoofing** — Redirecting traffic by poisoning DNS cache.
- **Firewall Evasion** — Bypassing network filters using tunneling or fragmentation.
- **DDoS Attacks** — Flooding a network/server with traffic to cause downtime.

---

## 📚 Resources

- [TryHackMe — Pre-Security Path](https://tryhackme.com/path/outline/presecurity)
- [Cisco Networking Academy](https://www.netacad.com/)
- [Professor Messer's CompTIA Network+](https://www.professormesser.com/)

---

> *"To hack the network, you must first understand the network."*