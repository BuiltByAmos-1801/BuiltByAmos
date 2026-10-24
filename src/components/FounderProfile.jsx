import { ArrowRight, ArrowUpRight, MapPin } from 'lucide-react';
import { siteConfig } from '../config/site.js';
import { projects } from '../data/content.js';

const services = [
  'Website development',
  'App development',
  'Business software',
  'UI/UX design',
  'AI automation',
  'SEO',
  'Website maintenance',
];

export default function FounderProfile() {
  return (
    <main className="founder-page">
      <header className="founder-header">
        <a className="wordmark" href="/#top" aria-label="Built By Amos home">
          <span className="wordmark-symbol" aria-hidden="true">B.</span>
          <span>BUILT BY AMOS</span>
        </a>
        <a className="text-link" href="/#top">Back to the studio <ArrowRight size={15} aria-hidden="true" /></a>
      </header>

      <section className="founder-hero" aria-labelledby="founder-title">
        <div>
          <span className="eyebrow">Founder profile</span>
          <h1 id="founder-title">Amos Anand</h1>
          <p className="founder-role">Founder of <a href="/#top">Built By Amos</a></p>
          <p className="founder-intro">
            Amos Anand leads Built By Amos, an independent digital studio focused on website and app development and practical digital solutions for businesses. The work spans discovery, design and development, with each project scoped around its actual needs.
          </p>
          <p className="founder-location"><MapPin size={16} aria-hidden="true" /> Ranchi, Jharkhand, India</p>
          <div className="founder-actions">
            <a className="button button-dark" href="/#contact">Contact the studio <ArrowUpRight size={16} aria-hidden="true" /></a>
            <a className="button button-outline" href={siteConfig.social.instagram} target="_blank" rel="noopener noreferrer">
              Built By Amos on Instagram <ArrowUpRight size={16} aria-hidden="true" />
            </a>
          </div>
        </div>
        <figure className="founder-artwork">
          <img
            src="/images/built-by-amos-ideas-to-solutions.png"
            alt="Built By Amos brand artwork with the message Ideas to Real Solutions"
            width="2048"
            height="768"
            fetchpriority="high"
          />
          <figcaption>Built By Amos brand artwork</figcaption>
        </figure>
      </section>

      <section className="founder-content-section" aria-labelledby="founder-work-title">
        <span className="eyebrow">Work and services</span>
        <h2 id="founder-work-title">Digital work shaped around real business needs.</h2>
        <p>
          Built By Amos works across website development, app development, business software, UI/UX design, AI automation, SEO and website maintenance. The appropriate approach depends on the project requirements and agreed scope.
        </p>
        <ul className="founder-service-list">
          {services.map((service) => <li key={service}>{service}</li>)}
        </ul>
      </section>

      <section className="founder-content-section" aria-labelledby="founder-projects-title">
        <span className="eyebrow">Selected concepts</span>
        <h2 id="founder-projects-title">Exploring ideas through design.</h2>
        <p>
          These self-initiated concepts are included as examples of design direction. They are not presented as client projects, testimonials or completed commercial work.
        </p>
        <div className="founder-project-grid">
          {projects.map((project) => (
            <article className="founder-project" key={project.number}>
              <img src={project.image} alt={project.alt} width="1200" height="760" loading="lazy" />
              <span className="founder-project-label">Self-initiated concept · {project.industry}</span>
              <h3>{project.title}</h3>
              <p>{project.description}</p>
            </article>
          ))}
        </div>
      </section>

      <footer className="founder-footer">
        <span>© {new Date().getFullYear()} Built By Amos</span>
        <a className="text-link" href="/#contact">Discuss a project <ArrowUpRight size={15} aria-hidden="true" /></a>
      </footer>
    </main>
  );
}
