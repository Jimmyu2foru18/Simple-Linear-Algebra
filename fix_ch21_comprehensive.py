#!/usr/bin/env python3
"""Comprehensive fix for Chapter 21: lambda/alpha, matrix notation, math expressions."""
import os, io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
filepath = os.path.join('chapters', 'chapter-21.html')

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix patterns: $\lambda$ followed by non-math text that should be inside the math block
# Pattern 1: $\lambda$ x → $\lambda x$
text = re.sub(r'\$\(\\lambda\)\$\s*x', r'$\\lambda x$', text)

# Pattern 2: $\lambda$^2 → $\lambda^2$
text = re.sub(r'\$\(\\lambda"\)\$^{\d}', r'$\\lambda^{\1}$', text)  # won't match
# Actually let me handle this differently
text = text.replace('$\\lambda$ x', '$\\lambda x$')
text = text.replace('$\\lambda$^2', '$\\lambda^2$')
text = text.replace('$\\lambda$ = i', '$\\lambda = i$')
text = text.replace('$\\lambda$ = -i', '$\\lambda = -i$')
text = text.replace('$\\lambda$ = 3', '$\\lambda = 3$')

# Pattern 3: ($\lambda$ + c) → $(\lambda + c)$
text = text.replace('($\\lambda$ + c)', r'$(\lambda + c)$')
text = text.replace('($\\lambda$+$\\alpha$)', r'$(\lambda + \alpha)$')

# Pattern 4: $\lambda_{i}$ → $\lambda_i$
text = text.replace('$\\lambda_{1}$', r'$\\lambda_1$')
text = text.replace('$\\lambda_{2}$', r'$\\lambda_2$')
text = text.replace('$\\lambda_{n}$', r'$\\lambda_n$')
text = text.replace('$\\lambda_{i}$', r'$\\lambda_i$')

# Pattern 5: Fix sum expressions
text = text.replace("tr(A) = $\\lambda_1$ + $\\lambda_2$ + ... + $\\lambda_n$", 
                     r'$tr(A) = \lambda_1 + \lambda_2 + \ldots + \lambda_n$')
text = text.replace("det(A) = $\\lambda_1$ * $\\lambda_2$ * ... * $\\lambda_n$",
                     r'$det(A) = \lambda_1 \cdot \lambda_2 \cdots \lambda_n$')

# Pattern 6: "eigenvalues $\lambda_1$, $\lambda_2$" → "eigenvalues $\lambda_1, \lambda_2$"
text = text.replace('eigenvalues $\\lambda_1$, $\\lambda_2$', r'eigenvalues $\lambda_1, \lambda_2$')

# Pattern 7: Fix remaining $\lambda$ standalone in expressions
text = text.replace("eigenvalue $\\lambda$ = 3", r'eigenvalue $\lambda = 3$')
text = text.replace("For $\\lambda$ = i:", r'For $\lambda = i$:')
text = text.replace("For $\\lambda$ = -i:", r'For $\lambda = -i$:')

# Pattern 8: Fix $\alpha$ standalone
text = text.replace("$\\alpha$", r"$\\alpha$")  # already correct, just normalize spacing
text = text.replace('($\lambda$ + $alpha$)', r'$(\lambda + \alpha)$')

# Pattern 9: Fix |$\lambda$| → $|\lambda|$
text = text.replace('|$\\lambda$|', r'$|\lambda|$')

# Pattern 10: Fix alpha_j not replaced (in non-math context)
text = re.sub(r'(?<!\\)\balpha_j\b', r'$\\alpha_j$', text)
text = re.sub(r'(?<!\\)\bhalpha\b', r'$\\alpha$', text)
text = re.sub(r'(?<!\\)\balpha\b(?!\w)', r'$\\alpha$', text)

# Pattern 11: Fix "($\\lambda$+$\\alpha$)I" 
text = text.replace(r'($\lambda$+$\alpha$)I', r'$(\lambda+\alpha)I$')

# Pattern 12: Fix "Ax = $\lambda$ x" → "Ax = $\lambda x$"
text = text.replace('Ax = $\\lambda$ x', r'Ax = $\lambda x$')
text = text.replace('Bx = $\\alpha$ x', r'Bx = $\alpha x$')

# Pattern 12b: Fix "(A+B)x = ($\\lambda$ + $\\alpha$)x"
text = text.replace('(A+B)x = ($\\lambda$ + $\\alpha$)x',
                     r'(A+B)x = $(\lambda + \alpha)x$')

# Pattern 13: Fix "Bx is not generally equal to $\\alpha$ x"
text = text.replace('equal to $\\alpha$ x', r'equal to $\alpha x$')

# Pattern 14: Fix "(A+B)x = $\\lambda$ x + Bx is not simply ($\\lambda$ + $\\alpha$)x"
text = text.replace('(A+B)x = $\\lambda$ x + Bx is not simply ($\\lambda$ + $\\alpha$)x',
                     r'(A+B)x = $\lambda x$ + Bx is not simply $(\lambda + \alpha)x$')

