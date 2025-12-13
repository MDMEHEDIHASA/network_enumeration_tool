# Network Enumeration Tool

Automated network enumeration tool for ethical hacking and security assessments.

**Course:** CSCI 4449/6658 - Ethical Hacking  
**Institution:** University of New Haven  
**Semester:** Fall 2025

## Overview

This tool automates the discovery and documentation of network hosts, services, and vulnerabilities. It integrates multiple reconnaissance and enumeration techniques and produces comprehensive Markdown reports.

## Features

- ✅ Support for multiple target formats (IP, DNS, CIDR)
- ✅ Host discovery and availability verification
- ✅ Operating system detection (Windows/Linux/Unix)
- ✅ Service and port enumeration
- ✅ Windows-specific enumeration (SMB, NetBIOS, AD)
- ✅ Automated vulnerability detection
- ✅ Professional Markdown report generation
- ✅ DNS safety confirmation prompts
- ✅ Host exclusion for out-of-scope targets

## Requirements

### System Requirements
- Python 3.12
- nmap (system installation)
- Linux, macOS, or Windows with WSL

### Optional Tools (for Windows enumeration)
- enum4linux
- smbclient
- nmblookup
- rpcclient

## Installation

### 1. Clone or download this repository
```bash
cd network_enumeration_tool
```

### 2. Create Python 3.12 virtual environment
```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Install system dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install nmap enum4linux smbclient
```

**macOS:**
```bash
brew install nmap
```

**Windows:**
- Download nmap from https://nmap.org/download.html
- Use WSL for full functionality

## Usage

### Basic Usage
```bash
# Scan a single IP
python main.py 192.168.1.1

# Scan a subnet
python main.py 192.168.1.0/24

# Scan multiple targets
python main.py 192.168.1.1,192.168.1.5,10.0.0.0/24
```

### Advanced Usage
```bash
# Scan with exclusions
python main.py 192.168.1.0/24 --exclude 192.168.1.1,192.168.1.50

# Custom output file
python main.py 192.168.1.0/24 -o /path/to/report.md

# Enable UDP scanning
python main.py 192.168.1.1 --udp

# Scan DNS hostname
python main.py server.example.com
```

### Help
```bash
python main.py --help
```

## Output

Reports are generated in Markdown format with the following structure:

- **Summary**: Overall statistics
- **Per-Host Sections**:
  - Verified Information (IP, hostname, OS, services)
  - Unverified Information (probable details, vulnerabilities)
  - Command Outputs (raw command results)

**Default filename:** `host_enumeration_report_YYYYMMDD_HHMM_UTC.md`

## Project Structure
```
network_enumeration_tool/
├── main.py                    # Main entry point
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── contributions.md           # Team contributions
├── limitations.md             # Known limitations
├── modules/
│   ├── __init__.py
│   ├── target_parser.py       # Parse target specifications
│   ├── nmap_handler.py        # Execute nmap scans
│   ├── nmap_parser.py         # Parse nmap output
│   ├── smb_enumerator.py      # Windows enumeration
│   ├── result_classes.py      # Data structures
│   ├── report_generator.py    # Generate reports
│   └── utils.py               # Utility functions
└── samples/                   # Sample output reports
```

## Legal and Ethical Considerations

⚠️ **WARNING**: This tool is for educational purposes and authorized security testing only.

- Only scan systems you own or have explicit written permission to test
- Unauthorized scanning may be illegal in your jurisdiction
- Always follow responsible disclosure practices
- Respect privacy and confidentiality

## License

This project is for educational purposes as part of CSCI 4449/6658 coursework.

## Authors

[Your names here]

## Acknowledgments

- University of New Haven - CSCI 4449/6658
- Instructor: Charles R Barone IV