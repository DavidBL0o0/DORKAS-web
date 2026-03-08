import re

file_path = r'd:\00 - PROYECTO DORKAS\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(
    r'<div class="h-40 w-full relative bg-brand-base">\s*'
    r'<img src="([^"]+)"\s*class="([^"]+)"\s*alt="([^"]+)">\s*'
    r'<div class="absolute inset-0 bg-gradient-to-t from-\[#090e1a\] to-transparent"></div>\s*'
    r'<div\s+class="([^"]+)">\s*'
    r'<i class="([^"]+)"></i>\s*'
    r'</div>\s*'
    r'</div>'
)

def replacer(match):
    img_src = match.group(1)
    img_class = match.group(2)
    img_alt = match.group(3)
    icon_container_class = match.group(4)
    icon_class = match.group(5)
    
    # We wrap the img and gradient in an overflow-hidden container
    # so that when the image expands on hover, it doesn't bleed out of the h-40 boundary
    return f'''<div class="h-40 w-full relative bg-transparent">
                            <div class="absolute inset-0 overflow-hidden rounded-t-2xl">
                                <img src="{img_src}" class="{img_class}" alt="{img_alt}">
                                <div class="absolute inset-0 bg-gradient-to-t from-brand-surface to-transparent pointer-events-none"></div>
                            </div>
                            <div class="{icon_container_class}">
                                <i class="{icon_class}"></i>
                            </div>
                        </div>'''

new_content = pattern.sub(replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Shadows and hover bleeding fixed!")
