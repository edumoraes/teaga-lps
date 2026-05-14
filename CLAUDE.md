# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

`AGENTS.md` contains the canonical contributor guide (structure, commands, style, commits). Read it first. The notes below add architectural context not obvious from a single file.

## Commands

- `hugo server -D` — local dev with drafts.
- `hugo --minify` — production build to `public/` (the required validation step; there is no test suite).
- `hugo --cleanDestinationDir --minify` — rebuild from a clean `public/`.

CI uses **Hugo 0.124.1 extended** (`.github/workflows/deploy-github-pages.yml`); match it locally when reproducing build issues. Deploy is GitHub Pages on push to `main`.

## Architecture

### Two independent rendering paths

The site has two pages and they do **not** share templates:

- **Home (`/`)** → `themes/marketing-theme/layouts/index.html`, which composes partials in `layouts/partials/` (`hero.html`, `benefits.html`, `services.html`, `cta_banner.html`, etc.).
- **Lawyer LP (`/lp-advogados/`)** → set by `layout: "law-landing"` in the markdown front matter, which resolves to `layouts/_default/law-landing.html`. This file inlines every section directly (header, hero, trust bar, audience, deliverables, FAQ, footer) — it does **not** use the partials above.

When editing the lawyer landing page, edit `_default/law-landing.html` directly. Changes to `partials/hero.html` etc. only affect the home page. The `law-lp-*` CSS class prefix is exclusive to the lawyer LP.

### Content-driven copy

The lawyer LP is almost entirely data-driven from front matter in `content/landing-page-teaga-advogados-ROMA-4Us.md`. Section copy, CTAs, FAQ items, audience cards, and the WhatsApp number all live there. **Default to editing front matter, not the template.** Add a template branch only when introducing new structural behavior.

WhatsApp CTAs are built from `whatsapp_number` + `whatsapp_message` front matter via a `$whatsappHref` variable defined at the top of `law-landing.html`. Reuse that variable; do not hardcode `wa.me` URLs.

### Icons

Lucide icons are loaded as CSS-masked SVGs from a jsDelivr CDN through `partials/lucide_icon.html` (called as `{{ partial "lucide_icon.html" (dict "icon" "name" "class" "...") }}`). Icon names in front matter (e.g. `icon: "scale"`) must match a Lucide icon slug.

### Design tokens

Canonical color/spacing tokens are documented in `docs/lp-advogados/DESIGN.md` and defined as CSS custom properties in `themes/marketing-theme/assets/css/style.css` under `:root`. Reuse existing tokens (`--color-brand-primary`, `--color-text-primary`, etc.) before introducing new values — the design doc and CSS must stay in sync.

### Assets pipeline

CSS and JS are processed through Hugo's asset pipeline (`resources.Get` → `minify` → `fingerprint`) at the bottom of each layout. New JS/CSS belongs in `themes/marketing-theme/assets/` so it picks up fingerprinting; static images go in `themes/marketing-theme/static/images/`.

## Conventions worth flagging

- Commits follow Conventional Commits (`feat:`, `style:`, `chore:`, …) — see recent log.
- Keep JS dependency-free (per `AGENTS.md`).
- Root-level images like `hero.png`, `incluso.jpeg`, `referencia-*.png` are working references / mockups, not site assets — do not link to them from templates.
