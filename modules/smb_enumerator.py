"""
SMB Enumerator Module
Handles Windows-specific enumeration including SMB, NetBIOS, and AD information.
"""

import subprocess
from typing import Dict, Optional


class SMBEnumerator:
    """Handles Windows-specific enumeration."""
    
    @staticmethod
    def enum4linux_scan(ip: str) -> Optional[str]:
        """
        Run enum4linux against Windows host.
        
        Args:
            ip: IP address of Windows host
            
        Returns:
            Raw enum4linux output or None if tool not available
        """
        try:
            print(f"[INFO] Running enum4linux on {ip}...")
            result = subprocess.run(
                ['enum4linux', '-a', ip],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.stdout
        except FileNotFoundError:
            print("[WARNING] enum4linux not found - skipping")
            return None
        except subprocess.TimeoutExpired:
            return "[ERROR] enum4linux timed out"
        except Exception as e:
            return f"[ERROR] enum4linux failed: {str(e)}"
    
    @staticmethod
    def smbclient_list_shares(ip: str) -> Optional[str]:
        """
        List SMB shares using smbclient.
        
        Args:
            ip: IP address of Windows host
            
        Returns:
            Raw smbclient output or None if tool not available
        """
        try:
            print(f"[INFO] Listing SMB shares on {ip}...")
            result = subprocess.run(
                ['smbclient', '-L', f'//{ip}', '-N'],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout
        except FileNotFoundError:
            print("[WARNING] smbclient not found - skipping")
            return None
        except subprocess.TimeoutExpired:
            return "[ERROR] smbclient timed out"
        except Exception as e:
            return f"[ERROR] smbclient failed: {str(e)}"
    
    @staticmethod
    def nmblookup_scan(ip: str) -> Optional[str]:
        """
        NetBIOS lookup using nmblookup.
        
        Args:
            ip: IP address of Windows host
            
        Returns:
            Raw nmblookup output or None if tool not available
        """
        try:
            print(f"[INFO] Running NetBIOS lookup on {ip}...")
            result = subprocess.run(
                ['nmblookup', '-A', ip],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout
        except FileNotFoundError:
            print("[WARNING] nmblookup not found - skipping")
            return None
        except subprocess.TimeoutExpired:
            return "[ERROR] nmblookup timed out"
        except Exception as e:
            return f"[ERROR] nmblookup failed: {str(e)}"
    
    @staticmethod
    def rpcclient_enumeration(ip: str) -> Optional[str]:
        """
        RPC enumeration using rpcclient.
        
        Args:
            ip: IP address of Windows host
            
        Returns:
            Raw rpcclient output or None if tool not available
        """
        try:
            print(f"[INFO] Running RPC enumeration on {ip}...")
            # Try to enumerate users
            result = subprocess.run(
                ['rpcclient', '-U', '', '-N', ip, '-c', 'enumdomusers'],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout
        except FileNotFoundError:
            print("[WARNING] rpcclient not found - skipping")
            return None
        except subprocess.TimeoutExpired:
            return "[ERROR] rpcclient timed out"
        except Exception as e:
            return f"[ERROR] rpcclient failed: {str(e)}"
    
    @staticmethod
    def run_all_windows_enumeration(ip: str) -> Dict[str, str]:
        """
        Run all Windows enumeration tools.
        
        Args:
            ip: IP address of Windows host
            
        Returns:
            Dictionary of tool_name -> output
        """
        results = {}
        
        enum4linux_output = SMBEnumerator.enum4linux_scan(ip)
        if enum4linux_output:
            results['enum4linux'] = enum4linux_output
        
        smbclient_output = SMBEnumerator.smbclient_list_shares(ip)
        if smbclient_output:
            results['smbclient'] = smbclient_output
        
        nmblookup_output = SMBEnumerator.nmblookup_scan(ip)
        if nmblookup_output:
            results['nmblookup'] = nmblookup_output
        
        rpcclient_output = SMBEnumerator.rpcclient_enumeration(ip)
        if rpcclient_output:
            results['rpcclient'] = rpcclient_output
        
        return results