"""
Alternative main.py - Uses Advanced Terminal with history and config management
"""

import sys
import os
from advanced_terminal import AdvancedSSHTerminal


def main():
    """Main entry point for the Advanced SSH Terminal Emulator"""
    try:
        terminal = AdvancedSSHTerminal()

        terminal.run()
    except ImportError as e:
        print(f"[-] Import Error: {e}")
        print("[*] Please install required packages: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Fatal Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

