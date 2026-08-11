#!/usr/bin/env python3
"""Fix em-dash (—) that should be multiplication sign (×) in math contexts."""
import os, io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
CHAPTERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chapters')
MULTIPLY = '\u00D7'
EM_DASH = '\u2014'

# Chapters that have em-dash in number context
chapters = [22, 23, 27, 29, 30, 32]

total_fixed = 0
for ch in chapters:
    fname = 'chapter-%02d.html' % ch
    filepath = os.path.join(CHAPTERS_DIR, fname)
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    
    # Fix em-dash between digits (e.g., "2—2" → "2×2", "4—2" → "4×2")
    # But only if it's in a math context or multiplication context
    # Pattern: digit(s)—digit(s) or digit(s)—digit(s)=
    text = re.sub(r'(\d)—(\d)', r'\1' + MULTIPLY + r'\2', text)
    
    count = len(re.findall(r'(\d)—(\d)', original))
    
    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        total_fixed += count
        print('%s: fixed %d em-dash(es) → ×' % (fname, count))

print('\nTotal: %d em-dash fixes across %d files' % (total_fixed, len(chapters)))
