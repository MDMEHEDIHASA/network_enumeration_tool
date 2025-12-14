# Network Enumeration Report
**Generated:** 2025-12-13 01:54:45 UTC
---

## Summary

- **Total Hosts Scanned:** 2
- **Hosts Alive:** 2
- **Windows Hosts:** 1
- **Linux Hosts:** 0
- **Other/Unknown:** 1

---

## Host: 45.33.32.156

### Verified Information

| Property | Value |
|----------|-------|
| **IP Address** | 45.33.32.156 |
| **Hostname** | scanme.nmap.org |
| **Domain** | N/A |
| **Operating System** | Windows |
| **Status** | Up |

#### Active Services

| Port | Protocol | Service | Version |
|------|----------|---------|----------|
| 22 | tcp | ssh | OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0) |
| 80 | tcp | http | Apache httpd 2.4.7 ((Ubuntu)) |
| 22 | tcp | ssh | 25/tcp    filtered smtp |
| 80 | tcp | http | 139/tcp   filtered netbios-ssn |
| 9929 | tcp | nping-echo | 31337/tcp open     Elite |

### Unverified Information

**Probable OS Version:** Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)

**Potential Vulnerabilities:**

- Outdated OpenSSH version detected - may be vulnerable to known exploits

### Command Outputs

**Command 1:** `nmap -sn 45.33.32.156`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:53 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.082s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.17 seconds
```

**Command 2:** `nmap -sV -F 45.33.32.156`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:53 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.085s latency).
Not shown: 95 closed tcp ports (reset)
PORT    STATE    SERVICE      VERSION
22/tcp  open     ssh          OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
25/tcp  filtered smtp
80/tcp  open     http         Apache httpd 2.4.7 ((Ubuntu))
139/tcp filtered netbios-ssn
445/tcp filtered microsoft-ds
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.96 seconds
```

**Command 3:** `nmap -O 45.33.32.156`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:53 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.083s latency).
Not shown: 993 closed tcp ports (reset)
PORT      STATE    SERVICE
22/tcp    open     ssh
25/tcp    filtered smtp
80/tcp    open     http
139/tcp   filtered netbios-ssn
445/tcp   filtered microsoft-ds
9929/tcp  open     nping-echo
31337/tcp open     Elite
Device type: general purpose|router
Running: Linux 5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 5.0 - 5.14, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 17 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 5.65 seconds
```

**Command 4:** `nmap -p 445,139 --script smb-os-discovery,smb-enum-shares 45.33.32.156`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:54 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.072s latency).

PORT    STATE    SERVICE
139/tcp filtered netbios-ssn
445/tcp filtered microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 2.11 seconds
```

**Command 5:** `enum4linux`

```
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sat Dec 13 01:54:03 2025

[34m =========================================( [0m[32mTarget Information[0m[34m )=========================================

[0mTarget ........... 45.33.32.156
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


[34m ============================( [0m[32mEnumerating Workgroup/Domain on 45.33.32.156[0m[34m )============================

[0m[33m
[E] [0m[31mCan't find workgroup/domain

[0m

[34m ================================( [0m[32mNbtstat Information for 45.33.32.156[0m[34m )================================

[0mLooking up status of 45.33.32.156
No reply from 45.33.32.156

[34m ===================================( [0m[32mSession Check on 45.33.32.156[0m[34m )===================================

[0m[33m
[E] [0m[31mServer doesn't allow session using username '', password ''.  Aborting remainder of tests.

[0m
```

**Command 6:** `nmblookup`

```
Looking up status of 45.33.32.156
No reply from 45.33.32.156

```

---

## Host: 127.0.0.1

### Verified Information

| Property | Value |
|----------|-------|
| **IP Address** | 127.0.0.1 |
| **Hostname** | localhost |
| **Domain** | N/A |
| **Operating System** | Unknown |
| **Status** | Up |

**Active Services:** None detected

### Unverified Information

*No unverified information to report.*

### Command Outputs

**Command 1:** `nmap -sn 127.0.0.1`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:54 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up.
Nmap done: 1 IP address (1 host up) scanned in 0.00 seconds
```

**Command 2:** `nmap -sV -F 127.0.0.1`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:54 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000013s latency).
All 100 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 100 closed tcp ports (reset)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.43 seconds
```

**Command 3:** `nmap -O 127.0.0.1`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:54 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000071s latency).
All 1000 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 1000 closed tcp ports (reset)
Too many fingerprints match this host to give specific OS details
Network Distance: 0 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.60 seconds
```

---

