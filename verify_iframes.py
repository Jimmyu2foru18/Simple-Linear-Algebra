import os
import re

root = r"C:\Users\James\Documents\GitHub\Simple-Linear-Algebra"
broken = []
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    for f in filenames:
        if not f.endswith(".html"):
            continue
        filepath = os.path.join(dirpath, f)
        with open(filepath, "r", encoding="utf-8") as fh:
            content = fh.read()
        matches = re.findall(r'<iframe[^>]*src="[^"]*youtube\.com/embed/[^"]*"', content)
        for m in matches:
            if 'title="' not in m:
                broken.append(filepath + ' -> ' + m[:80])

if broken:
    print("Iframes without title found in:")
    for i in broken:
        print(f"  {i}")
else:
    print("All iframes have title attributes.")
