; Inno Setup script for SSH Terminal Emulator built via PyInstaller
; Build the PyInstaller output first (dist\ssh-terminal\ssh-terminal.exe), then run this script in Inno Setup Compiler.

[Setup]
AppName=SSH Terminal Emulator
AppVersion=1.0.0
AppPublisher=SSH Terminal Emulator
DefaultDirName={pf64}\SSH Terminal Emulator
DefaultGroupName=SSH Terminal Emulator
OutputDir=dist\installer
OutputBaseFilename=ssh-terminal-setup
Compression=lzma
SolidCompression=yes
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64
DisableDirPage=yes
DisableProgramGroupPage=yes
PrivilegesRequired=admin
UninstallDisplayIcon={app}\ssh-terminal.exe
SetupLogging=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "dist\\ssh-terminal\\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\\SSH Terminal Emulator"; Filename: "{app}\\ssh-terminal.exe"
Name: "{commondesktop}\\SSH Terminal Emulator"; Filename: "{app}\\ssh-terminal.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\\ssh-terminal.exe"; Description: "Launch SSH Terminal Emulator"; Flags: nowait postinstall skipifsilent

