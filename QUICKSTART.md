# Quick Start Guide - SSH Terminal Emulator

## Windows Users

### Option 1: Quick Setup & Run (Recommended)
1. Double-click `setup.bat` - This will set up everything automatically
2. Double-click `run.bat` to start the terminal

### Option 2: Manual Setup
1. Open PowerShell or Command Prompt in this folder
2. Create virtual environment: `python -m venv .venv`
3. Activate it: `.venv\Scripts\activate.bat`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python main_advanced.py`

### Option 3: Simple Version
Just run `run_simple.bat` for the lightweight version without history

## Linux/Mac Users

1. Create virtual environment:
   ```bash
   python3 -m venv .venv
   ```

2. Activate it:
   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main_advanced.py
   ```

## First Time Usage

1. Start the application
2. Type `help` to see available commands
3. Type `connect` to establish SSH connection
4. When prompted, enter connection details:
   - `hostname` - required (e.g., example.com)
   - `username` - optional (defaults to current user)
   - `port` - optional (defaults to 22)
5. Authenticate with SSH key or password
6. Execute remote commands like: `ls`, `pwd`, `cat file.txt`, etc.
7. Type `exit` to disconnect and exit

## Example Workflow

```
$ connect
Enter connection details (host [username] [port]): example.com john 22
[*] Connecting to john@example.com:22...
[*] Found SSH key: ~/.ssh/id_rsa
[+] Connected using key-based authentication

john@example.com$ ls -la
total 48
drwxr-xr-x  5 john john 4096 Jan  1 12:00 .
drwxr-xr-x 14 root root 4096 Jan  1 11:00 ..
-rw-r--r--  1 john john  220 Jan  1 10:00 .bash_logout
...

john@example.com$ whoami
john

john@example.com$ exit
[*] Disconnected from server
[*] Goodbye!
```

## SSH Key Setup (Important!)

For key-based authentication to work, you need SSH keys:

### Generate new SSH key (if you don't have one):
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
# Or for older systems:
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```

### Add key to remote server:
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@hostname
```

### Key locations (automatically checked):
- `~/.ssh/id_rsa` (RSA)
- `~/.ssh/id_ed25519` (ED25519)
- `~/.ssh/id_ecdsa` (ECDSA)
- `~/.ssh/id_dsa` (DSA - legacy)

## Troubleshooting

### "ModuleNotFoundError: No module named 'paramiko'"
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

### "Permission denied (publickey)"
- Check SSH key permissions: `chmod 600 ~/.ssh/id_rsa`
- Verify key is on remote server: `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
- Try password authentication as fallback

### "Connection timeout"
- Check hostname/IP address is correct
- Verify server is reachable: `ping example.com`
- Check firewall allows SSH (port 22 or custom)

### "Connection refused"
- Verify SSH service is running on remote server
- Check custom SSH port if used

## Features Overview

### Basic Terminal (main.py / run_simple.bat)
- Connect to SSH servers
- Execute remote commands
- Simple, lightweight interface

### Advanced Terminal (main_advanced.py / run.bat)
- All basic features plus:
- Connection history tracking
- Quick-connect from history
- Persistent history between sessions
- Configuration management

## Security Tips

1. **Protect your SSH keys**
   - Set permissions: `chmod 600 ~/.ssh/id_rsa`
   - Never share private keys
   - Use key passphrases for extra security

2. **Use strong passwords** if using password authentication

3. **Verify server identity** when connecting to new servers

4. **Check connection history** - It's stored in `~/.ssh_terminal_history`

5. **Be cautious with commands** - Especially those with sudo or rm

## System Requirements

- Python 3.7 or higher
- Windows (tested), Linux, or macOS
- SSH access to target servers
- ~50MB disk space for dependencies

## File Structure

```
TerminalEmulator/
├── main.py                 # Basic terminal entry point
├── main_advanced.py        # Advanced terminal entry point
├── ssh_terminal.py         # Core SSH terminal class
├── advanced_terminal.py    # Extended features
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── run.bat               # Windows launcher (Advanced)
├── run_simple.bat        # Windows launcher (Simple)
├── setup.bat             # Windows setup script
├── QUICKSTART.md         # This file
└── README.md             # Full documentation
```

## Next Steps

1. Run the application
2. Connect to a test server
3. Try basic commands (ls, pwd, whoami, etc.)
4. Use `history` command (advanced version) to see saved connections
5. Refer to README.md for more detailed information

## Need Help?

- Type `help` in the terminal for command list
- Check README.md for detailed documentation
- Verify SSH key setup (see "SSH Key Setup" section above)
- Test SSH connection directly: `ssh user@hostname`

Happy terminal-ing! 🖥️

