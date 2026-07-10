import re
import base64
from PIL import Image, ImageDraw, ImageDraw2

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb).upper()

def process_image(bg_color_hex, filename):
    with open('test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    pre_match = re.search(r'<pre id="tiresult"[^>]*>(.*?)</pre>', html, re.DOTALL)
    lines = pre_match.group(1).strip().split('\n')
    
    char_w = 4
    char_h = 4
    
    img_w = max(sum(len(text) for _, text in re.findall(r'<b style="color:(#[0-9A-Fa-f]{6})">(.*?)</b>', line)) for line in lines) * char_w
    img_h = len(lines) * char_h
    
    # Draw original image
    img = Image.new('RGB', (img_w, img_h), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    for y, line in enumerate(lines):
        spans = re.findall(r'<b style="color:(#[0-9A-Fa-f]{6})">(.*?)</b>', line)
        x_idx = 0
        for color, text in spans:
            for ch in text:
                if ch != ' ':
                    x_pos = x_idx * char_w
                    y_pos = y * char_h
                    draw.rectangle([x_pos, y_pos, x_pos + char_w - 1, y_pos + char_h - 1], fill=color)
                x_idx += 1
                
    # Flood fill from (0,0) to replace the background
    target_bg = hex_to_rgb(bg_color_hex)
    
    # We will do a manual BFS flood fill because ImageDraw.floodfill can be tricky with exact matches
    pixels = img.load()
    start_color = pixels[0, 0]
    
    # If the start color is not close to white, we might be wrong, but let's assume (0,0) is background
    queue = [(0, 0), (img_w - 1, 0), (0, img_h - 1), (img_w - 1, img_h - 1)]
    visited = set(queue)
    
    while queue:
        x, y = queue.pop(0)
        if pixels[x, y] == start_color:
            pixels[x, y] = target_bg
            # Add neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < img_w and 0 <= ny < img_h:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

    # Base64 encode
    import io
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    # Embed into SVG
    image_tag = f'<image x="15" y="30" width="800" height="800" preserveAspectRatio="none" href="data:image/png;base64,{b64}" />'
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = re.sub(r'<text[^>]*class="ascii"[^>]*>.*?</text>', image_tag, content, flags=re.DOTALL)
    new_content = re.sub(r'<image[^>]*href="data:image/png;base64,[^>]*/>', image_tag, new_content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename} with solid bg {bg_color_hex}")

# Dark mode bg is #161b22
process_image('#161b22', 'dark_mode.svg')
# Light mode bg is #f6f8fa
process_image('#f6f8fa', 'light_mode.svg')
