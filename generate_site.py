from pathlib import Path
import json

root = Path(r"f:\BBA")

# Create required dirs
for folder in [
    "css", "js", "assets/images", "assets/icons", "assets/favicon",
    "services", "industries", "projects"
]:
    (root / folder).mkdir(parents=True, exist_ok=True)

# Shared CSS
style_css = '''
:root {
  --bg: #09090B;
  --bg-alt: #111116;
  --panel: #17171F;
  --line: rgba(255,255,255,0.08);
  --text: #FAFAFA;
  --muted: #A1A1AA;
  --violet: #A78BFA;
  --cyan: #8BE9FD;
  --shadow: 0 24px 70px rgba(8,7,17,0.52);
  --radius: 30px;
  --container: min(1200px, calc(100% - 2rem));
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: "Inter", Arial, sans-serif;
  background: radial-gradient(circle at top, rgba(167,139,250,0.12), transparent 25%), var(--bg);
  color: var(--text);
  line-height: 1.7;
}
body::before {
  content: "";
  position: fixed; inset: 0;
  background-image: linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 42px 42px;
  pointer-events: none;
}
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
button, input, select, textarea { font: inherit; }
.container { width: var(--container); margin: 0 auto; }
.section { padding: 5rem 0; }
.section + .section { border-top: 1px solid var(--line); }
.eyebrow {
  display: inline-block; padding: 0.5rem 0.8rem; border-radius: 999px;
  border: 1px solid rgba(139,233,253,0.25); background: rgba(139,233,253,0.08); color: var(--cyan);
  font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 700;
}
h1, h2, h3, h4 { margin: 0 0 1rem; font-family: "Space Grotesk", Arial, sans-serif; letter-spacing: -0.04em; line-height: 1.05; }
h1 { font-size: clamp(2.7rem, 5vw, 5rem); }
h2 { font-size: clamp(2.1rem, 4vw, 3.2rem); }
h3 { font-size: clamp(1.25rem, 2vw, 1.7rem); }
p { margin: 0 0 1rem; color: var(--muted); }
.lead { font-size: 1.02rem; color: var(--muted); }
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  padding: 0.9rem 1.35rem; border-radius: 999px; border: 1px solid transparent; transition: 0.2s ease; font-weight: 600;
}
.btn:hover { transform: translateY(-1px); }
.btn-primary {
  background: linear-gradient(135deg, var(--violet), #c4b5fd); color: #120d1c; box-shadow: 0 18px 35px rgba(167,139,250,0.28);
}
.btn-secondary {
  background: rgba(255,255,255,0.02); border-color: var(--line); color: var(--text);
}

.topbar {
  position: sticky; top: 0; z-index: 50; backdrop-filter: blur(16px); background: rgba(9,9,11,0.7); border-bottom: 1px solid rgba(255,255,255,0.06);
}
.topbar-inner {
  width: var(--container); margin: 0 auto; min-height: 78px; display: flex; align-items: center; justify-content: space-between; gap: 1rem;
}
.brand {
  display: inline-flex; align-items: center; gap: 0.7rem; font-weight: 700; font-family: "Space Grotesk", Arial, sans-serif; letter-spacing: -0.04em;
}
.brand-logo { width: clamp(125px, 16vw, 190px); height: auto; }
.brand-mark {
  width: 2.2rem; height: 2.2rem; display: inline-grid; place-items: center; border-radius: 14px; background: linear-gradient(135deg, rgba(167,139,250,0.25), rgba(139,233,253,0.18)); border: 1px solid rgba(255,255,255,0.08);
}
.brand-mark::before { content: "B"; }

.nav-panel { display: flex; align-items: center; gap: 1rem; }
.main-nav {
  display: flex; align-items: center; gap: 1.2rem; flex-wrap: wrap;
}
.nav-link, .nav-dropdown-toggle {
  background: transparent; border: 0; color: var(--muted); cursor: pointer; font-size: 0.94rem; padding: 0.25rem 0;
}
.nav-link:hover, .nav-dropdown-toggle:hover { color: var(--text); }
.nav-dropdown { position: relative; }
.nav-menu {
  position: absolute; top: calc(100% + 0.6rem); left: 0;
  min-width: 220px; padding: 0.8rem; border-radius: 18px; background: rgba(17,17,22,0.96); border: 1px solid var(--line); box-shadow: var(--shadow); display: none;
}
.nav-dropdown.is-open .nav-menu { display: grid; }
.nav-menu a { display: block; padding: 0.6rem 0.7rem; border-radius: 10px; color: var(--muted); }
.nav-menu a:hover { background: rgba(255,255,255,0.04); color: var(--text); }
.nav-toggle { display: none; }

.hero { padding-top: 5rem; }
.hero-grid {
  display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 2rem; align-items: center;
}
.hero-actions { display: flex; flex-wrap: wrap; gap: 0.9rem; margin: 1.6rem 0; }
.hero-meta { display: flex; flex-wrap: wrap; gap: 1.5rem; color: var(--muted); font-size: 0.9rem; }
.hero-meta strong { color: var(--text); display: block; font-size: 1.5rem; }
.hero-meta > div { min-width: 110px; }
.hero-panel img { width: 100%; min-height: 320px; object-fit: cover; }
.hero-visual {
  position: relative; min-height: 480px; border-radius: 32px; border: 1px solid var(--line); background: linear-gradient(135deg, rgba(167,139,250,0.1), rgba(139,233,253,0.08), rgba(17,17,31,0.9)); box-shadow: var(--shadow); padding: 1rem; display: grid; place-items: center;
}
.hero-panel {
  width: min(100%, 430px); border-radius: 28px; border: 1px solid rgba(255,255,255,0.08); background: rgba(17,17,31,0.94); padding: 1rem; box-shadow: var(--shadow);
}
.hero-panel img { border-radius: 22px; }
.mini-stats {
  position: absolute; bottom: 1rem; left: 1rem; padding: 0.9rem 1rem; border-radius: 18px; background: rgba(9,9,11,0.86); border: 1px solid rgba(255,255,255,0.08);
}
.mini-stats strong { display: block; font-size: 1.5rem; }
.service-card { min-height: 100%; display: flex; flex-direction: column; }
.service-card .card-footer { margin-top: auto; padding-top: 1.2rem; }
.service-symbol {
  width: 3rem; height: 3rem; display: grid; place-items: center; margin-bottom: 1.2rem;
  border-radius: 16px; color: var(--cyan); font-size: 1.35rem; font-weight: 700;
  background: linear-gradient(135deg, rgba(167,139,250,0.22), rgba(139,233,253,0.1));
  border: 1px solid rgba(255,255,255,0.08);
}
.detail-band {
  display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 0.8rem;
  padding: 1rem; border: 1px solid var(--line); border-radius: 24px;
  background: linear-gradient(110deg, rgba(167,139,250,0.08), rgba(139,233,253,0.04));
}
.detail-band span {
  padding: 0.7rem 1rem; border-right: 1px solid var(--line);
  color: var(--muted); text-align: center; font-size: 0.86rem;
}
.detail-band span:last-child { border-right: 0; }
.step-card { position: relative; overflow: hidden; min-height: 220px; }
.step-card::after {
  content: ""; position: absolute; width: 120px; height: 120px; right: -30px; bottom: -45px;
  border-radius: 50%; background: radial-gradient(circle, rgba(167,139,250,0.2), transparent 70%);
}
.section-header { max-width: 760px; margin-bottom: 2rem; }
.section-header p { max-width: 650px; }
.section-cta { margin-top: 2rem; }
.service-detail-grid { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 1.4rem; }
.service-detail-card { min-height: 100%; }
.service-detail-card .list { margin-top: 1rem; }
.soft-panel {
  padding: clamp(1.5rem, 4vw, 3rem); border-radius: 30px;
  background: radial-gradient(circle at 90% 10%, rgba(167,139,250,0.16), transparent 35%), linear-gradient(140deg, rgba(23,23,31,0.96), rgba(12,12,18,0.96));
  border: 1px solid var(--line); box-shadow: var(--shadow);
}

.grid-3, .grid-4 { display: grid; gap: 1.4rem; }
.grid-3 { grid-template-columns: repeat(3, minmax(0,1fr)); }
.grid-4 { grid-template-columns: repeat(4, minmax(0,1fr)); }
.card {
  padding: 1.5rem; border-radius: var(--radius); background: linear-gradient(180deg, rgba(23,23,31,0.95), rgba(17,17,31,0.88)); border: 1px solid rgba(255,255,255,0.08); box-shadow: var(--shadow);
}
.card-topline {
  display: flex; align-items: center; justify-content: space-between; gap: 0.8rem; margin-bottom: 1rem; color: var(--muted); font-size: 0.76rem; letter-spacing: 0.08em; text-transform: uppercase;
}
.tag {
  display: inline-flex; align-items: center; padding: 0.35rem 0.7rem; border-radius: 999px; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02); color: var(--muted); font-size: 0.68rem; letter-spacing: 0.08em; text-transform: uppercase;
}
.card-footer { display: flex; justify-content: space-between; align-items: center; gap: 1rem; margin-top: 1rem; color: var(--muted); }
.card-footer a { color: var(--text); font-weight: 600; }
.work-grid { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 1.5rem; }
.media-box { border-radius: 22px; overflow: hidden; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 1rem; }

.split-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; }
.point-item, .step-item, .info-item {
  display: grid; grid-template-columns: auto 1fr; gap: 1rem; align-items: start; padding: 1rem; border-radius: 18px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08);
}
.point-number, .step-index {
  width: 2.5rem; height: 2.5rem; border-radius: 14px; display: grid; place-items: center; background: linear-gradient(135deg, rgba(167,139,250,0.28), rgba(139,233,253,0.15)); font-weight: 700;
}
.faq { display: grid; gap: 0.8rem; }
.faq-item { border-radius: 18px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); overflow: hidden; }
.faq-question {
  width: 100%; background: transparent; color: var(--text); border: 0; text-align: left; padding: 1.15rem 1.25rem; font-weight: 600; display: flex; justify-content: space-between; align-items: center; cursor: pointer;
}
.faq-answer { display: none; padding: 0 1.25rem 1.1rem; color: var(--muted); }
.faq-item.is-open .faq-answer { display: block; }

.pricing-grid { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 1.5rem; }
.pricing-card { position: relative; }
.pricing-card.featured { border-color: rgba(167,139,250,0.4); }
.price { display: flex; align-items: end; gap: 0.2rem; font-size: clamp(2rem, 3vw, 3rem); font-family: "Space Grotesk", Arial, sans-serif; letter-spacing: -0.05em; margin: 1rem 0; }
.price small { font-size: 1rem; color: var(--muted); }
.pricing-card ul, .list { list-style: none; padding: 0; margin: 1.2rem 0 0; display: grid; gap: 0.7rem; }
.pricing-card li::before, .list li::before {
  content: "✓"; color: var(--cyan); margin-right: 0.7rem;
}
.contact-layout, .project-layout { display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 2rem; }
.form-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 1rem; }
.field { display: grid; gap: 0.4rem; }
.field.full { grid-column: 1 / -1; }
label { color: var(--muted); font-size: 0.9rem; }
input, select, textarea {
  width: 100%; padding: 0.9rem 1rem; border-radius: 14px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.03); color: var(--text);
}
textarea { min-height: 160px; resize: vertical; }
input:focus, select:focus, textarea:focus { outline: none; border-color: rgba(139,233,253,0.55); box-shadow: 0 0 0 4px rgba(139,233,253,0.08); }
.error-message { min-height: 1rem; color: #ff9e9e; font-size: 0.78rem; }
.page-header { padding: 4rem 0 2rem; border-bottom: 1px solid rgba(255,255,255,0.04); }
.page-header-inner { width: var(--container); margin: 0 auto; }
.process-steps { display: grid; gap: 1rem; }
.process-step { display: grid; grid-template-columns: 80px 1fr; gap: 1rem; padding: 1.2rem; border-radius: 22px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); }
.process-step .step-number {
  width: 80px; height: 80px; border-radius: 22px; display: grid; place-items: center; background: linear-gradient(135deg, rgba(167,139,250,0.28), rgba(139,233,253,0.15)); font-weight: 700; font-size: 1.4rem;
}
.project-visual {
  border-radius: 28px; overflow: hidden; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02); box-shadow: var(--shadow);
}
.footer { padding: 2.5rem 0 3rem; border-top: 1px solid rgba(255,255,255,0.05); }
.footer-grid { width: var(--container); margin: 0 auto; display: grid; grid-template-columns: 1.3fr .9fr .9fr .9fr; gap: 1.5rem; }
.footer-column h4 { margin-bottom: 1rem; color: var(--muted); font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.10em; }
.footer-bottom { width: var(--container); margin: 1.5rem auto 0; padding-top: 1.2rem; border-top: 1px solid rgba(255,255,255,0.06); display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; color: var(--muted); }

@media (max-width: 980px) {
  .hero-grid, .split-layout, .contact-layout, .project-layout, .pricing-grid, .work-grid { grid-template-columns: 1fr; }
  .grid-3 { grid-template-columns: 1fr 1fr; }
  .grid-4, .detail-band, .service-detail-grid { grid-template-columns: 1fr 1fr; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 760px) {
  .nav-toggle { display: inline-flex; }
  .nav-panel {
    position: absolute; top: 78px; left: 1rem; right: 1rem; background: rgba(17,17,22,0.96); border: 1px solid var(--line); border-radius: 18px; padding: 1rem; display: none; flex-direction: column; align-items: stretch;
  }
  body.nav-open .nav-panel { display: flex; }
  .main-nav { flex-direction: column; align-items: stretch; }
  .nav-dropdown { width: 100%; }
  .nav-menu { position: static; display: none; margin-top: 0.5rem; }
  .nav-dropdown.is-open .nav-menu { display: grid; }
  .grid-3, .grid-4, .form-grid, .footer-grid, .detail-band, .service-detail-grid { grid-template-columns: 1fr; }
  .detail-band span { border-right: 0; border-bottom: 1px solid var(--line); }
  .detail-band span:last-child { border-bottom: 0; }
  .hero { padding-top: 3.2rem; }
  .hero-actions { flex-direction: column; align-items: flex-start; }
  .process-step { grid-template-columns: 1fr; }
}
'''

