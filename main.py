#!/usr/bin/env python3
"""
Network Enumeration Tool
Main entry point for the automated network enumeration script.

CSCI 4449/6658 - Ethical Hacking Final Project
"""

import argparse
import sys
import os
from typing import List

# Import custom modules
from modules.target_parser import TargetParser
from modules.nmap_handler import NmapHandler
from modules.nmap_parser import NmapParser
from modules.smb_enumerator import SMBEnumerator
from modules.report_generator import ReportGenerator
from modules.result_classes import HostResult
from modules.utils import (
    prompt_dns_confirmation,
    get_default_output_filename
)


class NetworkEnumerationTool:
    """Main class for network enumeration tool."""
    
    def __init__(self, args):
        self.args = args
        self.target_parser = TargetParser()
        self.nmap_handler = NmapHandler()
        self.results: List[HostResult] = []
    
    def run(self):
        """Main execution flow."""
        print("\n" + "="*60)
        print("Network Enumeration Tool")
        print("="*60 + "\n")
        
        # Step 1: Parse and validate targets
        if not self._parse_targets():
            return False
        
        # Step 2: Get final target list
        targets = self.target_parser.get_final_targets()
        
        if not targets:
            print("[ERROR] No valid targets to scan after applying exclusions.")
            return False
        
        print(f"\n[INFO] Total targets to scan: {len(targets)}")
        print(f"[INFO] Targets: {', '.join(targets[:5])}")
        if len(targets) > 5:
            print(f"         ... and {len(targets) - 5} more")
        
        # Step 3: Enumerate each target
        print("\n" + "-"*60)
        print("Starting Enumeration")
        print("-"*60 + "\n")
        
        for idx, target in enumerate(targets, 1):
            print(f"\n[{idx}/{len(targets)}] Scanning {target}...")
            result = self._enumerate_host(target)
            self.results.append(result)
        
        # Step 4: Generate report
        print("\n" + "-"*60)
        print("Generating Report")
        print("-"*60 + "\n")
        
        output_file = self.args.output if self.args.output else get_default_output_filename()
        
        report_gen = ReportGenerator(output_file)
        success = report_gen.generate_report(self.results)
        
        if success:
            print("\n" + "="*60)
            print("Enumeration Complete!")
            print("="*60 + "\n")
            return True
        else:
            print("\n[ERROR] Failed to generate report.")
            return False
    
    def _parse_targets(self) -> bool:
        """Parse and validate target specifications."""
        # Check for DNS names and prompt if found
        if self.target_parser.contains_dns_names(self.args.targets):
            if not prompt_dns_confirmation():
                return False
        
        # Parse targets
        print("[INFO] Parsing target specifications...")
        self.target_parser.set_targets(self.args.targets)
        
        # Parse exclusions if provided
        if self.args.exclude:
            print("[INFO] Parsing exclusion specifications...")
            self.target_parser.set_exclusions(self.args.exclude)
        
        return True
    
    def _enumerate_host(self, ip: str) -> HostResult:
        """
        Perform complete enumeration of a single host.
        
        Args:
            ip: IP address to enumerate
            
        Returns:
            HostResult object with all enumeration data
        """
        result = HostResult(ip_address=ip)
        nmap_outputs = {}
        
        # Step 1: Check if host is alive
        print(f"  [1/5] Checking if host is alive...")
        is_alive, ping_output = self.nmap_handler.check_host_alive(ip)
        result.is_alive = is_alive
        result.add_command_output(
            self.nmap_handler.get_command_string('ping', ip),
            ping_output
        )
        
        if not is_alive:
            print(f"  [INFO] Host {ip} appears to be down. Skipping further scans.")
            return result
        
        # Step 2: Quick TCP scan
        print(f"  [2/5] Running quick TCP scan...")
        tcp_quick_output = self.nmap_handler.tcp_quick_scan(ip)
        nmap_outputs['tcp_quick'] = tcp_quick_output
        result.add_command_output(
            self.nmap_handler.get_command_string('tcp_quick', ip),
            tcp_quick_output
        )
        
        # Step 3: OS detection
        print(f"  [3/5] Detecting operating system...")
        os_output = self.nmap_handler.os_detection_scan(ip)
        nmap_outputs['os_detection'] = os_output
        result.add_command_output(
            self.nmap_handler.get_command_string('os_detection', ip),
            os_output
        )
        
        # Parse initial results to determine OS
        temp_result = NmapParser.parse_to_host_result(ip, nmap_outputs)
        result.os_type = temp_result.os_type
        result.hostname = temp_result.hostname
        result.services = temp_result.services
        result.probable_os_version = temp_result.probable_os_version
        result.potential_vulnerabilities = temp_result.potential_vulnerabilities
        
        # Step 4: Windows-specific enumeration
        if result.is_windows():
            print(f"  [4/5] Windows detected - running Windows-specific enumeration...")
            
            # SMB enumeration with nmap
            smb_output = self.nmap_handler.smb_enumeration_scan(ip)
            nmap_outputs['smb'] = smb_output
            result.add_command_output(
                self.nmap_handler.get_command_string('smb', ip),
                smb_output
            )
            
            # Parse SMB info
            result.smb_info = NmapParser.parse_smb_info(smb_output)
            if 'domain' in result.smb_info:
                result.domain = result.smb_info['domain']
            
            # Additional Windows tools (enum4linux, smbclient, etc.)
            windows_outputs = SMBEnumerator.run_all_windows_enumeration(ip)
            for tool_name, output in windows_outputs.items():
                result.add_command_output(tool_name, output)
        else:
            print(f"  [4/5] Non-Windows system detected - skipping Windows enumeration...")
        
        # Step 5: UDP scan (optional, can be slow)
        if self.args.udp:
            print(f"  [5/5] Running UDP scan...")
            udp_output = self.nmap_handler.udp_scan(ip)
            result.add_command_output(
                self.nmap_handler.get_command_string('udp', ip),
                udp_output
            )
            # Re-parse to include UDP services
            nmap_outputs['udp'] = udp_output
            temp_result = NmapParser.parse_to_host_result(ip, nmap_outputs)
            result.services = temp_result.services
        else:
            print(f"  [5/5] UDP scan skipped (use --udp to enable)")
        
        print(f"  [DONE] Enumeration of {ip} complete.")
        return result


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description='Network Enumeration Tool - Automated host discovery and enumeration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan a single IP address
  python main.py 192.168.1.1

  # Scan a subnet
  python main.py 192.168.1.0/24

  # Scan multiple targets
  python main.py 192.168.1.1,192.168.1.5,10.0.0.0/24

  # Scan with exclusions
  python main.py 192.168.1.0/24 --exclude 192.168.1.1,192.168.1.50

  # Scan a DNS hostname
  python main.py server.example.com

  # Custom output file
  python main.py 192.168.1.0/24 -o /path/to/custom_report.md

  # Enable UDP scanning (slower but more thorough)
  python main.py 192.168.1.1 --udp

