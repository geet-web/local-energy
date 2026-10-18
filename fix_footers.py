import re
import os

pages_dir = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy\pages'

# The exact footer content to apply strictly to all pages
footer_template = """  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="../index.html" class="nav-logo footer-logo">
            <span class="logo-icon"><i class="fas fa-solar-panel"></i></span>
            <span class="logo-text">Local<span class="accent">Energy</span></span>
          </a>
          <p>India's trusted partner for rooftop solar solutions. Helping homes and businesses generate clean, affordable energy since 2009.</p>
          <p class="footer-tagline">"Local Energy — <em>Powering a Greener Tomorrow</em>"</p>
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
          <h4>Contact Us</h4>
          <ul>
            <li><i class="fas fa-map-marker-alt" style="color:#F97316;margin-right:8px;"></i> Gomti Nagar, Lucknow – 226010</li>
            <li><i class="fas fa-phone-alt" style="color:#F97316;margin-right:8px;"></i> +91 98765 43210</li>
            <li><i class="fas fa-envelope" style="color:#F97316;margin-right:8px;"></i> hello@localenergy.in</li>
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
      </div>
      <div class="footer-bottom">
        <p>&copy; 2024 Local Energy Pvt. Ltd. All rights reserved. | CIN: U40109UP2009PTC123456 | MNRE Empanelled Installer</p>
        <p>Designed with <i class="fas fa-heart" style="color:#FF6B35"></i> for a greener India</p>
      </div>
    </div>
  </footer>"""

for filename in os.listdir(pages_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(pages_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to target everything from <!-- FOOTER --> to </footer>
        pattern = r'(?:  <!-- [═]*\s*FOOTER\s*[═]* -->\s*|  <!-- FOOTER -->\s*)?<footer class="footer">.*?</footer>'
        
        new_content = re.sub(pattern, footer_template, content, flags=re.DOTALL)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated footer in: {filename}')
        else:
            print(f'Footer already matching in: {filename}')

print('All inner pages updated to match the landing page footer exactly.')