responsive_css = '''
@media (max-width: 980px) {
  .work-grid, .pricing-grid { grid-template-columns: 1fr 1fr; }
  .nav-toggle { display: inline-flex; }
  .nav-panel {
    position: absolute; top: 78px; left: 1rem; right: 1rem; background: rgba(17,17,22,0.96); border: 1px solid var(--line); border-radius: 18px; padding: 1rem; display: none; flex-direction: column; align-items: stretch;
  }
  body.nav-open .nav-panel { display: flex; }
  .main-nav { flex-direction: column; align-items: stretch; }
  .nav-dropdown { width: 100%; }
  .nav-menu { position: static; display: none; margin-top: 0.5rem; }
  .nav-dropdown.is-open .nav-menu { display: grid; }
}
@media (max-width: 760px) {
  .topbar-inner { min-height: 68px; }
  .card, .pricing-card, .contact-layout .card { padding: 1.2rem; }
  .work-grid { grid-template-columns: 1fr; }
}
'''

pages_css = '''
.page-shell { padding-top: 2rem; }
.filter-bar { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 2rem; }
.filter-btn.is-active {
  background: linear-gradient(135deg, rgba(167,139,250,0.16), rgba(139,233,253,0.1));
  border-color: rgba(167,139,250,0.42);
  color: var(--text);
}
.inline-list { display: flex; flex-wrap: wrap; gap: 0.6rem; }
.inline-list span {
  padding: 0.45rem 0.7rem; border-radius: 999px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); color: var(--muted);
}
.maintenance-hero { padding: clamp(3rem, 8vw, 7rem) 0; }
.maintenance-layout { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: clamp(2rem, 6vw, 6rem); align-items: center; }
.maintenance-visual { min-width: 0; padding: 1rem; border: 1px solid var(--line); border-radius: 32px; background: linear-gradient(145deg, rgba(167,139,250,0.13), rgba(139,233,253,0.06)); box-shadow: var(--shadow); }
.maintenance-visual img { width: 100%; height: auto; border: 1px solid var(--line); border-radius: 24px; }
.maintenance-copy { max-width: 600px; }
.maintenance-copy h1 { font-size: clamp(2.7rem, 5vw, 4.7rem); }
.maintenance-status { display: inline-flex; align-items: center; gap: 0.6rem; }
.maintenance-status::before { content: ""; width: 0.6rem; height: 0.6rem; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 1rem rgba(139,233,253,0.7); }
.maintenance-card { margin: 1.5rem 0; }
.maintenance-card p { margin-bottom: 0; }
.maintenance-card .card-topline { margin-bottom: 0.4rem; }
.maintenance-card .progress-track { height: 0.55rem; margin: 1rem 0; overflow: hidden; border-radius: 999px; background: rgba(255,255,255,0.08); }
.maintenance-card .progress-fill { display: block; width: 68%; height: 100%; border-radius: inherit; background: linear-gradient(90deg, var(--violet), var(--cyan)); }
.maintenance-card .progress-foot { display: flex; justify-content: space-between; align-items: center; color: var(--muted); font-size: 0.85rem; }
.maintenance-card .pulse { color: var(--cyan); }
.maintenance-capabilities { padding-top: 1rem; }
.profile-details { display: grid; gap: 0.65rem; }
.profile-details p { margin: 0; }
.profile-links { display: flex; flex-wrap: wrap; gap: 0.8rem; }
@media (max-width: 760px) {
  .maintenance-layout { grid-template-columns: 1fr; }
  .maintenance-copy { order: -1; }
  .maintenance-visual { max-width: 560px; margin: 0 auto; }
}
'''

(root / 'css' / 'style.css').write_text(style_css, encoding='utf-8')
(root / 'css' / 'responsive.css').write_text(responsive_css, encoding='utf-8')
(root / 'css' / 'pages.css').write_text(pages_css, encoding='utf-8')

# JS
main_js = '''
document.addEventListener('DOMContentLoaded', function () {
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  document.querySelectorAll('.filter-btn').forEach(function (button) {
    button.addEventListener('click', function () {
      const filter = button.dataset.filter;
      document.querySelectorAll('.filter-btn').forEach((btn) => btn.classList.toggle('is-active', btn === button));
      document.querySelectorAll('[data-category]').forEach((card) => {
        const show = filter === 'all' || card.dataset.category === filter;
        card.style.display = show ? '' : 'none';
      });
    });
  });

  document.querySelectorAll('.faq-question').forEach(function (button) {
    button.addEventListener('click', function () {
      const item = button.closest('.faq-item');
      if (!item) return;
      const open = item.classList.contains('is-open');
      document.querySelectorAll('.faq-item').forEach(function (faqItem) {
        faqItem.classList.remove('is-open');
      });
      if (!open) item.classList.add('is-open');
    });
  });
});
'''
nav_js = '''
document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.querySelector('.nav-toggle');
  const body = document.body;
  if (toggle) {
    toggle.addEventListener('click', function () {
      body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', String(body.classList.contains('nav-open')));
    });
  }

  document.querySelectorAll('.nav-dropdown').forEach(function (dropdown) {
    const trigger = dropdown.querySelector('.nav-dropdown-toggle');
    if (!trigger) return;
    trigger.addEventListener('click', function (event) {
      event.stopPropagation();
      const forced = dropdown.classList.contains('is-open');
      document.querySelectorAll('.nav-dropdown').forEach(function (item) {
        item.classList.remove('is-open');
        const btn = item.querySelector('.nav-dropdown-toggle');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
      if (!forced) {
        dropdown.classList.add('is-open');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
  });

  document.addEventListener('click', function (event) {
    if (!event.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown').forEach(function (item) {
        item.classList.remove('is-open');
        const btn = item.querySelector('.nav-dropdown-toggle');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
    }
  });
});
'''
forms_js = '''
document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('[data-contact-form]');
  if (!form) return;

  const setError = function (name, message) {
    const field = form.querySelector('[name="' + name + '"]');
    const messageNode = form.querySelector('[data-error-for="' + name + '"]');
    if (!field || !messageNode) return;
    field.setAttribute('aria-invalid', message ? 'true' : 'false');
    messageNode.textContent = message;
  };

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    let valid = true;

    const checks = [
      ['name', function (value) { return value.trim().length >= 2; }, 'Please enter your name.'],
      ['email', function (value) { return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(value.trim()); }, 'Please enter a valid email address.'],
      ['service', function (value) { return value.trim().length > 0; }, 'Please choose a service.'],
      ['budget', function (value) { return value.trim().length > 0; }, 'Please choose a budget range.'],
      ['details', function (value) { return value.trim().length >= 20; }, 'Please share a few more details about your project.'],
    ];

    checks.forEach(function ([name, validator, message]) {
      const field = form.querySelector('[name="' + name + '"]');
      const value = field ? field.value : '';
      if (!validator(value)) {
        setError(name, message);
        valid = false;
      } else {
        setError(name, '');
      }
    });

    if (valid) {
      const params = new URLSearchParams({
        subject: 'Built By Amos project enquiry',
        body: [
          'Name: ' + form.querySelector('[name="name"]').value,
          'Email: ' + form.querySelector('[name="email"]').value,
          'Service: ' + form.querySelector('[name="service"]').value,
          'Budget: ' + form.querySelector('[name="budget"]').value,
          '',
          'Project details:',
          form.querySelector('[name="details"]').value,
        ].join('\\n')
      });
      window.location.href = 'mailto:hello@builtbyamos.in?' + params.toString();
    }
  });
});
'''

