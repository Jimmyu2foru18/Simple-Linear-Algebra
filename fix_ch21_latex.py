#!/usr/bin/env python3
"""Fix plain-text 'lambda'/'alpha' and [[matrix]] notation in Chapter 21."""
import os, io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
filepath = os.path.join('chapters', 'chapter-21.html')

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Split on $$ delimiters
DD = '$$'
parts = text.split(DD)

# In odd-indexed parts (inside $$ blocks), fix plain lambda/alpha
# In even-indexed parts (outside $$ blocks), wrap lambda/alpha in $\...$
for i, part in enumerate(parts):
    if i % 2 == 1:
        # Inside $$ math block - replace bare lambda with \lambda
        part = re.sub(r'(?<!\\)\blambda\b', r'\\lambda', part)
        part = re.sub(r'(?<!\\)\balpha\b', r'\\alpha', part)
        # Fix |lambda| -> |\lambda|
        part = part.replace('|lambda|', '|\\lambda|')
        # Fix [1, -i]^T patterns - convert to bmatrix
        part = re.sub(r'\[([^\[\]]+)\]\^T', lambda m: 
            '\\begin{bmatrix} ' + m.group(1).replace(',', ' \\\\ ') + ' \\end{bmatrix}^T', part)
    else:
        # Outside $$ blocks - wrap lambda/alpha in $...$
        part = re.sub(r'(?<!\\)\blambda_(\w+)', r'$\\lambda_{\1}$', part)
        part = re.sub(r'(?<!\\)\blambda\b', r'$\\lambda$', part)
        part = re.sub(r'(?<!\\)\balpha\b', r'$\\alpha$', part)
        # Fix |lambda| outside math
        part = re.sub(r'\|lambda\|', r'$|\\lambda|$', part)
        # Fix [[a, b], [c, d]] -> \begin{bmatrix} a & b \\ c & d \end{bmatrix}
        def matrix_to_bmatrix(m):
            inner = m.group(1)
            rows = re.findall(r'\[([^\[\]]+)\]', inner)
            if len(rows) >= 2:
                formatted = ' \\\\ '.join(
                    ' & '.join(item.strip() for item in row.split(','))
                    for row in rows
                )
                return '\\begin{bmatrix} ' + formatted + ' \\end{bmatrix}'
            return m.group(0)
        part = re.sub(r'\[\[([^\]]+)\]\]', matrix_to_bmatrix, part)
        # Fix standalone [a, b]^T -> bmatrix
        part = re.sub(r'\[([^\[\]]+)\]\^T', lambda m:
            '\\begin{bmatrix} ' + m.group(1).replace(',', ' \\\\ ') + ' \\end{bmatrix}^T', part)

    parts[i] = part

text = DD.join(parts)

# Verify
plain_lambda = len(re.findall(r'(?<!\\)\blambda\b', text))
plain_alpha = len(re.findall(r'(?<!\\)\balpha\b', text))
print('Remaining plain lambda:', plain_lambda)
print('Remaining plain alpha:', plain_alpha)
print('Remaining [[ count:', text.count(' [['))

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
print('Chapter 21 fixed')
