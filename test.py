"""
Test script to verify SSH Terminal Emulator is working correctly
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported"""
    print("[*] Testing module imports...")

    try:
        from ssh_terminal import SSHTerminal
        print("  [+] ssh_terminal module imported")
    except Exception as e:
        print(f"  [-] Failed to import ssh_terminal: {e}")
        return False

    try:
        from advanced_terminal import AdvancedSSHTerminal
        print("  [+] advanced_terminal module imported")
    except Exception as e:
        print(f"  [-] Failed to import advanced_terminal: {e}")
        return False

    try:
        from config import Config
        print("  [+] config module imported")
    except Exception as e:
        print(f"  [-] Failed to import config: {e}")
        return False

    return True


def test_dependencies():
    """Test that required packages are installed"""
    print("\n[*] Testing dependencies...")

    try:
        import paramiko
        print(f"  [+] paramiko {paramiko.__version__} installed")
    except ImportError:
        print("  [-] paramiko not installed: pip install paramiko")
        return False

    try:
        import cryptography
        print(f"  [+] cryptography {cryptography.__version__} installed")
    except ImportError:
        print("  [-] cryptography not installed: pip install cryptography")
        return False

    return True


def test_config():
    """Test configuration functionality"""
    print("\n[*] Testing configuration...")

    try:
        from config import Config
        keys = Config.get_available_keys()
        print(f"  [+] Config module working")
        if keys:
            print(f"  [+] Found {len(keys)} SSH key(s):")
            for key in keys:
                print(f"      - {key}")
        else:
            print("  [!] No SSH keys found (you can still use password auth)")
        return True
    except Exception as e:
        print(f"  [-] Config test failed: {e}")
        return False


def test_ssh_terminal():
    """Test SSHTerminal class instantiation"""
    print("\n[*] Testing SSHTerminal class...")

    try:
        from ssh_terminal import SSHTerminal
        terminal = SSHTerminal()
        print(f"  [+] SSHTerminal instantiated successfully")
        print(f"  [+] Connected: {terminal.connected}")
        return True
    except Exception as e:
        print(f"  [-] SSHTerminal test failed: {e}")
        return False


def test_advanced_terminal():
    """Test AdvancedSSHTerminal class instantiation"""
    print("\n[*] Testing AdvancedSSHTerminal class...")

    try:
        from advanced_terminal import AdvancedSSHTerminal
        terminal = AdvancedSSHTerminal()
        print(f"  [+] AdvancedSSHTerminal instantiated successfully")
        print(f"  [+] Connection history: {len(terminal.connection_history)} entries")
        return True
    except Exception as e:
        print(f"  [-] AdvancedSSHTerminal test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("SSH Terminal Emulator - System Test")
    print("=" * 60)

    results = []

    results.append(("Dependencies", test_dependencies()))
    results.append(("Module Imports", test_imports()))
    results.append(("Configuration", test_config()))
    results.append(("SSHTerminal Class", test_ssh_terminal()))
    results.append(("AdvancedSSHTerminal Class", test_advanced_terminal()))

    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    all_passed = True
    for test_name, result in results:
        status = "[✓] PASS" if result else "[✗] FAIL"
        print(f"{status} - {test_name}")
        if not result:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n[+] All tests passed! The application is ready to use.")
        print("\n[*] To start the SSH Terminal:")
        print("    Windows: run.bat or run.ps1")
        print("    Linux/Mac: python main_advanced.py")
        print("\n[*] For more info, see: QUICKSTART.md or README.md")
        return 0
    else:
        print("\n[-] Some tests failed. Please check the errors above.")
        print("[*] Try: pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())

