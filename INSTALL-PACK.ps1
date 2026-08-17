# Copie le pack FR v2 vers l'install Steam. Jeu fermé. Admin parfois requis.
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "francais"
$dst = "C:\Program Files (x86)\Steam\steamapps\common\Underrail\data\localization\francais"
if (-not (Test-Path $src)) { throw "Pack introuvable: $src" }
if (-not (Test-Path (Split-Path $dst))) { throw "Install Underrail introuvable" }
Write-Host "Source: $src"
Write-Host "Dest:   $dst"
if (Test-Path $dst) {
  $bakRoot = Join-Path $PSScriptRoot "backups"
  New-Item -ItemType Directory -Force -Path $bakRoot | Out-Null
  $bak = Join-Path $bakRoot "francais.backup-$(Get-Date -Format yyyyMMdd-HHmmss)"
  Write-Host "Backup -> $bak"
  Copy-Item $dst $bak -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $dst | Out-Null
# Copier le *contenu* (évite dest\francais\francais)
Copy-Item (Join-Path $src '*') $dst -Recurse -Force
# Dossier niqué d'un vieil install
$nested = Join-Path $dst "francais"
if (Test-Path $nested) {
  Remove-Item $nested -Recurse -Force
  Write-Host "Supprime nest francais\francais"
}
Write-Host "OK. Options -> Language -> Francais. Quitter le process. Relancer."
Get-Content (Join-Path $dst "info.txt")
