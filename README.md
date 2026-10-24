# Built By Amos — React + Vite

A responsive studio website built with React, Vite, JavaScript, and custom CSS. The old static website files were intentionally removed from the working tree before this rebuild; they have not been restored or overwritten. The owner-provided founder artwork is reused as a local asset.

The site has a studio homepage and a dedicated founder profile at `https://builtbyamos.in/about-amos/`. The trailing slash is the canonical directory-index URL; configure the production host to redirect `/about-amos` to `/about-amos/`.

## Requirements

- Node.js 20.19+ or 22.12+ (LTS recommended).
- npm, included with Node.js.

On Windows, install Node.js LTS from [nodejs.org](https://nodejs.org/), then reopen PowerShell or the VS Code terminal.

## Run locally

1. Open the `F:\BBA` folder in VS Code (`File` → `Open Folder`).
2. Open the integrated terminal (`Terminal` → `New Terminal`).
3. Install the declared dependencies:

   ```powershell
   npm install
   ```

4. Start the development server:

   ```powershell
   npm run dev
   ```

5. Open the local URL printed by Vite, usually `http://localhost:5173`.

## Production build and preview

```powershell
npm run build
npm run preview
```

Vite writes production files to `dist\`. Preview the build locally before uploading it.

## Content and owner-specific configuration

- Edit `src\config\site.js` to update the studio name, founder, location, production URL, email, and official social links.
- Edit `src\data\content.js` to update project concepts, services, provisional starting prices, process steps, and FAQs.
- The three work visuals in `public\images\` are self-initiated design concepts, not client case studies.
- The founder artwork at `public\images\built-by-amos-ideas-to-solutions.png` was provided by the site owner. Replace it only with an approved image.
- No separate founder portrait or personal social profile was available during implementation. The profile page uses the supplied brand artwork, does not present it as a portrait, and links only to the agency's official Instagram.
- The listed starting prices are initial figures from the owner-provided brief; confirm them before treating them as current quotes.
- No WhatsApp number or personal social profile has been configured. Add only verified public details.
- A privacy-policy page has not been included in this single-page rebuild.

## Contact form

The form validates required fields in the browser and opens the visitor's email application with a prefilled message addressed to `hello@builtbyamos.in`. It does not submit to a server or claim that a message was delivered. To use a hosted form provider or backend, configure a real endpoint and update `src\components\ContactForm.jsx`; never put private API keys in browser code.

## Deploy safely

1. Keep a backup of the current hosting files and confirm access to the hosting provider before changing the live site. This project does not publish or switch domains.
2. Run and review `npm run build`, then test with `npm run preview`.
3. Deploy the contents of `dist\` to a static host, or connect a Git repository and set the build command to `npm run build` and publish directory to `dist`.
4. Preview the new build on a host-provided preview URL before changing production.
5. Only after approving the preview, configure the production domain and enable the host's HTTPS certificate. Do not change DNS until the new deployment is verified.
6. The homepage canonical is `https://builtbyamos.in/`; the founder profile canonical is `https://builtbyamos.in/about-amos/`. Both URLs are listed in the sitemap in `public\`. Confirm these URLs return successfully after deployment.
7. Configure and verify a permanent redirect from `/about-amos` to `/about-amos/`; redirect syntax depends on the chosen static host.

## Project structure

```text
public/
  favicon.svg
  images/
  robots.txt
  sitemap.xml
about-amos/
  index.html
src/
  components/
    FounderProfile.jsx
  config/
  data/
  App.jsx
  index.css
  main.jsx
index.html
vite.config.js
```
