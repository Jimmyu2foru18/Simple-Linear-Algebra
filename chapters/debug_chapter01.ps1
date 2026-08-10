$mapping = @(
  @("J7DzL2_Na80","csgNflj69-Y","rGWcIeCdwGg","XkY2DOUCWMU"),
  @("QVKj3LADCnA","T2Gtt8WygiU","zIeHOGhWEtc","P5GJJ02OG08"),
  @("FX4C-JpTFgY","P5GJJ02OG08","3xR9zTx9y74","kWorj5BBy9k"),
  @("5hO3MrzPa0A","T2Gtt8WygiU","zIeHOGhWEtc","P5GJJ02OG08"),
  @("JibVXBElKL0","EP2ghkO0lSk","pXp3nQ5exms","Zd7wCsUM4pg"),
  @("8o5Cmfpeo6g","uQhTuRlWMxw","4nLq5VDS4ok","EP2ghkO0lSk"),
  @("VqP2tREMvt0","9kDpbZCK62Y","4nLq5VDS4ok","T2Gtt8WygiU"),
  @("9Q1q7s1jTzU","zIeHOGhWEtc","T2Gtt8WygiU","P5GJJ02OG08"),
  @("yjBerM5jWsc","9kDpbZCK62Y","4C9GKyfUQkc","L-vWPl7mAjI"),
  @("nHlE7EgJFds","uQhTuRlWMxw","4nLq5VDS4ok","k7RM-ot2NWY"),
  @("2IdtqGM6KWU","EP2ghkO0lSk","L-vWPl7mAjI","9kDpbZCK62Y"),
  @("6-wh6yvk6uc","T2Gtt8WygiU","zIeHOGhWEtc","P5GJJ02OG08"),
  @("l88D4r74gtM","csgNflj69-Y","rGWcIeCdwGg","T2Gtt8WygiU"),
  @("YzZUIYRCE38","6nqMegdbxik","vL4Qp4EoJS8","uQhTuRlWMxw"),
  @("Y_Ac6KiQ1t0","6nqMegdbxik","vL4Qp4EoJS8","uQhTuRlWMxw"),
  @("osh80YCg_GM","uQhTuRlWMxw","zIeHOGhWEtc","T2Gtt8WygiU"),
  @("uNsCkP9mgRk","zHbfZWZJTGc","P4VBYJo8BnY","6nqMegdbxik"),
  @("srjxexLishgY","CcbyMH3Noow","FzGF-7pIoic","k7RM-ot2NWY"),
  @("23LLB9mNJvc","CcbyMH3Noow","FzGF-7pIoic","k7RM-ot2NWY"),
  @("QNpj-gOXW9M","kWorj5BBy9k","uNHRUXh4uH4","3xR9zTx9y74"),
  @("lXNXrLcoerU","TQvxWaXnrqI","M-e2_GS9Ekg","PFDu9oVAE-g"),
  @("13r9QY6cmjc","WTLl03D4TNA","CW9g9XI5pxw","kYB8IZa5AuE"),
  @("IZqwi0wJovM","WTLl03D4TNA","Zd7wCsUM4pg","kYB8IZa5AuE"),
  @("8MF3pz-oYHo","is1cg5yhdds","AP-1ukgcG-s","T2Gtt8WygiU"),
  @("sFxA8eIS6tA","csgNflj69-Y","rGWcIeCdwGg","T2Gtt8WygiU"),
  @("umt6BB1nJ4w","DUuTx2nbizM","vL4Qp4EoJS8","6nqMegdbxik"),
  @("M0Sa8fLOajA","DUuTx2nbizM","Zd7wCsUM4pg","is1cg5yhdds"),
  @("vF7eyJ2g3kU","DUuTx2nbizM","vL4Qp4EoJS8","6nqMegdbxik"),
  @("z_zYQHmrh08","WTLl03D4TNA","CW9g9XI5pxw","kYB8IZa5AuE"),
  @("Nx0lRBaXoz4","J9pyaNyM7vE","zHbfZWZJTGc","P4VBYJo8BnY"),
  @("Ts3o2I8_Mxc","is1cg5yhdds","Zd7wCsUM4pg","kYB8IZa5AuE"),
  @("vGkn-3NFGck","HZa1RwFHgwU","kYB8IZa5AuE","P2LTAUO1TdA"),
  @("HgC1l_6ySkc","HZa1RwFHgwU","kYB8IZa5AuE","P2LTAUO1TdA"),
  @("Go2aLo7ZOlU","uNHRUXh4uH4","kWorj5BBy9k","kYB8IZa5AuE"),
  @("RWvi4Vx4CDc","csgNflj69-Y","rGWcIeCdwGg","XkY2DOUCWMU")
)

$sourceNames = @("Prof Dave Explains", "Dr. Valerie Hower", "3Blue1Brown")

$chapterNum = 1
$file = "chapter-{0:D2}.html" -f $chapterNum
$content = Get-Content $file -Raw
$urls = $mapping[$chapterNum - 1]
Write-Output "urls count: $($urls.Count)"
Write-Output "urls[0]: $($urls[0])"
Write-Output "urls[3]: $($urls[3])"

$h2Match = [regex]::Match($content, '<h2>Chapter\s+\d+:\s*(.*?)</h2>')
$lectureTitle = ""
if ($h2Match.Success) { $lectureTitle = $h2Match.Groups[1].Value }
Write-Output "lectureTitle: $lectureTitle"

$pattern = '(<iframe\b[^>]*?>)'
$parts = [regex]::Split($content, $pattern, 'Singleline')
Write-Output "parts count: $($parts.Count)"

for ($i = 1; $i -lt $parts.Count; $i += 2) {
  $idx = [int]($i / 2)
  Write-Output "i=$i idx=$idx"
  $tag = $parts[$i]
  $newSrc = $urls[$idx]
  Write-Output "newSrc: $newSrc"
  $titleMatch = [regex]::Match($tag, 'title="([^"]*)"')
  $currentTitle = $titleMatch.Groups[1].Value
  if ($idx -eq 0) {
    if ($lectureTitle) {
      $newTitle = "$chapterNum. $lectureTitle$([char]0x2014) Gilbert Strang"
    } else {
      $newTitle = $currentTitle
    }
  } else {
    $topic = $currentTitle
    if ($currentTitle -match ' — ') {
      $topic = $currentTitle.Substring($currentTitle.IndexOf(' — ') + 3)
    } elseif ($currentTitle -match ' - ') {
      $topic = $currentTitle.Substring($currentTitle.IndexOf(' - ') + 3)
    }
    $newTitle = "$($sourceNames[$idx-1])$([char]0x2014) $topic"
  }
  Write-Output "newTitle: $newTitle"
  $newTag = $tag -replace 'src="[^"]*"', "src=`"https://www.youtube.com/embed/$newSrc`"" -replace 'title="[^"]*"', "title=`"$newTitle`""
  $parts[$i] = $newTag
}

$newContent = [string]::Join('', $parts)
Set-Content -LiteralPath $file -Value $newContent -Encoding UTF8
Write-Output "Updated $file"
