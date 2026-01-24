"""
Nmap Handler Module
Executes various nmap scans and returns raw output.
"""

import nmap
import subprocess
from typing import Optional, Dict


class NmapHandler:
    """Handles execution of nmap scans."""
    
    def __init__(self):
        self.nm = nmap.PortScanner()
    
    def check_host_alive(self, ip: str) -> tuple[bool, str]:
        """
        Quick ping scan to check if host is alive.
        
        Args:
            ip: IP address to check
            
        Returns:
            Tuple of (is_alive: bool, raw_output: str)
        """
        command = f"nmap -sn {ip}"
        try:
            result = subprocess.run(
                ['nmap', '-sn', ip],
                capture_output=True,
                text=True,
                timeout=30
            )
            output = result.stdout
            
            # Check if host is up
            is_alive = 'Host is up' in output or '1 host up' in output
            
            return is_alive, output
            
        except subprocess.TimeoutExpired:
            return False, "[ERROR] Ping scan timed out"
        except Exception as e:
            return False, f"[ERROR] Ping scan failed: {str(e)}"
    
    def tcp_quick_scan(self, ip: str) -> str:
        """
        Quick TCP scan of top 100 ports.
        
        Args:
            ip: IP address to scan
            
        Returns:
            Raw nmap output

        -sV means service version detected which software is running.
        """
        command = f"nmap -sV -F {ip}"
        try:
            result = subprocess.run(
                ['nmap', '-sV', '-F', ip],
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes
            )
            return result.stdout
            
        except subprocess.TimeoutExpired:
            return "[ERROR] TCP quick scan timed out after 5 minutes"
        except Exception as e:
            return f"[ERROR] TCP quick scan failed: {str(e)}"
    
    def tcp_full_scan(self, ip: str) -> str:
        """
        Full TCP scan of all 65535 ports with service detection.
        
        Args:
            ip: IP address to scan
            
        Returns:
            Raw nmap output
        -sV: Service version detection
        -sC: Run default nmap scripts (safe checks for vulnerabilities)
        -p-: Scan all 65535 ports (instead of just common ones)
        """
        command = f"nmap -sV -sC -p- {ip}"
        try:
            print(f"[INFO] Running full TCP scan on {ip} (this may take a while)...")
            result = subprocess.run(
                ['nmap', '-sV', '-sC', '-p-', ip],
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour
            )
            return result.stdout
            
        except subprocess.TimeoutExpired:
            return "[ERROR] Full TCP scan timed out after 1 hour"
        except Exception as e:
            return f"[ERROR] Full TCP scan failed: {str(e)}"
    
    def udp_scan(self, ip: str) -> str:
        """
        UDP scan of common ports.
        
        Args:
            ip: IP address to scan
            
        Returns:
            Raw nmap output
        """
        command = f"nmap -sU --top-ports 20 {ip}"
        try:
            print(f"[INFO] Running UDP scan on {ip}...")
            result = subprocess.run(
                ['nmap', '-sU', '--top-ports', '20', ip],
                capture_output=True,
                text=True,
                timeout=600  # 10 minutes
            )
            return result.stdout
            
        except subprocess.TimeoutExpired:
            return "[ERROR] UDP scan timed out after 10 minutes"
        except Exception as e:
            return f"[ERROR] UDP scan failed: {str(e)}"
    
    def os_detection_scan(self, ip: str) -> str:
        """
        OS detection scan.
        
        Args:
            ip: IP address to scan
            
        Returns:
            Raw nmap output
        """
        command = f"nmap -O {ip}"
        try:
            print(f"[INFO] Running OS detection on {ip}...")
            result = subprocess.run(
                ['nmap', '-O', ip],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.stdout
            
        except subprocess.TimeoutExpired:
            return "[ERROR] OS detection scan timed out"
        except Exception as e:
            return f"[ERROR] OS detection failed: {str(e)}"
    
    def aggressive_scan(self, ip: str) -> str:
        """
        Aggressive scan with OS detection, version detection, script scanning.
        
        Args:
            ip: IP address to scan
            
        Returns:
            Raw nmap output
        -A: Enables OS detection, version detection, script scanning, traceroute
        -T4: Timing template (faster/more aggressive)

        T0 = slowest (paranoid)
        T3 = default
        T5 = fastest (insane)
        """
        command = f"nmap -A -T4 {ip}"
        try:
            print(f"[INFO] Running aggressive scan on {ip}...")
            result = subprocess.run(
                ['nmap', '-A', '-T4', ip],
                capture_output=True,
                text=True,
                timeout=600
            )
            return result.stdout
            
        except subprocess.TimeoutExpired:
            return "[ERROR] Aggressive scan timed out"
        except Exception as e:
            return f"[ERROR] Aggressive scan failed: {str(e)}"
    
    def smb_enumeration_scan(self, ip: str) -> str:
        """
        SMB enumeration using nmap scripts.
        
        Args:
            ip: IP address to scan
            
        Returns:
            Raw nmap output
        """
        command = f"nmap -p 445,139 --script smb-os-discovery,smb-enum-shares {ip}"
        try:
            print(f"[INFO] Running SMB enumeration on {ip}...")
            result = subprocess.run(
                ['nmap', '-p', '445,139', '--script', 
                 'smb-os-discovery,smb-enum-shares', ip],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.stdout
            
        except subprocess.TimeoutExpired:
            return "[ERROR] SMB enumeration timed out"
        except Exception as e:
            return f"[ERROR] SMB enumeration failed: {str(e)}"
    
    def get_command_string(self, scan_type: str, ip: str) -> str:
        """
        Get the command string for a given scan type.
        
        Args:
            scan_type: Type of scan
            ip: Target IP
            
        Returns:
            Command string
        """
        commands = {
            'ping': f'nmap -sn {ip}',
            'tcp_quick': f'nmap -sV -F {ip}',
            'tcp_full': f'nmap -sV -sC -p- {ip}',
            'udp': f'nmap -sU --top-ports 20 {ip}',
            'os_detection': f'nmap -O {ip}',
            'aggressive': f'nmap -A -T4 {ip}',
            'smb': f'nmap -p 445,139 --script smb-os-discovery,smb-enum-shares {ip}'
        }
        return commands.get(scan_type, f'nmap {ip}')