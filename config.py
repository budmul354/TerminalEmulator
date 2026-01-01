"""
SSH Terminal Configuration Module
"""

import os
from pathlib import Path


class Config:
    """Configuration class for SSH Terminal Emulator"""

    # Application settings
    APP_NAME = "SSH Terminal Emulator"
    APP_VERSION = "1.0.0"

    # Default SSH settings
    DEFAULT_PORT = 22
    DEFAULT_TIMEOUT = 10
    KEEPALIVE_INTERVAL = 60  # seconds between keepalive pings
    KEEPALIVE_DURATION = 300  # seconds to keepalive when requested

    # SSH key locations
    SSH_KEY_PATHS = [
        os.path.expanduser("~/.ssh/id_rsa"),
        os.path.expanduser("~/.ssh/id_ed25519"),
        os.path.expanduser("~/.ssh/id_ecdsa"),
        os.path.expanduser("~/.ssh/id_dsa"),
    ]

    # Known hosts file
    KNOWN_HOSTS_FILE = os.path.expanduser("~/.ssh/known_hosts")

    # Connection history file
    HISTORY_FILE = os.path.expanduser("~/.ssh_terminal_history")

    @staticmethod
    def get_available_keys() -> list:
        """Get list of available SSH keys"""
        available = []
        for key_path in Config.SSH_KEY_PATHS:
            if os.path.exists(key_path):
                available.append(key_path)
        return available

    @staticmethod
    def ensure_ssh_dir():
        """Ensure SSH directory exists"""
        ssh_dir = os.path.expanduser("~/.ssh")
        if not os.path.exists(ssh_dir):
            os.makedirs(ssh_dir, mode=0o700)

