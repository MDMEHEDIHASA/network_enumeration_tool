# Network Enumeration Report
**Generated:** 2025-12-13 01:59:24 UTC
---

## Summary

- **Total Hosts Scanned:** 1
- **Hosts Alive:** 1
- **Windows Hosts:** 0
- **Linux Hosts:** 0
- **Other/Unknown:** 1

---

## Host: 172.67.72.192

### Verified Information

| Property | Value |
|----------|-------|
| **IP Address** | 172.67.72.192 |
| **Hostname** | N/A |
| **Domain** | N/A |
| **Operating System** | Unix |
| **Status** | Up |

#### Active Services

| Port | Protocol | Service | Version |
|------|----------|---------|----------|
| 80 | tcp | http | Cloudflare http proxy |
| 443 | tcp | ssl/https | cloudflare |
| 8080 | tcp | http | Cloudflare http proxy |
| 8443 | tcp | ssl/https-alt | cloudflare |
| 80 | tcp | http | 443/tcp  open  https |
| 8080 | tcp | http-proxy | 8443/tcp open  https-alt |

### Unverified Information

*No unverified information to report.*

### Command Outputs

**Command 1:** `nmap -sn 172.67.72.192`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:59 UTC
Nmap scan report for 172.67.72.192
Host is up (0.033s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
```

**Command 2:** `nmap -sV -F 172.67.72.192`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:59 UTC
Nmap scan report for 172.67.72.192
Host is up (0.025s latency).
Not shown: 96 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Cloudflare http proxy
443/tcp  open  ssl/https     cloudflare
8080/tcp open  http          Cloudflare http proxy
8443/tcp open  ssl/https-alt cloudflare

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.08 seconds
```

**Command 3:** `nmap -O 172.67.72.192`

```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-13 01:59 UTC
Nmap scan report for 172.67.72.192
Host is up (0.030s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE
80/tcp   open  http
443/tcp  open  https
8080/tcp open  http-proxy
8443/tcp open  https-alt
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Apple iOS 14.0 - 15.6 or tvOS 14.3 - 16.1 (Darwin 20.0.0 - 22.1.0) (89%), Apple iOS 15.7 (Darwin 21.7.0) (89%), Apple macOS 11 (Big Sur) - 13 (Ventura) or iOS 16 (Darwin 20.6.0 - 22.4.0) (89%), Apple macOS 13 (Ventura) (Darwin 22.0.0) (89%), FreeBSD 11.0-RELEASE (89%), FreeBSD 11.0-STABLE (89%), FreeBSD 11.1-STABLE (89%), FreeBSD 11.3-RELEASE (89%), FreeBSD 12.0-RELEASE - 12.1-RELEASE (89%), FreeBSD 12.2-RELEASE - 13.0-RELEASE (89%)
No exact OS matches for host (test conditions non-ideal).

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.07 seconds
```

---

