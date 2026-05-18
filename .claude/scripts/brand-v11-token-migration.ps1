#requires -Version 5.1
<#
Brand v1.0 -> v1.1 token migration across all .html files.

Replaces hardcoded legacy values with v1.1 equivalents:
  - Adds 'Fraunces' to every Google Fonts <link> URL (preserves Instrument Serif as fallback)
  - 'Instrument Serif'  -> 'Fraunces','Instrument Serif'  (font-family stacks)
  - #FAF8F4  -> #F5F0E8   (paper bg / on-dark cream)
  - #F6F2EA  -> #EEE7DA   (paper-tint surface)
  - #8E5F22  -> #9C6A2E   (accent-deep)

Skips: dist/, node_modules, .git/, anything under /assets/.
Preserves UTF-8 (no BOM) encoding.

Run from anywhere; it auto-locates the site root via $PSScriptRoot.
#>

$ErrorActionPreference = 'Stop'

$siteRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Write-Host "Site root: $siteRoot"
Write-Host ""

# Ordered replacement list. Order matters: more specific patterns first.
$replacements = @(
    # 1) Google Fonts URL — add Fraunces before Instrument Serif (handles both with/without Newsreader variants)
    @{
        find    = 'family=Instrument+Serif:ital@0;1&family=Inter+Tight'
        replace = 'family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;0,9..144,900;1,9..144,400&family=Instrument+Serif:ital@0;1&family=Inter+Tight'
        label   = 'fonts.googleapis: +Fraunces'
    },
    # 2) Inline font-family stacks: add Fraunces as primary, keep Instrument Serif as fallback
    @{
        find    = "'Instrument Serif',serif"
        replace = "'Fraunces','Instrument Serif',serif"
        label   = "font-family stack -> +Fraunces (serif fallback)"
    },
    @{
        find    = "'Instrument Serif'"
        replace = "'Fraunces','Instrument Serif'"
        label   = "font-family stack -> +Fraunces"
    },
    # 3) Color tokens (case-insensitive — match both #FAF8F4 and #faf8f4)
    @{
        find    = '#FAF8F4'
        replace = '#F5F0E8'
        label   = 'paper bg / on-dark cream'
        caseInsensitive = $true
    },
    @{
        find    = '#F6F2EA'
        replace = '#EEE7DA'
        label   = 'paper-tint surface'
        caseInsensitive = $true
    },
    @{
        find    = '#8E5F22'
        replace = '#9C6A2E'
        label   = 'accent-deep'
        caseInsensitive = $true
    }
)

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$files = Get-ChildItem -Path $siteRoot -Recurse -Filter *.html -File | Where-Object {
    $_.FullName -notmatch '\\dist\\' `
    -and $_.FullName -notmatch '\\\.git\\' `
    -and $_.FullName -notmatch '\\assets\\' `
    -and $_.FullName -notmatch '\\node_modules\\'
}

$totalFiles = 0
$totalReplacements = 0
$perPattern = @{}
foreach ($r in $replacements) { $perPattern[$r.label] = 0 }

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
    $original = $content
    $fileReplacements = 0

    foreach ($r in $replacements) {
        if ($r.caseInsensitive) {
            # Case-insensitive count + replace via regex
            $escaped = [regex]::Escape($r.find)
            $rx = New-Object System.Text.RegularExpressions.Regex($escaped, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
            $matches = $rx.Matches($content)
            if ($matches.Count -gt 0) {
                $content = $rx.Replace($content, $r.replace)
                $fileReplacements += $matches.Count
                $perPattern[$r.label] += $matches.Count
            }
        } else {
            # Literal string replace; count by length diff
            if ($content.Contains($r.find)) {
                $count = ($content.Length - $content.Replace($r.find, '').Length) / $r.find.Length
                $content = $content.Replace($r.find, $r.replace)
                $fileReplacements += [int]$count
                $perPattern[$r.label] += [int]$count
            }
        }
    }

    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
        $totalFiles++
        $totalReplacements += $fileReplacements
        $relPath = $file.FullName.Substring($siteRoot.Length + 1)
        Write-Host ("  {0,4} subs in  {1}" -f $fileReplacements, $relPath)
    }
}

Write-Host ""
Write-Host "============ Per-pattern totals ============"
foreach ($r in $replacements) {
    Write-Host ("  {0,5}  {1}" -f $perPattern[$r.label], $r.label)
}
Write-Host ""
Write-Host ("Done. Files modified: {0}, total substitutions: {1}" -f $totalFiles, $totalReplacements)
