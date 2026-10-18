import os
import re

root_dir = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy'

# Update any logo.svg to logo.png
logo_pattern = re.compile(r'assets/logo\.svg')

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = logo_pattern.sub('assets/logo.png', content)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file_path}")
