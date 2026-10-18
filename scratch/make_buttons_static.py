import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy"
files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
pages_dir = os.path.join(base_dir, "pages")
files += [os.path.join("pages", f) for f in os.listdir(pages_dir) if f.endswith(".html")]

# Pattern to remove 'hidden' class from sticky-quote-btn
pattern_hidden = re.compile(r'(class="sticky-quote-btn)\s+hidden"', re.IGNORECASE)

# Pattern to remove the JS scroll logic for stickyQuote
# It usually looks like:
# if (stickyQuote) {
#   if (window.scrollY > 150) {
#     stickyQuote.classList.remove('hidden');
#   } else {
#     stickyQuote.classList.add('hidden');
#   }
# }
pattern_js = re.compile(r'if\s*\(stickyQuote\)\s*\{.*?\}', re.DOTALL)

for rel_path in files:
    if rel_path == "pages": continue
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.isfile(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove 'hidden' class
    new_content = pattern_hidden.sub(r'\1"', content)
    
    # 2. Remove JS logic
    new_content = pattern_js.sub('', new_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {rel_path}")
