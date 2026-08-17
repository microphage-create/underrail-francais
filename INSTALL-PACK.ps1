# Install one language pack into Steam. Close the game first.
param(
  [string]$Pack = "francais",
  [string]$GameRoot = "C:\Program Files (x86)\Steam\steamapps\common\Underrail"
)
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "packs\$Pack"
if (-not (Test-Path $src)) { throw "Pack not found: $src" }
$loc = Join-Path $GameRoot "data\localization"
if (-not (Test-Path $loc)) { throw "Underrail localization folder not found: $loc" }
$dst = Join-Path $loc $Pack
Write-Host "Source: $src"
Write-Host "Dest:   $dst"
if (Test-Path $dst) {
  $bakRoot = Join-Path $PSScriptRoot "backups"
  New-Item -ItemType Directory -Force -Path $bakRoot | Out-Null
  $bak = Join-Path $bakRoot "$Pack.backup-$(Get-Date -Format yyyyMMdd-HHmmss)"
  Write-Host "Backup -> $bak"
  Copy-Item $dst $bak -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $dst | Out-Null
Copy-Item (Join-Path $src '*') $dst -Recurse -Force
$nested = Join-Path $dst $Pack
if (Test-Path $nested) {
  Remove-Item $nested -Recurse -Force
  Write-Host "Removed nested $Pack\$Pack"
}
$info = Join-Path $dst "info.txt"
Write-Host "OK. Options -> Language -> $((Get-Content $info -Raw).Trim())"
Write-Host "Quit the process, then relaunch."
