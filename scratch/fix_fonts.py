import os
import re

root_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy"

def replace_font(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace("'Montserrat'", "'Poppins'")
    new_content = new_content.replace('font-family: Montserrat', "font-family: 'Poppins', sans-serif")

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated font in: {file_path}")

for root, _, files in os.walk(root_dir):
    if "scratch" in root:
        continue
    for file in files:
        if file.endswith('.css') or file.endswith('.html'):
            replace_font(os.path.join(root, file))
