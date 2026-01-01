# SSH Terminal Emulator - PowerShell Launcher

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "SSH Terminal Emulator" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path ".venv\Scripts\Activate.ps1")) {
    Write-Host "[-] Virtual environment not found!" -ForegroundColor Red
    Write-Host "[*] Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv

    if ($LASTEXITCODE -ne 0) {
        Write-Host "[-] Failed to create virtual environment" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Activate virtual environment
& .venv\Scripts\Activate.ps1

# Check if paramiko is installed
try {
    python -c "import paramiko" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Module not found"
    }
} catch {
    Write-Host "[*] Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host ""
}

# Run the advanced terminal
Write-Host "[*] Starting SSH Terminal Emulator..." -ForegroundColor Yellow
Write-Host ""

python main_advanced.py

Write-Host ""
Read-Host "Press Enter to exit"

