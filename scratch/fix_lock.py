import os
import re

base_dir = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy'
pages_dir = os.path.join(base_dir, 'pages')

files = [os.path.join(base_dir, 'index.html')] + [os.path.join(pages_dir, f) for f in os.listdir(pages_dir) if f.endswith('.html')]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the lock icon and change its style
    content = content.replace(
        '<p style="font-size:0.75rem;color:var(--clr-green);text-align:center;margin-top:14px;">',
        '<p style="font-size:0.75rem;color:#94A3B8;text-align:center;margin-top:14px;">'
    )
    # Fix the trailing broken /html> or l> tags
    content = re.sub(r'</html>\s*[/<]*h?t?m?l?>?\s*.*$', '</html>\n', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done fixing locks and html tags')
