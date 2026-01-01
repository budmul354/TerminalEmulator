# SSH Terminal Emulator - Installation & Usage Guide

## ✅ What Has Been Created

A complete Python SSH Terminal Emulator application with the following components:

### Core Application Files (5 files)
1. **main.py** - Entry point for basic terminal
2. **ssh_terminal.py** - Core SSH connectivity and terminal logic
3. **main_advanced.py** - Entry point for advanced terminal with history
4. **advanced_terminal.py** - Extended terminal with connection history
5. **config.py** - Configuration and settings management

### Documentation Files (4 files)
1. **README.md** - Complete feature documentation
2. **QUICKSTART.md** - Quick start guide for new users
3. **PROJECT_INFO.md** - Detailed project information
4. **INSTALLATION.md** - This file

### Configuration & Dependencies
1. **requirements.txt** - Python package dependencies
   - paramiko >= 3.0.0 (SSH library)
   - cryptography >= 41.0.0 (Cryptographic functions)

### Windows Launch Scripts (4 files)
1. **run.bat** - Launch advanced terminal (recommended)
2. **run_simple.bat** - Launch basic terminal
3. **run.ps1** - PowerShell launcher with better output
4. **setup.bat** - One-time setup script

### Testing & Verification
1. **test.py** - Comprehensive system verification script

**Total: 17 files created**

## 🚀 Installation Instructions

### Prerequisites
- Python 3.7 or higher
- Windows 7+, Linux, or macOS
- ~100MB free disk space

### Windows - Option 1: Automatic Setup (Recommended)

This is the easiest method for Windows users:

```batch
1. Navigate to the TerminalEmulator folder
2. Double-click: setup.bat
3. Follow the prompts
4. After setup completes, run: run.bat
```

**What setup.bat does:**
- ✓ Checks Python installation
- ✓ Creates virtual environment (.venv)
- ✓ Installs all dependencies from requirements.txt
- ✓ Verifies installation

### Windows - Option 2: Manual Command Line Setup

If you prefer manual control:

```powershell
# Open PowerShell or Command Prompt in the TerminalEmulator folder

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Verify installation
python test.py

# Run the application
python main_advanced.py
```

### Windows - Option 3: PowerShell Setup

```powershell
# Run as PowerShell script
.\run.ps1
```

### Linux/macOS Setup

```bash
# Navigate to TerminalEmulator directory
cd TerminalEmulator

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python test.py

# Run the application
python main_advanced.py
```

## ✅ Verification

After installation, verify everything is working:

### Windows
```batch
python test.py
```

### Linux/macOS
```bash
python test.py
```

**Expected Output:**
```
============================================================
Test Results Summary
============================================================
[✓] PASS - Dependencies
[✓] PASS - Module Imports
[✓] PASS - Configuration
[✓] PASS - SSHTerminal Class
[✓] PASS - AdvancedSSHTerminal Class
============================================================

[+] All tests passed! The application is ready to use.
```

## 🎯 Quick Start (After Installation)

### Windows Users - Easiest Method
```
1. Double-click: run.bat
2. Type: connect
3. Enter hostname (e.g., example.com)
4. Authenticate (key or password)
5. Run commands like: ls, pwd, whoami
6. Type: exit
```

### Linux/macOS Users
```bash
python main_advanced.py

# Then:
$ connect
$ # Enter hostname
$ # Authenticate
$ ls -la
$ exit
```

## 🔐 SSH Setup (One-Time)

To use SSH key authentication (recommended):

### Generate SSH Key (if you don't have one)

**Windows (PowerShell):**
```powershell
ssh-keygen -t ed25519 -C "your-email@example.com"
# Press Enter to accept default location: ~/.ssh/id_ed25519
# Enter passphrase (recommended) or leave empty
```

**Linux/macOS:**
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
# Press Enter for defaults
# Enter passphrase or leave empty
```

### Copy Key to Server

**Windows (PowerShell):**
```powershell
ssh-copy-id -i $env:USERPROFILE\.ssh\id_ed25519.pub user@hostname
# Enter password when prompted
```

**Linux/macOS:**
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@hostname
# Enter password when prompted
```

