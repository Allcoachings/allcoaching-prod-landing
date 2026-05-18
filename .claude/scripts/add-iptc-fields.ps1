#requires -Version 5.1
<#
Adds IPTC metadata fields (copyrightNotice, license, creditText, acquireLicensePage)
to every ImageObject in JSON-LD blocks across all HTML files under the site root.
Fixes Google Search Console "Image Metadata structured data" non-critical issues.

Uses JSON unicode escape © for the copyright symbol so the script file
encoding (PS 5.1 reads .ps1 as ANSI by default) cannot corrupt the output.
#>

$ErrorActionPreference = 'Stop'

# .claude/scripts -> .claude -> site root
$siteRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Write-Host "Site root: $siteRoot"

# JSON unicode escape for © to avoid PS5.1 ANSI-vs-UTF8 source encoding issues
$iptcFields = ',"copyrightNotice":"© 2026 AllCoaching Technologies Pvt. Ltd.","license":"https://allcoaching.in/terms","creditText":"AllCoaching","acquireLicensePage":"https://allcoaching.in/contact"'

function Add-IPTCFields {
    param([string]$content)

    $sb = New-Object System.Text.StringBuilder
    $pos = 0
    $needle = '"@type":"ImageObject"'
    $patched = 0

    while ($pos -lt $content.Length) {
        $idx = $content.IndexOf($needle, $pos)
        if ($idx -lt 0) {
            [void]$sb.Append($content.Substring($pos))
            break
        }

        $openBrace = $content.LastIndexOf('{', $idx)
        if ($openBrace -lt $pos) {
            [void]$sb.Append($content.Substring($pos, $idx + $needle.Length - $pos))
            $pos = $idx + $needle.Length
            continue
        }

        $depth = 0
        $i = $openBrace
        $inString = $false
        $escape = $false
        $closePos = -1

        while ($i -lt $content.Length) {
            $c = $content[$i]
            if ($escape) {
                $escape = $false
            } elseif ($c -eq '\') {
                $escape = $true
            } elseif ($c -eq '"') {
                $inString = -not $inString
            } elseif (-not $inString) {
                if ($c -eq '{') { $depth++ }
                elseif ($c -eq '}') {
                    $depth--
                    if ($depth -eq 0) { $closePos = $i; break }
                }
            }
            $i++
        }

        if ($closePos -lt 0) {
            [void]$sb.Append($content.Substring($pos))
            break
        }

        $objContent = $content.Substring($openBrace, $closePos - $openBrace + 1)

        [void]$sb.Append($content.Substring($pos, $closePos - $pos))
        if ($objContent -notmatch '"copyrightNotice"') {
            [void]$sb.Append($iptcFields)
            $patched++
        }
        [void]$sb.Append('}')
        $pos = $closePos + 1
    }

    return @{ Content = $sb.ToString(); Patched = $patched }
}

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$files = Get-ChildItem -Path $siteRoot -Recurse -Filter *.html -File | Where-Object { $_.FullName -notmatch '\\dist\\' }

$totalFiles = 0
$totalPatched = 0

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
    if ($content -notmatch '"@type":"ImageObject"') { continue }

    $result = Add-IPTCFields -content $content
    if ($result.Patched -gt 0) {
        [System.IO.File]::WriteAllText($file.FullName, $result.Content, $utf8NoBom)
        $totalFiles++
        $totalPatched += $result.Patched
        Write-Host ("Patched {0,2} ImageObject(s) in {1}" -f $result.Patched, $file.FullName.Substring($siteRoot.Length + 1))
    }
}

Write-Host ""
Write-Host ("Done. Files modified: {0}, ImageObjects patched: {1}" -f $totalFiles, $totalPatched)