(root / 'js' / 'main.js').write_text(main_js, encoding='utf-8')
(root / 'js' / 'navigation.js').write_text(nav_js, encoding='utf-8')
(root / 'js' / 'forms.js').write_text(forms_js, encoding='utf-8')

# Assets
svg_hero = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 760"><defs><linearGradient id="g" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#A78BFA"/><stop offset="1" stop-color="#8BE9FD"/></linearGradient></defs><rect width="900" height="760" fill="#101015"/><circle cx="640" cy="180" r="190" fill="url(#g)" opacity="0.35"/><rect x="130" y="150" width="620" height="430" rx="36" fill="#17171F" stroke="rgba(255,255,255,0.12)"/><rect x="170" y="190" width="540" height="310" rx="28" fill="#0E0E13"/><rect x="190" y="215" width="150" height="18" rx="9" fill="#A78BFA" opacity="0.8"/><rect x="190" y="250" width="220" height="12" rx="6" fill="#FAFAFA" opacity="0.22"/><rect x="190" y="278" width="260" height="12" rx="6" fill="#FAFAFA" opacity="0.15"/><rect x="190" y="332" width="480" height="130" rx="20" fill="url(#g)" opacity="0.2"/><rect x="670" y="510" width="70" height="70" rx="18" fill="#8BE9FD" opacity="0.18"/><rect x="510" y="542" width="150" height="16" rx="8" fill="#FAFAFA" opacity="0.15"/></svg>'''
svg_fashion = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 700"><rect width="900" height="700" fill="#111116"/><rect x="80" y="90" width="740" height="520" rx="28" fill="#17171F" stroke="rgba(255,255,255,0.1)"/><rect x="120" y="130" width="180" height="440" rx="18" fill="#0d0d11"/><rect x="330" y="130" width="440" height="110" rx="18" fill="#1f1f2b"/><rect x="330" y="270" width="200" height="210" rx="22" fill="#A78BFA" opacity="0.22"/><rect x="550" y="270" width="200" height="210" rx="22" fill="#8BE9FD" opacity="0.14"/><rect x="140" y="165" width="140" height="16" rx="8" fill="#FAFAFA" opacity="0.28"/><rect x="140" y="208" width="110" height="12" rx="6" fill="#FAFAFA" opacity="0.12"/><rect x="140" y="240" width="115" height="12" rx="6" fill="#FAFAFA" opacity="0.12"/><rect x="360" y="160" width="170" height="20" rx="10" fill="#FAFAFA" opacity="0.25"/><rect x="560" y="160" width="150" height="20" rx="10" fill="#FAFAFA" opacity="0.18"/></svg>'''
svg_fitness = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 700"><rect width="900" height="700" fill="#111116"/><rect x="60" y="70" width="780" height="560" rx="30" fill="#17171F"/><rect x="100" y="120" width="700" height="90" rx="18" fill="#0d0d11"/><rect x="100" y="245" width="220" height="290" rx="18" fill="#A78BFA" opacity="0.18"/><rect x="340" y="245" width="220" height="290" rx="18" fill="#8BE9FD" opacity="0.1"/><rect x="580" y="245" width="220" height="290" rx="18" fill="#17171F" stroke="rgba(255,255,255,0.08)"/><rect x="130" y="145" width="160" height="18" rx="9" fill="#FAFAFA" opacity="0.24"/><rect x="130" y="286" width="160" height="120" rx="16" fill="#111116"/><rect x="380" y="286" width="140" height="120" rx="16" fill="#111116"/><rect x="610" y="286" width="160" height="120" rx="16" fill="#111116"/><circle cx="260" cy="430" r="44" fill="#8BE9FD" opacity="0.2"/><circle cx="500" cy="430" r="42" fill="#A78BFA" opacity="0.2"/></svg>'''
svg_beauty = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 700"><rect width="900" height="700" fill="#111116"/><rect x="80" y="90" width="740" height="520" rx="32" fill="#17171F"/><rect x="120" y="135" width="660" height="120" rx="24" fill="#0d0d11"/><rect x="120" y="288" width="220" height="250" rx="22" fill="#A78BFA" opacity="0.18"/><rect x="360" y="288" width="200" height="250" rx="22" fill="#8BE9FD" opacity="0.12"/><rect x="580" y="288" width="200" height="250" rx="22" fill="#17171F" stroke="rgba(255,255,255,0.08)"/><rect x="150" y="165" width="170" height="18" rx="9" fill="#FAFAFA" opacity="0.25"/><rect x="150" y="332" width="160" height="150" rx="14" fill="#111116"/><rect x="390" y="332" width="140" height="150" rx="14" fill="#111116"/><rect x="610" y="332" width="140" height="150" rx="14" fill="#111116"/></svg>'''
for file_name, svg in {
    'hero-abstract.svg': svg_hero,
    'fashion-store.svg': svg_fashion,
    'fitness-website.svg': svg_fitness,
    'beauty-store.svg': svg_beauty,
}.items():
    (root / 'assets' / 'images' / file_name).write_text(svg, encoding='utf-8')

(root / 'assets' / 'favicon' / 'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="18" fill="#09090B"/><rect x="10" y="10" width="44" height="44" rx="14" fill="url(#g)" opacity="0.18"/><path d="M23 18h18l-6 28h-7l2-9h-8l-6 9h-8l6-28Zm6 8h6l-1.6 12h-6L29 26Z" fill="#FAFAFA"/><defs><linearGradient id="g" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#A78BFA"/><stop offset="1" stop-color="#8BE9FD"/></linearGradient></defs></svg>''', encoding='utf-8')

# Page builder

def nav(prefix: str) -> str:
    return f'''
    <nav class="topbar" aria-label="Main navigation">
      <div class="topbar-inner">
        <a href="{prefix}index.html" class="brand" aria-label="Built By Amos home">
          <img class="brand-logo" src="{prefix}assets/images/BuiltByAmos-Wordmark.png" alt="Built By Amos" />
        </a>

        <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false">Menu</button>

        <div class="nav-panel">
          <div class="main-nav">
            <a href="{prefix}index.html" class="nav-link">Home</a>

            <div class="nav-dropdown">
              <button class="nav-dropdown-toggle" type="button" aria-expanded="false">Services ▾</button>
              <div class="nav-menu">
                <a href="{prefix}services/index.html">All Services</a>
                <a href="{prefix}services/website-development.html">Website Development</a>
                <a href="{prefix}services/app-development.html">App Development</a>
                <a href="{prefix}services/custom-software.html">Custom Software</a>
              </div>
            </div>

            <div class="nav-dropdown">
              <button class="nav-dropdown-toggle" type="button" aria-expanded="false">Industries ▾</button>
              <div class="nav-menu">
                <a href="{prefix}industries/index.html">All Industries</a>
                <a href="{prefix}industries/fashion.html">Fashion</a>
                <a href="{prefix}industries/fitness.html">Fitness</a>
                <a href="{prefix}industries/beauty.html">Beauty</a>
                <a href="{prefix}industries/jewellery.html">Jewellery</a>
              </div>
            </div>

            <a href="{prefix}work.html" class="nav-link">Our Work</a>
            <a href="{prefix}about.html" class="nav-link">About</a>
            <a href="{prefix}about-amos/" class="nav-link">Amos Anand</a>
            <a href="{prefix}pricing.html" class="nav-link">Pricing</a>
            <a href="{prefix}contact.html" class="nav-link">Contact</a>
          </div>
          <a href="{prefix}contact.html" class="btn btn-primary">Start a Project</a>
        </div>
      </div>
    </nav>
    '''

def footer(prefix: str) -> str:
    return f'''
    <footer class="footer">
      <div class="footer-grid">
        <div class="footer-column">
          <a href="{prefix}index.html" class="brand" aria-label="Built By Amos home"><img class="brand-logo" src="{prefix}assets/images/BuiltByAmos-Wordmark.png" alt="Built By Amos" /></a>
          <p>Premium digital experiences for ambitious brands in fashion, fitness, beauty, and beyond.</p>
          <p style="font-size:0.8rem; line-height:1.6; color: var(--muted);">Stock imagery is used for concept presentation only and should be reviewed before production deployment. Source: Unsplash.</p>
        </div>
        <div class="footer-column">
          <h4>Services</h4>
          <p><a href="{prefix}services/website-development.html">Website development</a></p>
          <p><a href="{prefix}services/app-development.html">App development</a></p>
          <p><a href="{prefix}services/custom-software.html">Custom software</a></p>
        </div>
        <div class="footer-column">
          <h4>Company</h4>
          <p><a href="{prefix}about.html">About</a></p>
          <p><a href="{prefix}about-amos/">Founder: Amos Anand</a></p>
          <p><a href="{prefix}work.html">Work</a></p>
          <p><a href="{prefix}pricing.html">Pricing</a></p>
        </div>
        <div class="footer-column">
          <h4>Contact</h4>
          <p><a href="mailto:hello@builtbyamos.in">hello@builtbyamos.in</a></p>
          <p><a href="mailto:builtbyamos@gmail.com">builtbyamos@gmail.com</a></p>
          <p><a href="https://www.instagram.com/built.byamos/" target="_blank" rel="noopener noreferrer">Instagram ↗</a></p>
          <p><a href="{prefix}contact.html">Request a quote</a></p>
          <p><a href="{prefix}privacy-policy.html">Privacy Policy</a></p>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year"></span> Built By Amos</span>
        <span><a href="{prefix}terms.html">Terms</a> · <a href="{prefix}privacy-policy.html">Privacy</a></span>
      </div>
    </footer>
    '''

