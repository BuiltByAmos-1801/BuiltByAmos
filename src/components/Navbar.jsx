import { useEffect, useState } from 'react';
import { ArrowUpRight, Menu, X } from 'lucide-react';
import { siteConfig } from '../config/site.js';

const links = [
  ['Work', '#work'],
  ['Services', '#services'],
  ['About', '#about'],
  ['Process', '#process'],
  ['Contact', '#contact'],
];

export default function Navbar() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    function closeOnEscape(event) {
      if (event.key === 'Escape') setOpen(false);
    }
    document.addEventListener('keydown', closeOnEscape);
    return () => document.removeEventListener('keydown', closeOnEscape);
  }, []);

  function closeMenu() {
    setOpen(false);
  }

  return (
    <>
      <div className="announcement">
        <span>Independent digital studio</span>
        <span aria-hidden="true" className="announcement-divider">/</span>
        <span>{siteConfig.location}</span>
      </div>
      <header className="site-header">
        <nav className="nav-shell" aria-label="Main navigation">
          <a className="wordmark" href="#top" onClick={closeMenu} aria-label="Built By Amos home">
            <span className="wordmark-symbol" aria-hidden="true">B.</span>
            <span>BUILT BY AMOS</span>
          </a>
          <button
            className="menu-toggle"
            type="button"
            aria-label={open ? 'Close navigation menu' : 'Open navigation menu'}
            aria-expanded={open}
            aria-controls="primary-navigation"
            onClick={() => setOpen((value) => !value)}
          >
            {open ? <X size={21} aria-hidden="true" /> : <Menu size={21} aria-hidden="true" />}
          </button>
          <div id="primary-navigation" className={`nav-content${open ? ' is-open' : ''}`}>
            <ul className="nav-links">
              {links.map(([label, href]) => (
                <li key={href}>
                  <a href={href} onClick={closeMenu}>{label}</a>
                </li>
              ))}
            </ul>
            <a className="button button-dark nav-cta" href="#contact" onClick={closeMenu}>
              Start a Project <ArrowUpRight size={16} aria-hidden="true" />
            </a>
          </div>
        </nav>
      </header>
    </>
  );
}
