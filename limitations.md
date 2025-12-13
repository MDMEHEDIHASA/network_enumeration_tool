# Known Limitations and Edge Cases

## Current Limitations

### 1. Performance
- **Full port scans can be very slow**: Scanning all 65,535 ports on multiple hosts can take hours
- **UDP scans are particularly slow**: UDP scanning is inherently slower than TCP
- **No parallel scanning**: Current implementation scans hosts sequentially

### 2. Tool Dependencies
- **Requires nmap installation**: Tool will not work without nmap on the system
- **Windows enumeration tools optional**: enum4linux, smbclient, etc. provide additional info but are not required
- **Linux/Unix optimized**: Best performance on Linux systems; Windows support requires WSL

### 3. Detection Accuracy
- **OS detection not always accurate**: Nmap OS fingerprinting can be wrong, especially with firewalls
- **Service version detection limited**: Depends on banner grabbing; may miss obfuscated services
- **False negatives possible**: Firewalls and IDS may block scans, making hosts appear offline

### 4. Network Constraints
- **No authentication**: Tool does not perform authenticated scans
- **No SSL/TLS certificate enumeration**: Does not deeply analyze encrypted services
- **Basic vulnerability detection**: Only identifies obvious vulnerabilities based on versions

### 5. DNS Handling
- **Single DNS server check**: Only checks primary system DNS resolver
- **No reverse DNS validation**: Does not verify reverse DNS records
- **DNS caching**: May get cached results instead of current resolutions

## Known Edge Cases

### 1. Target Parsing
- **Invalid CIDR notation**: Tool shows error but continues with valid targets
- **Unresolvable DNS names**: Prints warning and skips the hostname
- **Duplicate targets**: Automatically deduplicated by using sets

### 2. Scanning Edge Cases
- **Host filtering**: Some hosts may filter ICMP, appearing down even if services are running
  - *Mitigation*: TCP scan still runs even if ping fails
- **Rate limiting**: Aggressive scanning may trigger rate limits or IDS alerts
  - *Mitigation*: Use appropriate timing (consider adding -T options)
- **Timeouts**: Very slow networks may cause timeout errors
  - *Current timeout*: 5-60 minutes depending on scan type

### 3. Windows Enumeration
- **Null session required**: Many Windows enumeration techniques require null sessions
- **Modern Windows more secure**: Windows 10/11 and Server 2016+ block many enumeration techniques
- **Domain-joined hosts**: May require credentials for full enumeration

### 4. Report Generation
- **Large outputs**: Very verbose nmap output may create large report files (10+ MB)
- **Special characters**: Some service banners contain characters that may not render in Markdown
- **UTF-8 encoding**: Non-ASCII characters in hostnames may cause encoding issues

### 5. Permissions
- **Requires elevated privileges**: Some scans (OS detection, SYN scan) require root/administrator
- **Firewall interference**: Local firewalls may block outgoing scans
- **Network ACLs**: Enterprise networks may block certain scan types

## Future Improvements

### Potential Enhancements
1. **Parallel scanning**: Implement threading/multiprocessing for faster scans
2. **Authenticated scans**: Add support for credential-based enumeration
3. **Better error recovery**: More graceful handling of network errors
4. **Progress indicators**: Real-time progress bars for long-running scans
5. **HTML reports**: Additional output format option
6. **Scan profiles**: Pre-configured scan profiles (quick, normal, thorough)
7. **Rate limiting**: Built-in rate limiting to avoid IDS alerts
8. **IPv6 support**: Currently only supports IPv4
9. **Cloud integration**: Export results to security platforms
10. **Screenshot capabilities**: Automated screenshots of web services

## Testing Notes

### Successfully Tested Scenarios
- ✅ Single IP address scanning
- ✅ CIDR subnet scanning (up to /24)
- ✅ Mixed target types (IP + DNS + CIDR)
- ✅ Host exclusion functionality
- ✅ Windows Server 2019 enumeration
- ✅ Ubuntu 20.04 enumeration
- ✅ Report generation with various host counts

### Known Issues During Testing
- ⚠️ Very old Windows versions (XP, 2003) may not respond to modern nmap scripts
- ⚠️ Highly secured environments may return minimal information
- ⚠️ Virtual machines sometimes show inaccurate OS detection
- ⚠️ DNS resolution can be slow on some networks (30+ seconds per hostname)

## Recommendations for Users

1. **Start with small target ranges**: Test with 1-5 hosts before larger subnets
2. **Use exclusions carefully**: Verify exclusion list matches your scope document
3. **Be patient with scans**: Full enumeration can take 10-30 minutes per host
4. **Check tool availability**: Verify enum4linux and SMB tools are installed for Windows targets
5. **Run with appropriate privileges**: Use sudo/root for full functionality
6. **Monitor network impact**: Be aware of bandwidth usage during large scans
7. **Verify DNS configuration**: Ensure DNS server is correct before scanning hostnames
8. **Keep nmap updated**: Older nmap versions may have different output formats

## Contact

For questions about limitations or to report bugs:
- [Your email]
- [Partner email]