def render(title: str, description: str, content: str, prefix: str = "", canonical: str = "", structured_data: str = "") -> str:
    css_path = f"{prefix}css/" if prefix else "css/"
    js_path = f"{prefix}js/" if prefix else "js/"
    metadata = ""
    if canonical:
        metadata = f'''
    <link rel="canonical" href="{canonical}" />
    <meta property="og:type" content="profile" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="{canonical}" />
    <meta property="og:site_name" content="Built By Amos" />
    <meta property="og:image" content="https://builtbyamos.in/assets/images/BuiltByAmos-Wordmark.png" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{description}" />
    <meta name="twitter:image" content="https://builtbyamos.in/assets/images/BuiltByAmos-Wordmark.png" />
    {structured_data}'''
    return f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{description}" />
    <title>{title}</title>
    {metadata}
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
    <link rel="icon" type="image/png" sizes="512x512" href="{prefix}assets/favicon/BuiltByAmos-Favicon.png" />
    <link rel="stylesheet" href="{css_path}style.css" />
    <link rel="stylesheet" href="{css_path}responsive.css" />
    <link rel="stylesheet" href="{css_path}pages.css" />
    <script defer src="{js_path}main.js"></script>
    <script defer src="{js_path}navigation.js"></script>
    <script defer src="{js_path}forms.js"></script>
  </head>
  <body>
    {nav(prefix)}
    {content}
    {footer(prefix)}
  </body>
</html>
'''

# Roots
home = '''
<main>
  <section class="hero section">
    <div class="container hero-grid">
      <div>
        <span class="eyebrow">Creative digital agency</span>
        <h1>We build what’s next.</h1>
        <p class="lead">Built By Amos creates premium websites, apps, and custom software for ambitious businesses that want digital experiences to feel sharper, clearer, and ready to grow.</p>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-primary">Book a discovery call</a>
          <a href="work.html" class="btn btn-secondary">View our work</a>
        </div>
        <div class="hero-meta">
          <div><strong>Strategy</strong>first principles</div>
          <div><strong>Design</strong>with clarity</div>
          <div><strong>Build</strong>for momentum</div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-panel">
          <img src="assets/images/hero-abstract.svg" alt="Abstract illustration of a digital product interface" />
        </div>
        <div class="mini-stats"><strong>Built for you</strong><span>Strategy to launch</span></div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:1rem;">
    <div class="container">
      <div class="detail-band" aria-label="Ways we can help">
        <span>Brand and website strategy</span>
        <span>Responsive web design</span>
        <span>Digital product experiences</span>
        <span>Custom business tools</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card" style="margin-bottom:1.5rem; padding:1.2rem;">
        <p style="margin:0; font-size:0.82rem; color: var(--muted);">Real lifestyle photography used for concept presentation only. Source: Unsplash. Final production assets should be licensed and reviewed before deployment.</p>
      </div>
      <div class="section-header">
        <span class="eyebrow">Core services</span>
        <h2>Design-led execution for digital growth.</h2>
      </div>
      <div class="grid-3">
        <article class="card service-card"><div class="service-symbol" aria-hidden="true">↗</div><div class="card-topline"><span>01 / Presence</span><span class="tag">Web</span></div><h3>Website Development</h3><p>Premium business websites and storefronts shaped around conversion, clarity, and brand presence.</p><div class="inline-list"><span>Strategy</span><span>UX/UI</span><span>Development</span></div><div class="card-footer"><span>Brand + UX</span><a href="services/website-development.html">Learn more</a></div></article>
        <article class="card service-card"><div class="service-symbol" aria-hidden="true">▣</div><div class="card-topline"><span>02 / Product</span><span class="tag">Mobile</span></div><h3>App Development</h3><p>Digital product experiences and app interfaces designed around real user journeys and product logic.</p><div class="inline-list"><span>User flows</span><span>Interfaces</span><span>Integrations</span></div><div class="card-footer"><span>Product + API</span><a href="services/app-development.html">Learn more</a></div></article>
        <article class="card service-card"><div class="service-symbol" aria-hidden="true">⌘</div><div class="card-topline"><span>03 / Operations</span><span class="tag">Systems</span></div><h3>Custom Software</h3><p>Dashboards, workflows, and business tools that support scale, efficiency, and sharper internal operations.</p><div class="inline-list"><span>Dashboards</span><span>Portals</span><span>Automation</span></div><div class="card-footer"><span>Operations</span><a href="services/custom-software.html">Learn more</a></div></article>
      </div>
      <div class="section-cta"><a href="services/index.html" class="btn btn-secondary">Explore all services</a></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">Selected work</span>
        <h2>Concepts for brands that want a more premium digital presence.</h2>
      </div>
      <div class="work-grid">
        <article class="card"><div class="media-box"><img src="https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=900&q=80" alt="Fashion storefront concept from real brand photography" /></div><div class="card-topline"><span>Fashion</span><span class="tag">Concept</span></div><h3>Streetwear storefront</h3><p>Editorial shopping experiences with stronger conversion and lifestyle storytelling.</p><div class="card-footer"><span>E-commerce</span><a href="projects/fashion-store.html">See project</a></div></article>
        <article class="card"><div class="media-box"><img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=900&q=80" alt="Fitness and gym brand photography" /></div><div class="card-topline"><span>Fitness</span><span class="tag">Concept</span></div><h3>Membership platform</h3><p>High-energy layouts for gyms, classes, and membership growth.</p><div class="card-footer"><span>Membership UX</span><a href="projects/fitness-website.html">See project</a></div></article>
        <article class="card"><div class="media-box"><img src="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=900&q=80" alt="Beauty and skincare product photography" /></div><div class="card-topline"><span>Beauty</span><span class="tag">Concept</span></div><h3>Skincare commerce</h3><p>Elegant, trust-led experiences built for product education and conversion.</p><div class="card-footer"><span>Commerce design</span><a href="projects/beauty-store.html">See project</a></div></article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">Industries</span>
        <h2>Built for modern brands and growth-stage businesses.</h2>
      </div>
      <div class="grid-4">
        <article class="card"><h3>Fashion & streetwear</h3><p>Luxury positioning and commerce design for highly visual, culture-driven brands.</p><div class="card-footer"><span>Retail strategy</span><a href="industries/fashion.html">Explore</a></div></article>
        <article class="card"><h3>Fitness & studios</h3><p>Membership flow and class booking experiences built to feel energetic and easy to join.</p><div class="card-footer"><span>Booking UX</span><a href="industries/fitness.html">Explore</a></div></article>
        <article class="card"><h3>Beauty & skincare</h3><p>Trust-building storefronts and product experiences for education-heavy purchasing journeys.</p><div class="card-footer"><span>Product storytelling</span><a href="industries/beauty.html">Explore</a></div></article>
        <article class="card"><h3>Jewellery & lifestyle</h3><p>Detail-led product presentation and considered shopping journeys for premium collections.</p><div class="card-footer"><span>Product presentation</span><a href="industries/jewellery.html">Explore</a></div></article>
      </div>
      <div class="section-cta"><a href="industries/index.html" class="btn btn-secondary">Explore industries</a></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">A thoughtful process</span>
        <h2>From first conversation to a confident launch.</h2>
        <p>Every project is shaped around its goals and scope. These are the typical stages that keep decisions clear and work moving.</p>
      </div>
      <div class="grid-4">
        <article class="card step-card"><div class="card-topline"><span>01</span><span class="tag">Align</span></div><h3>Discover</h3><p>Understand your audience, offer, priorities, and what the project needs to achieve.</p></article>
        <article class="card step-card"><div class="card-topline"><span>02</span><span class="tag">Plan</span></div><h3>Shape the direction</h3><p>Agree on the structure, content, user journeys, and visual approach before build.</p></article>
        <article class="card step-card"><div class="card-topline"><span>03</span><span class="tag">Create</span></div><h3>Design and build</h3><p>Turn the approved direction into a responsive experience and review it together.</p></article>
        <article class="card step-card"><div class="card-topline"><span>04</span><span class="tag">Launch</span></div><h3>Test and hand over</h3><p>Check key pages and interactions, prepare release, and share what you need to move forward.</p></article>
      </div>
      <div class="section-cta"><a href="process.html" class="btn btn-secondary">See our full process</a></div>
    </div>
  </section>

  <section class="section">
    <div class="container split-layout">
      <div>
        <span class="eyebrow">Why Built By Amos</span>
        <h2>Strategic thinking meets polished execution.</h2>
        <div class="point-item"><div class="point-number">1</div><div><h3>Clear positioning</h3><p>We sharpen your offer and message so the brand feels instantly more legible and premium.</p></div></div>
        <div class="point-item"><div class="point-number">2</div><div><h3>Lean collaboration</h3><p>We work efficiently, align decisively, and keep the process moving without unnecessary drag.</p></div></div>
        <div class="point-item"><div class="point-number">3</div><div><h3>Built to scale</h3><p>Every experience is designed to work for today but remain useful as the brand grows.</p></div></div>
      </div>
      <div class="card">
        <h3>Our approach</h3>
        <p>We don’t just design attractive screens. We build digital systems that help your business communicate more clearly, convert more consistently, and feel more premium at every touchpoint.</p>
        <ul class="list"><li>Discovery and positioning</li><li>UX strategy and concept design</li><li>Build, QA, and launch support</li></ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header"><span class="eyebrow">FAQ</span><h2>Questions before we begin?</h2></div>
      <div class="faq">
        <div class="faq-item"><button class="faq-question" type="button">What kinds of projects do you take on?<span>+</span></button><div class="faq-answer">We work with startup brands, modern retailers, service businesses, and digital-first companies that need premium websites, apps, and business tooling.</div></div>
        <div class="faq-item"><button class="faq-question" type="button">How does the process begin?<span>+</span></button><div class="faq-answer">Most projects begin with a short discovery conversation and project brief followed by a scope, timeline, and design direction.</div></div>
        <div class="faq-item"><button class="faq-question" type="button">Do you work across industries?<span>+</span></button><div class="faq-answer">Yes. We serve fashion, fitness, beauty, jewellery, startups, and broader businesses that need sharper digital positioning.</div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="card" style="text-align:center; padding:2rem;">
        <span class="eyebrow">Start your project</span>
        <h2>Ready to build what’s next?</h2>
        <p>Whether you need a premium website, a digital product concept, or a custom tool for your business, let’s shape the right next step.</p>
        <div class="hero-actions" style="justify-content:center;">
          <a href="contact.html" class="btn btn-primary">Request a quote</a>
          <a href="pricing.html" class="btn btn-secondary">See pricing</a>
        </div>
      </div>
    </div>
  </section>
