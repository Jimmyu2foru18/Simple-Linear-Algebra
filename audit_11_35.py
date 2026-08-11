#!/usr/bin/env python3
"""Comprehensive audit of chapters 11-35 for encoding and LaTeX issues."""
import sys, io, os, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
CHAPTERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chapters')

# Known good mathematical Unicode characters
KNOWN_GOOD = {
    0x2014, 0x201C, 0x201D, 0x2192, 0x2260, 0x2208, 0x2209, 0x2713,
    0x00A0, 0x2212, 0x00D7, 0x2026, 0x2018, 0x2019, 0x2264, 0x2265,
    0x2200, 0x2203, 0x2211, 0x2295, 0x2299, 0x221E, 0x2550, 0x22A5,
    0x03BB, 0x039B, 0x221A, 0x21D2, 0x00B0, 0x00B7, 0x2081, 0x207B,
}

# Encoding corruption patterns to check
CORRUPTION_PATTERNS = [
    '\u00E2\u2030\u02C6',  # ≠ corrupted
    '\u00E2\u02C6\u02C6',   # ∈ corrupted
    '\u00E2\u02C6\u2030',   # ∉ corrupted
    '\u00E2\u0153\u201C',   # ✓ corrupted
    '\u00E2\u2020\u2019',   # → corrupted
    '\u00E2\u20AC\u201D',   # — corrupted
    '\u00CE\u00BB',         # λ corrupted
    '\u00CE\u203A',         # Λ corrupted
    '\u00E2\u02C6\u0161',   # √ corrupted
    '\u00E2\u02C6\u017E',   # ∞ corrupted
    '\u00E2\u2021\u2019',   # ⇒ corrupted
    '\u00C2\u00B0',         # ° corrupted
    '\u00C2\u00B7',         # · corrupted
    '\u00E2\u201A\u0081',   # ₁ corrupted
    '\u00E2\u0081\u00BB',   # ⁻ corrupted
    '\u00C2\u00A4',         # ¤ corrupted
    '\uFEFF',               # BOM
]

issues_found = []

for i in range(11, 36):
    fname = 'chapter-%02d.html' % i
    filepath = os.path.join(CHAPTERS_DIR, fname)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    chapter_issues = []
    
    # 1. Check encoding patterns
    if text.startswith('\ufeff'):
        chapter_issues.append('BOM')
    
    for pat in CORRUPTION_PATTERNS:
        c = text.count(pat)
        if c > 0:
            chapter_issues.append('encoding: %r x%d' % (pat[0], c))
    
    # Check stray U+00C3
    if '\u00C3' in text:
        chapter_issues.append('stray U+00C3 (Ã)')
    
    # Check stray U+00C2 before high chars
    idx = 0
    while True:
        idx = text.find('\u00C2', idx)
        if idx < 0:
            break
        if idx + 1 < len(text) and ord(text[idx + 1]) > 127:
            chapter_issues.append('stray U+00C2 before U+%04X' % ord(text[idx + 1]))
        idx += 1
    
    # 2. Check $$ balance
    test_text = text.replace("displayMath: [['$$', '$$'],", "")
    dollar_count = test_text.count('$$')
    if dollar_count % 2 != 0:
        chapter_issues.append('unbalanced $$ (count=%d)' % dollar_count)
    
    # 3. Check for stray single $ inside $$ blocks
    for m in re.finditer(r'\$\$(.*?)\$\$', test_text, re.DOTALL):
        content = m.group(1)
        lines_with_dollar = [l.strip() for l in content.split('\n')
                           if '$' in l and '$$' not in l and l.strip()]
        if lines_with_dollar:
            chapter_issues.append('stray $ in $$ block: %r' % lines_with_dollar[0][:40])
    
    # 4. Check mu-deletion (word boundary)
    mu_patterns = [
        (r'\bltiply\b', 'multiply'),
        (r'\bltiplying\b', 'multiplying'),
        (r'\bltiple\b', 'multiple'),
        (r'\bltiplication\b', 'multiplication'),
        (r'\bltiplications\b', 'multiplications'),
        (r'\bltiplied\b', 'multiplied'),
        (r'\bForla\b', 'Formula'),
        (r'\bforla\b', 'formula'),
        (r'\bPertation\b', 'Permutation'),
        (r'\bpertation\b', 'permutation'),
        (r'\bComte\b', 'Commute'),
        (r'\bcomte\b', 'commute'),
        (r'\bComtativity\b', 'Commutativity'),
        (r'\bcomtativity\b', 'commutativity'),
        (r'\baximum\b', 'maximum'),
    ]
    for pat, correct in mu_patterns:
        matches = re.findall(pat, text)
        if matches:
            chapter_issues.append('mu-deletion: %s -> %s' % (matches[0], correct))
    
    # 5. Check 'st be/have'
    if re.search(r'\bst be\b|\bst have\b|\bst obey\b', text):
        chapter_issues.append('st be/have/obe')
    
    # 6. Check for backslash N typo (\Nullspace)
    if '\\Nullspace' in text:
        chapter_issues.append('\\Nullspace typo')
    
    if chapter_issues:
        issues_found.append((fname, chapter_issues))
        print('%s: %s' % (fname, chapter_issues[:5]))

if not issues_found:
    print('ALL 25 CHAPTERS (11-35) ARE CLEAN - no encoding, LaTeX, or mu-deletion issues found')
else:
    print('\n%d chapters have issues' % len(issues_found))
