import re
f=open('dark_mode.svg','r',encoding='utf-8')
c=f.read()
f.close()

m=re.search(r'<text[^>]*class="ascii"[^>]*>(.*?)</text>', c, re.DOTALL)
print('Found ascii block:', bool(m))
if m:
    block = m.group(1)
    # Try to find tspan lines
    outer = re.findall(r'<tspan x="15" dy="[^"]*">(.*?)</tspan>', block)
    print(f'Outer tspans found: {len(outer)}')
    if outer:
        print(f'First outer[:100]: {outer[0][:100]}')
    else:
        # Show raw block start
        print(f'Block start: {block[:300]}')
        # Try multiline
        outer2 = re.findall(r'<tspan x="15" dy="[^"]*">(.*?)</tspan>', block, re.DOTALL)
        print(f'With DOTALL: {len(outer2)}')
