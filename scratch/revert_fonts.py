import os

root_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy"

def revert_font(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to put Montserrat back for headings, which we previously brute-force replaced.
    # In my previous script, I replaced "'Montserrat'" with "'Poppins'" and "Montserrat" with "'Poppins', sans-serif".
    # I will specifically target the main heading classes in style.css and inner.css
    if "style.css" in file_path or "inner.css" in file_path:
        new_content = content.replace(".section-title {\n  font-family: 'Poppins', sans-serif;", ".section-title {\n  font-family: 'Montserrat', sans-serif;")
        new_content = new_content.replace(".inner-hero h1 {\n  font-family: 'Poppins', sans-serif;", ".inner-hero h1 {\n  font-family: 'Montserrat', sans-serif;")
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Reverted global headings to Montserrat in: {file_path}")

for root, _, files in os.walk(root_dir):
    if "scratch" in root:
        continue
    for file in files:
        if file.endswith('.css'):
            revert_font(os.path.join(root, file))
