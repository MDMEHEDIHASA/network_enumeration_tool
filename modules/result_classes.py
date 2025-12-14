"""
Result Classes
Data classes to store enumeration results for each host.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Service:
    """Represents a network service."""
    port: int
    protocol: str
    service_name: str
    version: str = ""
    
    def __str__(self):
        if self.version:
            return f"{self.service_name} ({self.version}) on {self.port}/{self.protocol}"
        return f"{self.service_name} on {self.port}/{self.protocol}"


@dataclass
class HostResult:
    """Stores all enumeration results for a single host."""
    
    # Verified Information
    ip_address: str
    hostname: Optional[str] = None
    domain: Optional[str] = None
    os_type: str = "Unknown"
    is_alive: bool = False
    services: List[Service] = field(default_factory=list)
    
    # Windows-specific
    smb_info: Dict[str, str] = field(default_factory=dict)
    netbios_info: Dict[str, str] = field(default_factory=dict)
    ad_info: Dict[str, str] = field(default_factory=dict)
    
    # Unverified Information
    probable_os_version: Optional[str] = None
    potential_vulnerabilities: List[str] = field(default_factory=list)
    
    # Raw Command Outputs
    command_outputs: List[Dict[str, str]] = field(default_factory=list)
    
    def add_command_output(self, command: str, output: str):
        """Add a command and its output to the results."""
        self.command_outputs.append({
            'command': command,
            'output': output
        })
    
    def is_windows(self) -> bool:
        """Check if this host is running Windows."""
        return 'windows' in self.os_type.lower()
    
    def is_linux(self) -> bool:
        """Check if this host is running Linux."""
        return 'linux' in self.os_type.lower()