</main>
'''

about = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">About Built By Amos · India</span><h1>Fashion-first digital experiences, built with care.</h1><p class="lead">Built By Amos is an independent digital studio helping ambitious fashion and lifestyle brands build a stronger online presence through distinctive digital storefronts, thoughtful responsive experiences, and clear communication.</p></div></section>
  <section class="section"><div class="container split-layout"><div><span class="eyebrow">The studio</span><h2>Strategy, design, and delivery under one roof.</h2><p>From shaping the first idea to preparing for launch, the focus is on creating a digital experience that feels like the brand and works for its customers.</p><p>That means pairing fashion-aware visual direction with useful structure, responsive design, and a straightforward project process. The studio can also support app experiences and custom tools where a project calls for them.</p><div class="inline-list"><span>Fashion</span><span>Clothing</span><span>Lifestyle</span><span>Digital products</span></div></div><div class="soft-panel"><span class="eyebrow">The person behind it</span><h2 style="margin-top:1rem;">Amos Anand</h2><p>Amos Anand is the founder of Built By Amos. Learn more about his work in the <a href="about-amos/">founder profile</a>.</p><a href="about-amos/" class="btn btn-secondary">Meet Amos Anand</a></div></div></section>
  <section class="section"><div class="container"><div class="section-header"><span class="eyebrow">What we focus on</span><h2>Brand character, customer experience, and practical execution.</h2></div><div class="grid-3"><article class="card"><div class="service-symbol" aria-hidden="true">✳</div><h3>Fashion-first design</h3><p>Distinctive digital storefronts for clothing and lifestyle brands, with visual storytelling that keeps the product and brand identity in focus.</p></article><article class="card"><div class="service-symbol" aria-hidden="true">↗</div><h3>Built for the customer</h3><p>Thoughtful responsive experiences that help people explore, understand, and take the next step across screen sizes.</p></article><article class="card"><div class="service-symbol" aria-hidden="true">→</div><h3>Made to move forward</h3><p>Clear communication from the first conversation to launch, with scope and priorities aligned along the way.</p></article></div></div></section>
  <section class="section"><div class="container"><div class="soft-panel"><span class="eyebrow">Let’s build together</span><h2>Have a fashion or lifestyle project in mind?</h2><p>Share what you are building, who it is for, and what you would like to improve. We can discuss a useful next step.</p><div class="hero-actions"><a href="contact.html" class="btn btn-primary">Start a project</a><a href="work.html" class="btn btn-secondary">View concepts</a></div></div></div></section>
</main>
'''

maintenance_home = '''
<main>
  <section class="hero section maintenance-hero">
    <div class="container maintenance-layout">
      <div class="maintenance-visual"><img src="assets/images/Built%20By%20Amos_%20Ideas%20to%20Real%20Solutions.png" alt="Built By Amos — Ideas to Real Solutions" fetchpriority="high" decoding="async" /></div>
      <div class="maintenance-copy">
        <span class="eyebrow maintenance-status">Website refresh in progress</span>
        <span class="eyebrow">Something better is taking shape</span>
        <h1>A better digital<br /><span>experience is on its way.</span></h1>
        <p class="lead">We're refreshing our website to bring you a sharper look at what we do. Built By Amos helps ambitious fashion and lifestyle brands build a stronger online presence. We'll be back soon.</p>
        <div class="card maintenance-card">
          <div class="card-topline"><span>Upgrading our digital home</span><span class="tag">In progress</span></div>
          <div class="progress-track" role="progressbar" aria-label="Website refresh in progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="68"><span class="progress-fill"></span></div>
          <div class="progress-foot"><span>Designing. Refining. Building.</span><span class="pulse" aria-hidden="true">●</span></div>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="mailto:hello@builtbyamos.in"><span>Discuss a project</span><span aria-hidden="true">↗</span></a>
          <a class="btn btn-secondary" href="https://www.instagram.com/built.byamos/" target="_blank" rel="noopener noreferrer">Follow our journey <span aria-hidden="true">↗</span></a>
        </div>
        <p>Have a project in mind? You can still reach us directly.</p>
        <p><a href="about-amos/">Meet Amos Anand, Founder of Built By Amos</a></p>
      </div>
    </div>
  </section>
  <section class="section maintenance-capabilities">
    <div class="container">
      <div class="section-header"><span class="eyebrow">Our focus</span><h2>Digital work, built with care.</h2></div>
      <div class="grid-3">
        <article class="card"><div class="card-topline"><span>01</span></div><h3>Fashion-first design</h3><p>Distinctive digital storefronts for clothing and lifestyle brands.</p></article>
        <article class="card"><div class="card-topline"><span>02</span></div><h3>Built for the customer</h3><p>Thoughtful, responsive experiences across screen sizes.</p></article>
        <article class="card"><div class="card-topline"><span>03</span></div><h3>Made to move forward</h3><p>Clear communication from the first conversation to launch.</p></article>
      </div>
    </div>
  </section>
</main>
'''

founder_profile = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Founder · Built By Amos · Ranchi, India</span><h1>Amos Anand</h1><p class="lead">Founder of Built By Amos, working on websites, apps, business software, and digital experiences for businesses.</p></div></section>
  <section class="section"><div class="container split-layout">
    <div><span class="eyebrow">About</span><h2>Building useful digital experiences.</h2><p>I’m Amos Anand, founder of Built By Amos, an independent digital studio based in Ranchi, Jharkhand, India. I work on website and app development, business software, and the design and implementation that help digital products serve their users.</p><p>My work through Built By Amos also includes UI/UX design, AI automation, SEO, and website maintenance. Each engagement is shaped around its actual goals and scope.</p><div class="hero-actions"><a href="../contact.html" class="btn btn-primary">Contact Built By Amos</a><a href="../index.html" class="btn btn-secondary">Back to Built By Amos</a></div></div>
    <aside class="card"><span class="eyebrow">Profile</span><div class="profile-details"><p><strong>Name:</strong> Amos Anand</p><p><strong>Role:</strong> Founder, Built By Amos</p><p><strong>Location:</strong> Ranchi, Jharkhand, India</p><p><strong>Website:</strong> <a href="https://builtbyamos.in/">builtbyamos.in</a></p></div></aside>
  </div></section>
  <section class="section"><div class="container">
    <div class="section-header"><span class="eyebrow">Services</span><h2>What I work on</h2><p>Services offered through Built By Amos include:</p></div>
    <div class="grid-3"><article class="card"><h3>Web and app development</h3><p>Website development, app development, and responsive digital product experiences.</p></article><article class="card"><h3>Business software and design</h3><p>Business software, workflow tools, and UI/UX design shaped around practical requirements.</p></article><article class="card"><h3>Ongoing digital support</h3><p>AI automation, SEO, and website maintenance.</p></article></div>
  </div></section>
  <section class="section"><div class="container">
    <div class="section-header"><span class="eyebrow">Selected work</span><h2>Projects and case studies</h2></div>
    <div class="card"><p>No verified client projects or case studies are currently available to feature here. Examples on the agency website are explicitly presented as design concepts, not completed client work.</p></div>
  </div></section>
  <section class="section"><div class="container">
    <div class="soft-panel"><span class="eyebrow">Connect</span><h2>Find Built By Amos online</h2><p>This is the agency’s official Instagram profile.</p><div class="profile-links"><a href="https://www.instagram.com/built.byamos/" target="_blank" rel="noopener noreferrer">@built.byamos on Instagram ↗</a><a href="../contact.html">Agency contact page</a></div></div>
  </div></section>
</main>
'''

contact = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Contact</span><h1>Tell us about your project.</h1><p class="lead">Share your goals, current challenges, and the type of experience you want to build. We’ll be in touch with next steps.</p></div></section>
  <section class="section"><div class="container contact-layout"><aside class="card"><span class="eyebrow">Built By Amos · India</span><h2>Start with a conversation.</h2><p>For project enquiries, email the studio or connect on Instagram.</p><div class="info-item"><div aria-hidden="true">✉</div><div><strong>Project enquiries</strong><p><a href="mailto:hello@builtbyamos.in">hello@builtbyamos.in</a></p></div></div><div class="info-item"><div aria-hidden="true">✉</div><div><strong>Alternate email</strong><p><a href="mailto:builtbyamos@gmail.com">builtbyamos@gmail.com</a></p></div></div><div class="info-item"><div aria-hidden="true">↗</div><div><strong>Instagram</strong><p><a href="https://www.instagram.com/built.byamos/" target="_blank" rel="noopener noreferrer">@built.byamos</a></p></div></div><h3 style="margin-top:1.5rem;">What happens next?</h3><div class="info-item"><div>1</div><div><strong>Share your brief</strong><p>Tell us what you need, the audience you serve, and what success looks like.</p></div></div><div class="info-item"><div>2</div><div><strong>Review scope</strong><p>We align on direction, priorities, timeline, budget, and a practical delivery plan.</p></div></div><div class="info-item"><div>3</div><div><strong>Move into build</strong><p>Once approved, we move into design, implementation, testing, and launch support.</p></div></div></aside><div class="card"><form data-contact-form novalidate><div class="form-grid"><div class="field"><label for="name">Name</label><input id="name" name="name" type="text" aria-invalid="false" /><div class="error-message" data-error-for="name"></div></div><div class="field"><label for="email">Email</label><input id="email" name="email" type="email" aria-invalid="false" /><div class="error-message" data-error-for="email"></div></div><div class="field"><label for="service">Service</label><select id="service" name="service" aria-invalid="false"><option value="">Select a service</option><option>Website development</option><option>App development</option><option>Custom software</option><option>Brand strategy</option><option>Not sure yet</option></select><div class="error-message" data-error-for="service"></div></div><div class="field"><label for="budget">Budget</label><select id="budget" name="budget" aria-invalid="false"><option value="">Select budget range</option><option>Under ₹1L</option><option>₹1L – ₹3L</option><option>₹3L – ₹6L</option><option>₹6L+</option><option>Open to discussion</option></select><div class="error-message" data-error-for="budget"></div></div><div class="field full"><label for="details">Project details</label><textarea id="details" name="details" aria-invalid="false" placeholder="Tell us about your goals, current situation, and what you want to build."></textarea><div class="error-message" data-error-for="details"></div></div><div class="field full"><button type="submit" class="btn btn-primary">Send enquiry</button></div></div></form></div></div></section>
</main>
'''

work = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Our work</span><h1>Concept-driven work shaped for modern brands.</h1><p class="lead">These examples explore premium brand experiences for fashion, fitness, and beauty businesses. All are clearly labelled as design concepts unless real client work is provided.</p></div></section>
  <section class="section"><div class="container"><div class="filter-bar"><button class="btn btn-secondary filter-btn is-active" data-filter="all">All</button><button class="btn btn-secondary filter-btn" data-filter="fashion">Fashion</button><button class="btn btn-secondary filter-btn" data-filter="fitness">Fitness</button><button class="btn btn-secondary filter-btn" data-filter="beauty">Beauty</button></div><div class="work-grid"><article class="card" data-category="fashion"><div class="media-box"><img src="assets/images/fashion-store.svg" alt="Fashion concept" /></div><div class="card-topline"><span>Fashion</span><span class="tag">Concept</span></div><h3>Streetwear storefront</h3><p>Editorial shopping experience blending premium storytelling and conversion flow.</p><div class="card-footer"><span>E-commerce</span><a href="projects/fashion-store.html">View project</a></div></article><article class="card" data-category="fitness"><div class="media-box"><img src="assets/images/fitness-website.svg" alt="Fitness concept" /></div><div class="card-topline"><span>Fitness</span><span class="tag">Concept</span></div><h3>Membership platform</h3><p>Product and membership experience for training businesses and studio communities.</p><div class="card-footer"><span>Membership UX</span><a href="projects/fitness-website.html">View project</a></div></article><article class="card" data-category="beauty"><div class="media-box"><img src="assets/images/beauty-store.svg" alt="Beauty concept" /></div><div class="card-topline"><span>Beauty</span><span class="tag">Concept</span></div><h3>Skincare commerce</h3><p>Premium storytelling and clear product journeys for beauty and self-care brands.</p><div class="card-footer"><span>Commerce</span><a href="projects/beauty-store.html">View project</a></div></article></div></div></section>
</main>
'''

process = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Our process</span><h1>A clear path from idea to launch.</h1><p class="lead">We structure the work so each phase has a purpose, each decision is deliberate, and momentum stays strong from brief to launch.</p></div></section>
  <section class="section"><div class="container process-steps"><article class="process-step"><div class="step-number">01</div><div><h3>Discovery</h3><p>We clarify goals, audience, offer, positioning, and the practical constraints of the business.</p></div></article><article class="process-step"><div class="step-number">02</div><div><h3>Planning and design</h3><p>We develop the structure, content priorities, and creative direction before building begins.</p></div></article><article class="process-step"><div class="step-number">03</div><div><h3>Development</h3><p>We build the experience with a strong focus on polish, responsiveness, and real-world usability.</p></div></article><article class="process-step"><div class="step-number">04</div><div><h3>Testing</h3><p>We review the experience across devices and flows to catch issues before launch.</p></div></article><article class="process-step"><div class="step-number">05</div><div><h3>Launch</h3><p>We prepare the deployment, final approval, and launch checklist so the rollout stays clean.</p></div></article><article class="process-step"><div class="step-number">06</div><div><h3>Handover and support</h3><p>We provide the tools, guidance, and support needed for ongoing updates and future improvements.</p></div></article></div></section>
</main>
'''

pricing = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Pricing</span><h1>Project pricing designed to be clear and easy to update.</h1><p class="lead">The structure below intentionally serves as editable placeholders until actual pricing is finalized. Update ranges and scopes to match your service model.</p></div></section>
  <section class="section"><div class="container pricing-grid"><article class="card pricing-card"><span class="tag">Website</span><h3>Brand & marketing website</h3><div class="price">₹1L<small> starting</small></div><p>Suitable for business websites, landing pages, and conversion-led marketing experiences.</p><ul><li>Strategy and UX planning</li><li>Responsive design</li><li>Development and QA</li><li>Launch support</li></ul></article><article class="card pricing-card featured"><span class="tag">App</span><h3>App product experience</h3><div class="price">₹3L<small> starting</small></div><p>For product concepts, mobile journeys, and interactive app-first experiences with API integrations.</p><ul><li>Discovery and user flows</li><li>UI design and prototyping</li><li>Frontend and logic</li><li>Launch readiness</li></ul></article><article class="card pricing-card"><span class="tag">Custom software</span><h3>Business systems</h3><div class="price">₹5L<small> starting</small></div><p>For CRM tools, dashboards, booking systems, inventory flows, and internal operations products.</p><ul><li>Requirements mapping</li><li>Workflow design</li><li>Custom functionality</li><li>Ongoing support planning</li></ul></article></div></section>
  <section class="section"><div class="container split-layout"><div class="card"><h3>What’s included</h3><ul class="list"><li>Discovery and strategy call</li><li>Design direction and site structure</li><li>Responsive implementation</li><li>Testing and release support</li></ul></div><div class="card"><h3>Quoted separately</h3><ul class="list"><li>Advanced integration work</li><li>Complex custom logic</li><li>Copywriting and content production</li><li>Retainer or ongoing support plans</li></ul></div></div></section>
  <section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Custom quote</span><h2>Need a pricing estimate for your project?</h2><p>Tell us what you are building, the user problem you want to solve, and the timeline you are targeting. We’ll recommend the next step.</p><div class="hero-actions" style="justify-content:center;"><a href="contact.html" class="btn btn-primary">Request a custom quote</a></div></div></div></section>
</main>
'''

# service pages
services_index = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Services / What we do</span><h1>Digital experiences, designed around your next move.</h1><p class="lead">From your first website to a custom tool for the team, we help turn business goals into thoughtful, useful digital experiences. Every scope is tailored to the project—not forced into a one-size-fits-all package.</p></div></section>
  <section class="section"><div class="container">
    <div class="section-header"><span class="eyebrow">Our capabilities</span><h2>Choose the right starting point.</h2><p>Not sure which service fits? Start with the challenge you want to solve and we can define the right scope together.</p></div>
    <div class="service-detail-grid">
      <article class="card service-detail-card"><div class="service-symbol" aria-hidden="true">↗</div><div class="card-topline"><span>01 / Presence</span><span class="tag">Web</span></div><h3>Website Development</h3><p>Build a clear, credible online presence that tells your story and gives visitors a natural next step.</p><ul class="list"><li>Business and campaign websites</li><li>Landing pages and storefronts</li><li>Redesigns and responsive builds</li><li>Content structure and user journeys</li></ul><div class="card-footer"><a href="website-development.html">Explore website development →</a></div></article>
      <article class="card service-detail-card"><div class="service-symbol" aria-hidden="true">▣</div><div class="card-topline"><span>02 / Product</span><span class="tag">Mobile</span></div><h3>App Development</h3><p>Shape an app experience around the people who use it and the product logic behind it.</p><ul class="list"><li>Product discovery and user flows</li><li>Mobile-first interface design</li><li>Prototypes and functional experiences</li><li>API and service integration planning</li></ul><div class="card-footer"><a href="app-development.html">Explore app development →</a></div></article>
      <article class="card service-detail-card"><div class="service-symbol" aria-hidden="true">⌘</div><div class="card-topline"><span>03 / Operations</span><span class="tag">Systems</span></div><h3>Custom Software</h3><p>Make complex internal work easier to understand with tools designed around your real workflow.</p><ul class="list"><li>Dashboards and reporting</li><li>Booking and scheduling tools</li><li>Portals, CRM, and inventory flows</li><li>Workflow and automation concepts</li></ul><div class="card-footer"><a href="custom-software.html">Explore custom software →</a></div></article>
    </div>
  </div></section>
  <section class="section"><div class="container split-layout">
    <div><span class="eyebrow">What to expect</span><h2>Clear scope. Thoughtful delivery.</h2><p class="lead">Good digital work starts before the first screen is designed. We make room for the questions, decisions, and reviews that keep a project useful and coherent.</p><ul class="list"><li>A shared understanding of goals and audience</li><li>Priorities and scope agreed before implementation</li><li>Responsive design and considered user journeys</li><li>Review, quality checks, and practical handover</li></ul></div>
    <div class="soft-panel"><span class="tag">One connected workflow</span><h3 style="margin-top:1rem;">Strategy → design → build → launch</h3><p>We connect each stage so the finished experience reflects the original business need—not just a visual brief.</p><div class="inline-list"><span>Discovery</span><span>Direction</span><span>Delivery</span><span>Handover</span></div><p style="margin-top:1.4rem;"><a href="../process.html" class="btn btn-secondary">View the process</a></p></div>
  </div></section>
  <section class="section"><div class="container"><div class="soft-panel"><div class="section-header"><span class="eyebrow">Let’s find your starting point</span><h2>Have a goal, but not a technical brief?</h2><p>Tell us what feels difficult today and what you want to make easier. We can help turn that into a practical first scope.</p></div><a href="../contact.html" class="btn btn-primary">Talk about your project</a></div></div></section>
</main>
'''

website_service = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Website development</span><h1>Web experiences built to sell ideas and support growth.</h1><p class="lead">We design and build polished digital experiences for businesses that want a more refined online presence and a stronger path from attention to action.</p></div></section>
  <section class="section"><div class="container split-layout"><div><h2>What this service solves</h2><ul class="list"><li>Outdated websites that don’t match a premium brand presence</li><li>Low-trust digital experiences that lack clarity or flow</li><li>Conversion friction on landing pages or storefronts</li></ul></div><div class="card"><h3>Includes</h3><ul class="list"><li>Responsive strategy and UX structure</li><li>Landing pages and commerce experiences</li><li>Redesign and refresh work</li><li>Maintenance-friendly implementation</li></ul></div></div></section>
  <section class="section"><div class="container"><div class="section-header"><span class="eyebrow">How we work</span><h2>Strategy, design, and build in a simple flow.</h2></div><div class="grid-3"><article class="card"><h3>Structure</h3><p>We map the key user journeys, content priorities, and conversion moments that matter most.</p></article><article class="card"><h3>Design</h3><p>We shape the brand personality into polished layouts and a clear visual system.</p></article><article class="card"><h3>Build</h3><p>We create a responsive front-end that feels premium and remains easy to evolve over time.</p></article></div></div></section>
  <section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Ready to begin</span><h2>Need a sharper website presence?</h2><a href="../contact.html" class="btn btn-primary">Start a project</a></div></div></section>
