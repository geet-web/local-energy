import os
import re

footer_standard_pages = """  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="../index.html" class="nav-logo footer-logo">
            <span class="logo-icon"><i class="fas fa-solar-panel"></i></span>
            <span class="logo-text">Local<span class="accent">Energy</span></span>
          </a>
          <p>India's trusted partner for rooftop solar solutions. Helping homes and businesses generate clean, affordable energy since 2009.</p>
          <div class="footer-social">
            <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="https://wa.me/919876543210" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
          </div>
        </div>

        <div class="footer-links-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="why-us.html">Why Us</a></li>
            <li><a href="calculator.html">Savings Calculator</a></li>
            <li><a href="how-it-works.html">How It Works</a></li>
          </ul>
        </div>

        <div class="footer-links-col">
          <h4>Company</h4>
          <ul>
            <li><a href="faq.html">FAQs</a></li>
            <li><a href="javascript:void(0)" id="linkPrivacy">Privacy Policy</a></li>
            <li><a href="javascript:void(0)" id="linkTerms">Terms & Conditions</a></li>
          </ul>
        </div>

        <div class="footer-links-col">
          <h4>Our Services</h4>
          <ul>
            <li><a href="services.html">Residential Solar</a></li>
            <li><a href="services.html">Commercial Solar</a></li>
            <li><a href="services.html">Solar Maintenance</a></li>
          </ul>
        </div>

        <div class="footer-links-col">
          <h4>Contact Us</h4>
          <ul>
            <li><i class="fas fa-map-marker-alt" style="color:#F97316;margin-right:8px;"></i> Gomti Nagar, Lucknow – 226010</li>
            <li><i class="fas fa-phone" style="color:#F97316;margin-right:8px;"></i> +91 98765 43210</li>
            <li><i class="fas fa-envelope" style="color:#F97316;margin-right:8px;"></i> hello@localenergy.in</li>
          </ul>
        </div>

      </div>
      <div class="footer-bottom">
        <div class="footer-copyright">
          <p>© 2024 Local Energy Pvt. Ltd. All rights reserved. | MNRE Empanelled Installer</p>
        </div>
      </div>
    </div>
  </footer>

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
        <h2>Terms & Conditions</h2>
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

# index.html logic
footer_standard_index = footer_standard_pages.replace('href="why-us.html"', 'href="pages/why-us.html"').replace('href="calculator.html"', 'href="pages/calculator.html"').replace('href="how-it-works.html"', 'href="pages/how-it-works.html"').replace('href="faq.html"', 'href="pages/faq.html"').replace('href="services.html"', 'href="pages/services.html"').replace('href="../index.html"', 'href="#hero"')

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy"
pages_dir = os.path.join(base_dir, "pages")

footer_pattern = re.compile(r"<footer class=\"footer\">.*?</footer>", re.DOTALL)
modal_pattern = re.compile(r"<!-- ═══════════════════════════ MODALS ═══════════════════════════ -->.*?</div>\s*</div>\s*</div>", re.DOTALL)

# Update index.html
with open(os.path.join(base_dir, "index.html"), 'r', encoding='utf-8') as f:
    content = f.read()
content = footer_pattern.sub(footer_standard_index, content)
# Ensure modals are present and not duplicated
if "legal-modal-overlay" in content and footer_standard_index.count("legal-modal-overlay") > 0:
    # It will replace everything from footer starts to footer ends, 
    # and footer_standard_index includes modals.
    pass

with open(os.path.join(base_dir, "index.html"), 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")

# Update interior pages
files = [f for f in os.listdir(pages_dir) if f.endswith(".html")]
for filename in files:
    filepath = os.path.join(pages_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = footer_pattern.sub(footer_standard_pages, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
