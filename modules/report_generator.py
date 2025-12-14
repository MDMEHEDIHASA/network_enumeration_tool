"""
Report Generator Module
Generates professional Markdown reports from enumeration results.
"""

from typing import List, Dict
from modules.result_classes import HostResult, Service
from datetime import datetime, timezone


class ReportGenerator:
    """Generates Markdown reports from enumeration results."""
    
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.content = []
    
    def add_header(self):
        """Add report header with metadata."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        
        self.content.append("# Network Enumeration Report\n")
        self.content.append(f"**Generated:** {timestamp}\n")
        self.content.append("---\n\n")
    
    def add_host_section(self, host: HostResult):
        """
        Add a complete section for a single host.
        
        Args:
            host: HostResult object containing all host information
        """
        self.content.append(f"## Host: {host.ip_address}\n\n")
        
        # Add verified information table
        self._add_verified_info_table(host)
        
        # Add unverified information section
        self._add_unverified_info_section(host)
        
        # Add command outputs section
        self._add_command_outputs_section(host)
        
        self.content.append("---\n\n")
    
    def _add_verified_info_table(self, host: HostResult):
        """Add verified information table for a host."""
        self.content.append("### Verified Information\n\n")
        
        # Create markdown table
        self.content.append("| Property | Value |\n")
        self.content.append("|----------|-------|\n")
        
        # IP Address
        self.content.append(f"| **IP Address** | {host.ip_address} |\n")
        
        # Hostname
        hostname = host.hostname if host.hostname else "N/A"
        self.content.append(f"| **Hostname** | {hostname} |\n")
        
        # Domain
        domain = host.domain if host.domain else "N/A"
        self.content.append(f"| **Domain** | {domain} |\n")
        
        # Operating System
        self.content.append(f"| **Operating System** | {host.os_type} |\n")
        
        # Host Status
        status = "Up" if host.is_alive else "Down"
        self.content.append(f"| **Status** | {status} |\n")
        
        self.content.append("\n")
        
        # Active Services Section
        if host.services:
            self.content.append("#### Active Services\n\n")
            self.content.append("| Port | Protocol | Service | Version |\n")
            self.content.append("|------|----------|---------|----------|\n")
            
            for service in host.services:
                version = service.version if service.version else "N/A"
                self.content.append(
                    f"| {service.port} | {service.protocol} | "
                    f"{service.service_name} | {version} |\n"
                )
            self.content.append("\n")
        else:
            self.content.append("**Active Services:** None detected\n\n")
        
        # Windows-specific information
        if host.is_windows() and host.smb_info:
            self.content.append("#### Windows-Specific Information\n\n")
            self.content.append("| Property | Value |\n")
            self.content.append("|----------|-------|\n")
            
            for key, value in host.smb_info.items():
                formatted_key = key.replace('_', ' ').title()
                self.content.append(f"| **{formatted_key}** | {value} |\n")
            
            self.content.append("\n")
    
    def _add_unverified_info_section(self, host: HostResult):
        """Add unverified information section for a host."""
        self.content.append("### Unverified Information\n\n")
        
        has_unverified = False
        
        # OS Version information
        if host.probable_os_version:
            self.content.append(f"**Probable OS Version:** {host.probable_os_version}\n\n")
            has_unverified = True
        
        # Potential vulnerabilities
        if host.potential_vulnerabilities:
            self.content.append("**Potential Vulnerabilities:**\n\n")
            for vuln in host.potential_vulnerabilities:
                self.content.append(f"- {vuln}\n")
            self.content.append("\n")
            has_unverified = True
        
        if not has_unverified:
            self.content.append("*No unverified information to report.*\n\n")
    
    def _add_command_outputs_section(self, host: HostResult):
        """Add raw command outputs section for a host."""
        self.content.append("### Command Outputs\n\n")
        
        if not host.command_outputs:
            self.content.append("*No command outputs recorded.*\n\n")
            return
        
        for idx, cmd_output in enumerate(host.command_outputs, 1):
            command = cmd_output['command']
            output = cmd_output['output']
            
            # Add command in single-line code block
            self.content.append(f"**Command {idx}:** `{command}`\n\n")
            
            # Add output in multi-line code block
            self.content.append("```\n")
            self.content.append(output)
            if not output.endswith('\n'):
                self.content.append('\n')
            self.content.append("```\n\n")
    
    def add_summary(self, total_hosts: int, alive_hosts: int, windows_hosts: int, linux_hosts: int):
        """
        Add summary section at the beginning of the report.
        
        Args:
            total_hosts: Total number of hosts scanned
            alive_hosts: Number of hosts that responded
            windows_hosts: Number of Windows hosts detected
            linux_hosts: Number of Linux hosts detected
        """
        summary = [
            "## Summary\n\n",
            f"- **Total Hosts Scanned:** {total_hosts}\n",
            f"- **Hosts Alive:** {alive_hosts}\n",
            f"- **Windows Hosts:** {windows_hosts}\n",
            f"- **Linux Hosts:** {linux_hosts}\n",
            f"- **Other/Unknown:** {alive_hosts - windows_hosts - linux_hosts}\n\n",
            "---\n\n"
        ]
        
        # Insert summary after header (after first 3 items: title, timestamp, separator)
        self.content[3:3] = summary
    
    def write_report(self):
        """Write the complete report to file."""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.writelines(self.content)
            print(f"\n[SUCCESS] Report written to: {self.output_file}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to write report: {str(e)}")
            return False
    
    def generate_report(self, hosts: List[HostResult]) -> bool:
        """
        Generate complete report from list of host results.
        
        Args:
            hosts: List of HostResult objects
            
        Returns:
            True if report was successfully written
        """
        # Add header
        self.add_header()
        
        # Calculate summary statistics
        total_hosts = len(hosts)
        alive_hosts = sum(1 for h in hosts if h.is_alive)
        windows_hosts = sum(1 for h in hosts if h.is_windows())
        linux_hosts = sum(1 for h in hosts if h.is_linux())
        
        # Add each host section
        for host in hosts:
            self.add_host_section(host)
        
        # Add summary (will be inserted after header)
        self.add_summary(total_hosts, alive_hosts, windows_hosts, linux_hosts)
        
        # Write to file
        return self.write_report()