</main>
'''

app_service = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">App development</span><h1>Product experiences built around real user behavior.</h1><p class="lead">We design and build app experiences that combine clear user journeys, business logic, and interface quality.</p></div></section>
  <section class="section"><div class="container split-layout"><div><h2>Business problems solved</h2><ul class="list"><li>App ideas without a clear user journey or product architecture</li><li>Interfaces that look polished but do not support business processes</li><li>Weak onboarding or unclear conversion paths</li></ul></div><div class="card"><h3>Typical features</h3><ul class="list"><li>Onboarding flows</li><li>Booking or ordering systems</li><li>Dashboards and notifications</li><li>API integration</li></ul></div></div></section>
  <section class="section"><div class="container"><div class="section-header"><span class="eyebrow">What we deliver</span><h2>Strategy, interface, and launch quality.</h2></div><div class="grid-3"><article class="card"><h3>UX flows</h3><p>We map user tasks, decision points, and onboarding steps before building the experience.</p></article><article class="card"><h3>Design system</h3><p>We define an interface language that remains consistent across screens and product moments.</p></article><article class="card"><h3>Launch readiness</h3><p>We validate the product experience and edge cases before handoff and release.</p></article></div></div></section>
  <section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Need an app concept</span><h2>Let’s shape the product foundation.</h2><a href="../contact.html" class="btn btn-primary">Discuss your app</a></div></div></section>
</main>
'''

software_service = '''
<main>
  <section class="page-header"><div class="page-header-inner"><span class="eyebrow">Custom software</span><h1>Operational tools designed around the way your business actually works.</h1><p class="lead">We build business systems that improve workflows, reduce waste, and make operations easier to run at scale.</p></div></section>
  <section class="section"><div class="container split-layout"><div><h2>Typical use cases</h2><ul class="list"><li>Booking and scheduling systems</li><li>CRM and lead tracking dashboards</li><li>Inventory and fulfilment workflows</li><li>Internal operations portals and reporting dashboards</li></ul></div><div class="card"><h3>Why custom software</h3><p>Templates often fall short when the business has unique processes, internal logic, and operational complexity.</p></div></div></section>
  <section class="section"><div class="container"><div class="section-header"><span class="eyebrow">Workflow</span><h2>From requirements to delivery.</h2></div><div class="grid-3"><article class="card"><h3>Map the process</h3><p>We identify business goals, responsibilities, and decision points before building anything.</p></article><article class="card"><h3>Design the system</h3><p>We turn the workflow into a simple, usable, and scalable interface and logic structure.</p></article><article class="card"><h3>Deliver the tool</h3><p>We build a practical system that your operations can use and evolve over time.</p></article></div></div></section>
  <section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Talk to us</span><h2>Need a tool built for your business?</h2><a href="../contact.html" class="btn btn-primary">Request a consultation</a></div></div></section>
</main>
'''

# industries
industries_index = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Industries</span><h1>We help brands create a sharper digital presence.</h1><p class="lead">From retail and lifestyle to service businesses and startups, we help brands build experiences that feel modern, credible, and conversion-aware.</p></div></section><section class="section"><div class="container grid-3"><article class="card"><h3>Fashion & streetwear</h3><p>Premium buying journeys and brand storytelling for drop-driven, visual-first brands.</p><div class="card-footer"><a href="fashion.html">Explore</a></div></article><article class="card"><h3>Fitness & wellness</h3><p>Membership, classes, and conversion flows designed around community and active lifestyles.</p><div class="card-footer"><a href="fitness.html">Explore</a></div></article><article class="card"><h3>Beauty & skincare</h3><p>Trust-led shopping experiences that communicate value and product confidence through design.</p><div class="card-footer"><a href="beauty.html">Explore</a></div></article><article class="card"><h3>Jewellery</h3><p>Elegant product storytelling and premium presentation for detail-driven lifestyle brands.</p><div class="card-footer"><a href="jewellery.html">Explore</a></div></article></div></section></main>'''

fashion_ind = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Fashion</span><h1>Brand-first ecommerce experiences with edge and elegance.</h1><p class="lead">Fashion and streetwear brands need digital design that captures identity, product desire, and a clear path to purchase.</p></div></section><section class="section"><div class="container split-layout"><div><h2>Common needs</h2><ul class="list"><li>Editorial campaigns and capsule-driven storytelling</li><li>Premium storefronts with clean product focus</li><li>Higher-conversion product browsing and seasonal offers</li></ul></div><div class="card"><h3>Suitable services</h3><ul class="list"><li>Website development</li><li>Landing pages and campaigns</li><li>E-commerce design</li></ul></div></div></section><section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Concept example</span><h2>Streetwear storefront concept</h2><a href="../projects/fashion-store.html" class="btn btn-primary">View concept</a></div></div></section></main>'''
fitness_ind = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Fitness</span><h1>Digital experiences that make training, membership, and community easy to join.</h1><p class="lead">Fitness businesses need a strong brand presence, clear offers, and friction-free journeys for bookable classes and memberships.</p></div></section><section class="section"><div class="container split-layout"><div><h2>Common needs</h2><ul class="list"><li>Membership offer pages and trial conversions</li><li>Class schedules and trainer storytelling</li><li>High-energy landing pages for campaigns or openings</li></ul></div><div class="card"><h3>Suitable services</h3><ul class="list"><li>Website development</li><li>Booking UX exploration</li><li>Campaign landing pages</li></ul></div></div></section><section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Concept example</span><h2>Fitness membership concept</h2><a href="../projects/fitness-website.html" class="btn btn-primary">View concept</a></div></div></section></main>'''
beauty_ind = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Beauty</span><h1>Product-first experiences that build trust and purchase confidence.</h1><p class="lead">Beauty brands need premium design that balances product education, skincare storytelling, and calm ordering journeys.</p></div></section><section class="section"><div class="container split-layout"><div><h2>Common needs</h2><ul class="list"><li>Ingredient-led storytelling and trust-building</li><li>Routine-driven product discovery</li><li>Elegant shopping experiences with strong product presentation</li></ul></div><div class="card"><h3>Suitable services</h3><ul class="list"><li>E-commerce design</li><li>Brand storytelling</li><li>Landing pages and product education</li></ul></div></div></section><section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Concept example</span><h2>Beauty commerce concept</h2><a href="../projects/beauty-store.html" class="btn btn-primary">View concept</a></div></div></section></main>'''
jewellery_ind = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Jewellery</span><h1>Luxury-grade digital experiences for premium collections.</h1><p class="lead">Jewellery and lifestyle brands need highly refined storytelling, product detail, and shopping journeys built with elegance and clarity.</p></div></section><section class="section"><div class="container split-layout"><div><h2>Common needs</h2><ul class="list"><li>Collection storytelling and premium visual presentation</li><li>Detailed product experiences</li><li>High-end browsing and purchase journeys</li></ul></div><div class="card"><h3>Suitable services</h3><ul class="list"><li>Luxury commerce design</li><li>Responsive storefronts</li><li>Editorial landing pages</li></ul></div></div></section></main>'''

# projects
project_fashion = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Concept project</span><h1>Streetwear storefront concept</h1><p class="lead">A premium concept for a fashion brand focused on drops, editorial storytelling, and conversion-led product browsing.</p></div></section><section class="section"><div class="container project-layout"><div class="project-visual"><img src="../assets/images/fashion-store.svg" alt="Fashion concept mockup" /></div><aside class="card"><h3>Project overview</h3><p>A storefront concept designed to feel premium and insider-driven while still guiding shoppers through a clear, conversion-friendly product journey.</p><h3>Goals</h3><ul class="list"><li>Present premium products with stronger clarity</li><li>Create a campaign-led collection journey</li><li>Support product discovery and drop-oriented engagement</li></ul><h3>Design direction</h3><p>Dark editorial styling, strong typography, and a clean conversion-focused layout for premium streetwear culture.</p></aside></div></section><section class="section"><div class="container"><div class="grid-3"><article class="card"><h3>Hero storytelling</h3><p>Strong first-screen brand direction supports the seasonal identity and product energy.</p></article><article class="card"><h3>Collection browsing</h3><p>Thoughtful categories and product layouts reduce friction while creating visual rhythm.</p></article><article class="card"><h3>Purchase clarity</h3><p>Calls to action and key merchandising moments help the product journey feel confident and direct.</p></article></div></div></section><section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Similar project</span><h2>Want a premium commerce concept for your brand?</h2><a href="../contact.html" class="btn btn-primary">Discuss a similar project</a></div></div></section></main>'''
project_fitness = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Concept project</span><h1>Fitness membership concept</h1><p class="lead">A concept for a modern gym or training studio looking to communicate energy, value, and community through a sharper digital presence.</p></div></section><section class="section"><div class="container project-layout"><div class="project-visual"><img src="../assets/images/fitness-website.svg" alt="Fitness concept mockup" /></div><aside class="card"><h3>Project overview</h3><p>Designed to balance class schedules, memberships, and community trust in a way that feels active and action-oriented.</p><h3>Goals</h3><ul class="list"><li>Drive trial sign-ups and memberships</li><li>Highlight class offerings and community energy</li><li>Create a confident first impression for the studio</li></ul><h3>Design direction</h3><p>Motion-inspired, high-contrast visual language with strong calls to action and a clear hierarchy.</p></aside></div></section><section class="section"><div class="container"><div class="grid-3"><article class="card"><h3>Membership focus</h3><p>Clear offer blocks and straightforward value communication reduce decision friction.</p></article><article class="card"><h3>Community feel</h3><p>Trainer and class highlights create emotional energy and social proof.</p></article><article class="card"><h3>Direct action</h3><p>Strong CTAs support sign-up flows with little ambiguity or delay.</p></article></div></div></section><section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Need a similar concept</span><h2>Looking for a stronger digital presence in fitness?</h2><a href="../contact.html" class="btn btn-primary">Discuss a similar project</a></div></div></section></main>'''
project_beauty = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Concept project</span><h1>Beauty storefront concept</h1><p class="lead">A refined concept for a beauty or skincare brand that wants to convert through trust, product education, and a premium shopping journey.</p></div></section><section class="section"><div class="container project-layout"><div class="project-visual"><img src="../assets/images/beauty-store.svg" alt="Beauty concept mockup" /></div><aside class="card"><h3>Project overview</h3><p>The concept balances a premium visual language with clear product education so the buying decision feels easier and more confident.</p><h3>Goals</h3><ul class="list"><li>Highlight ingredients and routines clearly</li><li>Build trust through product education</li><li>Support a calm, confident purchase moment</li></ul><h3>Design direction</h3><p>Soft contrast, premium space, and clear hierarchy blend into a refined but approachable commercial experience.</p></aside></div></section><section class="section"><div class="container"><div class="grid-3"><article class="card"><h3>Learning-first UX</h3><p>Product information is structured to support curiosity, trust, and confidence.</p></article><article class="card"><h3>Visual clarity</h3><p>Premium visuals and disciplined layout create a polished product-first shopping flow.</p></article><article class="card"><h3>Purchase confidence</h3><p>Simple decisions and clearly placed actions help keep the journey calm and effective.</p></article></div></div></section><section class="section"><div class="container"><div class="card" style="text-align:center; padding:2rem;"><span class="eyebrow">Need a similar concept</span><h2>Looking for a beauty or skincare storefront?</h2><a href="../contact.html" class="btn btn-primary">Discuss a similar project</a></div></div></section></main>'''

