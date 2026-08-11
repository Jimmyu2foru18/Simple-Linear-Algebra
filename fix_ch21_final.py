#!/usr/bin/env python3
"""Comprehensive fix for Chapter 21 LaTeX formatting."""
import os, io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
filepath = os.path.join('chapters', 'chapter-21.html')

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 1: Standalone $\lambda$ that should be part of larger math expression
# Pattern: "$\lambda$ x" → "$\lambda x$"
text = re.sub(r'\$\(\\lambda\)\$\s*x\b', r'$\\lambda x$', text)
text = re.sub(r'\$\(\\lambda\)\$\s*\+\s*c', r'$\\lambda + c$', text)
text = re.sub(r'\$\(\\lambda\)\$\s*\+\s*\$\(\\alpha\)\$', r'$(\\lambda + \\alpha)$', text)
text = re.sub(r'\$\(\\alpha\)\$\s*x\b', r'$\\alpha x$', text)

# Fix "det(Q - $\lambda$ I)" → "$det(Q - \lambda I)$"
text = re.sub(r'det\(([^)]+)\s+\$\(\\lambda\)\$\s*I\)', r'$det(\1 - \lambda I)$', text)
text = re.sub(r'det\(([^)]+)\s+\$\(\\alpha\)\$\s*I\)', r'$det(\1 - \alpha I)$', text)
text = re.sub(r'det\(([^)]+)\s+\$\(\\lambda\)\$\)', r'$det(\1 - \lambda)$', text)

# Fix "|$\lambda$| =" → "$|\lambda| ="
text = re.sub(r'\|\$\(\\lambda\)\$\|\s*=\s*(\d)', r'$|\\lambda| = \1$', text)
text = re.sub(r'\|\$\(\\lambda\)\$\|', r'$|\\lambda$', text)

# Fix "eigenvalues $\lambda$ = i" → "eigenvalues $\lambda = i$"
text = re.sub(r'eigenvalue\$s?\$\s*=\s*i', r'eigenvalues $\lambda = i$', text)
text = re.sub(r'\$\(\\lambda\)\$\s*=\s*i\b', r'$\\lambda = i$', text)
text = re.sub(r'\$\(\\lambda\)\$\s*=\s*-i', r'$\\lambda = -i$', text)
text = re.sub(r'\$\(\\lambda\)\$\s*=\s*3', r'$\\lambda = 3$', text)
text = re.sub(r'\$\(\\lambda\)\$_{1}\s*=\s*3', r'$\\lambda_1 = 3$', text)
text = re.sub(r'\$\(\\lambda\)\$_{2}\s*=\s*3', r'$\\lambda_2 = 3$', text)
text = re.sub(r'\$\(\\lambda\)\$_{1}\s*=\s*i', r'$\\lambda_1 = i$', text)
text = re.sub(r'\$\(\\lambda\)\$_{2}\s*=\s*-i', r'$\\lambda_2 = -i$', text)

# Fix det(A - $\lambda$ I) patterns
text = re.sub(r'\(A\s*-\s*\$\(\\lambda\)\$\s*I\)x', r'$(A - \lambda I)x$', text)
text = re.sub(r'\(A\s*-\s*\$\(\\alpha\)\$\s*I\)', r'$(A - \alpha I)$', text)
text = re.sub(r'\(A\s*-\s*\$\(\\lambda\)\$\s*I\)', r'$(A - \lambda I)$', text)

# Fix "($\lambda$+$\alpha$)I" → "(\lambda+\alpha)I"
text = re.sub(r'\$(\$\(\\lambda\)\$+\$\(\\alpha\)\$\)I', r'$(\lambda+\alpha)I$', text)
# Fix broken: ($\\lambda$+$\\alpha$) → $(\lambda+\alpha)$
text = re.sub(r'\$(\\\$\(\\lambda\)\\\$\+\\\$\(\\alpha\)\\\$\)', r'$(\lambda+\alpha)$', text)
text = text.replace(r'($\lambda$+$\alpha$)', r'$(\lambda + \alpha)$')
text = text.replace(r'($\lambda$ + $alpha$)', r'$(\lambda + \alpha)$')

# Fix remaining $\alpha$ standalone outside larger expressions
text = re.sub(r'\$\(\\alpha\)\$\s*x\b', r'$\\alpha x$', text)
text = re.sub(r'\bequal to \$\(\\alpha\)\$\s*x\b', r'equal to $\\alpha x$', text)

# Fix "tr(A) = $\lambda_{1}$ + $\lambda_{2}$ + ... + $\lambda_{n}$"
text = re.sub(r'tr\(A\) = \$\(\\lambda\)\$_{\{1\}\}\s*\+\s*\$\(\\lambda\)\$_{\{2\}\}\s*\+\s*\.\.\.\s*\+\s*\$\(\\lambda\)\$_{\{n\}\}',
              r'$tr(A) = \lambda_1 + \lambda_2 + \ldots + \lambda_n$', text)
text = re.sub(r'det\(A\) = \$\(\\lambda\)\$_{\{1\}\}\s*\*\s*\$\(\\lambda\)\$_{\{2\}\}\s*\*\s*\.\.\.\s*\*\s*\$\(\\lambda\)\$_{\{n\}\}',
              r'$det(A) = \lambda_1 \cdot \lambda_2 \cdots \lambda_n$', text)

