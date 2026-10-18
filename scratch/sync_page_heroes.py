import os
import re

root_dir = r'c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\local-energy'

def standardize_page_hero(content, filename):
    if filename == 'index.html':
        return content

    page_title_map = {
        'about.html': 'About Us',
        'calculator.html': 'Calculator',
        'contact.html': 'Contact',
        'faq.html': 'FAQ',
        'how-it-works.html': 'How It Works',
        'services.html': 'Services',
        'why-us.html': 'Why Us',
        'solar-in-lucknow.html': 'Solar in Lucknow'
    }
    
    badge_map = {
        'about.html': ('fa-leaf', 'Since 2009 — 15+ Years of Solar'),
        'calculator.html': ('fa-calculator', 'Instant Savings Estimate'),
        'contact.html': ('fa-envelope', 'Free Consultation — No Commitment'),
        'faq.html': ('fa-question-circle', 'Frequently Asked Questions'),
        'how-it-works.html': ('fa-route', 'Simple 4-Step Process'),
        'services.html': ('fa-solar-panel', 'End-to-End Solar Solutions'),
        'why-us.html': ('fa-award', 'Why Choose Us'),
        'solar-in-lucknow.html': ('fa-location-dot', 'Solar Partner in Lucknow')
    }

    h1_map = {
        'about.html': 'We Make Solar <span class="accent-text">Simple & Reliable</span>',
        'calculator.html': 'How Much Will You <span class="accent-text">Save with Solar?</span>',
        'contact.html': 'Let\'s Start Your <span class="accent-text">Solar Journey Together</span>',
        'faq.html': 'Everything You Want to Know <span class="accent-text">About Solar</span>',
        'how-it-works.html': 'Going Solar is <span class="accent-text">Easier Than You Think</span>',
        'services.html': 'Everything Solar, <br /><span class="accent-text">All Under One Roof</span>',
        'why-us.html': 'Solar Energy That Works <br /><span class="accent-text">For You</span>',
        'solar-in-lucknow.html': 'Rooftop Solar in <br /><span class="accent-text">Lucknow</span>'
    }

    subtitle_map = {
        'about.html': 'Founded with a mission to make clean energy accessible to every Indian home and business, regardless of their budget.',
        'calculator.html': 'Enter your monthly electricity bill and roof details to get an instant, personalised savings estimate and subsidy calculation.',
        'contact.html': 'Fill the quick form below or WhatsApp us directly. Our solar advisors will get in touch within 2 hours for a free site visit.',
        'faq.html': 'Honest, simple answers to the most common questions we hear from homeowners and businesses considering rooftop solar.',
        'how-it-works.html': 'From your first call to generating clean energy — our end-to-end process is designed to be completely hassle-free.',
        'services.html': 'From residential rooftops and commercial plants to ongoing maintenance and subsidy management — we deliver it all.',
        'why-us.html': 'From rooftop surveys to post-installation support — we handle everything so you can focus on savings.',
        'solar-in-lucknow.html': 'Save up to 90% on electricity bills with a custom solar system designed for your Lucknow home or business.'
    }

    page_title = page_title_map.get(filename, 'Page')
    icon, badge_text = badge_map.get(filename, ('fa-sun', 'Local Energy Solutions'))
    h1_text = h1_map.get(filename, 'Local Solar Solutions')
    subtitle = subtitle_map.get(filename, 'Professional solar installations for your home and business.')

    buttons_html = f'''      <div class="hero-btns">
        <a href="contact.html" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Get a Free Quote</a>
        <a href="calculator.html" class="btn btn-outline btn-lg"><i class="fas fa-calculator"></i> Estimate Savings</a>
      </div>'''
    
    if filename == 'calculator.html':
        buttons_html = f'''      <div class="hero-btns">
        <a href="contact.html" class="btn btn-primary btn-lg"><i class="fas fa-phone"></i> Get a Free Quote</a>
        <a href="how-it-works.html" class="btn btn-outline btn-lg"><i class="fas fa-play"></i> See How It Works</a>
      </div>'''

    new_hero_html = f'''  <section class="inner-hero">
    <div class="container inner-hero-content">
      <div class="breadcrumb">
        <a href="../index.html">Home</a><i class="fas fa-chevron-right"></i><span>{page_title}</span>
      </div>
      <div class="inner-hero-badge"><i class="fas {icon}"></i> {badge_text}</div>
      <h1>{h1_text}</h1>
      <p>{subtitle}</p>
{buttons_html}
    </div>
  </section>'''

    # Flexible regex to catch id="hero" or other attributes
    content = re.sub(r'<section class="inner-hero".*?>.*?</section>', new_hero_html, content, flags=re.DOTALL)
    
    return content

pages_dir = os.path.join(root_dir, 'pages')
for file in os.listdir(pages_dir):
    if file.endswith('.html'):
        file_path = os.path.join(pages_dir, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = standardize_page_hero(content, file)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
