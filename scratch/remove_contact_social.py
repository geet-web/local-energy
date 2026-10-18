import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy"
pages_dir = os.path.join(base_dir, "pages")

social_links_pattern = re.compile(r'<div class="social-links">.*?</div>', re.DOTALL)

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = social_links_pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed social-links from {os.path.basename(filepath)}")

# Clean index.html
clean_file(os.path.join(base_dir, "index.html"))

# Clean interior pages
if os.path.exists(pages_dir):
    for filename in os.listdir(pages_dir):
        if filename.endswith(".html"):
            clean_file(os.path.join(pages_dir, filename))
