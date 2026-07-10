import re
with open('test.html', 'r', encoding='utf-8') as f:
    html = f.read()
m = re.search(r'<pre id="tiresult"[^>]*>(.*?)</pre>', html, re.DOTALL)
lines = m.group(1).strip().split('\n')
print('First line colors:', re.findall(r'<b style="color:(#[0-9A-Fa-f]{6})">(.*?)</b>', lines[0])[:5])
