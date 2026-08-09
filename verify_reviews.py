#!/usr/bin/env python3
"""Verify navigation links in review pages."""
import os, re

reviews_dir = r"C:\Users\James\Documents\GitHub\Simple-Linear-Algebra\reviews"
files = sorted([f for f in os.listdir(reviews_dir) if f.endswith('.html')])
for f in files:
    filepath = os.path.join(reviews_dir, f)
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    prev = re.search(r'<a href="([^"]+)"[^>]*class="[^"]*review-nav-btn[^"]*"[^>]*>.*?← Previous', content, re.DOTALL)
    next_m = re.search(r'<a href="([^"]+)"[^>]*class="[^"]*review-nav-btn[^"]*"[^>]*>.*?Next', content, re.DOTALL)
    print(f'{f}:')
    print(f'  prev: {prev.group(1) if prev else "none"}')
    print(f'  next: {next_m.group(1) if next_m else "none"}')
    print()
