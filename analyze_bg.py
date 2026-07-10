import re
from collections import Counter

with open('test.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<pre id="tiresult"[^>]*>(.*?)</pre>', html, re.DOTALL)
lines = m.group(1).strip().split('\n')

edge_colors = []

for i, line in enumerate(lines):
    spans = re.findall(r'<b style="color:(#[0-9A-Fa-f]{6})">(.*?)</b>', line)
    
    # Check first and last span of every line
    if spans:
        edge_colors.append(spans[0][0])
        edge_colors.append(spans[-1][0])
        
    # Check all spans of first and last line
    if i == 0 or i == len(lines) - 1:
        for color, text in spans:
            for _ in text:
                edge_colors.append(color)

c = Counter(edge_colors)
print("Most common edge colors:", c.most_common(5))
