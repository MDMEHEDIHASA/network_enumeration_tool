"""
Target Parser Module
Handles parsing of target specifications including IPs, DNS names, CIDR ranges,
and comma-separated combinations.
"""

import ipaddress
import socket
import re
from typing import List, Set


class TargetParser:
    """Parses and validates target specifications."""
    
    def __init__(self):
        self.targets: Set[str] = set()
        self.exclusions: Set[str] = set()
    
    def parse_targets(self, target_string: str) -> Set[str]:
        """
        Parse target string into set of IP addresses.
        
        Args:
            target_string: Comma-separated list of IPs, DNS names, or CIDR ranges
            
        Returns:
            Set of IP addresses as strings
        """
        if not target_string:
            return set()
        
        # Split by comma and strip whitespace
        target_list = [t.strip() for t in target_string.split(',')]
        ip_set = set()
        
        for target in target_list:
            if not target:
                continue
                
            # Check if it's a CIDR range
            if '/' in target:
                ip_set.update(self._parse_cidr(target))
            # Check if it's an IP address
            elif self._is_valid_ip(target):
                ip_set.add(target)
            # Assume it's a DNS name
            else:
                resolved_ip = self._resolve_dns(target)
                if resolved_ip:
                    ip_set.add(resolved_ip)
        
        return ip_set
    
    def _parse_cidr(self, cidr: str) -> Set[str]:
        """
        Parse CIDR notation into individual IP addresses.
        
        Args:
            cidr: CIDR notation (e.g., 192.168.1.0/24)
            
        Returns:
            Set of IP addresses
        """
        try:
            network = ipaddress.ip_network(cidr, strict=False)
            return {str(ip) for ip in network.hosts()}
        except ValueError as e:
            print(f"[ERROR] Invalid CIDR notation '{cidr}': {e}")
            return set()
    
    def _is_valid_ip(self, ip_string: str) -> bool:
        """
        Check if string is a valid IPv4 address.
        
        Args:
            ip_string: String to validate
            
        Returns:
            True if valid IPv4, False otherwise
        """
        try:
            ipaddress.IPv4Address(ip_string)
            return True
        except ValueError:
            return False
    
    def _resolve_dns(self, hostname: str) -> str:
        """
        Resolve DNS hostname to IP address.
        
        Args:
            hostname: DNS hostname to resolve
            
        Returns:
            Resolved IP address or None if resolution fails
        """
        try:
            ip = socket.gethostbyname(hostname)
            print(f"[INFO] Resolved {hostname} to {ip}")
            return ip
        except socket.gaierror as e:
            print(f"[ERROR] Could not resolve DNS name '{hostname}': {e}")
            return None
    
    def set_targets(self, target_string: str):
        """Set the targets to scan."""
        self.targets = self.parse_targets(target_string)
    
    def set_exclusions(self, exclusion_string: str):
        """Set the hosts to exclude from scanning."""
        self.exclusions = self.parse_targets(exclusion_string)
    
    def get_final_targets(self) -> List[str]:
        """
        Get final list of targets after applying exclusions.
        
        Returns:
            Sorted list of IP addresses to scan
        """
        final = self.targets - self.exclusions
        return sorted(final, key=lambda ip: ipaddress.IPv4Address(ip))
    
    def contains_dns_names(self, target_string: str) -> bool:
        """
        Check if target string contains any DNS names.
        
        Args:
            target_string: Target specification string
            
        Returns:
            True if DNS names are present
        """
        if not target_string:
            return False
            
        targets = [t.strip() for t in target_string.split(',')]
        
        for target in targets:
            # Skip if it's CIDR or valid IP
            if '/' in target or self._is_valid_ip(target):
                continue
            # If it's not IP or CIDR, it's likely a DNS name
            if target:
                return True
        
        return False