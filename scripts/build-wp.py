#!/usr/bin/env python3
"""Build a WordPress-ready package for the /lp-advogados/ landing page.

Runs `hugo --minify`, then extracts:
  - wp-deploy/head-snippet.html  → inline <style> + fonts/favicon links, paste in WPCode "Site-wide Header"
  - wp-deploy/body-snippet.html  → page contents wrapped in <div class="law-lp"> + inline <script>
  - wp-deploy/images/            → every image referenced by the HTML and CSS

Image and home URLs are left as {{PLACEHOLDER}} tokens — replace them in WP after
uploading each file to the Media Library.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
OUT = ROOT / "wp-deploy"
SRC_HTML = PUBLIC / "lp-advogados" / "index.html"

BODY_IMAGE_PLACEHOLDERS = {
    "/images/logo.webp":                              "{{LOGO_URL}}",
    "/images/lp-advogados/deliverables-portrait.webp": "{{DELIVERABLES_URL}}",
    "/images/lp-advogados/gads-logo.webp":            "{{GADS_LOGO_URL}}",
    "/images/lp-advogados/mads-logo.webp":            "{{MADS_LOGO_URL}}",
}

CSS_IMAGE_PLACEHOLDERS = {
    "../images/lp-advogados/consultation-overlay.webp":  "{{CONSULTATION_OVERLAY_URL}}",
    "../images/lp-advogados/differentials-texture.webp": "{{DIFFERENTIALS_TEXTURE_URL}}",
    "../images/lp-advogados/final-cta-compass.webp":     "{{FINAL_CTA_COMPASS_URL}}",
    # hero-final.png is converted to WebP (1920×1080, q82) — see copy_images()
    "../images/lp-advogados/hero-final.png":             "{{HERO_FINAL_URL}}",
}

HERO_RESIZE = "2560x1440"
HERO_QUALITY = "95"


def run_hugo() -> None:
    print("→ hugo --minify")
    subprocess.run(["hugo", "--minify", "--cleanDestinationDir"], cwd=ROOT, check=True)


def extract_snippets() -> None:
    html = SRC_HTML.read_text(encoding="utf-8")

    css_match = re.search(r"href=(/css/style\.min\.[a-f0-9]+\.css)", html)
    js_match = re.search(r"src=(/js/law-landing\.min\.[a-f0-9]+\.js)", html)
    if not css_match or not js_match:
        sys.exit("could not locate CSS/JS asset references in index.html")

    css = (PUBLIC / css_match.group(1).lstrip("/")).read_text(encoding="utf-8")
    js = (PUBLIC / js_match.group(1).lstrip("/")).read_text(encoding="utf-8")

    head_inner = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
    body_inner = re.search(r"<body[^>]*>(.*?)</body>", html, re.S).group(1)

    head_inner = re.sub(r"<title>.*?</title>", "", head_inner, flags=re.S)
    head_inner = re.sub(r"<meta charset=[^>]*>", "", head_inner)
    head_inner = re.sub(r"<meta name=viewport[^>]*>", "", head_inner)
    head_inner = re.sub(r"<link rel=stylesheet href=/css/[^>]*>", "", head_inner)
    head_inner = re.sub(
        r'href="?/images/favicon\.png[^" >]*"?',
        'href="{{FAVICON_URL}}"',
        head_inner,
    )

    body_inner = re.sub(r"<script src=/js/[^>]*></script>", "<!-- JS injected below -->", body_inner)
    body_inner = body_inner.replace(
        "<a href=/ class=law-lp-logo-link",
        '<a href="{{HOME_URL}}" class=law-lp-logo-link',
    )
    for src, ph in BODY_IMAGE_PLACEHOLDERS.items():
        body_inner = body_inner.replace(src, ph)

    for src, ph in CSS_IMAGE_PLACEHOLDERS.items():
        css = css.replace(src, ph)

    head_out = head_inner.strip() + "\n<style>\n" + css + "\n</style>\n"
    body_out = (
        '<div class="law-lp">\n'
        + body_inner.strip()
        + "\n</div>\n<script>\n"
        + js
        + "\n</script>\n"
    )

    OUT.mkdir(exist_ok=True)
    (OUT / "head-snippet.html").write_text(head_out, encoding="utf-8")
    (OUT / "body-snippet.html").write_text(body_out, encoding="utf-8")
    print(f"  head-snippet.html: {len(head_out):,} bytes")
    print(f"  body-snippet.html: {len(body_out):,} bytes")


def copy_images() -> None:
    images_out = OUT / "images"
    if images_out.exists():
        shutil.rmtree(images_out)
    images_out.mkdir(parents=True)

    sources = [
        "images/favicon.png",
        "images/logo.webp",
        "images/lp-advogados/deliverables-portrait.webp",
        "images/lp-advogados/gads-logo.webp",
        "images/lp-advogados/mads-logo.webp",
        "images/lp-advogados/consultation-overlay.webp",
        "images/lp-advogados/differentials-texture.webp",
        "images/lp-advogados/final-cta-compass.webp",
    ]
    total = 0
    for rel in sources:
        src = PUBLIC / rel
        if not src.exists():
            sys.exit(f"missing source image: {src}")
        shutil.copy2(src, images_out / src.name)
        total += src.stat().st_size

    hero_src = PUBLIC / "images/lp-advogados/hero-final.png"
    hero_dst = images_out / "hero-final.webp"
    if not hero_src.exists():
        sys.exit(f"missing hero source: {hero_src}")
    subprocess.run(
        ["magick", str(hero_src), "-resize", HERO_RESIZE, "-quality", HERO_QUALITY, str(hero_dst)],
        check=True,
    )
    total += hero_dst.stat().st_size
    print(f"  images/: {len(sources) + 1} files, {total / 1024:,.1f} KB total")


def main() -> None:
    if "--skip-hugo" not in sys.argv:
        run_hugo()
    extract_snippets()
    copy_images()
    print(f"\n✓ wp-deploy/ ready at {OUT}")


if __name__ == "__main__":
    main()