### Verify Key Works

```bash
ssh user@hostname
# Should connect without password
exit
```

## 📁 Directory Structure After Installation

```
TerminalEmulator/
├── .venv/                      # Virtual environment (created by setup)
│   ├── Scripts/               # Windows scripts
│   ├── lib/                   # Python packages
│   └── ...
├── __pycache__/               # Python cache (auto-created)
├── Main Application
│   ├── main.py               # ← Simple terminal
│   ├── main_advanced.py      # ← Advanced terminal (recommended)
│   ├── ssh_terminal.py       # ← Core SSH code
│   ├── advanced_terminal.py  # ← Extended features
│   └── config.py             # ← Configuration
├── Launch Scripts
│   ├── run.bat              # ← Windows Advanced (use this)
│   ├── run.ps1              # ← PowerShell version
│   ├── run_simple.bat       # ← Windows Simple
│   └── setup.bat            # ← Setup script
├── Documentation
│   ├── README.md            # ← Full documentation
│   ├── QUICKSTART.md        # ← Quick start
│   ├── PROJECT_INFO.md      # ← Project details
│   └── INSTALLATION.md      # ← This file
├── Configuration
│   ├── requirements.txt     # ← Dependencies (installed in .venv)
│   └── .ssh/               # ← SSH keys (if configured)
└── Testing
    └── test.py             # ← Verification script
```

## 🔧 Using the Application

### Command Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `help` | Show help | `help` |
| `connect` | Connect to server | `connect` |
| `disconnect` | Close connection | `disconnect` |
| `status` | Show connection info | `status` |
| `history` | Show saved connections | `history` |
| `clear` | Clear screen | `clear` |
| `exit` | Exit application | `exit` |

### Basic Workflow

```
$ help                          # See available commands
$ connect                       # Start new connection
Enter hostname: example.com     # Enter server
Enter username: john            # Enter username (optional)
[+] Connected                   # Successfully connected!

john@example.com$ ls -la        # Execute remote command
total 48
drwxr-xr-x 5 john john ...

john@example.com$ pwd           # Another command
/home/john

john@example.com$ exit          # Disconnect and quit
[*] Goodbye!
```

### Advanced Features (History)

```
$ connect
Options:
  1. Enter new connection details
  2. Use connection from history
  3. Cancel

Select option (1-3): 2          # Use history
1. john@example.com:22
2. admin@server.local:2222

Enter connection number: 1      # Quick reconnect!
[+] Connected to: john@example.com:22
```

## 🐛 Troubleshooting

### Python Not Found
```
'python' is not recognized as an internal or external command
```
**Solution:**
- Install Python from https://www.python.org
- Add Python to PATH during installation
- Verify: Open new terminal and type `python --version`

