#requires -Version 5.1
<#
Renames user-visible "essay/essays" to "guide/guides" across the site while
preserving:
  - CSS class names like .essay-link, essay-grid       (followed by "-")
  - URL fragments / id refs like #essays, "essays"     (preceded by # ' / _ . -)
  - HTML id="essays"                                   (id="..." kept stable)

Case is preserved: Essays -> Guides, ESSAYS -> GUIDES, essay -> guide.
#>

$ErrorActionPreference = 'Stop'

$siteRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Write-Host "Site root: $siteRoot"

$pattern = "(?<![.\#\-_/'])\bEssay(s?)\b(?!-)"
$opts    = [System.Text.RegularExpressions.RegexOptions]::IgnoreCase
$rx      = New-Object System.Text.RegularExpressions.Regex($pattern, $opts)

$callback = {
    param($m)
    $orig = $m.Value
    $hasS = $m.Groups[1].Length -gt 0
    if ($orig -ceq $orig.ToUpper()) {
        if ($hasS) { return 'GUIDES' } else { return 'GUIDE' }
    } elseif ([char]::IsUpper($orig[0])) {
        if ($hasS) { return 'Guides' } else { return 'Guide' }
    } else {
        if ($hasS) { return 'guides' } else { return 'guide' }
    }
}

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$files = Get-ChildItem -Path $siteRoot -Recurse -Filter *.html -File | Where-Object {
    $_.FullName -notmatch '\\dist\\' -and $_.FullName -notmatch '\\\.git\\'
}

$totalFiles = 0
$totalReplacements = 0

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
    $matches = $rx.Matches($content)
    if ($matches.Count -eq 0) { continue }

    $new = $rx.Replace($content, $callback)
    if ($new -ne $content) {
        [System.IO.File]::WriteAllText($file.FullName, $new, $utf8NoBom)
        $totalFiles++
        $totalReplacements += $matches.Count
        Write-Host ("Updated {0,3} occurrences in {1}" -f $matches.Count, $file.FullName.Substring($siteRoot.Length + 1))
    }
}

Write-Host ""
Write-Host ("Done. Files modified: {0}, occurrences replaced: {1}" -f $totalFiles, $totalReplacements)
