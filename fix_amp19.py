#!/usr/bin/env python3
"""Fix &amp; inside LaTeX math delimiters ($$) in Chapter 19."""
import os, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
filepath = os.path.join('chapters', 'chapter-19.html')

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

DD = '$$'
parts = text.split(DD)
for i in range(1, len(parts), 2):
    parts[i] = parts[i].replace('&amp;', '&')
text = DD.join(parts)

remaining = text.count('&amp;')
print('Remaining &amp;:', remaining)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed &amp; -> & in all $$ math blocks')
