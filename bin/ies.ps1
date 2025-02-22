
# Prompt user before executing the script
Write-Host "---------------------INITIALIZE ENGINE SETUP---------------------"
Write-Host "Auto Install necessary programs and configure your environment."
Write-Host ""
$confirmation = Read-Host "Do you want to continue? (Y/N)"
if ($confirmation -ne "Y" -and $confirmation -ne "y") {
    Write-Host "Operation cancelled."
    exit
}
Write-Host ""

# Function to check if a command exists
function Command-Exists {
    param ($command)
    $exists = Get-Command $command -ErrorAction SilentlyContinue
    return $exists -ne $null
}

# Install Scoop if not installed
if (-not (Command-Exists "scoop")) {
    Write-Host "Scoop not found. Installing Scoop..."
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
} else {
    Write-Host "Scoop is already installed."
}

# Ensure Scoop is in the PATH
$env:Path += ";$HOME\scoop\shims"

# Define required programs
$programs = @(
    @{name="Anaconda"; id="Anaconda.Anaconda3"; source="winget"},
    @{name="Windows Terminal"; id="Microsoft.WindowsTerminal"; source="winget"},
    @{name="Git"; id="Git.Git"; source="winget"},
    @{name="WinRAR"; id="RARLab.WinRAR"; source="winget"},
    @{name="Notepad++"; id="Notepad++.Notepad++"; source="winget"},
    @{name="Go"; id="GoLang.Go"; source="winget"},
    @{name="NodeJS"; id="NodeJS.NodeJS"; source="winget"},
    @{name="Neovim"; id="Neovim.Neovim"; source="scoop"},
    @{name="Pandoc"; id="Pandoc.Pandoc"; source="winget"},
    @{name="Power BI Desktop"; id="Microsoft.PowerBIDesktop"; source="winget"}
)

# Install programs via winget or scoop
foreach ($program in $programs) {
    $name = $program.name
    $id = $program.id
    $source = $program.source

    if ($source -eq "winget") {
        $installed = winget list --exact --id $id 2>$null
        if ($installed -match $id) {
            Write-Host "$name is already installed."
        } else {
            Write-Host "Installing $name..."
            winget install -e --id $id --silent
        }
    }
}

# Install Python packages if requirements.txt exists
$pythonrequirementsPath = Join-Path -Path $PSScriptRoot -ChildPath "..\config\ies_python_requirements.txt"
if (Test-Path $pythonrequirementsPath) {
    Write-Host "Installing Python packages from requirements.txt..."
    pip install -r ies_python_requirements.txt
} else {
    Write-Host "No requirements.txt found. Skipping Python package installation."
}

# Restore Windows Terminal settings if available
$terminalSettings = "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
$wtsettingsPath = Join-Path -Path $PSScriptRoot -ChildPath "..\config\ies_wt_settings.json"
if (Test-Path $wtsettingsPath) {
    Write-Host "Restoring Windows Terminal settings..."
    Copy-Item -Force $wtsettingsPath $terminalSettings
} else {
    Write-Host "No settings.json found. Skipping Windows Terminal configuration."
}

# Clone kickstart.nvim into AppData and rename folder
$nvimConfigPath = "$env:LOCALAPPDATA\nvim"
if (-not (Test-Path $nvimConfigPath)) {
    Write-Host "Cloning kickstart.nvim..."
    Set-Location $env:LOCALAPPDATA
    git clone https://github.com/nvim-lua/kickstart.nvim.git
    Rename-Item "kickstart.nvim" "nvim"
} else {
    Write-Host "Neovim config already exists at $nvimConfigPath. Skipping cloning."
}

Write-Host "Setup completed successfully!"