# Fix "eigenvalues at positions $\lambda_{1}$, $\lambda_{2}$"
text = re.sub(r'positions \$\(\\lambda\)\$_{\{1\}\},\s*\$\(\\lambda\)\$_{\{2\}\}',
              r'positions $\lambda_1, \lambda_2$', text)

# Fix "Eigenvalues: $\lambda_{1}$ = i, $\lambda_{2}$ = -i"
text = re.sub(r'Eigenvalues:\s*\$(\$\(\\lambda\)\$_{\{1\}\}\s*=\s*i,\s*\$\(\\lambda\)\$_{\{2\}\}\s*=\s*-i)',
              r'Eigenvalues: $\lambda_1 = i$, $\lambda_2 = -i$', text)
text = re.sub(r'eigenvalues \$\(\\lambda\)\$_{\{1\}\}\s*=\s*3,\s*\$\(\\lambda\)\$_{\{2\}\}\s*=\s*3',
              r'eigenvalues $\lambda_1 = 3$, $\lambda_2 = 3$', text)

# Fix "eigenvalue $\lambda$ = 3"
text = re.sub(r'eigenvalue \$\(\\lambda\)\$\s*=\s*3', r'eigenvalue $\lambda = 3$', text)
text = re.sub(r'For \$\(\\lambda\)\$\s*=\s*i:', r'For $\lambda = i$:', text)
text = re.sub(r'For \$\(\\lambda\)\$\s*=\s*-i:', r'For $\lambda = -i$:', text)

# Fix "eigenvalue $\lambda$ with eigenvector"
text = re.sub(r'eigenvalue \$\(\\lambda\)\$\s+with', r'eigenvalue $\lambda$ with', text)

# Fix "A + cI has eigenvalue $\lambda$ + c"
text = re.sub(r'has eigenvalue \$\(\\lambda\)\$\s*\+\s*c', r'has eigenvalue $\lambda + c$', text)

# Fix "eigenvalues $\lambda$ = i and $\lambda$ = -i"
text = re.sub(r'eigenvalues \$\(\\lambda\)\$\s*=\s*i\s+and\s+\$\(\\lambda\)\$\s*=\s*-i',
              r'eigenvalues $\lambda = i$ and $\lambda = -i$', text)

# Fix "$\lambda$^2" → "$\lambda^2$"
text = re.sub(r'\$\(\\lambda\)\$^{\d}', r'$\\lambda^{\1}$', text)

# Fix remaining alpha_j
text = re.sub(r'(?<!\\)\balpha_j\b', r'$\\alpha_j$', text)

# Fix matrix notation [[a, b], [c, d]] → \begin{bmatrix} a & b \\ c & d \end{bmatrix}
def fix_plain_matrix(m):
    content = m.group(1)
    rows = re.findall(r'\[([^\[\]]+)\]', content)
    if len(rows) >= 2:
        formatted = ' \\\\ '.join(
            ' & '.join(item.strip() for item in row.split(','))
            for row in rows
        )
        return '\\begin{bmatrix} ' + formatted + ' \\end{bmatrix}'
    return m.group(0)

text = re.sub(r'\[\[([^\[\]]+(?:\[[^\[\]]+\][^\[\]]*)*)\]\]', fix_plain_matrix, text)

# Fix "{\begin{bmatrix} 1 \\ 0 \end{bmatrix}^T}" → "\begin{bmatrix} 1 \\ 0 \end{bmatrix}^T"
text = re.sub(r'\{(\\-?\\begin\{bmatrix\}.*?\\end\{bmatrix\})\^T\}', r'\1^T', text)
text = re.sub(r'\{\\begin\{bmatrix\}', r'\\begin{bmatrix}', text)

# Fix extra spaces in bmatrix
text = re.sub(r'\\ \\  +', r' \\\\ ', text)
text = re.sub(r'\\\\  +', r' \\\\ ', text)
text = re.sub(r'\s+\\end\{bmatrix\}', r' \\end{bmatrix}', text)

# Fix "x = \begin{bmatrix} i \\ 1 \end{bmatrix}^T, or equivalently"
text = re.sub(r'x = \\begin\{bmatrix\} i \\ 1 \\end\{bmatrix\}\^T', 
              r'x = $\begin{bmatrix} i \\ 1 \end{bmatrix}^T$', text)

# Fix remaining [[0, 5, 0], [0, 0, 3], [0, 0, 0]] pattern
text = re.sub(r'det\(\[\[0, 5, 0\], \[0, 0, 3\], \[0, 0, 0\]\]\)x = 0',
              r'$det(\begin{bmatrix} 0 & 5 & 0 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{bmatrix})x = 0$', text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

# Verify
plain_lambda = len(re.findall(r'(?<!\\)\blambda\b', text))
plain_alpha = len(re.findall(r'(?<!\\)\balpha\b', text))
plain_matrix = text.count('[[')
print('Remaining plain lambda:', plain_lambda)
print('Remaining plain alpha:', plain_alpha)
print('Remaining [[ count:', plain_matrix)
