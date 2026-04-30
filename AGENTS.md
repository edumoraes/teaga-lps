# Repository Guidelines

## Project Structure & Module Organization

This repository is a Hugo static site for Teaga landing pages. The root `hugo.toml` sets `theme = "marketing-theme"` and `languageCode = "pt-br"`. Main page content lives in `content/`, including `content/_index.md` and the lawyer landing page at `content/landing-page-teaga-advogados-ROMA-4Us.md`. Theme templates are under `themes/marketing-theme/layouts/`; reusable page sections are in `themes/marketing-theme/layouts/partials/`. Styles and JavaScript live in `themes/marketing-theme/assets/css/style.css` and `themes/marketing-theme/assets/js/law-landing.js`. Static images such as `logo.webp` and `favicon.webp` are in `themes/marketing-theme/static/images/`. Generated output goes to `public/` and should not be edited by hand.

## Build, Test, and Development Commands

- `hugo server -D`: run the local development server with draft content enabled.
- `hugo --minify`: build the production site into `public/` and minify assets.
- `hugo --cleanDestinationDir --minify`: rebuild from a clean `public/` directory when checking for stale generated files.

No npm, Makefile, or package-managed workflow is currently present.

## Coding Style & Naming Conventions

Use two-space indentation in Hugo templates, YAML/TOML front matter, CSS, and JavaScript. Keep Hugo partial names lowercase with underscores, for example `lead_form.html` and `cta_banner.html`. Prefer content changes in Markdown front matter over hardcoded template text. CSS custom properties belong in `:root`; reuse existing tokens such as `--accent-primary`, `--font-sans`, and `--bg-color` before adding new values. Keep JavaScript plain and dependency-free unless a clear project need is introduced.

## Testing Guidelines

There is no automated test suite yet. Treat a successful `hugo --minify` build as the required validation step for every change. For layout or copy changes, also run `hugo server -D` and manually review `/` and `/lp-advogados/` at desktop and mobile widths. Check forms, anchor links, sticky navigation, and WhatsApp redirect behavior when editing related partials or `law-landing.js`.

## Commit & Pull Request Guidelines

Git history uses Conventional Commit-style prefixes such as `feat:`, `style:`, and `chore:`. Keep commits focused and use messages like `feat: add lawyer landing form` or `style: refine hero spacing`. Pull requests should include a concise summary, the validation command run, affected URLs, and screenshots for visual changes. Link related issues or client requests when available, and call out any content, phone number, tracking, or compliance-sensitive changes.

## Security & Configuration Tips

Do not commit real secrets, analytics credentials, or private client data. Keep configurable contact details in content front matter, such as `whatsapp_number`, instead of embedding them in templates or scripts.
