@echo off
REM SSH Terminal Emulator - Windows Batch Launcher
REM This script activates the virtual environment and runs the SSH terminal

echo ========================================
echo SSH Terminal Emulator
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [-] Virtual environment not found!
    echo [*] Please run: python -m venv .venv
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if requirements are installed
.venv\Scripts\python -c "import paramiko" 2>nul
if %ERRORLEVEL% neq 0 (
    echo [*] Installing dependencies...
    .venv\Scripts\pip install -r requirements.txt
    echo.
)

REM Run the advanced terminal
echo [*] Starting SSH Terminal Emulator...
echo.
.venv\Scripts\python main_advanced.py

pause

