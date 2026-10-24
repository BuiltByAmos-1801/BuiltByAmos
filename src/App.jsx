import {
  ArrowDown,
  ArrowRight,
  ArrowUpRight,
  Code2,
  Layers3,
  Smartphone,
  Workflow,
} from 'lucide-react';
import Navbar from './components/Navbar.jsx';
import FAQ from './components/FAQ.jsx';
import ContactForm from './components/ContactForm.jsx';
import { siteConfig } from './config/site.js';
import { packages, principles, processSteps, projects, services } from './data/content.js';

function SectionHeading({ id, eyebrow, title, description, light = false }) {
  return (
    <div className={`section-heading${light ? ' section-heading--light' : ''}`}>
      <span className="eyebrow">{eyebrow}</span>
      <h2 id={id}>{title}</h2>
      {description && <p>{description}</p>}
    </div>
  );
}

function ProjectCard({ project }) {
  return (
    <article className="project-card">
      <a className={`project-image ${project.tone}`} href="#contact" aria-label={`Discuss a project like ${project.title}`}>
        <img src={project.image} alt={project.alt} width="1200" height="760" loading="lazy" />
        <span className="project-image-label">Self-initiated concept</span>
        <span className="project-image-action" aria-hidden="true"><ArrowUpRight size={20} /></span>
      </a>
      <div className="project-meta">
        <span>{project.number} <i aria-hidden="true">/</i> {project.industry}</span>
        <span>{project.type}</span>
      </div>
      <div className="project-copy">
        <h3>{project.title}</h3>
        <p>{project.description}</p>
        <a className="text-link" href="#contact">Discuss a similar project <ArrowRight size={15} aria-hidden="true" /></a>
      </div>
    </article>
  );
}

