@echo off
REM Setup script for SSH Terminal Emulator

echo ========================================
echo SSH Terminal Emulator - Setup
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [-] Python is not installed or not in PATH!
    echo [*] Please install Python 3.7+ from https://www.python.org
    pause
    exit /b 1
)

echo [+] Python found:
python --version

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo [*] Creating virtual environment...
    python -m venv .venv
    if %ERRORLEVEL% neq 0 (
        echo [-] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [+] Virtual environment created
) else (
    echo [+] Virtual environment already exists
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Install requirements
echo [*] Installing dependencies...
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo [-] Failed to install dependencies
    pause
    exit /b 1
)

echo [+] Installation complete!
echo.
echo [*] To run the terminal:
echo    - Double-click run.bat (Advanced version with history)
echo    - Or: python main_advanced.py
echo.
echo [*] For simple version:
echo    - Double-click run_simple.bat
echo    - Or: python main.py
echo.

pause

