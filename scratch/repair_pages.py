import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy"
pages_dir = os.path.join(base_dir, "pages")
files = [os.path.join("pages", f) for f in os.listdir(pages_dir) if f.endswith(".html")]

# Pattern to fix the broken scroll listener and remove stickyQuote logic
# from: window.addEventListener('scroll', () => { ... });
pattern_scroll = re.compile(r'window\.addEventListener\(\'scroll\',.*?\s+stickyQuote\.classList\.add\(\'hidden\'\);.*?\n\s+.*?\}\s+.*?\}\);', re.DOTALL)

replacement_scroll = """window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    });"""

# Also fix the corrupted tails (</html> repeated)
pattern_tail = re.compile(r'</html>.*</html>', re.DOTALL)

for rel_path in files:
    filepath = os.path.join(base_dir, rel_path)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix scroll listener
    content = pattern_scroll.sub(replacement_scroll, content)
    
    # 2. Fix tails
    content = pattern_tail.sub('</html>', content)
    
    # 3. Ensure 'hidden' class is gone from sticky-quote-btn
    content = content.replace('sticky-quote-btn hidden', 'sticky-quote-btn')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Repaired {rel_path}")
