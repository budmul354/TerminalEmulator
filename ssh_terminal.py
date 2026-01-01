"""
SSH Terminal Module - Core SSH connection and terminal functionality
"""

import paramiko
import socket
import os
import sys
from typing import Optional, Tuple
import getpass
from datetime import datetime


class SSHTerminal:
    """SSH Terminal Emulator Class for connecting to remote servers"""

    def __init__(self):
        """Initialize the SSH Terminal"""
        self.ssh_client = None
        self.shell = None
        self.connected = False
        self.host = None
        self.username = None
        self.port = 22
        self.session = None
        self.known_hosts_file = os.path.expanduser("~/.ssh/known_hosts")

    def connect(self, host: str, username: str, password: Optional[str] = None,
                port: int = 22, key_file: Optional[str] = None) -> bool:
        """
        Connect to SSH server

        Args:
            host: Hostname or IP address
            username: Username for authentication
            password: Password for authentication (optional if using key)
            port: SSH port (default: 22)
            key_file: Path to private key file (optional)

        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.ssh_client = paramiko.SSHClient()

            # Set auto-add policy for unknown hosts
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Try to load known hosts
            try:
                self.ssh_client.load_system_host_keys()
            except Exception:
                pass

            print(f"[*] Connecting to {username}@{host}:{port}...")

            # Connect using key file if provided
            if key_file and os.path.exists(key_file):
                self.ssh_client.connect(
                    hostname=host,
                    username=username,
                    port=port,
                    key_filename=key_file,
                    look_for_keys=True,
                    allow_agent=True,
                    timeout=10
                )
                print(f"[+] Connected using key file: {key_file}")
            elif password:
                # Connect using password
                self.ssh_client.connect(
                    hostname=host,
                    username=username,
                    password=password,
                    port=port,
                    look_for_keys=False,
                    allow_agent=False,
                    timeout=10
                )
                print("[+] Connected using password authentication")
            else:
                # Try key-based authentication
                self.ssh_client.connect(
                    hostname=host,
                    username=username,
                    port=port,
                    look_for_keys=True,
                    allow_agent=True,
                    timeout=10
                )
                print("[+] Connected using key-based authentication")

            self.connected = True
            self.host = host
            self.username = username
            self.port = port

            return True

        except paramiko.AuthenticationException as e:
            print(f"[-] Authentication failed: {e}")
            return False
        except socket.timeout:
            print(f"[-] Connection timeout while connecting to {host}:{port}")
            return False
        except socket.error as e:
            print(f"[-] Socket error: {e}")
            return False
        except Exception as e:
            print(f"[-] Connection error: {e}")
            return False

    def disconnect(self):
        """Disconnect from SSH server"""
        if self.ssh_client:
            self.ssh_client.close()
            self.connected = False
            print("[*] Disconnected from server")

    def execute_command(self, command: str) -> Tuple[str, str, int]:
        """
        Execute a single command on the remote server

        Args:
            command: Command to execute

        Returns:
            Tuple of (stdout, stderr, return_code)
        """
        if not self.connected or not self.ssh_client:
            print("[-] Not connected to server")
            return "", "", 1

        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            out = stdout.read().decode('utf-8', errors='ignore')
            err = stderr.read().decode('utf-8', errors='ignore')
            return_code = stdout.channel.recv_exit_status()
            return out, err, return_code
        except Exception as e:
            print(f"[-] Error executing command: {e}")
            return "", str(e), 1

    def execute_interactive(self, command: str):
        """
        Execute command with interactive output (for better user experience)

        Args:
            command: Command to execute
        """
        if not self.connected or not self.ssh_client:
            print("[-] Not connected to server")
            return

        try:
            stdout, stderr, return_code = self.execute_command(command)

            if stdout:
                print(stdout, end='')
            if stderr:
                print(stderr, end='', file=sys.stderr)

        except Exception as e:
            print(f"[-] Error: {e}")

    def get_info(self) -> str:
        """Get connection information"""
        if self.connected:
            return f"{self.username}@{self.host}:{self.port}"
        return "Not connected"

    def print_welcome(self):
        """Print welcome banner"""
        print("\n" + "="*60)
        print("SSH Terminal Emulator")
        print("="*60)
        print("Type 'help' for available commands")
        print("Type 'exit' to disconnect and exit")
        print("="*60 + "\n")

    def print_help(self):
        """Print help information"""
        help_text = """
