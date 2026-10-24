
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
