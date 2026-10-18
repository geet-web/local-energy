import os
import re

root_dir = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy'

def fix_inner_hero(content, filename):
    # Ensure inner-hero has breadcrumb and badge
    if '<section class="inner-hero">' not in content:
        return content
    
    # 1. Ensure breadcrumb exists
    if '<div class="breadcrumb">' not in content:
        # Insert breadcrumb after inner-hero-content start
        page_name = filename.replace('.html', '').replace('-', ' ').title()
        if page_name == 'Index': page_name = 'Home'
        breadcrumb_html = f'\n      <div class="breadcrumb">\n        <a href="../index.html">Home</a><i class="fas fa-chevron-right"></i><span>{page_name}</span>\n      </div>'
        content = content.replace('<div class="container inner-hero-content">', '<div class="container inner-hero-content">' + breadcrumb_html)

    # 2. Ensure badge exists
    if 'inner-hero-badge' not in content:
        badge_map = {
            'calculator.html': '<div class="inner-hero-badge"><i class="fas fa-calculator"></i> Free Savings Estimate</div>',
            'contact.html': '<div class="inner-hero-badge"><i class="fas fa-envelope"></i> Get in Touch</div>',
            'faq.html': '<div class="inner-hero-badge"><i class="fas fa-question-circle"></i> Frequently Asked Questions</div>',
            'solar-in-lucknow.html': '<div class="inner-hero-badge"><i class="fas fa-location-dot"></i> Solar Partner in Lucknow</div>'
        }
        badge_html = badge_map.get(filename, '<div class="inner-hero-badge"><i class="fas fa-sun"></i> Local Energy Solutions</div>')
        # Insert badge before h1
        content = re.sub(r'(<h1.*?>)', f'\n      {badge_html}\n      \\1', content)

    return content

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html') and file != 'index.html' and root.endswith('pages'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = fix_inner_hero(content, file)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Standardized hero for {file_path}")
