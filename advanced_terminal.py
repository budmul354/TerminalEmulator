"""
Advanced SSH Terminal with Session Management
This module provides enhanced SSH terminal functionality with connection history
and configuration management.
"""

from ssh_terminal import SSHTerminal
from config import Config
import json
import os
from datetime import datetime


class AdvancedSSHTerminal(SSHTerminal):
    """Extended SSH Terminal with session management"""

    def __init__(self):
        """Initialize the Advanced SSH Terminal"""
        super().__init__()
        Config.ensure_ssh_dir()
        self.connection_history = self.load_history()

    def load_history(self) -> list:
        """Load connection history from file"""
        if os.path.exists(Config.HISTORY_FILE):
            try:
                with open(Config.HISTORY_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_history(self):
        """Save connection history to file"""
        try:
            with open(Config.HISTORY_FILE, 'w') as f:
                json.dump(self.connection_history, f, indent=2)
        except Exception as e:
            print(f"[-] Failed to save history: {e}")

    def add_to_history(self, host: str, username: str, port: int):
        """Add connection to history"""
        entry = {
            "host": host,
            "username": username,
            "port": port,
            "timestamp": datetime.now().isoformat()
        }

        # Remove duplicate if exists
        self.connection_history = [
            h for h in self.connection_history
            if not (h["host"] == host and h["username"] == username and h["port"] == port)
        ]

        # Add new entry at the beginning
        self.connection_history.insert(0, entry)

        # Keep only last 20 connections
        self.connection_history = self.connection_history[:20]

        self.save_history()

    def print_history(self):
        """Print connection history"""
        if not self.connection_history:
            print("[-] No connection history")
            return

        print("\n--- Connection History ---")
        for i, entry in enumerate(self.connection_history, 1):
            host = entry.get("host")
            username = entry.get("username")
            port = entry.get("port")
            print(f"{i}. {username}@{host}:{port}")
        print()

    def _handle_connect(self):
        """Enhanced connect command with history support"""
        print("\n--- SSH Connection ---")
        print("Options:")
        print("  1. Enter new connection details")
        print("  2. Use connection from history")
        print("  3. Cancel")

        choice = input("Select option (1-3): ").strip()

        if choice == "1":
            super()._handle_connect()
            if self.connected:
                self.add_to_history(self.host, self.username, self.port)
        elif choice == "2":
            self.print_history()
            history_choice = input("Enter connection number (or press Enter to cancel): ").strip()
            if history_choice.isdigit():
                idx = int(history_choice) - 1
                if 0 <= idx < len(self.connection_history):
                    entry = self.connection_history[idx]
                    host = entry["host"]
                    username = entry["username"]
                    port = entry["port"]

                    # Try key auth first
                    key_file = None
                    for key in Config.get_available_keys():
                        if os.path.exists(key):
                            key_file = key
                            break

                    if key_file:
                        if self.connect(host, username, port=port, key_file=key_file):
                            self.add_to_history(host, username, port)
                            return

                    # Try password auth
                    import getpass
                    password = getpass.getpass(f"Password for {username}: ")
                    if self.connect(host, username, password=password, port=port):
                        self.add_to_history(host, username, port)
                    else:
                        print("[-] Connection failed")
                else:
                    print("[-] Invalid selection")
            else:
                print("[-] Cancelled")
        else:
            print("[-] Cancelled")

    def print_help(self):
        """Extended help information"""
        help_text = """
SSH Terminal Emulator - Help
========================================

Available Commands:
  help              - Show this help message
  connect           - Connect to a new SSH server
  disconnect        - Disconnect from current server
  status            - Show connection status
  history           - Show connection history
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
        """Main interactive terminal loop with history support"""
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

                elif command == "history":
                    self.print_history()

                elif command == "status":
                    if self.connected:
                        print(f"[+] Connected to: {self.get_info()}")
                    else:
                        print("[-] Not connected to any server")

                elif command == "clear":
                    import os
                    os.system("cls" if os.name == "nt" else "clear")

                elif command == "exit":
                    if self.connected:
                        self.disconnect()
                    print("[*] Goodbye!")
                    import sys
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
                import sys
                sys.exit(0)
            except EOFError:
                print("\n[*] EOF reached")
                if self.connected:
                    self.disconnect()
                import sys
                sys.exit(0)
            except Exception as e:
                print(f"[-] Error: {e}")

