import { useState } from 'react';
import { ArrowUpRight } from 'lucide-react';
import { siteConfig } from '../config/site.js';

const initialForm = {
  name: '',
  email: '',
  business: '',
  projectType: '',
  budget: '',
  timeframe: '',
  brief: '',
};

export default function ContactForm() {
  const [form, setForm] = useState(initialForm);
  const [status, setStatus] = useState('');

  function updateField(event) {
    setForm((current) => ({ ...current, [event.target.name]: event.target.value }));
    setStatus('');
  }

  function submitEnquiry(event) {
    event.preventDefault();
    const subject = `Project enquiry from ${form.name.trim()}`;
    const body = [
      `Name: ${form.name.trim()}`,
      `Email: ${form.email.trim()}`,
      `Business / brand: ${form.business.trim() || 'Not provided'}`,
      `Project type: ${form.projectType}`,
      `Approximate budget: ${form.budget || 'Not provided'}`,
      `Target timeframe: ${form.timeframe || 'Not provided'}`,
      '',
      'Project brief:',
      form.brief.trim(),
    ].join('\n');

    window.location.href =
      `mailto:${siteConfig.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    setStatus(
      `Your email app should open with this enquiry addressed to ${siteConfig.email}. If it does not, email us directly using the link beside the form.`,
    );
  }

  return (
    <form className="contact-form" onSubmit={submitEnquiry}>
      <div className="form-grid">
        <label className="field">
          <span>Name <span aria-hidden="true">*</span></span>
          <input autoComplete="name" name="name" value={form.name} onChange={updateField} required />
        </label>
        <label className="field">
          <span>Email <span aria-hidden="true">*</span></span>
          <input autoComplete="email" type="email" name="email" value={form.email} onChange={updateField} required />
        </label>
        <label className="field">
          <span>Business or brand</span>
          <input autoComplete="organization" name="business" value={form.business} onChange={updateField} />
        </label>
        <label className="field">
          <span>Project type <span aria-hidden="true">*</span></span>
          <select name="projectType" value={form.projectType} onChange={updateField} required>
            <option value="">Select a project type</option>
            <option>Website design & development</option>
            <option>E-commerce development</option>
            <option>Mobile app development</option>
            <option>Custom software & automation</option>
            <option>Not sure yet</option>
          </select>
        </label>
        <label className="field">
          <span>Approximate budget</span>
          <select name="budget" value={form.budget} onChange={updateField}>
            <option value="">Choose if known</option>
            <option>Under ₹15,000</option>
            <option>₹15,000 – ₹25,000</option>
            <option>₹25,000 – ₹40,000</option>
            <option>₹40,000+</option>
            <option>Open to discussion</option>
          </select>
        </label>
        <label className="field">
          <span>Target launch timeframe</span>
          <input
            name="timeframe"
            placeholder="e.g. Flexible / this quarter"
            value={form.timeframe}
            onChange={updateField}
          />
        </label>
        <label className="field field-wide">
          <span>Briefly describe your project <span aria-hidden="true">*</span></span>
          <textarea
            name="brief"
            rows="5"
            minLength="20"
            value={form.brief}
            onChange={updateField}
            required
            placeholder="What are you looking to build, and what should it help you do?"
          />
          <span className="field-hint">A few sentences is enough to start the conversation.</span>
        </label>
      </div>
      <div className="form-submit-row">
        <button className="button button-dark" type="submit">
          Prepare email enquiry <ArrowUpRight size={17} aria-hidden="true" />
        </button>
        <a href={`mailto:${siteConfig.email}`}>{siteConfig.email}</a>
      </div>
      <p className="form-status" aria-live="polite">{status}</p>
      <p className="form-note">This form prepares an email in your email application; it does not submit data to a server.</p>
    </form>
  );
}
