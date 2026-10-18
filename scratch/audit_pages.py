import os

base = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy'
pages = os.path.join(base, 'pages')

files = [(base, 'index.html')] + [(pages, f) for f in sorted(os.listdir(pages)) if f.endswith('.html')]

for d, fn in files:
    path = os.path.join(d, fn)
    with open(path, encoding='utf-8') as f:
        content = f.read()
    modal_count = content.count('legal-modal-overlay')
    yt_count = content.count('fa-youtube')
    fb_count = content.count('fa-facebook')
    old_social = content.count('class="social-links"')
    print(f'{fn:28s}  modals={modal_count}  youtube={yt_count}  facebook={fb_count}  old_social={old_social}')
