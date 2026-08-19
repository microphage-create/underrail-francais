# Patch Underrail floating combat / skill bubbles EN -> FR (personal use).
# Same UTF-16LE slot rules as patch-custom-difficulty-fr.ps1. FR must be <= EN length.
param(
  [string]$ExePath = "C:\Program Files (x86)\Steam\steamapps\common\Underrail\underrail.exe",
  [string]$BackupDir = "C:\Users\Marcel\Documents\Underrail-FR\backups",
  [switch]$WhatIf
)
$ErrorActionPreference = 'Stop'
$e = [char]233   # e-acute lowercase
$E = [char]201   # E-acute uppercase

$replacements = @(
  @{ En = 'Success'; Fr = ('R' + $e + 'ussi') }                         # pickpocket bubble (7)
  @{ En = 'You have been caught pickpocketing!'; Fr = 'Pris la main dans le sac !' } # 35 -> 26
  @{ En = 'Success!'; Fr = ('R' + $e + 'ussi !') }                      # fishing (8)
  @{ En = 'It got away!'; Fr = ('Il a fil' + $e + ' !') }               # fishing 12 -> 11
  @{ En = 'Failure'; Fr = ($E + 'chec !') }                             # 7 -> 6
  @{ En = 'Dodged!'; Fr = ('Esquiv' + $e) }                             # 7
  @{ En = ' Critical Hit!'; Fr = ' Coup critique' }                     # 14 including leading space
  @{ En = 'Blocked! ({0})'; Fr = ('Bloqu' + $e + '!({0})') }            # 14 -> 13
  @{ En = 'Immune'; Fr = ('Immun' + $e) }                               # 6
  @{ En = 'Resists'; Fr = ('R' + $e + 'siste') }                        # 7
  @{ En = 'Locking successful.'; Fr = 'Verrouillage OK.' }              # 19 -> 17
  @{ En = 'Lock disabled successfully.'; Fr = ('Serrure d' + $e + 'sactiv' + $e + 'e.') } # 27 -> 20
  @{ En = 'Unlocked.'; Fr = 'Ouvert.' }                                 # 9 -> 7
)

function Find-Utf16([byte[]]$bytes, [string]$text) {
  $needle = [Text.Encoding]::Unicode.GetBytes($text)
  $hits = [System.Collections.Generic.List[int]]::new()
  $limit = $bytes.Length - $needle.Length
  for ($i = 0; $i -le $limit; $i++) {
    $ok = $true
    for ($j = 0; $j -lt $needle.Length; $j++) {
      if ($bytes[$i + $j] -ne $needle[$j]) { $ok = $false; break }
    }
    if ($ok) {
      if ($i -ge 1) {
        $lenByte = $bytes[$i - 1]
        $expected = $text.Length * 2 + 1
        if ($lenByte -eq $expected) {
          $flagOff = $i + $text.Length * 2
          if ($flagOff -lt $bytes.Length -and $bytes[$flagOff] -eq 0) {
            $hits.Add($i)
          }
        }
      }
      $i += $needle.Length - 1
    }
  }
  return $hits
}

function Write-Utf16Slot([byte[]]$bytes, [int]$contentOff, [string]$en, [string]$fr) {
  if ($fr.Length -gt $en.Length) {
    throw "FR longer than EN slot: '$fr' ($($fr.Length)) > '$en' ($($en.Length))"
  }
  $lenOff = $contentOff - 1
  $oldLen = $bytes[$lenOff]
  $expectedOld = $en.Length * 2 + 1
  if ($oldLen -ne $expectedOld) {
    throw "Length prefix mismatch at $lenOff for '$en': got $oldLen expected $expectedOld"
  }
  for ($k = 0; $k -lt $oldLen; $k++) { $bytes[$contentOff + $k] = 0 }
  $newPayload = [Text.Encoding]::Unicode.GetBytes($fr)
  [Array]::Copy($newPayload, 0, $bytes, $contentOff, $newPayload.Length)
  $bytes[$contentOff + $newPayload.Length] = 0
  $bytes[$lenOff] = [byte]($fr.Length * 2 + 1)
}

if (-not (Test-Path -LiteralPath $ExePath)) { throw "Exe not found: $ExePath" }

try {
  $fsTest = [IO.File]::Open($ExePath, 'Open', 'ReadWrite', 'None')
  $fsTest.Close()
} catch {
  throw "Cannot open exe for write (quit Underrail completely first). $_"
}

New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$bak = Join-Path $BackupDir "underrail.exe.bak-floaters-$stamp"
Copy-Item -LiteralPath $ExePath -Destination $bak -Force
Write-Host "backup $bak"

$bytes = [IO.File]::ReadAllBytes($ExePath)
$nOk = 0
foreach ($r in $replacements) {
  $hits = Find-Utf16 $bytes $r.En
  if ($hits.Count -eq 0) {
    Write-Host "MISS  '$($r.En)' (already patched?)"
    continue
  }
  if ($hits.Count -gt 3) {
    Write-Host "SKIP  '$($r.En)' too many hits ($($hits.Count)), not unique enough"
    continue
  }
  foreach ($h in $hits) {
    if (-not $WhatIf) {
      Write-Utf16Slot $bytes $h $r.En $r.Fr
    }
    Write-Host "OK    '$($r.En)' -> '$($r.Fr)' @$h"
    $nOk++
  }
}

if (-not $WhatIf) {
  [IO.File]::WriteAllBytes($ExePath, $bytes)
}
Write-Host "patched $nOk slots. Steam verify restores EN."
