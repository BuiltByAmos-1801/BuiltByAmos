
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
      ['email', function (value) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim()); }, 'Please enter a valid email address.'],
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
        ].join('\n')
      });
      window.location.href = 'mailto:hello@builtbyamos.in?' + params.toString();
    }
  });
});