IMPORTANT NOTES:
  - Only scan systems you own or have explicit permission to test
  - DNS names will trigger a confirmation prompt to prevent accidental scans
  - Default output location is the current working directory
  - Reports are timestamped in UTC timezone

Target Specification Formats:
  - Single IPv4: 192.168.1.1
  - DNS hostname: server.example.com
  - CIDR subnet: 192.168.1.0/24
  - Comma-separated list: 192.168.1.1,192.168.1.5,10.0.0.1

Required Tools:
  - nmap must be installed on your system
  - Optional: enum4linux, smbclient, nmblookup, rpcclient (for Windows enumeration)
        """
    )
    
    # Required positional argument
    parser.add_argument(
        'targets',
        type=str,
        help='Target specification (IP, DNS, CIDR, or comma-separated list)'
    )
    
    # Optional arguments
    parser.add_argument(
        '--exclude',
        type=str,
        default=None,
        help='Hosts to exclude from scan (same format as targets)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=None,
        help='Custom output file path (default: host_enumeration_report_YYYYMMDD_HHMM_UTC.md)'
    )
    
    parser.add_argument(
        '--udp',
        action='store_true',
        help='Enable UDP scanning (slower but more thorough)'
    )
    
    return parser


def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Create and run the tool
    tool = NetworkEnumerationTool(args)
    success = tool.run()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
