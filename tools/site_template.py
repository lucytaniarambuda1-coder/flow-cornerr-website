#!/usr/bin/env python3
"""
Shared nav / footer / script template for the Flow Corner site.

This is the single source of truth for the bits that used to be hand-duplicated
across every HTML file (nav, mobile nav, footer, the reveal+hamburger script).
Edit THIS file, then re-run tools/generate.py to regenerate every page.
"""

NAV_ITEMS = [
    ("/about/", "About"),
    ("/how-it-works/", "How It Works"),
    ("/services/", "Services"),
    ("/learning-hub/", "Learning Hub"),
    ("/work/", "Work"),
    ("/contact/", "Contact"),
]

SOCIAL_SVGS = {
    "linkedin": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
    "instagram": '<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>',
}

FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">'


def nav(active_path):
    """active_path: one of NAV_ITEMS' hrefs, or None for pages with no matching top-level item
    (Learning Hub sub-pages pass '/learning-hub/' so the Learning Hub nav item still highlights)."""
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active_path else ''
        links.append(f'    <li><a href="{href}"{cls}>{label}</a></li>')
    links_html = "\n".join(links)
    li_svg = SOCIAL_SVGS["linkedin"].format(size=18)
    ig_svg = SOCIAL_SVGS["instagram"].format(size=18)
    mobile_links = "\n".join(
        f'  <a href="{href}" class="mobile-link{" active" if href == active_path else ""}">{label}</a>'
        for href, label in NAV_ITEMS
    )
    return f'''<!-- NAV -->
<nav>
  <a href="/" class="nav-logo" style="text-decoration:none;">Lucy M.</a>
  <ul class="nav-links">
{links_html}
  </ul>
  <div class="nav-social">
    <a href="https://www.linkedin.com/in/mukhethwa-lucytania-rambuda-836575169/" target="_blank" rel="noopener" aria-label="LinkedIn">{li_svg}</a>
    <a href="https://www.instagram.com/flow_cornerr/" target="_blank" rel="noopener" aria-label="Instagram">{ig_svg}</a>
  </div>
</nav>

<!-- HAMBURGER BUTTON (mobile only) -->
<button class="hamburger" id="hamburger" aria-label="Open menu">
  <span></span><span></span><span></span>
</button>

<!-- MOBILE NAV OVERLAY -->
<div class="mobile-nav" id="mobileNav">
  <button class="mobile-nav-close" id="mobileClose">✕</button>
  <a href="/" class="mobile-link">Home</a>
{mobile_links}
</div>'''


def footer():
    li_svg = SOCIAL_SVGS["linkedin"].format(size=16)
    ig_svg = SOCIAL_SVGS["instagram"].format(size=16)
    return f'''<!-- FOOTER -->
<footer>
  <p><strong>Lucy Mukhethwa | Flow Corner</strong> — Career Strategist & Coach</p>
  <p style="margin-top:0.4rem;">Based in Johannesburg, South Africa · Available for remote services globally</p>
  <div class="footer-social">
    <a href="https://www.linkedin.com/in/mukhethwa-lucytania-rambuda-836575169/" target="_blank" rel="noopener" aria-label="LinkedIn">{li_svg}</a>
    <a href="https://www.instagram.com/flow_cornerr/" target="_blank" rel="noopener" aria-label="Instagram">{ig_svg}</a>
  </div>
  <p style="margin-top:0.6rem; font-size:0.74rem;">© 2026 Lucy Mukhethwa. All rights reserved.</p>
</footer>'''


SCRIPT = '''<script>
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 75);
      }
    });
  }, { threshold: 0.08 });
  reveals.forEach(el => observer.observe(el));

  // Mobile hamburger nav
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobileNav');
  const mobileClose = document.getElementById('mobileClose');
  if (hamburger && mobileNav && mobileClose) {
    hamburger.addEventListener('click', () => mobileNav.classList.add('open'));
    mobileClose.addEventListener('click', () => mobileNav.classList.remove('open'));
    document.querySelectorAll('.mobile-link').forEach(link => {
      link.addEventListener('click', () => mobileNav.classList.remove('open'));
    });
  }
</script>'''


def page(title, description, active_path, body, extra_head="", extra_scripts=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
{FONT_LINK}
<link rel="stylesheet" href="/assets/styles.css">
{extra_head}</head>
<body>

{nav(active_path)}

{body}

{footer()}

{SCRIPT}
{extra_scripts}
</body>
</html>
'''
