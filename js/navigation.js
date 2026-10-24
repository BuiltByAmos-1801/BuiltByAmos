
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
