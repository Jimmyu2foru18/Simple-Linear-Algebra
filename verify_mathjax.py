import os

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
        if "$$ignoreHtmlClass: 'no-mathjax'$$" in content:
            broken.append(filepath)

if broken:
    print("Broken MathJax config found in:")
    for i in broken:
        print(f"  {i}")
else:
    print("No broken MathJax config found.")