# Pattern 15: Fix eigenvalue $\\lambda$ with eigenvector
text = text.replace('eigenvalue $\\lambda$ with eigenvector',
                     r'eigenvalue $\lambda$ with eigenvector')

# Pattern 16: Fix "eigenvalues $\\lambda_1$ = i, $\\lambda_2$ = -i"
text = text.replace('Eigenvalues: $\\lambda_1$ = i, $\\lambda_2$ = -i',
                     r'Eigenvalues: $\lambda_1 = i$, $\lambda_2 = -i$')
text = text.replace('eigenvalues $\\lambda_1$ = 3, $\\lambda_2$ = 3',
                     r'eigenvalues $\lambda_1 = 3$, $\lambda_2 = 3$')
text = text.replace('eigenvalues at positions $\\lambda_1$, $\\lambda_2$',
                     r'eigenvalues at positions $\lambda_1, \lambda_2$')

# Pattern 17: Fix det(Q - $\\lambda$ I) → det(Q - $\lambda I$)
text = text.replace("det(Q - $\\lambda$ I)", r'det$(Q - \lambda I)$')
text = text.replace("det(A - $\\lambda$ I)", r'det$(A - \lambda I)$')
text = text.replace("A - $\\lambda$ I)x", r'A - $\lambda I)x')
text = text.replace("(A - $\\lambda$ I)x", r'$(A - \lambda I)x$')

# Pattern 18: Fix det((A+B) - ($\lambda$+$\alpha$)I)
text = text.replace('det((A+B) - ($\\lambda$+$\\alpha$)I)', 
                     r'det$(A+B) - (\lambda + \alpha)I$')

# Pattern 19: Fix [[a, b], [c, d]] → bmatrix
def fix_matrix(m):
    content = m.group(1)
    # Parse rows - each row is [num, num, ...]
    rows = re.findall(r'\[([^\[\]]+)\]', content)
    if len(rows) >= 2:
        formatted = ' \\\\\n                    '.join(
            ' & '.join(item.strip() for item in row.split(','))
            for row in rows
        )
        indent = m.group(0).split('[[')[0]  # before [[
        return '\\begin{bmatrix} ' + formatted + ' \\end{bmatrix}'
    return m.group(0)

text = re.sub(r'\[\[([^\[\]]+(?:\[[^\[\]]+\][^\[\]]*)*)\]\]', fix_matrix, text)

# Pattern 20: Fix det([[-$\lambda$, -1], [1, -$\lambda$]]) 
# This is tricky, let me handle it specifically
text = text.replace("det([[-$\\lambda$, -1], [1, $-\\lambda$]])", 
                     r'det\begin{bmatrix} -\lambda & -1 \\ 1 & -\lambda \end{bmatrix}')

# Pattern 21: Fix [[-i, -1], [1, -i]]x = 0
text = text.replace('[[-i, -1], [1, -i]]x = 0', 
                     r'\begin{bmatrix} -i & -1 \\ 1 & -i \end{bmatrix}x = 0')

# Pattern 22: Fix [[0, 3], [0, 0]]x = 0
text = text.replace('[[0, 3], [0, 0]]x = 0',
                     r'\begin{bmatrix} 0 & 3 \\ 0 & 0 \end{bmatrix}x = 0')

# Pattern 23: Fix remaining $\\lambda$ standalone issues
text = re.sub(r'\$\(\\lambda\)\$', r'$\lambda$', text)

# Pattern 24: Fix "$\lambda$ + c" → "$\lambda + c$"
text = text.replace("$\lambda$ + c", r"$\lambda + c$")

# Pattern 25: Fix extra spaces in bmatrix: " \\  " → " \\ "
text = re.sub(r'\\\\\s+', r' \\\\ ', text)

# Pattern 26: Fix {\begin{bmatrix}...}} - remove extra braces
text = text.replace('{\\begin{bmatrix}', '\\begin{bmatrix}')
text = re.sub(r'\\end\{bmatrix\}\^T\}([^}])', r'\\end{bmatrix}^T\1', text)

# Pattern 27: Fix "x = \begin{bmatrix} 1 \\  0 \end{bmatrix}^T" extra space
text = text.replace(r' \end{bmatrix}', r'\end{bmatrix}')
text = re.sub(r'\\begin\{bmatrix\}\s+\(', r'\begin{bmatrix}(', text)

# Fix double space in bmatrix rows
text = re.sub(r'\\\\  +', r' \\\\ ', text)

# Fix bmatrix with extra spaces
text = re.sub(r'\\begin\{bmatrix\}\s+\\end\{bmatrix\}', r'\\begin{bmatrix} \\end{bmatrix}', text)
text = re.sub(r'\\end\{bmatrix\}\s+\}\^T', r'\\end{bmatrix}^T', text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

# Verify
plain_lambda = len(re.findall(r'(?<!\\)\blambda\b', text))
plain_alpha = len(re.findall(r'(?<!\\)\balpha\b', text))
plain_matrix = text.count('[[')
print('Remaining plain lambda:', plain_lambda)
print('Remaining plain alpha:', plain_alpha)
print('Remaining [[ count:', plain_matrix)
