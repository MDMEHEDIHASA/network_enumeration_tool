"""
Nmap Parser Module
Parses nmap output and extracts relevant information using regex.
"""

import re
from typing import List, Optional, Dict
from modules.result_classes import Service, HostResult


class NmapParser:
    """Parses nmap scan output to extract information."""
    
    @staticmethod
    def parse_hostname(nmap_output: str) -> Optional[str]:
        """
        Extract hostname from nmap output.
        
        Args:
            nmap_output: Raw nmap output
            
        Returns:
            Hostname if found, None otherwise
        """
        # Pattern: Nmap scan report for hostname (ip)
        pattern = r'Nmap scan report for ([a-zA-Z0-9\.\-]+) \('
        match = re.search(pattern, nmap_output)
        if match:
            return match.group(1)
        return None
    
    @staticmethod
    def parse_os_type(nmap_output: str) -> str:
        """
        Extract OS type from nmap output.
        
        Args:
            nmap_output: Raw nmap output
            
        Returns:
            OS type string (Windows/Linux/Unix/Unknown)
        """
        output_lower = nmap_output.lower()
        
        # Check for Windows indicators
        windows_indicators = [
            'microsoft windows',
            'windows server',
            'windows 10',
            'windows 7',
            'windows 8',
            'smb',
            'microsoft-ds'
        ]
        
        for indicator in windows_indicators:
            if indicator in output_lower:
                return "Windows"
        
        # Check for Linux indicators
        linux_indicators = [
            'linux',
            'ubuntu',
            'debian',
            'centos',
            'red hat',
            'fedora'
        ]
        
        for indicator in linux_indicators:
            if indicator in output_lower:
                return "Linux"
        
        # Check for Unix indicators
        unix_indicators = [
            'unix',
            'bsd',
            'solaris',
            'aix'
        ]
        
        for indicator in unix_indicators:
            if indicator in output_lower:
                return "Unix"
        
        return "Unknown"
    
    @staticmethod
    def parse_os_version(nmap_output: str) -> Optional[str]:
        """
        Extract probable OS version from nmap output.
        
        Args:
            nmap_output: Raw nmap output
            
        Returns:
            OS version string if found
        """
        # Look for OS details line
        pattern = r'OS details: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            return match.group(1).strip()
        
        # Look for OS CPE line
        pattern = r'OS CPE: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            return match.group(1).strip()
        
        return None
    
    @staticmethod
    def parse_services(nmap_output: str) -> List[Service]:
        """
        Extract services from nmap output.
        
        Args:
            nmap_output: Raw nmap output
            
        Returns:
            List of Service objects
        """
        services = []
        
        # Pattern: PORT     STATE SERVICE     VERSION
        # Example: 22/tcp   open  ssh         OpenSSH 7.4 (protocol 2.0)
        pattern = r'(\d+)/(tcp|udp)\s+open\s+(\S+)(?:\s+(.+?))?(?:\n|$)'
        
        matches = re.finditer(pattern, nmap_output)
        
        for match in matches:
            port = int(match.group(1))
            protocol = match.group(2)
            service_name = match.group(3)
            version = match.group(4).strip() if match.group(4) else ""
            
            service = Service(
                port=port,
                protocol=protocol,
                service_name=service_name,
                version=version
            )
            services.append(service)
        
        return services
    
    @staticmethod
    def parse_smb_info(nmap_output: str) -> Dict[str, str]:
        """
        Extract SMB information from nmap output.
        
        Args:
            nmap_output: Raw nmap output
            
        Returns:
            Dictionary of SMB information
        """
        smb_info = {}
        
        # Extract OS version
        pattern = r'OS: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            smb_info['os'] = match.group(1).strip()
        
        # Extract Computer name
        pattern = r'Computer name: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            smb_info['computer_name'] = match.group(1).strip()
        
        # Extract NetBIOS computer name
        pattern = r'NetBIOS computer name: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            smb_info['netbios_name'] = match.group(1).strip()
        
        # Extract Domain name
        pattern = r'Domain name: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            smb_info['domain'] = match.group(1).strip()
        
        # Extract Forest name
        pattern = r'Forest name: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            smb_info['forest'] = match.group(1).strip()
        
        # Extract FQDN
        pattern = r'FQDN: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            smb_info['fqdn'] = match.group(1).strip()
        
        # Extract Workgroup
        pattern = r'Workgroup: (.+?)(?:\n|$)'
        match = re.search(pattern, nmap_output)
        if match:
            smb_info['workgroup'] = match.group(1).strip()
        
        return smb_info
    
    @staticmethod
    def detect_vulnerabilities(nmap_output: str) -> List[str]:
        """
        Detect potential vulnerabilities from service versions.
        
        Args:
            nmap_output: Raw nmap output
            
        Returns:
            List of potential vulnerability descriptions
        """
        vulnerabilities = []
        
        output_lower = nmap_output.lower()
        
        # Check for outdated SSH versions
        if 'openssh 5' in output_lower or 'openssh 6' in output_lower:
            vulnerabilities.append("Outdated OpenSSH version detected - may be vulnerable to known exploits")
        
        # Check for SMBv1
        if 'smbv1' in output_lower or 'smb 1.0' in output_lower:
            vulnerabilities.append("SMBv1 is enabled - vulnerable to EternalBlue (MS17-010)")
        
        # Check for old Windows versions
        if 'windows xp' in output_lower or 'windows 2003' in output_lower:
            vulnerabilities.append("Unsupported Windows version - no security updates available")
        
        # Check for anonymous FTP
        if 'ftp' in output_lower and 'anonymous' in output_lower:
            vulnerabilities.append("Anonymous FTP access may be enabled")
        
        # Check for Telnet
        if re.search(r'23/tcp\s+open\s+telnet', nmap_output, re.IGNORECASE):
            vulnerabilities.append("Telnet service detected - unencrypted protocol")
        
        return vulnerabilities
    
    @staticmethod
    def parse_to_host_result(ip: str, nmap_outputs: Dict[str, str]) -> HostResult:
        """
        Parse all nmap outputs and create a HostResult object.
        
        Args:
            ip: Target IP address
            nmap_outputs: Dictionary of scan_type -> output
            
        Returns:
            HostResult object with parsed information
        """
        result = HostResult(ip_address=ip)
        
        # Combine all outputs for parsing
        combined_output = "\n".join(nmap_outputs.values())
        
        # Parse basic information
        result.hostname = NmapParser.parse_hostname(combined_output)
        result.os_type = NmapParser.parse_os_type(combined_output)
        result.probable_os_version = NmapParser.parse_os_version(combined_output)
        result.services = NmapParser.parse_services(combined_output)
        result.potential_vulnerabilities = NmapParser.detect_vulnerabilities(combined_output)
        
        # Parse SMB info if available
        if 'smb' in nmap_outputs:
            result.smb_info = NmapParser.parse_smb_info(nmap_outputs['smb'])
            if 'domain' in result.smb_info:
                result.domain = result.smb_info['domain']
        
        # Check if host is alive
        result.is_alive = 'Host is up' in combined_output
        
        return result