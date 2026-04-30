# DESIGN.md - Tokens da LP Advogados

Esta documentacao define os tokens de cor da landing page `/lp-advogados/`.
Os tokens sao semanticos: descrevem papel de uso, nao apenas a cor isolada.

## Color

### Base

| Token | CSS | Valor |
| --- | --- | --- |
| `color.base.black` | `--color-base-black` | `#0B0B0C` |
| `color.base.charcoal` | `--color-base-charcoal` | `#121314` |
| `color.base.dark-gray` | `--color-base-dark-gray` | `#1E1F21` |
| `color.base.gray` | `--color-base-gray` | `#6B6F76` |
| `color.base.light-gray` | `--color-base-light-gray` | `#D9D9D9` |
| `color.base.off-white` | `--color-base-off-white` | `#F5F5F3` |
| `color.base.cream` | `--color-base-cream` | `#E6E0D6` |
| `color.base.gold` | `--color-base-gold` | `#C6A86B` |
| `color.base.gold-strong` | `--color-base-gold-strong` | `#A8843B` |
| `color.base.gold-soft` | `--color-base-gold-soft` | `#E3CFA0` |

### Brand

| Token | CSS | Valor |
| --- | --- | --- |
| `color.brand.primary` | `--color-brand-primary` | `#C6A86B` |
| `color.brand.primary-hover` | `--color-brand-primary-hover` | `#A8843B` |
| `color.brand.primary-active` | `--color-brand-primary-active` | `#8F6E2E` |
| `color.brand.secondary` | `--color-brand-secondary` | `#121314` |
| `color.brand.secondary-hover` | `--color-brand-secondary-hover` | `#1E1F21` |

### Background

| Token | CSS | Valor |
| --- | --- | --- |
| `color.background.default` | `--color-background-default` | `#0B0B0C` |
| `color.background.surface` | `--color-background-surface` | `#121314` |
| `color.background.subtle` | `--color-background-subtle` | `#1E1F21` |
| `color.background.inverse` | `--color-background-inverse` | `#E6E0D6` |

### Text

| Token | CSS | Valor |
| --- | --- | --- |
| `color.text.primary` | `--color-text-primary` | `#F5F5F3` |
| `color.text.secondary` | `--color-text-secondary` | `#D9D9D9` |
| `color.text.muted` | `--color-text-muted` | `#6B6F76` |
| `color.text.inverse` | `--color-text-inverse` | `#0B0B0C` |
| `color.text.brand` | `--color-text-brand` | `#C6A86B` |

### Border

| Token | CSS | Valor |
| --- | --- | --- |
| `color.border.default` | `--color-border-default` | `#2A2C2F` |
| `color.border.subtle` | `--color-border-subtle` | `#1E1F21` |
| `color.border.strong` | `--color-border-strong` | `#6B6F76` |
| `color.border.brand` | `--color-border-brand` | `#C6A86B` |

### Icon

| Token | CSS | Valor |
| --- | --- | --- |
| `color.icon.primary` | `--color-icon-primary` | `#F5F5F3` |
| `color.icon.secondary` | `--color-icon-secondary` | `#C6A86B` |
| `color.icon.muted` | `--color-icon-muted` | `#6B6F76` |

### State

| Token | CSS | Valor |
| --- | --- | --- |
| `color.state.success` | `--color-state-success` | `#3FAF7A` |
| `color.state.warning` | `--color-state-warning` | `#D4A017` |
| `color.state.error` | `--color-state-error` | `#C94A4A` |
| `color.state.info` | `--color-state-info` | `#3B82F6` |

### Overlay

| Token | CSS | Valor |
| --- | --- | --- |
| `color.overlay.dark` | `--color-overlay-dark` | `rgba(0, 0, 0, 0.6)` |
| `color.overlay.gold` | `--color-overlay-gold` | `rgba(198, 168, 107, 0.15)` |

### Section Backgrounds

| CSS | Uso |
| --- | --- |
| `--color-section-dark-gradient` | Secao dark com superficie charcoal e dourado sutil. |
| `--color-section-dark-solid` | Secao dark com preto profundo solido. |
| `--color-section-light-solid` | Secao light com creme quente solido. |

## Usage

- Hero: use `color.background.default` for the page base, `color.text.primary` for headline text, and `color.text.brand` for highlights and eyebrow labels.
- Sections: repeat this order across the LP: dark with gradient, dark solid, light solid. Light sections use the warmer cream background and switch text and border aliases locally for contrast.
- Buttons: primary CTAs use `color.brand.primary`, hover uses `color.brand.primary-hover`, and text uses `color.text.inverse`.
- Cards and form panels: use `color.background.surface` or a subtle gold overlay, with `color.border.brand` at low opacity.
- Text: body and long-form support copy use `color.text.secondary` for readability; reserve `color.text.muted` for low-emphasis metadata.
- Icons: functional and decorative legal icons use `color.icon.secondary`; inactive or supporting icons use `color.icon.muted`.

## Image Assets

| Arquivo | Uso |
| --- | --- |
| `images/lp-advogados/hero-legal-compass.webp` | Background editorial do hero com overlay escuro para leitura. |
| `images/lp-advogados/differentials-texture.webp` | Textura discreta da secao de diferenciais em fundo light. |
| `images/lp-advogados/method-editorial.webp` | Imagem editorial lateral da secao de metodo. |
| `images/lp-advogados/consultation-overlay.webp` | Overlay sutil da secao de consultoria estrategica. |
| `images/lp-advogados/final-cta-compass.webp` | Background sutil do CTA final. |

## Compatibility Aliases

The current CSS keeps legacy local aliases scoped to `.law-lp`, such as `--bg-color`,
`--text-main`, `--text-muted`, `--accent-primary`, and `--border-light`. These aliases
map to the semantic tokens above so shared landing styles can keep working without
affecting the main site.
