import os
import re

root_dir = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy'
pages_dir = os.path.join(root_dir, 'pages')

home_nav_html = """  <nav class="navbar" id="navbar">
    <div class="nav-container">
      <a href="#hero" class="nav-logo">
        <img src="assets/logo.png" alt="Local Energy" class="main-logo" />
      </a>
      <ul class="nav-links" id="navLinks">
        <li><a href="pages/why-us.html">Why Us</a></li>
        <li><a href="pages/services.html">Services</a></li>
        <li><a href="pages/calculator.html">Calculator</a></li>
        <li><a href="pages/how-it-works.html">How It Works</a></li>
        <li><a href="pages/contact.html">Contact</a></li>
      </ul>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>"""

inner_nav_html = """  <nav class="navbar" id="navbar">
    <div class="nav-container">
      <a href="../index.html" class="nav-logo">
        <img src="../assets/logo.png" alt="Local Energy" class="main-logo" />
      </a>
      <ul class="nav-links" id="navLinks">
        <li><a href="why-us.html">Why Us</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="calculator.html">Calculator</a></li>
        <li><a href="how-it-works.html">How It Works</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>"""

# Update index.html
index_path = os.path.join(root_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<nav class="navbar".*?</nav>', home_nav_html, content, flags=re.DOTALL)
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html navbar")

# Update inner pages
for file in os.listdir(pages_dir):
    if file.endswith('.html'):
        file_path = os.path.join(pages_dir, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(r'<nav class="navbar".*?</nav>', inner_nav_html, content, flags=re.DOTALL)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file} navbar")