privacy = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Privacy policy</span><h1>Draft privacy policy</h1><p class="lead">This is a sample policy template and should be reviewed and tailored to match the actual data collection, tools, and legal obligations used by the business.</p></div></section><section class="section"><div class="container card" style="padding:2rem;"><h3>1. Information we may collect</h3><p>We may collect information you provide directly when you contact us, submit a form, or request a quote. This may include your name, email address, company details, and any project information you voluntarily share.</p><h3>2. How we use information</h3><p>We use contact information to respond to enquiries, assess project fit, communicate next steps, and provide the services requested. We do not use your information for unrelated marketing without consent.</p><h3>3. Cookies and analytics</h3><p>We may use analytics, cookies, or embedded tools to understand site usage and improve website performance. Any analytics platform used should be reviewed and disclosed clearly.</p><h3>4. Data sharing</h3><p>We may share information with trusted service providers where necessary to support hosting, website operations, project delivery, or communications. This should be reviewed against your actual tools and vendor relationships.</p><h3>5. Your rights</h3><p>You may request access to, correction of, or deletion of your personal information, subject to legal requirements and the terms of your actual data processing setup.</p><h3>6. Review and customization</h3><p>This policy should be reviewed by legal counsel and customized to reflect actual business practices, retention periods, third-party integrations, and regional privacy obligations.</p></div></section></main>'''
terms = '''<main><section class="page-header"><div class="page-header-inner"><span class="eyebrow">Terms</span><h1>Draft terms of service</h1><p class="lead">This sample document should be reviewed and customized before publication to match the exact services, payment model, and business structure.</p></div></section><section class="section"><div class="container card" style="padding:2rem;"><h3>1. Scope of services</h3><p>Built By Amos provides digital strategy, design, development, and support services based on the agreed scope of each project. Final deliverables and responsibilities are defined in the proposal or engagement agreement.</p><h3>2. Client responsibilities</h3><p>Clients are responsible for providing content, approvals, access, assets, and timely feedback required to progress the project.</p><h3>3. Payment and milestones</h3><p>Payment terms, milestones, and pricing should be confirmed in writing before the project begins. Delays caused by late feedback or incomplete information may affect scheduling.</p><h3>4. Intellectual property</h3><p>Ownership of client-provided materials and final project deliverables should be clarified in the project agreement to avoid ambiguity.</p><h3>5. Support and warranties</h3><p>Any support windows, warranty periods, or maintenance terms should be defined in the contract and reviewed against the actual service model.</p><h3>6. Review and customization</h3><p>This document requires business-specific review to match delivery terms, payment milestones, liability, service boundaries, and legal obligations.</p></div></section></main>'''
not_found = '''<main><section class="section"><div class="container" style="text-align:center; padding:5rem 0;"><span class="eyebrow">404</span><h1>Page not found.</h1><p class="lead">The page you were looking for may have moved or does not exist.</p><div class="hero-actions" style="justify-content:center;"><a href="index.html" class="btn btn-primary">Home</a><a href="services/index.html" class="btn btn-secondary">Services</a><a href="work.html" class="btn btn-secondary">Work</a><a href="contact.html" class="btn btn-secondary">Contact</a></div></div></section></main>'''

# Write main pages
pages = {
    'index.html': ('Built By Amos | Digital Agency', 'Built By Amos is refreshing its website. Contact the studio for website, app, and business software projects.', maintenance_home, ''),
    'about.html': ('About Built By Amos | Amos Anand', 'Meet Amos Anand and learn about Built By Amos, an independent, fashion-first digital studio in India.', about, ''),
    'about-amos/index.html': ('Amos Anand — Founder of Built By Amos', 'Amos Anand is the founder of Built By Amos in Ranchi, India, working on websites, apps, business software, and digital experiences.', founder_profile, '../'),
    'contact.html': ('Contact Built By Amos', 'Get in touch for a website, app, or custom software project.', contact, ''),
    'work.html': ('Our Work | Built By Amos', 'Concept-driven portfolio for fashion, fitness, and beauty-focused brands.', work, ''),
    'process.html': ('Our Process | Built By Amos', 'A structured process from discovery through launch and handover.', process, ''),
    'pricing.html': ('Pricing | Built By Amos', 'Editable project pricing for website, app, and custom software work.', pricing, ''),
    'services/index.html': ('All Services | Built By Amos', 'Overview of website, app, and custom software services.', services_index, '../'),
    'services/website-development.html': ('Website Development | Built By Amos', 'Premium business websites, storefronts, and campaign experiences for brands that want stronger digital presence.', website_service, '../'),
    'services/app-development.html': ('App Development | Built By Amos', 'App experiences designed around user flows, product logic, and mobile-first journeys.', app_service, '../'),
    'services/custom-software.html': ('Custom Software | Built By Amos', 'Operational tools, workflows, and dashboards for business growth.', software_service, '../'),
    'industries/index.html': ('Industries | Built By Amos', 'Industry-focused digital experiences for lifestyle, retail, and business brands.', industries_index, '../'),
    'industries/fashion.html': ('Fashion Industry | Built By Amos', 'Premium fashion and streetwear digital experiences built around product storytelling and conversion.', fashion_ind, '../'),
    'industries/fitness.html': ('Fitness Industry | Built By Amos', 'Website, booking, and membership experiences for modern gyms and studios.', fitness_ind, '../'),
    'industries/beauty.html': ('Beauty Industry | Built By Amos', 'Beauty, skincare, and self-care shopping experiences designed for trust and product education.', beauty_ind, '../'),
    'industries/jewellery.html': ('Jewellery Industry | Built By Amos', 'Luxury market digital experiences for jewellery, lifestyle, and premium product presentation.', jewellery_ind, '../'),
    'projects/fashion-store.html': ('Fashion Store Concept | Built By Amos', 'Concept ecommerce store for a premium streetwear brand.', project_fashion, '../../'),
    'projects/fitness-website.html': ('Fitness Website Concept | Built By Amos', 'Concept website for a gym or fitness brand with memberships and class booking.', project_fitness, '../../'),
    'projects/beauty-store.html': ('Beauty Store Concept | Built By Amos', 'Concept storefront for a skincare or beauty brand with product education and ecommerce flow.', project_beauty, '../../'),
    'privacy-policy.html': ('Privacy Policy | Built By Amos', 'Draft privacy policy template to be reviewed and customized.', privacy, ''),
    'terms.html': ('Terms of Service | Built By Amos', 'Draft terms-of-service language to be reviewed and customized.', terms, ''),
    '404.html': ('404 | Built By Amos', 'Custom not-found page for Built By Amos.', not_found, ''),
}

for rel_path, (title, description, body, prefix) in pages.items():
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    options = {}
    if rel_path == 'about-amos/index.html':
        canonical = 'https://builtbyamos.in/about-amos/'
        person = {
            '@context': 'https://schema.org',
            '@type': 'Person',
            'name': 'Amos Anand',
            'jobTitle': 'Founder',
            'url': canonical,
            'homeLocation': {
                '@type': 'Place',
                'address': {
                    '@type': 'PostalAddress',
                    'addressLocality': 'Ranchi',
                    'addressRegion': 'Jharkhand',
                    'addressCountry': 'India',
                },
            },
            'worksFor': {
                '@type': 'Organization',
                'name': 'Built By Amos',
                'url': 'https://builtbyamos.in/',
            },
        }
        options = {
            'canonical': canonical,
            'structured_data': '<script type="application/ld+json">' + json.dumps(person, ensure_ascii=False) + '</script>',
        }
    path.write_text(render(title, description, body, prefix, **options), encoding='utf-8')

# Robots + sitemap + readme
(root / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://builtbyamos.in/sitemap.xml\n', encoding='utf-8')
(root / 'sitemap.xml').write_text('''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://builtbyamos.in/</loc></url>\n  <url><loc>https://builtbyamos.in/about.html</loc></url>
  <url><loc>https://builtbyamos.in/about-amos/</loc></url>\n  <url><loc>https://builtbyamos.in/contact.html</loc></url>\n  <url><loc>https://builtbyamos.in/work.html</loc></url>\n  <url><loc>https://builtbyamos.in/process.html</loc></url>\n  <url><loc>https://builtbyamos.in/pricing.html</loc></url>\n  <url><loc>https://builtbyamos.in/services/index.html</loc></url>\n  <url><loc>https://builtbyamos.in/services/website-development.html</loc></url>\n  <url><loc>https://builtbyamos.in/services/app-development.html</loc></url>\n  <url><loc>https://builtbyamos.in/services/custom-software.html</loc></url>\n  <url><loc>https://builtbyamos.in/industries/index.html</loc></url>\n  <url><loc>https://builtbyamos.in/industries/fashion.html</loc></url>\n  <url><loc>https://builtbyamos.in/industries/fitness.html</loc></url>\n  <url><loc>https://builtbyamos.in/industries/beauty.html</loc></url>\n  <url><loc>https://builtbyamos.in/industries/jewellery.html</loc></url>\n  <url><loc>https://builtbyamos.in/projects/fashion-store.html</loc></url>\n  <url><loc>https://builtbyamos.in/projects/fitness-website.html</loc></url>\n  <url><loc>https://builtbyamos.in/projects/beauty-store.html</loc></url>\n  <url><loc>https://builtbyamos.in/privacy-policy.html</loc></url>\n  <url><loc>https://builtbyamos.in/terms.html</loc></url>\n</urlset>\n''', encoding='utf-8')
(root / 'README.md').write_text('# Built By Amos Website\n\nStatic multi-page website for Built By Amos.\n\n## Local preview\nOpen `index.html` in a browser, or serve the folder via any static host such as Netlify or GitHub Pages.\n\n## Founder profile\nThe founder profile is available at `/about-amos/` and uses a canonical URL on `builtbyamos.in`. Add a real profile image and verified personal social profiles only after they are supplied.\n\n## Notes\n- Contact form uses a mailto fallback and clearly explains the next step.\n- Example pricing is deliberately editable placeholder pricing.\n- Project pages are clearly labelled as design concepts.\n', encoding='utf-8')

print('Generated static website in', root)