### Virtual Environment Issues
```
Cannot activate virtual environment
```
**Solution:**
```batch
# Delete and recreate
rmdir /s .venv
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Dependency Installation Fails
```
ERROR: Could not install packages
```
**Solution:**
```batch
pip install --upgrade pip
pip install -r requirements.txt
```

### SSH Connection Fails
```
[-] Connection refused
```
**Solutions:**
1. Verify SSH server is running: `telnet hostname 22`
2. Check firewall allows port 22
3. Verify hostname/IP is correct
4. Check server status with: `ssh -v user@hostname`

### Authentication Failed
```
[-] Authentication failed
```
**Solutions:**
1. Verify username is correct
2. Check SSH key permissions: `chmod 600 ~/.ssh/id_*`
3. Verify key is on server
4. Try password authentication
5. Check server allows your user

### Key Authentication Not Working
```
[-] Key authentication failed
```
**Solutions:**
1. Generate key: `ssh-keygen -t ed25519 -C "email@example.com"`
2. Copy to server: `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host`
3. Verify: `ssh -v user@host`
4. Check server SSH config allows keys

## 📊 System Requirements

### Minimum
- Python 3.7
- 100MB disk space
- Internet connection (to install packages)

### Recommended
- Python 3.9+
- 200MB disk space
- Fast internet (for first installation)
- SSH keys configured on target servers

### Supported Operating Systems
- ✅ Windows 7, 8, 10, 11
- ✅ Linux (Ubuntu, CentOS, Debian, etc.)
- ✅ macOS 10.14+

## 🔒 Security Recommendations

1. **SSH Keys**
   - Use ED25519 keys (most secure)
   - Set permissions: `chmod 600 ~/.ssh/id_*`
   - Use passphrases for extra security

2. **Passwords**
   - Use strong passwords
   - Never use production passwords for testing
   - Don't share SSH credentials

3. **Connection History**
   - Located in `~/.ssh_terminal_history`
   - Only contains host, username, port
   - Review periodically

4. **General**
   - Keep Python updated
   - Keep SSH keys secure
   - Use firewall rules appropriately

## 📝 Configuration Files

### SSH Keys (Auto-detected)
Location: `~/.ssh/`

Supported formats:
- id_rsa (RSA 2048/4096)
- id_ed25519 (ED25519) - **Recommended**
- id_ecdsa (ECDSA)
- id_dsa (DSA - legacy)

### Connection History (Advanced Terminal)
Location: `~/.ssh_terminal_history`

Format: JSON with structure:
```json
[
  {
    "host": "example.com",
    "username": "john",
    "port": 22,
    "timestamp": "2026-01-01T12:00:00.000000"
  }
]
```

### Application Config
File: `config.py`

Customizable settings:
- DEFAULT_PORT (default: 22)
- DEFAULT_TIMEOUT (default: 10 seconds)
- SSH_KEY_PATHS (auto-discovered)

## 🎓 Features Included

### Basic Terminal (main.py)
- ✓ SSH connections
- ✓ Key/password authentication
- ✓ Remote command execution
- ✓ Connection status
- ✓ Basic commands (help, connect, disconnect, etc.)

### Advanced Terminal (main_advanced.py)
All of the above, plus:
- ✓ Connection history (saves last 20 connections)
- ✓ Quick-connect from history
- ✓ Persistent history between sessions
- ✓ Enhanced configuration

## 💾 Backing Up Your Configuration

To preserve your SSH keys and history:

```bash
# Backup SSH directory
cp -r ~/.ssh ~/ssh_backup

# Backup history (Advanced Terminal)
cp ~/.ssh_terminal_history ~/ssh_terminal_history_backup
```

## 🔄 Updating/Reinstalling

If you need to reinstall or update:

```batch
# Windows
.venv\Scripts\activate.bat
pip install --upgrade -r requirements.txt
python test.py
```

```bash
# Linux/macOS
source .venv/bin/activate
pip install --upgrade -r requirements.txt
python test.py
```

## 📞 Getting Help

### Built-in Help
```
$ help          # Show commands
$ connect       # Interactive guide
```

### Documentation
- **README.md** - Complete feature guide
- **QUICKSTART.md** - Quick start examples
- **PROJECT_INFO.md** - Technical details
- **test.py** - System diagnostics

### Testing System
```
python test.py
```

Shows:
- Python dependencies status
- Module imports status
- SSH key availability
- Configuration status

## ✨ Next Steps

1. **Install** - Run `setup.bat` (Windows) or follow Linux/macOS instructions
2. **Verify** - Run `python test.py`
3. **Generate SSH Key** - If you don't have one
4. **Configure Server** - Copy your SSH public key to server
5. **Launch** - Run `run.bat` (Windows) or `python main_advanced.py`
6. **Connect** - Type `connect` and follow prompts
7. **Execute** - Run remote commands like `ls`, `pwd`, etc.

## 🎉 You're Ready!

Your SSH Terminal Emulator is fully installed and ready to use!

**To start:**
- **Windows:** Double-click `run.bat`
- **Linux/macOS:** Run `python main_advanced.py`

For detailed usage, see **README.md** or **QUICKSTART.md**

Happy terminal-ing! 🖥️

---

**Version:** 1.0.0  
**Status:** Production Ready ✅  
**Last Updated:** January 1, 2026

