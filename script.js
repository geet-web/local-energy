/* ═══════════════════════════════════════════════════════════════
   LOCAL ENERGY — JavaScript
   Savings Calculator, Scroll Animations, Navbar, etc.
   ═══════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ─── Navbar scroll effect ─── */
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  /* ─── Mobile hamburger ─── */
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('open');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navLinks.classList.remove('open');
    });
  });

  /* ─── Scroll Reveal Animation ─── */
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        const delay = entry.target.dataset.delay || 0;
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, delay);
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  // Add staggered delays to sibling cards
  document.querySelectorAll('.benefits-bento, .benefits-grid, .services-grid, .steps-wrapper, .benefits-banner-grid, .testimonials-grid, .areas-grid').forEach(grid => {
    grid.querySelectorAll('.reveal').forEach((el, i) => {
      el.dataset.delay = i * 100;
    });
  });

  revealElements.forEach(el => revealObserver.observe(el));

  /* ─── Animated Counter ─── */
  const counters = document.querySelectorAll('.stat-num');
  let countersStarted = false;

  function startCounters() {
    if (countersStarted) return;
    countersStarted = true;
    counters.forEach(counter => {
      const target = parseInt(counter.dataset.target);
      const duration = 2000;
      const step = target / (duration / 16);
      let current = 0;

      const timer = setInterval(() => {
        current += step;
        if (current >= target) {
          counter.textContent = target;
          clearInterval(timer);
        } else {
          counter.textContent = Math.floor(current);
        }
      }, 16);
    });
  }

  const heroSection = document.getElementById('hero');
  if (heroSection) {
    const heroObserver = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        setTimeout(startCounters, 800);
      }
    }, { threshold: 0.3 });
    heroObserver.observe(heroSection);
  }

  /* ─── Floating Particles ─── */
  const particlesContainer = document.getElementById('heroParticles');
  if (particlesContainer) {
    function createParticle() {
      const p = document.createElement('div');
      p.classList.add('particle');
      const size = Math.random() * 4 + 2;
      p.style.cssText = `
        width: ${size}px;
        height: ${size}px;
        left: ${Math.random() * 100}%;
        animation-duration: ${Math.random() * 12 + 8}s;
        animation-delay: ${Math.random() * 6}s;
        opacity: ${Math.random() * 0.5 + 0.2};
        background: ${Math.random() > 0.5 ? 'rgba(249,115,22,0.7)' : 'rgba(251,191,36,0.6)'};
      `;
      particlesContainer.appendChild(p);
      setTimeout(() => p.remove(), 20000);
    }
    for (let i = 0; i < 20; i++) createParticle();
    setInterval(createParticle, 2000);
  }

  /* ─── Savings Calculator ─── */
  const calcBtn = document.getElementById('calcBtn');
  const monthlyBillInput = document.getElementById('monthlyBill');
  const stateSelect = document.getElementById('stateSelect');
  const resultsContent = document.getElementById('resultsContent');
  const resultPlaceholder = document.querySelector('.result-placeholder');

  // Rate per unit by state (₹/kWh approximate)
  const stateRates = {
    up: 6.5,
    delhi: 7.5,
    haryana: 6.8,
    rajasthan: 6.2,
    maharashtra: 9.0,
    other: 7.0
  };

  function formatCurrency(val) {
    return '₹' + Math.round(val).toLocaleString('en-IN');
  }

  function calculateSavings() {
    const bill = parseFloat(monthlyBillInput.value);
    if (!bill || bill < 100) {
      monthlyBillInput.style.borderColor = 'var(--clr-orange-deep)';
      monthlyBillInput.focus();
      monthlyBillInput.style.animation = 'shake 0.4s ease';
      setTimeout(() => { monthlyBillInput.style.animation = ''; monthlyBillInput.style.borderColor = ''; }, 400);
      return;
    }

    const state = stateSelect.value;
    const ratePerUnit = stateRates[state] || 7.0;

    // Monthly units consumed
    const monthlyUnits = bill / ratePerUnit;

    // System size (kW) — roughly 1 kW generates ~120 units/month in India
    const systemKw = Math.ceil(monthlyUnits / 120 * 10) / 10;
    const adjustedKw = Math.max(1, Math.min(systemKw, 500));

    // After solar: remaining 5-10% grid dependency
    const gridDependency = 0.08;
    const newBill = bill * gridDependency;
    const monthlySavings = bill - newBill;
    const annualSavings = monthlySavings * 12;

    // System cost estimate: ₹50,000 per kW installed (with subsidy adjustment)
    const rawCost = adjustedKw * 55000;
    const subsidy = adjustedKw <= 3 ? Math.min(adjustedKw * 18000, 78000) : 0;
    const netCost = rawCost - subsidy;
    const paybackYears = netCost / annualSavings;

    // CO₂ saved: 0.82 kg per unit (India grid emission factor)
    const co2PerYear = (monthlyUnits * 12 * 0.82) / 1000; // tonnes

    // Update results
    document.getElementById('rMonthlySavings').textContent = formatCurrency(monthlySavings) + '/mo';
    document.getElementById('rAnnualSavings').textContent = formatCurrency(annualSavings) + '/yr';
    document.getElementById('rSystemSize').textContent = adjustedKw.toFixed(1) + ' kW System';
    document.getElementById('rPayback').textContent = paybackYears.toFixed(1) + ' Years';
    document.getElementById('rCo2').textContent = co2PerYear.toFixed(2) + ' Tonnes/Year';

    // Show results
    resultPlaceholder.style.display = 'none';
    resultsContent.classList.remove('hidden');

    // Animate new premium result elements natively
    const animElements = [
      resultsContent.querySelector('.rc-hero'),
      ...resultsContent.querySelectorAll('.rc-metric'),
      resultsContent.querySelector('.rc-bars'),
      resultsContent.querySelector('.result-cta')
    ];

    animElements.forEach((el, i) => {
      if (!el) return;
      el.style.opacity = '0';
      el.style.transform = 'translateY(15px)';
      setTimeout(() => {
        el.style.transition = 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)';
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      }, i * 80);
    });

    // Trigger progress bar animations (after elements appear)
    const billBar = document.getElementById('rBillBar');
    const cleanBar = document.getElementById('rCleanBar');
    if (billBar && cleanBar) {
      billBar.style.width = '0%';
      cleanBar.style.width = '0%';
      setTimeout(() => {
        billBar.style.width = '92%';
        cleanBar.style.width = '88%';
      }, 300);
    }
  }

  if (calcBtn) {
    calcBtn.addEventListener('click', calculateSavings);
    monthlyBillInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') calculateSavings();
    });
  }

  // Shake animation style
  const shakeStyle = document.createElement('style');
  shakeStyle.textContent = `
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20% { transform: translateX(-8px); }
      40% { transform: translateX(8px); }
      60% { transform: translateX(-5px); }
      80% { transform: translateX(5px); }
    }
  `;
  document.head.appendChild(shakeStyle);

  /* ─── Contact Form ─── */
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('fullName').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const city = document.getElementById('city').value.trim();
      const bill = document.getElementById('bill').value.trim();

      // Basic validation
      let hasError = false;
      [
        { el: document.getElementById('fullName'), val: name },
        { el: document.getElementById('phone'), val: phone },
        { el: document.getElementById('city'), val: city },
        { el: document.getElementById('bill'), val: bill },
      ].forEach(({ el, val }) => {
        if (!val) {
          el.style.borderColor = '#EF4444';
          hasError = true;
          setTimeout(() => el.style.borderColor = '', 2000);
        }
      });

      if (hasError) return;

      // Phone validation
      if (!/^[6-9]\d{9}$/.test(phone.replace(/\s/g, ''))) {
        const phoneEl = document.getElementById('phone');
        phoneEl.style.borderColor = '#EF4444';
        phoneEl.placeholder = 'Enter valid 10-digit mobile number';
        setTimeout(() => { phoneEl.style.borderColor = ''; phoneEl.placeholder = 'e.g. 98765 43210'; }, 3000);
        return;
      }

      // Simulate form submission
      const submitBtn = document.getElementById('submitBtn');
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
      submitBtn.disabled = true;

      setTimeout(() => {
        contactForm.classList.add('hidden');
        formSuccess.classList.remove('hidden');
      }, 1800);
    });
  }

  /* ─── Smooth scroll for anchor links ─── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ─── Active nav link highlight ─── */
  const sections = document.querySelectorAll('section[id]');
  const navLinksAll = document.querySelectorAll('.nav-links a');

  const activeSectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinksAll.forEach(link => {
          link.style.color = '';
          if (link.getAttribute('href') === '#' + entry.target.id) {
            link.style.color = 'var(--clr-orange)';
          }
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => activeSectionObserver.observe(s));

  /* ─── Legal Modals ─── */
  const linkPrivacy = document.getElementById('linkPrivacy');
  const linkTerms = document.getElementById('linkTerms');
  const modalOverlay = document.getElementById('modalOverlay');
  const modalPrivacy = document.getElementById('modalPrivacy');
  const modalTerms = document.getElementById('modalTerms');
  const closeBtns = document.querySelectorAll('.modal-close');

  function openModal(modalEl) {
    if (!modalEl || !modalOverlay) return;
    modalOverlay.classList.add('active');
    modalEl.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
  }

  function closeAllModals() {
    if (!modalOverlay) return;
    modalOverlay.classList.remove('active');
    if (modalPrivacy) modalPrivacy.classList.remove('active');
    if (modalTerms) modalTerms.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (linkPrivacy) {
    linkPrivacy.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(modalPrivacy);
    });
  }

  if (linkTerms) {
    linkTerms.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(modalTerms);
    });
  }

  closeBtns.forEach(btn => {
    btn.addEventListener('click', closeAllModals);
  });

  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeAllModals();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAllModals();
  });

});