function App() {
  return (
    <>
      <a className="skip-link" href="#main-content">Skip to main content</a>
      <Navbar />
      <main id="main-content">
        <section className="hero section-wrap" id="top" aria-labelledby="hero-title">
          <h1 className="hero-banner-heading" id="hero-title">Modern digital solutions for ambitious brands.</h1>
          <figure className="hero-banner">
            <img
              src="/images/modern-digital-solutions-hero-banner.png"
              alt="Built By Amos creates modern digital experiences for ambitious brands, including websites, apps and automation."
              width="1983"
              height="793"
              fetchpriority="high"
            />
            <a className="hero-banner-cta hero-banner-cta--project" href="#contact" aria-label="Start a project" />
            <a className="hero-banner-cta hero-banner-cta--work" href="#work" aria-label="Explore our work" />
          </figure>
          <div className="hero-banner-mobile">
            <span className="eyebrow">Independent digital studio <i aria-hidden="true">·</i> India / Worldwide</span>
            <p>We design and build thoughtful websites, online stores and digital products for ambitious brands.</p>
            <div className="hero-actions">
              <a className="button button-dark" href="#contact">Start a Project <ArrowUpRight size={17} aria-hidden="true" /></a>
              <a className="button button-outline" href="#work">Explore Our Work <ArrowDown size={16} aria-hidden="true" /></a>
            </div>
          </div>
        </section>

        <section className="studio-banner section-wrap" aria-label="Built By Amos digital studio">
          <img
            src="/images/amos-banner.png"
            alt="Built By Amos — independent digital studio creating websites, apps and automation for businesses."
            width="1983"
            height="793"
            loading="lazy"
          />
        </section>

        <section className="work-section section-wrap" id="work" aria-labelledby="work-title">
          <SectionHeading
            id="work-title"
            eyebrow="Selected work"
            title="Ideas made tangible."
            description="A selection of digital experiences, concepts and solutions. Concept work is clearly identified; no client results or endorsements are implied."
          />
          <div className="project-grid">
            {projects.map((project) => <ProjectCard key={project.number} project={project} />)}
          </div>
        </section>

        <section className="services-section section-wrap" id="services" aria-labelledby="services-title">
          <div className="services-intro">
            <SectionHeading
              id="services-title"
              eyebrow="What we do"
              title="Digital solutions, designed around your business."
              description="The right solution starts with understanding what your business and customers actually need."
            />
            <a className="text-link" href="#contact">Discuss your project <ArrowUpRight size={16} aria-hidden="true" /></a>
          </div>
          <div className="service-list">
            {services.map((service, index) => {
              const Icon = [Code2, Layers3, Smartphone, Workflow][index];
              return (
                <article className="service-row" key={service.number}>
                  <span className="service-number">{service.number}</span>
                  <span className="service-icon" aria-hidden="true"><Icon size={24} strokeWidth={1.5} /></span>
                  <div className="service-copy">
                    <h3>{service.title}</h3>
                    <p>{service.description}</p>
                    <ul className="deliverable-list">
                      {service.deliverables.map((item) => <li key={item}>{item}</li>)}
                    </ul>
                  </div>
                  <a className="service-action" href="#contact" aria-label={`Discuss ${service.title}`}><ArrowUpRight size={19} /></a>
                </article>
              );
            })}
          </div>
        </section>

        <section className="principles-section section-wrap" aria-labelledby="principles-title">
          <div className="principles-heading">
            <span className="eyebrow">A considered way of working</span>
            <h2 id="principles-title">Small studio.<br /><em>Thoughtful execution.</em></h2>
            <p>Work directly with the person shaping your project, from first conversation to handover.</p>
          </div>
          <div className="principles-list">
            {principles.map((principle) => (
              <article className="principle-row" key={principle.number}>
                <span>{principle.number}</span>
                <h3>{principle.title}</h3>
                <p>{principle.description}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="process-section section-wrap" id="process" aria-labelledby="process-title">
          <SectionHeading
            id="process-title"
            eyebrow="A clear way forward"
            title="From idea to launch."
            description="The exact timeline depends on project scope, complexity and content readiness."
          />
          <ol className="process-grid">
            {processSteps.map((step) => (
              <li className="process-step" key={step.number}>
                <span className="process-number">{step.number}</span>
                <span className="process-rule" aria-hidden="true" />
                <h3>{step.title}</h3>
                <p>{step.description}</p>
              </li>
            ))}
          </ol>
        </section>

        <section className="about-section section-wrap" id="about" aria-labelledby="about-title">
          <div className="about-image-wrap">
            <img
              src="/images/Amos-BuiltByAmos.png"
              alt="Amos Anand, founder of Built By Amos"
              width="1310"
              height="1200"
              loading="lazy"
            />
            <span className="about-image-caption">Amos Anand <i>·</i> Founder</span>
          </div>
          <div className="about-copy">
            <span className="eyebrow">A founder-led studio</span>
            <h2 id="about-title">Built with intention.<br /><em>Led by Amos.</em></h2>
            <p>
              Built By Amos is an independent digital studio focused on helping ambitious businesses build a stronger presence online. From websites and online stores to custom digital products, every project starts with understanding the business behind it.
            </p>
            <p>
              Amos Anand leads the studio from Ranchi, Jharkhand, India, working across website and app development, business software, UI/UX design, AI automation, SEO and website maintenance.
            </p>
            <a className="text-link" href={`mailto:${siteConfig.email}`}>Start a conversation <ArrowUpRight size={16} aria-hidden="true" /></a>
            <a className="text-link founder-profile-link" href="/about-amos/">Read Amos’s founder profile <ArrowUpRight size={16} aria-hidden="true" /></a>
          </div>
        </section>

        <section className="pricing-section section-wrap" id="pricing" aria-labelledby="pricing-title">
          <SectionHeading
            id="pricing-title"
            eyebrow="Project investment"
            title="An investment in your next stage."
            description="Starting prices help frame a conversation. Final pricing depends on requirements, complexity and agreed deliverables."
          />
          <div className="pricing-grid">
            {packages.map((plan) => (
              <article className={`price-card${plan.featured ? ' price-card--featured' : ''}`} key={plan.name}>
                <div className="price-card-heading"><span>{plan.name}</span><span>{plan.suffix}</span></div>
                <p className="price-amount">{plan.price}</p>
                <p className="price-description">{plan.description}</p>
                <ul className="price-features">{plan.features.map((feature) => <li key={feature}>{feature}</li>)}</ul>
                <a className={plan.featured ? 'button button-light' : 'button button-outline'} href="#contact">
                  Discuss this package <ArrowUpRight size={16} aria-hidden="true" />
                </a>
              </article>
            ))}
          </div>
          <p className="pricing-note">Every project is scoped individually. Final pricing depends on requirements and agreed deliverables. Hosting, domains, third-party fees and ongoing maintenance are not included unless agreed in the project scope.</p>
        </section>

        <section className="faq-section section-wrap" aria-labelledby="faq-title">
          <div className="faq-intro">
            <span className="eyebrow">Good to know</span>
            <h2 id="faq-title">Questions, <em>answered.</em></h2>
            <p>A few practical details to help you decide on a next step.</p>
          </div>
          <FAQ />
        </section>

        <section className="contact-section section-wrap" id="contact" aria-labelledby="contact-title">
          <div className="contact-heading">
            <span className="eyebrow">Tell us what you’re building</span>
            <h2 id="contact-title">Have something <em>worth building?</em></h2>
            <p>Tell us about your goals and requirements. We’ll discuss a useful next step.</p>
            <div className="contact-direct">
              <a href={`mailto:${siteConfig.email}`}>{siteConfig.email} <ArrowUpRight size={15} aria-hidden="true" /></a>
              <a href={siteConfig.social.instagram} target="_blank" rel="noreferrer">Instagram <ArrowUpRight size={15} aria-hidden="true" /></a>
            </div>
          </div>
          <ContactForm />
        </section>
      </main>

      <footer className="site-footer">
        <div className="footer-main">
          <div className="footer-brand">
            <a className="wordmark wordmark--footer" href="#top" aria-label="Built By Amos home">
              <img className="wordmark-image" src="/images/amos-logo.png" alt="Built By Amos" width="380" height="90" />
            </a>
            <p>An independent digital studio building thoughtful digital experiences for ambitious brands.</p>
            <span className="footer-location">{siteConfig.location}</span>
          </div>
          <div className="footer-column">
            <span className="footer-label">Explore</span>
            <a href="#work">Work</a><a href="#services">Services</a><a href="#about">About</a><a href="#process">Process</a><a href="#pricing">Pricing</a>
          </div>
          <div className="footer-column">
            <span className="footer-label">Get in touch</span>
            <a href="#contact">Start a project</a><a href={`mailto:${siteConfig.email}`}>{siteConfig.email}</a>
            <a href={siteConfig.social.instagram} target="_blank" rel="noreferrer">Instagram <ArrowUpRight size={13} aria-hidden="true" /></a>
          </div>
        </div>
        <div className="footer-bottom">
          <span>© {new Date().getFullYear()} Built By Amos</span>
          <a href="#top">Back to top ↑</a>
          <span>Ideas → Code → Real Solutions</span>
        </div>
      </footer>
    </>
  );
}

export default App;
