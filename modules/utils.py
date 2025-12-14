"""
Utility Functions
Common helper functions used across the project.
"""

import socket
from datetime import datetime, timezone


def get_current_dns_server() -> str:
    """
    Get the currently configured DNS server.
    
    Returns:
        DNS server address as string
    """
    try:
        # This is a simplified approach - reads from /etc/resolv.conf on Linux
        with open('/etc/resolv.conf', 'r') as f:
            for line in f:
                if line.startswith('nameserver'):
                    return line.split()[1]
    except:
        pass
    
    # Fallback: return system default
    return "System Default DNS"


def prompt_dns_confirmation() -> bool:
    """
    Prompt user for DNS confirmation.
    
    Returns:
        True if user confirms, False otherwise
    """
    dns_server = get_current_dns_server()
    print(f"\n[WARNING] DNS names detected in targets.")
    print(f"[INFO] Current DNS server: {dns_server}")
    print(f"[PROMPT] This will resolve DNS names using the above server.")
    
    response = input("Do you want to proceed? (y/N): ").strip().lower()
    
    if response == 'y' or response == 'yes':
        return True
    
    print("[INFO] Scan cancelled by user.")
    return False


def get_utc_timestamp() -> str:
    """
    Get current UTC timestamp in format: YYYYMMDD_HHMM
    
    Returns:
        Formatted timestamp string
    """
    now = datetime.now(timezone.utc)
    return now.strftime("%Y%m%d_%H%M")


def get_default_output_filename() -> str:
    """
    Generate default output filename with UTC timestamp.
    
    Returns:
        Default filename string
    """
    timestamp = get_utc_timestamp()
    return f"host_enumeration_report_{timestamp}_UTC.md"