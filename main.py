"""
SSH Terminal Emulator - A Python-based terminal for connecting to remote servers via SSH
"""

import sys
import os
from ssh_terminal import SSHTerminal


def main():
    """Main entry point for the SSH Terminal Emulator"""
    terminal = SSHTerminal()
    terminal.run()


if __name__ == "__main__":
    main()

