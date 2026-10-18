import os
import re

root_dir = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy'

logo_pattern = re.compile(r'<a href="[^"]*" class="nav-logo[^"]*">.*?</a>', re.DOTALL)

def replace_logo(content, is_index=False):
    def replacer(match):
        href = re.search(r'href="([^"]*)"', match.group(0)).group(1)
        classes = re.search(r'class="([^"]*)"', match.group(0)).group(1)
        path_prefix = '' if is_index else '../'
        # Check if it's footer logo
        if 'footer-logo' in classes:
             return f'<a href="{href}" class="{classes}">\n            <img src="{path_prefix}assets/logo.svg" alt="Local Energy" class="main-logo" />\n          </a>'
        else:
             return f'<a href="{href}" class="{classes}">\n        <img src="{path_prefix}assets/logo.svg" alt="Local Energy" class="main-logo" />\n      </a>'
    
    return logo_pattern.sub(replacer, content)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            is_index = file == 'index.html'
            new_content = replace_logo(content, is_index)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file_path}")
