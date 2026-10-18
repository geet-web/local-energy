import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy"
pages_dir = os.path.join(base_dir, "pages")

# Canonical single modal block we want to keep (no duplicates)
MODAL_BLOCK = """
  <!-- ═══════════════════════════ MODALS ═══════════════════════════ -->
  <div class="legal-modal-overlay" id="modalOverlay">
    <div class="legal-modal" id="modalPrivacy">
      <button class="modal-close" aria-label="Close modal">&times;</button>
      <div class="modal-header">
        <h2>Privacy Policy</h2>
        <p>Effective Date: April 2026</p>
      </div>
      <div class="modal-body">
        <h3>1. Information We Collect</h3>
        <p>We collect information you provide directly to us, such as when you request a consultation, fill out a form, or communicate with us.</p>
        <h3>2. How We Use Your Information</h3>
        <p>We use the information we collect to evaluate your property's solar potential and provide accurate estimates.</p>
        <h3>3. Data Sharing and Security</h3>
        <p>Your data is securely stored and never sold to third parties.</p>
      </div>
    </div>
    <div class="legal-modal" id="modalTerms">
      <button class="modal-close" aria-label="Close modal">&times;</button>
      <div class="modal-header">
        <h2>Terms &amp; Conditions</h2>
        <p>Effective Date: April 2026</p>
      </div>
      <div class="modal-body">
        <h3>1. Acceptance of Terms</h3>
        <p>By using our website, you agree to these terms.</p>
        <h3>2. Service Description</h3>
        <p>Local Energy provides solar panel installation and consultation services.</p>
      </div>
    </div>
  </div>"""

# Pattern to match the entire modal overlay block (one or more)
modal_pattern = re.compile(
    r'\s*<!-- ═+\s*MODALS\s*═+ -->\s*<div class="legal-modal-overlay"[^>]*>.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all modal blocks
    matches = list(modal_pattern.finditer(content))
    if len(matches) <= 1:
        # Check for trailing junk after </html>
        cleaned = re.sub(r'(</html>)\s*[\w<>]+\s*$', r'\1\n', content)
        if cleaned != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            print(f"Cleaned trailing junk from {os.path.basename(filepath)}")
        return

    # Remove all modal blocks from content
    content_no_modals = modal_pattern.sub('', content)

    # Find insertion point: right before </body>
    body_close_match = re.search(r'(\s*<script src=)', content_no_modals)
    if not body_close_match:
        body_close_match = re.search(r'(\s*</body>)', content_no_modals)

    if body_close_match:
        insert_pos = body_close_match.start()
        content_fixed = content_no_modals[:insert_pos] + '\n' + MODAL_BLOCK + '\n' + content_no_modals[insert_pos:]
    else:
        content_fixed = content_no_modals

    # Clean trailing junk after </html>
    content_fixed = re.sub(r'(</html>)\s*[\w<>]+\s*$', r'\1\n', content_fixed, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content_fixed)
    print(f"Fixed {len(matches)} duplicate modal blocks in {os.path.basename(filepath)}")

# Process index.html
fix_file(os.path.join(base_dir, "index.html"))

# Process all inner pages
for filename in sorted(os.listdir(pages_dir)):
    if filename.endswith(".html"):
        fix_file(os.path.join(pages_dir, filename))

print("Done!")