SSH Terminal Emulator - Help
========================================

Available Commands:
  help              - Show this help message
  connect           - Connect to a new SSH server
  disconnect        - Disconnect from current server
  status            - Show connection status
  clear             - Clear terminal screen
  exit              - Disconnect and exit
  
Any other command will be executed on the remote server.

Connection Format:
  When prompted, enter: hostname [username] [port]
  
Authentication Methods:
  1. SSH Keys (from ~/.ssh/)
  2. Password Authentication
  
Examples:
  ls -la              - List files on remote server
  cd /tmp && pwd      - Navigate and print working directory
  cat file.txt        - Display file contents
  whoami              - Show current remote user
  
========================================
"""
        print(help_text)

    def run(self):
        """Main interactive terminal loop"""
        self.print_welcome()

        while True:
            try:
                # Get prompt based on connection status
                if self.connected:
                    prompt = f"{self.username}@{self.host}$ "
                else:
                    prompt = "$ "

                # Get user input
                user_input = input(prompt).strip()

                if not user_input:
                    continue

                # Parse command
                command = user_input.lower()

                # Handle built-in commands
                if command == "help":
                    self.print_help()

                elif command == "connect":
                    self._handle_connect()

                elif command == "disconnect":
                    if self.connected:
                        self.disconnect()
                    else:
                        print("[-] Not connected to any server")

                elif command == "status":
                    if self.connected:
                        print(f"[+] Connected to: {self.get_info()}")
                    else:
                        print("[-] Not connected to any server")

                elif command == "clear":
                    os.system("cls" if os.name == "nt" else "clear")

                elif command == "exit":
                    if self.connected:
                        self.disconnect()
                    print("[*] Goodbye!")
                    sys.exit(0)

                else:
                    # Execute remote command if connected
                    if self.connected:
                        self.execute_interactive(user_input)
                    else:
                        print("[-] Not connected to server. Use 'connect' command first.")

            except KeyboardInterrupt:
                print("\n[*] Interrupted by user")
                if self.connected:
                    self.disconnect()
                sys.exit(0)
            except EOFError:
                print("\n[*] EOF reached")
                if self.connected:
                    self.disconnect()
                sys.exit(0)
            except Exception as e:
                print(f"[-] Error: {e}")

    def _handle_connect(self):
        """Handle the connect command flow"""
        print("\n--- SSH Connection ---")

        # Get connection details
        connection_str = input("Enter connection details (host [username] [port]): ").strip()

        if not connection_str:
            print("[-] Connection cancelled")
            return

        parts = connection_str.split()
        host = parts[0]
        username = parts[1] if len(parts) > 1 else getpass.getuser()
        port = int(parts[2]) if len(parts) > 2 else 22

        # Check for SSH key
        key_file = None
        default_keys = [
            os.path.expanduser("~/.ssh/id_rsa"),
            os.path.expanduser("~/.ssh/id_ed25519"),
            os.path.expanduser("~/.ssh/id_ecdsa"),
        ]

        for key in default_keys:
            if os.path.exists(key):
                key_file = key
                break

        # Try key-based auth first, then prompt for password
        if key_file:
            print(f"[*] Found SSH key: {key_file}")
            if self.connect(host, username, port=port, key_file=key_file):
                return
            print("[-] Key authentication failed, trying password...")

        # Prompt for password
        password = getpass.getpass(f"Password for {username}: ")

        if self.connect(host, username, password=password, port=port):
            return
        else:
            print("[-] Connection failed")

