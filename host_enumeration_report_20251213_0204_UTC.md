# Network Enumeration Report
**Generated:** 2025-12-13 02:04:33 UTC
---

## Summary

- **Total Hosts Scanned:** 1
- **Hosts Alive:** 1
- **Windows Hosts:** 0
- **Linux Hosts:** 1
- **Other/Unknown:** 0

---

## Host: 67.81.204.128

### Verified Information

| Property | Value |
|----------|-------|
| **IP Address** | 67.81.204.128 |
| **Hostname** | ool-4351cc80.dyn.optonline.net |
| **Domain** | N/A |
| **Operating System** | Linux |
| **Status** | Up |

#### Active Services

| Port | Protocol | Service | Version |
|------|----------|---------|----------|
| 53 | tcp | tcpwrapped | 80/tcp   filtered http |
| 8000 | tcp | http-alt | 8080/tcp filtered http-proxy |
| 53 | tcp | domain | 80/tcp   filtered http |
| 8000 | tcp | http-alt | 8080/tcp filtered http-proxy |

### Unverified Information

**Probable OS Version:** Linux 4.15 - 5.19, OpenWrt 21.02 (Linux 5.4), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)

### Command Outputs

**Command 1:** `nmap -sn 67.81.204.128`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 02:04 UTC
Nmap scan report for ool-4351cc80.dyn.optonline.net (67.81.204.128)
Host is up (0.0015s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds
```

**Command 2:** `nmap -sV -F 67.81.204.128`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 02:04 UTC
Nmap scan report for ool-4351cc80.dyn.optonline.net (67.81.204.128)
Host is up (0.0029s latency).
Not shown: 93 closed tcp ports (reset)
PORT     STATE    SERVICE    VERSION
22/tcp   filtered ssh
23/tcp   filtered telnet
53/tcp   open     tcpwrapped
80/tcp   filtered http
443/tcp  filtered https
8000/tcp open     http-alt
8080/tcp filtered http-proxy
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8000-TCP:V=7.95%I=7%D=12/13%Time=693CC9AE%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,8A,"HTTP/1\.1\x20302\x20Found\r\nDate:\r\nServer:\r\nLocation
SF::https://www\.optimum\.net/internet/manage-router\r\nConnection:\x20clo
SF:se\r\nContent-Type:\x20text/html\r\n\n")%r(FourOhFourRequest,8A,"HTTP/1
SF:\.1\x20302\x20Found\r\nDate:\r\nServer:\r\nLocation:https://www\.optimu
SF:m\.net/internet/manage-router\r\nConnection:\x20close\r\nContent-Type:\
SF:x20text/html\r\n\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.20 seconds
```

**Command 3:** `nmap -O 67.81.204.128`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 02:04 UTC
Nmap scan report for ool-4351cc80.dyn.optonline.net (67.81.204.128)
Host is up (0.0023s latency).
Not shown: 991 closed tcp ports (reset)
PORT     STATE    SERVICE
22/tcp   filtered ssh
23/tcp   filtered telnet
53/tcp   open     domain
80/tcp   filtered http
443/tcp  filtered https
8000/tcp open     http-alt
8080/tcp filtered http-proxy
8181/tcp filtered intermapper
9000/tcp filtered cslistener
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, OpenWrt 21.02 (Linux 5.4), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
Network Distance: 1 hop

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2.82 seconds
```

---

