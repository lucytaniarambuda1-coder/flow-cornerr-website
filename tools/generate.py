#!/usr/bin/env python3
"""
Generates every page of the Flow Corner site from site_template.py + the
content defined below. Run this after editing nav/footer (site_template.py)
or any page content in this file:

    python3 tools/generate.py

Output HTML files are committed to the repo (this is a source-generates-output
setup, not a live build step) so the repo always reflects what's deployed.
"""
import os
import urllib.parse
import sys

sys.path.insert(0, os.path.dirname(__file__))
from site_template import page, SITE_URL  # noqa: E402
import business_pages as biz  # noqa: E402
import free_tools_pages as ft  # noqa: E402
import employer_pages as emp  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ICON = {
    "person": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.5-7 8-7s8 3 8 7"/></svg>',
    "briefcase": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><path d="M2 13h20"/></svg>',
    "folder": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7Z"/></svg>',
    "book": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2Z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7Z"/></svg>',
    "search": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    "filecheck": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/><path d="m9 15 2 2 4-4"/></svg>',
    "message": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    "bulb": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.3h6c0-1 .4-1.8 1-2.3A7 7 0 0 0 12 2Z"/></svg>',
    "zap": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "star": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    "compass": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
    "rocket": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>',
    "upload": '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14.9A5 5 0 0 1 6 5.3 6.5 6.5 0 0 1 19 8a4.5 4.5 0 0 1-1 8.9"/><path d="M12 12v9"/><path d="m8 16 4-4 4 4"/></svg>',
}

WHATSAPP_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:-3px; margin-right:0.3em;"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.06c-.24.68-1.4 1.3-1.93 1.38-.5.08-1.11.11-1.79-.11-.41-.13-.95-.31-1.63-.6-2.87-1.24-4.74-4.12-4.88-4.31-.14-.19-1.17-1.56-1.17-2.98 0-1.42.74-2.12 1-2.41.26-.29.57-.36.76-.36.19 0 .38 0 .55.01.18.01.41-.07.64.49.24.58.81 2 .88 2.14.07.14.12.31.02.5-.09.19-.14.31-.28.48-.14.17-.29.37-.42.5-.14.14-.28.29-.12.57.16.28.71 1.17 1.52 1.89 1.05.93 1.93 1.22 2.21 1.36.28.14.44.12.6-.07.16-.19.68-.79.87-1.06.19-.27.37-.22.63-.13.26.09 1.63.77 1.91.91.28.14.47.21.54.33.07.12.07.68-.17 1.36z"/></svg>'

FT = ft.build(ICON, WHATSAPP_SVG)
EMP = emp.build(WHATSAPP_SVG)

# ============================================================== HOME
home_body = f'''<!-- HERO -->
<section class="hero">
  <div class="hero-blob-yellow"></div>
  <div class="hero-text">
    <div class="hero-tag">Free Resources · Paid Career Services</div>
    <h1>Find Your <em>Flow.</em></h1>
    <p class="hero-lead">Your CV isn't getting through. Your LinkedIn isn't getting found. <em>Let's fix that.</em></p>
    <p class="hero-sub">The tools and guides here are free for every South African job-seeker. When you want me on your CV or career plan, that's paid one-on-one help, and your first 15-minute call is free.</p>
    <div class="hero-btns">
      <a href="/learning-hub/cv-check/" class="btn-primary">Try the Free CV Check</a>
      <a href="/free-tools/" class="btn-secondary">Explore Free Tools</a>
    </div>
    <ul class="hero-trust">
      <li>No sign-up</li>
      <li>Runs in your browser</li>
      <li>Made in South Africa</li>
    </ul>
  </div>
  <div class="hero-visual">
    <div class="hero-stack" id="heroStack">
      <a href="/free-tools/" class="hero-card hero-card-free">
        <div class="label">Free for everyone</div>
        <div class="value">Guides, tools &amp; career tests</div>
        <ul class="hero-chips">
          <li>Job-readiness score</li>
          <li>CV Check</li>
          <li>CV Builder</li>
          <li>Cover letters</li>
          <li>Interview practice</li>
        </ul>
        <div class="sub">No sign-up, no cost →</div>
      </a>
      <div class="hero-paid-row">
        <a href="/services/" class="hero-card hero-card-paid">
          <div class="label">Paid service</div>
          <div class="value">CV &amp; LinkedIn</div>
          <div class="sub">From R100</div>
        </a>
        <a href="/services/" class="hero-card hero-card-paid">
          <div class="label">Paid service</div>
          <div class="value">Career Roadmap</div>
          <div class="sub">From R500</div>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- FLOW BRAND BAR -->
<div class="flow-bar">
  <p>Flow is when work stops feeling like a fight: you're in a role that fits what you're good at and what you care about. <strong>Flow Corner is here to help you get there,</strong> with free tools, practical guides and one-on-one help when you need it.</p>
</div>

<!-- CHECK / BUILD / FIND / PRACTISE -->
<section class="verbs">
  <div class="section-label reveal">Free Career Tools</div>
  <div class="section-title reveal">Check it. Build it. Find it. <em>Practise it.</em></div>
  <div class="divider reveal"></div>
  <div class="explore-grid">
    <a href="/learning-hub/job-readiness/" class="explore-card reveal">
      <div class="explore-icon">{ICON['zap']}</div>
      <span class="verb-tag">Check it</span>
      <div class="explore-title">How job-ready are you?</div>
      <div class="explore-desc">Ten questions, a score out of 100 and a plan to fix your biggest gaps.</div>
      <span class="explore-arrow">Get my score →</span>
    </a>
    <a href="/free-tools/" class="explore-card reveal">
      <div class="explore-icon">{ICON['folder']}</div>
      <span class="verb-tag">Build it</span>
      <div class="explore-title">CV &amp; cover letter</div>
      <div class="explore-desc">Build a clean CV and a professional cover letter, then save them as a PDF.</div>
      <span class="explore-arrow">Open the tools →</span>
    </a>
    <a href="/opportunities/" class="explore-card reveal">
      <div class="explore-icon">{ICON['search']}</div>
      <span class="verb-tag">Find it</span>
      <div class="explore-title">Jobs &amp; opportunities</div>
      <div class="explore-desc">Job platforms, learnerships and youth programmes, each with the official link.</div>
      <span class="explore-arrow">See what's open →</span>
    </a>
    <a href="/free-tools/interview-practice/" class="explore-card reveal">
      <div class="explore-icon">{ICON['star']}</div>
      <span class="verb-tag">Practise it</span>
      <div class="explore-title">Interview practice</div>
      <div class="explore-desc">Common questions, a two-minute timer and the STAR method for strong answers.</div>
      <span class="explore-arrow">Start practising →</span>
    </a>
  </div>
</section>

<!-- FREE VS PAID -->
<section class="fp">
  <div class="section-label reveal">What's Free, What's Paid</div>
  <div class="section-title reveal">Free to learn. <em>Paid</em> when I work with you.</div>
  <div class="divider reveal"></div>
  <div class="fp-grid">
    <div class="fp-card fp-free reveal">
      <div class="fp-badge">Free</div>
      <h3>Free resources</h3>
      <p class="fp-lead">Use these as often as you like.</p>
      <ul class="fp-list">
        <li>Job-readiness score with an action plan</li>
        <li>Instant CV Check, CV Builder and Cover Letter Generator</li>
        <li>Interview practice with a timer</li>
        <li>Opportunities board for jobs and youth programmes</li>
        <li>Plain-English guides to using AI</li>
        <li>South African job sites and how to stand out</li>
        <li>Step-by-step guide to starting a small business</li>
        <li>Career assessment, with a follow-up from me</li>
        <li>Your first 15-minute call with me</li>
      </ul>
      <a href="/learning-hub/" class="fp-link">Go to the Learning Hub →</a>
    </div>
    <div class="fp-card fp-paid reveal">
      <div class="fp-badge">Paid</div>
      <h3>Services and products</h3>
      <p class="fp-lead">Where I spend my time on your work, or a kit you keep.</p>
      <div class="fp-group">One-on-one services</div>
      <ul class="fp-list">
        <li><span>CV Revamp</span><span>from R100</span></li>
        <li><span>LinkedIn Profile Revamp</span><span>from R150</span></li>
        <li><span>Career Development Roadmap</span><span>from R500</span></li>
        <li><span>Business Start-Up Support</span><span>quoted</span></li>
        <li><span>Websites and portfolios</span><span>from R1,200</span></li>
      </ul>
      <div class="fp-group">Digital products</div>
      <ul class="fp-list">
        <li><span><a href="/get-hired/">Get Hired with AI kit</a></span><span>R149</span></li>
        <li><span>Admin Template Bundles</span><span>from R150</span></li>
      </ul>
      <p class="fp-note">Founding clients pay half price on the first three services while spots last.</p>
      <a href="/services/" class="fp-link">See services &amp; pricing →</a>
    </div>
  </div>
</section>

<!-- WHY FREE -->
<section class="why-free">
  <div class="why-free-inner reveal">
    <div class="section-label">Why it's free</div>
    <h2>The basics shouldn't cost you anything.</h2>
    <p>Job hunting is expensive enough: data, transport, printing. Nobody should have to pay just to find out where they stand, or to get a CV that doesn't embarrass them. So the tools and guides are free, with no sign-up and no email trap, and what you type never leaves your device.</p>
    <p>What you pay for is my time. If you want me to rewrite your CV, fix your LinkedIn or build your career roadmap with you, that's the paid work, and it's what keeps the free part going.</p>
  </div>
</section>

<!-- EXPLORE -->
<section class="explore">
  <div class="section-label reveal">Find Your Way Around</div>
  <div class="section-title reveal">Explore <em>Flow Corner</em></div>
  <div class="divider reveal"></div>
  <div class="explore-grid">
    <a href="/learning-hub/" class="explore-card reveal">
      <div class="explore-icon">{ICON['book']}</div>
      <div class="explore-title">Learning Hub</div>
      <div class="explore-desc">Free AI guides, job-search resources, a CV check and a business start-up guide. The best place to start.</div>
      <span class="explore-arrow">Start here →</span>
    </a>
    <a href="/services/" class="explore-card reveal">
      <div class="explore-icon">{ICON['briefcase']}</div>
      <div class="explore-title">Services & Pricing</div>
      <div class="explore-desc">Paid one-on-one help with your CV, LinkedIn and career plan, plus a founding-client offer.</div>
      <span class="explore-arrow">See services →</span>
    </a>
    <a href="/about/" class="explore-card reveal">
      <div class="explore-icon">{ICON['person']}</div>
      <div class="explore-title">About Lucy</div>
      <div class="explore-desc">My story, credentials, and the principles behind how I coach.</div>
      <span class="explore-arrow">Meet Lucy →</span>
    </a>
    <a href="/about/#experience" class="explore-card reveal">
      <div class="explore-icon">{ICON['folder']}</div>
      <div class="explore-title">Experience & Work</div>
      <div class="explore-desc">What I've done in HR, BPO operations and AI projects.</div>
      <span class="explore-arrow">See the work →</span>
    </a>
  </div>
</section>

<!-- CTA -->
<section class="cta">
  <h2 class="reveal">Your career should feel<br>like <em>flow.</em></h2>
  <p class="reveal">Tell me where you're stuck. The first 15-minute call is free, and we'll work out your next step together.</p>
  <div class="cta-btns reveal">
    <a href="/contact/" class="btn-pink">Book My Free Call</a>
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%20would%20like%20to%20enquire%20about%20your%20services" class="btn-whatsapp" target="_blank" rel="noopener">{WHATSAPP_SVG}Chat on WhatsApp</a>
  </div>
</section>'''

# ============================================================== ABOUT
about_body = f'''<div class="page-header">
  <div class="section-label">About Me</div>
  <h1>Hi, I'm <em>Lucy.</em></h1>
  <div class="hero-tag" style="margin:0.5rem auto 1.6rem;">Career Strategist · AI Projects Manager · I&amp;O Psychology</div>
  <div class="stats-row" style="max-width:420px; margin:0 auto 1.8rem;">
    <div class="hero-card">
      <div class="label">Experience</div>
      <div class="value">6+ yrs</div>
      <div class="sub">HR & Operations</div>
    </div>
    <div class="hero-card">
      <div class="label">Credentials</div>
      <div class="value" style="font-size:1.1rem;">Masters</div>
      <div class="sub">I&amp;O Psychology (studying)</div>
    </div>
  </div>
  <p>"Passion. Purpose. Peace." <span style="opacity:0.6;">The title of my upcoming book, and how I try to show up every day.</span></p>
</div>

<section class="about">
  <div class="about-grid">
    <div>
      <img class="about-photo" src="/assets/lucy.jpg" srcset="/assets/lucy-480.jpg 480w, /assets/lucy.jpg 768w" sizes="220px" width="220" height="220" alt="Lucy Mukhethwa" loading="lazy">
      <div class="pillars">
        <span class="pillar">ATS-Optimised CVs</span>
        <span class="pillar">LinkedIn Strategy</span>
        <span class="pillar">Career Psychology</span>
        <span class="pillar">C-Suite Insight</span>
        <span class="pillar">Executive Communication</span>
        <span class="pillar">People-First Coaching</span>
      </div>
    </div>
    <div class="about-text">
      <p>I'm Lucy Mukhethwa, a South African career strategist based near Johannesburg. I have 6+ years in HR and operations. Today I work as an AI Projects Manager at a global BPO, and I support C-suite leadership, working directly with the COO across multi-country strategic initiatives.</p>
      <p>My background spans HR and administration, progressing from HR Assistant through to Generalist and into operations and leadership support. As an AI Projects Manager I run AI adoption projects (voice bots, chatbot integration and automation strategy), which gives me a hands-on, practitioner's view of how AI is reshaping modern workplaces, not just a theoretical one.</p>
      <p>I'm studying a Masters in Industrial &amp; Organisational Psychology, with my research focused on career psychology. I'm also a Christian living author completing final review ahead of publication. What I want is simple: for capable people to stop getting filtered out because of a weak CV or a LinkedIn profile nobody can find.</p>
    </div>
  </div>
</section>

<!-- WHY LUCY -->
<section class="whylucy">
  <div class="section-label reveal">Why Choose Lucy</div>
  <div class="section-title reveal">What I <em>bring</em></div>
  <div class="divider reveal"></div>
  <div class="why-grid">
    <div class="why-card reveal">
      <div class="why-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5"/><path d="M22 10v6"/></svg></div>
      <h3>Grounded in psychology</h3>
      <p>I'm studying a Masters in Industrial &amp; Organisational Psychology, and my research focuses on career psychology, so the assessments and advice I use come from research, not guesswork.</p>
    </div>
    <div class="why-card reveal">
      <div class="why-icon">{ICON['briefcase']}</div>
      <h3>I've seen how executives decide</h3>
      <p>I have 6+ years in HR and operations, and I now support C-suite leadership as an AI Projects Manager. I know what decision-makers look for, and I build that into every CV, LinkedIn profile and career plan.</p>
    </div>
    <div class="why-card reveal">
      <div class="why-icon">{ICON['compass']}</div>
      <h3>Your work, your values</h3>
      <p>I care about where your career is going, not only the next job title. We'll connect your goals to what matters to you.</p>
    </div>
  </div>
</section>

<section class="cta" style="padding: 5rem 5%;">
  <h2 class="reveal">Ready to find <em>your</em> flow?</h2>
  <div class="cta-btns reveal">
    <a href="/how-it-works/" class="btn-pink">See How It Works</a>
    <a href="/contact/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5);">Get In Touch</a>
  </div>
</section>'''

# ============================================================== HOW IT WORKS
how_body = '''<div class="page-header">
  <div class="section-label">The Process</div>
  <h1>How we'll <em>work together</em></h1>
  <p>Three steps, from a free call to a CV and profile you're proud to send.</p>
</div>

<section class="how">
  <div class="steps-grid">
    <div class="step-card reveal">
      <div class="step-number">01</div>
      <div class="step-title">Book a Free Discovery Call</div>
      <div class="step-desc">Tell me where you are and where you want to be. In 15 minutes, we'll identify exactly what's holding you back and what needs to change.</div>
    </div>
    <div class="step-card reveal">
      <div class="step-number">02</div>
      <div class="step-title">We Build Your Strategy</div>
      <div class="step-desc">CV, LinkedIn, career roadmap, or all three. I rework them around the specific roles you're applying for, not a one-size-fits-all template.</div>
    </div>
    <div class="step-card reveal">
      <div class="step-number">03</div>
      <div class="step-title">You Show Up Differently</div>
      <div class="step-desc">You apply with a CV that shows your results, a LinkedIn profile recruiters can find, and a clear idea of what you're aiming for.</div>
    </div>
  </div>
  <div style="text-align:center; margin-top:2.5rem; display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
    <a href="/contact/" class="btn-primary" style="display:inline-block;">Book My Free Call</a>
    <a href="/learning-hub/free-assessment/" class="btn-secondary" style="display:inline-block;">Take Free Assessment First →</a>
  </div>
  <p style="text-align:center; margin-top:1.3rem; font-size:0.85rem; color:var(--charcoal);">Not ready to book? <a href="/learning-hub/cv-check/" style="color:var(--pink-deep); font-weight:700;">Try the free CV Check</a> first.</p>
  <p style="text-align:center; margin-top:0.6rem; font-size:0.85rem; color:var(--charcoal);">Starting a business instead of looking for a job? The same three steps apply. <a href="/learning-hub/start-a-business/" style="color:var(--pink-deep); font-weight:700;">Start with our free guide</a>.</p>
</section>'''

# ============================================================== SERVICES
services_body = '''<div class="page-header">
  <div class="section-label">Services</div>
  <h1>How I can <em>help you</em></h1>
  <p>Paid, one-on-one career support, a helping hand if you're starting your own business, and a few digital products. Your first 15-minute call is free.</p>
</div>

<section class="services">
  <div class="services-grid">
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></div>
      <div class="service-title">LinkedIn Profile Revamp</div>
      <div class="service-desc">I rewrite your headline, summary, and experience using the keywords recruiters in your field actually search for.</div>
      <div class="service-price">Starting from R150</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/><path d="M9 13h6"/><path d="M9 17h6"/></svg></div>
      <div class="service-title">CV Revamp</div>
      <div class="service-desc">I restructure your CV so it gets through applicant tracking systems and reads well to a person, tailored to your industry and level.</div>
      <div class="service-price">Starting from R100</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg></div>
      <div class="service-title">Career Development Roadmap</div>
      <div class="service-desc">A personalised career roadmap including skills gap analysis, goal setting, and a clear action plan to get you where you want to be.</div>
      <div class="service-price">Starting from R500</div>
    </div>
  </div>
  <p style="text-align:center; margin-top:2rem; font-size:0.88rem; color:var(--charcoal);">Each service includes one full delivery and one round of revisions.</p>
  <p style="text-align:center; margin-top:0.6rem; font-size:0.88rem; color:var(--charcoal);">Not ready to book? <a href="/learning-hub/cv-check/" style="color:var(--pink-deep); font-weight:700;">Try our free CV Check</a> first. It's instant and it's free.</p>
</section>

<!-- BUSINESS START-UP SUPPORT -->
<section class="biz-support">
  <div class="biz-support-inner reveal">
    <div class="biz-support-icon">@@ROCKET@@</div>
    <div class="biz-support-text">
      <div class="extra-services-label">For Entrepreneurs</div>
      <h2>Business Start-Up Support</h2>
      <p>Thinking of starting your own business? I'll walk with you from idea to first customer: testing the idea, choosing a structure, getting registered, and getting ready to apply for funding.</p>
      <ul>
        <li>Idea check and a simple business plan</li>
        <li>Choosing a structure and getting registered (CIPC and SARS)</li>
        <li>Funding-readiness: your plan, pitch and documents</li>
        <li>Planning your first customers and first 90 days</li>
      </ul>
      <p class="biz-note"><strong>Free intro call, then a quote</strong> based on what you need. I'm a career strategist, not an accountant or attorney, so for tax and legal advice I'll point you to the right people.</p>
      <div class="biz-support-btns">
        <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%27d%20like%20help%20starting%20a%20business" class="btn-pink" target="_blank" rel="noopener">Book a Free Intro Call</a>
        <a href="/learning-hub/start-a-business/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5); color:var(--pink);">Read the Free Guides</a>
      </div>
    </div>
  </div>
</section>

<!-- ALSO AVAILABLE -->
<section class="extra-services">
  <div class="extra-services-inner">
    <div class="extra-services-label">Also Available: Websites</div>
    <div class="extra-list">
      <div class="extra-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15 15 0 0 1 0 20a15 15 0 0 1 0-20"/></svg>
        <div>
          <div class="extra-item-title">Website Building</div>
          <div class="extra-item-desc">Clean, modern websites for small businesses and consultants.</div>
          <div class="extra-item-price">From R1,500</div>
        </div>
      </div>
      <div class="extra-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-5-5L5 21"/></svg>
        <div>
          <div class="extra-item-title">Personal Portfolio Website</div>
          <div class="extra-item-desc">A digital portfolio for creatives, graduates, and freelancers.</div>
          <div class="extra-item-price">From R1,200</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- DIGITAL PRODUCTS -->
<section class="extra-services" style="padding-top:0;">
  <div class="extra-services-inner">
    <div class="extra-services-label">Digital Products: Buy Once, Keep</div>
    <div class="extra-list">
      <a class="extra-item" href="/get-hired/" style="text-decoration:none; color:inherit;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2Z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7Z"/></svg>
        <div>
          <div class="extra-item-title">Get Hired with AI kit</div>
          <div class="extra-item-desc">A 7-day guide, 45 AI prompts, 3 CV templates and a South African opportunities sheet. Do it yourself, at your own pace.</div>
          <div class="extra-item-price">R149 founding price (then R249) · See the kit →</div>
        </div>
      </a>
      <div class="extra-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        <div>
          <div class="extra-item-title">Admin Template Bundles</div>
          <div class="extra-item-desc">Ready-to-use SOP templates, email packs, and checklists.</div>
          <div class="extra-item-price">From R150</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FOUNDING CLIENTS -->
<section class="founding" style="background: var(--off-white);">
  <div class="section-label reveal">Founding Clients</div>
  <div class="section-title reveal">Founding client <em>rates</em></div>
  <div class="divider reveal"></div>
  <div class="founding-content">
    <p class="reveal">I'm currently taking on <strong>3 founding clients</strong> at <strong>half price</strong>, in exchange for an honest, detailed testimonial once we've worked together.</p>
    <p class="reveal">You get professional career support for half the normal price, and I get a testimonial to build on.</p>
    <div class="founding-what reveal" style="background: var(--white);">
      <div class="founding-item"><span><svg class="inline-star" width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> CV Revamp</span><span class="founding-price"><strong>R50</strong> <s>R100</s></span></div>
      <div class="founding-item"><span><svg class="inline-star" width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> LinkedIn Revamp</span><span class="founding-price"><strong>R75</strong> <s>R150</s></span></div>
      <div class="founding-item"><span><svg class="inline-star" width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> Career Roadmap</span><span class="founding-price"><strong>R250</strong> <s>R500</s></span></div>
      <p style="font-size:0.82rem; color:rgba(15,32,68,0.5); margin-top:0.9rem; text-align:left;">Same service as the full price: one full delivery and one round of revisions. Once complete, I'll follow up with a short testimonial request.</p>
    </div>
    <p class="founding-note reveal">Only 3 spots available. First come, first served.</p>
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%27d%20like%20to%20apply%20as%20a%20founding%20client" class="btn-pink reveal" target="_blank" rel="noopener">Apply as a Founding Client →</a>
  </div>
</section>'''

# ============================================================== WORK
work_body = f'''<div class="page-header">
  <div class="section-label">Professional Experience</div>
  <h1>Where I've <em>worked</em></h1>
  <p>6+ years across BPO, HR, and career development.</p>
</div>

<section class="experience">
  <div class="exp-grid" style="margin-top: 0;">
    <div class="exp-card reveal">
      <div class="exp-role">Administrative Coordinator</div>
      <div class="exp-area">Global BPO · Johannesburg, South Africa</div>
      <div class="exp-desc">Supporting executive-level operations across multiple countries. Coordinating board presentations, strategic projects, contract reviews, mentorship programmes, and cross-functional initiatives at C-suite level.</div>
      <div class="exp-tags">
        <span class="exp-tag">C-Suite Support</span>
        <span class="exp-tag">Global Operations</span>
        <span class="exp-tag">Strategic Coordination</span>
        <span class="exp-tag">AI Tools</span>
      </div>
    </div>
    <div class="exp-card reveal">
      <div class="exp-role">HR Professional</div>
      <div class="exp-area">HR Assistant → Generalist → Coordinator</div>
      <div class="exp-desc">Progressive HR career spanning employee relations, policy development, onboarding design, workforce engagement, and compliance, building a strong foundation in people operations across multiple industries.</div>
      <div class="exp-tags">
        <span class="exp-tag">HR Operations</span>
        <span class="exp-tag">Policy Development</span>
        <span class="exp-tag">Employee Relations</span>
        <span class="exp-tag">Compliance</span>
      </div>
    </div>
    <div class="exp-card reveal">
      <div class="exp-role">AI Projects Manager</div>
      <div class="exp-area">Global BPO · AI Adoption & Automation</div>
      <div class="exp-desc">Leading AI adoption initiatives within a contact-centre environment (voice bot deployment, chatbot integration and automation strategy), alongside hands-on use of ChatGPT, Claude, Perplexity, NotebookLM, and Gemini to enhance operational and administrative efficiency.</div>
      <div class="exp-tags">
        <span class="exp-tag">AI Strategy</span>
        <span class="exp-tag">ChatGPT</span>
        <span class="exp-tag">Claude</span>
        <span class="exp-tag">Workflow Automation</span>
      </div>
    </div>
    <div class="exp-card reveal">
      <div class="exp-role">Website & Digital Development</div>
      <div class="exp-area">Websites for Organisations & Ministry</div>
      <div class="exp-desc">Built and maintained professional websites for corporate and church environments. Comfortable working with web platforms, content management, and digital presence development.</div>
      <div class="exp-tags">
        <span class="exp-tag">Website Development</span>
        <span class="exp-tag">Digital Presence</span>
        <span class="exp-tag">CMS</span>
        <span class="exp-tag">Church & Corporate</span>
      </div>
    </div>
  </div>
</section>

<!-- PORTFOLIO -->
<section class="portfolio">
  <div class="section-label reveal">Experience Highlights</div>
  <div class="section-title reveal" style="color:var(--white);">Work I've <em>been part of</em></div>
  <div class="divider reveal"></div>
  <p class="reveal" style="text-align:center; color:rgba(255,255,255,0.6); font-size:0.9rem; max-width:580px; margin:0 auto 2.5rem; line-height:1.8;">A few projects I'm proud of from my HR and BPO roles.</p>
  <div class="portfolio-grid">
    <div class="port-card reveal">
      <div class="port-icon">{ICON['filecheck']}</div>
      <div class="port-title">Cross-Border Legal Documentation</div>
      <div class="port-desc">Adapted employment frameworks across different legal jurisdictions, ensuring full compliance with local labour laws and regulatory requirements.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15 15 0 0 1 0 20a15 15 0 0 1 0-20"/></svg></div>
      <div class="port-title">Global Expansion Support</div>
      <div class="port-desc">Supported multi-country office and operational expansion, from research and cost analysis through to stakeholder coordination and documentation.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg></div>
      <div class="port-title">AI-First Workflow Projects</div>
      <div class="port-desc">Contributed to AI adoption initiatives including voice bot deployment, chatbot integration, and agent augmentation projects within contact centre environments.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg></div>
      <div class="port-title">Brand & Digital Asset Development</div>
      <div class="port-desc">Designed professional brand books, presentations, and digital collateral, maintaining visual consistency and quality across organisational deliverables.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg></div>
      <div class="port-title">Executive Presentations & Reporting</div>
      <div class="port-desc">Produced board-level presentations and strategic reports, synthesising complex information into clear, decision-ready formats for senior leadership.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div>
      <div class="port-title">Book: Coming Soon</div>
      <div class="port-desc">Authored a Christian living book end-to-end, from manuscript to cover design and editorial review. Currently under final review ahead of publication. Title: <em>Passion. Purpose. Peace: Becoming Whole in Christ</em>.</div>
    </div>
  </div>
</section>

<section class="cta" style="padding: 5rem 5%;">
  <h2 class="reveal">Like what you <em>see?</em></h2>
  <div class="cta-btns reveal">
    <a href="/services/" class="btn-pink">View Services & Pricing</a>
    <a href="/contact/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5);">Get In Touch</a>
  </div>
</section>'''

# ============================================================== CONTACT
contact_body = '''<div class="page-header">
  <div class="section-label">Contact</div>
  <h1>Let's talk <em>flow.</em></h1>
  <p>Tell me where you're stuck, and we'll work out the next step together.</p>
</div>

<section class="cta" style="padding-top: 5rem;">
  <h2 class="reveal">Book your free 15-minute<br>discovery call <em>today.</em></h2>
  <p class="reveal">Prefer WhatsApp? Message me directly and I'll respond within 24 hours.</p>
  <div class="cta-btns reveal">
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%27d%20like%20to%20book%20my%20free%2015-minute%20discovery%20call" class="btn-pink" target="_blank" rel="noopener">Book My Free Call</a>
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%20would%20like%20to%20enquire%20about%20your%20services" class="btn-whatsapp" target="_blank" rel="noopener">''' + WHATSAPP_SVG + '''Chat on WhatsApp</a>
  </div>
</section>

<section class="about" style="text-align:center;">
  <div class="section-label reveal" style="justify-content:center; display:flex;">Not Ready to Talk Yet?</div>
  <div class="section-title reveal">Start with a <em>free assessment</em></div>
  <div class="divider reveal" style="margin-left:auto; margin-right:auto;"></div>
  <p class="reveal" style="max-width:560px; margin:0 auto 2rem; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">Take a free career test first, share your result, and I'll reach out to book your call.</p>
  <a href="/learning-hub/free-assessment/" class="btn-primary reveal" style="display:inline-block;">Take Free Assessment</a>
</section>

<section class="about" style="text-align:center; background: var(--off-white);">
  <div class="section-label reveal" style="justify-content:center; display:flex;">Starting a Business?</div>
  <div class="section-title reveal">Let's get your idea <em>off the ground</em></div>
  <div class="divider reveal" style="margin-left:auto; margin-right:auto;"></div>
  <p class="reveal" style="max-width:560px; margin:0 auto 2rem; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">Start with the free step-by-step guide and funding guide, or message me about Business Start-Up Support. The first call is free.</p>
  <div class="cta-btns reveal" style="justify-content:center;">
    <a href="/learning-hub/start-a-business/" class="btn-primary" style="display:inline-block;">Read the Free Guides</a>
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%27d%20like%20help%20starting%20a%20business" class="btn-secondary" style="display:inline-block;" target="_blank" rel="noopener">Ask About Start-Up Support</a>
  </div>
</section>'''

# ============================================================== LEARNING HUB — landing
hub_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Your Free <em>Career Toolkit</em></h1>
  <p>AI explained simply, real job-search resources, and tools to help you move forward. Everything in the hub is free, with no sign-up.</p>
</div>

<section class="explore">
  <p style="max-width:680px; margin:0 auto 1rem; text-align:center; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">AI is changing how people find work, from writing a standout CV to discovering roles you didn't know existed. This hub exists to make that useful for you, for free. And if you'd rather work for yourself, there's a guide for that too.</p>
  <div class="hub-grid">
    <a href="/learning-hub/learn-ai/" class="hub-card reveal">
      <div class="explore-icon">{ICON['bulb']}</div>
      <div class="hub-card-title">Understand & Use AI</div>
      <div class="hub-card-desc">What AI is, and how to use it for your CV, applications and everyday work.</div>
      <span class="hub-card-arrow">Start learning →</span>
    </a>
    <a href="/learning-hub/find-a-job/" class="hub-card reveal">
      <div class="explore-icon">{ICON['search']}</div>
      <div class="hub-card-title">Find a Job</div>
      <div class="hub-card-desc">Where South African job-seekers find roles, plus how to stand out once you do.</div>
      <span class="hub-card-arrow">Start searching →</span>
    </a>
    <a href="/learning-hub/cv-check/" class="hub-card reveal">
      <div class="explore-icon">{ICON['filecheck']}</div>
      <div class="hub-card-title">Check Your CV Instantly</div>
      <div class="hub-card-desc">Paste or upload your CV and get instant, free pointers. Nothing leaves your browser.</div>
      <span class="hub-card-arrow">Check my CV →</span>
    </a>
    <a href="/learning-hub/free-assessment/" class="hub-card reveal">
      <div class="explore-icon">{ICON['message']}</div>
      <div class="hub-card-title">Get Personalised Guidance</div>
      <div class="hub-card-desc">Take a free career assessment and I'll personally follow up with guidance for your situation.</div>
      <span class="hub-card-arrow">Take the test →</span>
    </a>
    <a href="/learning-hub/job-readiness/" class="hub-card reveal">
      <div class="explore-icon">{ICON['zap']}</div>
      <div class="hub-card-title">How Job-Ready Are You?</div>
      <div class="hub-card-desc">Ten questions, a score out of 100 and a plan to close your biggest gaps.</div>
      <span class="hub-card-arrow">Get my score →</span>
    </a>
    <a href="/free-tools/" class="hub-card reveal">
      <div class="explore-icon">{ICON['folder']}</div>
      <div class="hub-card-title">Free Career Tools</div>
      <div class="hub-card-desc">A CV builder, cover letter generator and interview practice, plus the opportunities board.</div>
      <span class="hub-card-arrow">Open the tools →</span>
    </a>
    <a href="/learning-hub/start-a-business/" class="hub-card hub-card-wide reveal">
      <div class="explore-icon">{ICON['rocket']}</div>
      <div class="hub-card-title">Start a Business</div>
      <div class="hub-card-desc">A step-by-step guide to starting a small business in South Africa, the funding available to youth and entrepreneurs, and the official links to get it done.</div>
      <span class="hub-card-arrow">Start your business →</span>
    </a>
  </div>
  <a href="/get-hired/" class="hub-paid reveal">
    <span class="hub-paid-badge">Paid · R149</span>
    <span class="hub-paid-title">Want it all in one kit? Get Hired with AI</span>
    <span class="hub-paid-desc">A 7-day guide, 45 AI prompts, 3 CV templates and an opportunities sheet. A paid digital product, separate from the free hub.</span>
    <span class="hub-card-arrow">See the kit →</span>
  </a>
  <p style="text-align:center; margin-top:3rem; font-size:0.88rem; color:var(--charcoal);">Want to talk to a real person instead? <a href="/contact/" style="color:var(--pink-deep); font-weight:700;">Get in touch</a>.</p>
</section>'''

# ============================================================== LEARNING HUB — learn-ai
def resource_card(title, desc, icon_key="bulb", href="#", external=None, label="Read more →"):
    """Card linking to an internal page or an external site (external links open in a new tab)."""
    if external is None:
        external = href.startswith("http")
    target_attr = ' target="_blank" rel="noopener"' if external else ''
    return f'''<a href="{href}" class="resource-card reveal"{target_attr}>
      <div class="resource-icon">{ICON[icon_key]}</div>
      <div>
        <div class="resource-title">{title}</div>
        <div class="resource-desc">{desc}</div>
        <div class="resource-link">{label}</div>
      </div>
    </a>'''


learn_ai_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Understand & Use <em>AI</em></h1>
  <p>What AI is, in plain English, and how to use it for your career.</p>
</div>

<section class="explore">
  <div class="hub-category-label">AI Basics</div>
  <p class="hub-category-intro">New to AI? Start here.</p>
  <div class="resource-grid">
    {resource_card("What Is AI, Really?", "A beginner's explainer: what AI is, and what it isn't.", "bulb", "/learning-hub/learn-ai/what-is-ai/")}
    {resource_card("How Tools Like ChatGPT & Claude Work", "A plain-language look at how AI chat tools work under the hood.", "zap", "/learning-hub/learn-ai/how-ai-chat-tools-work/")}
  </div>

  <div class="hub-category-label">Using AI Practically</div>
  <p class="hub-category-intro">Ready to put it to work? These focus on real, everyday use.</p>
  <div class="resource-grid">
    {resource_card("Prompting 101", "A beginner's guide to getting better, more useful results from AI chat tools.", "message", "/learning-hub/learn-ai/prompting-101/")}
    {resource_card("Free AI Tools Worth Trying", "A short list of free AI tools worth using for work and study.", "star", "/learning-hub/learn-ai/free-ai-tools/")}
    {resource_card("Using AI to Sharpen Your CV & LinkedIn", "How to use AI as a drafting assistant, not a replacement for your own voice.", "filecheck", "/learning-hub/learn-ai/ai-for-cv-linkedin/")}
  </div>

  <p style="text-align:center; margin-top:3rem; font-size:0.95rem;">Ready to see how your CV stacks up? <a href="/learning-hub/cv-check/" style="color:var(--pink-deep); font-weight:700;">Try the free CV Check →</a></p>
</section>'''

# ============================================================== LEARNING HUB — find-a-job
find_job_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Find Your Next <em>Job</em></h1>
  <p>Where to look, how to stand out, and how to get help when you're stuck.</p>
</div>

<section class="explore">
  <div class="hub-category-label">Where to Search</div>
  <p class="hub-category-intro">South African job boards and platforms worth checking regularly.</p>
  <div class="resource-grid">
    {resource_card("LinkedIn Jobs", "One of the most active platforms for professional roles in South Africa.", "search", "https://www.linkedin.com/jobs")}
    {resource_card("Indeed South Africa", "A large general job board covering roles across every industry.", "search", "https://za.indeed.com")}
    {resource_card("PNet", "A long-standing, popular South African job board.", "search", "https://www.pnet.co.za")}
  </div>

  <div class="hub-category-label">How to Stand Out</div>
  <p class="hub-category-intro">Getting found is only step one. Here's how to make an impression once you are.</p>
  <div class="resource-grid">
    <a href="/services/" class="resource-card reveal">
      <div class="resource-icon">{ICON['briefcase']}</div>
      <div>
        <div class="resource-title">LinkedIn Profile Revamp</div>
        <div class="resource-desc">Let's rewrite your headline and summary so recruiters notice you.</div>
        <div class="resource-link">See the service →</div>
      </div>
    </a>
    {resource_card("Interview Prep Basics", "A solid, free starting point for common interview questions and how to answer them.", "star", "https://www.indeed.com/career-advice/interviewing/top-interview-questions-and-answers")}
  </div>

  <p class="hub-category-intro" style="margin-top:2.5rem;">Would you rather work for yourself? <a href="/learning-hub/start-a-business/" style="color:var(--pink-deep); font-weight:700;">See our Start a Business guides</a>.</p>

  <div class="hub-category-label">Direct from Lucy</div>
  <p class="hub-category-intro">Prefer a more personal starting point?</p>
  <div class="resource-grid">
    <a href="/how-it-works/" class="resource-card reveal">
      <div class="resource-icon">{ICON['compass']}</div>
      <div><div class="resource-title">How It Works</div><div class="resource-desc">See exactly how we'd work together, step by step.</div><div class="resource-link">Learn more →</div></div>
    </a>
    <a href="/learning-hub/free-assessment/" class="resource-card reveal">
      <div class="resource-icon">{ICON['message']}</div>
      <div><div class="resource-title">Free Assessment</div><div class="resource-desc">Not sure what role fits you? Start with a free test.</div><div class="resource-link">Take the test →</div></div>
    </a>
    <a href="/contact/" class="resource-card reveal">
      <div class="resource-icon">{ICON['person']}</div>
      <div><div class="resource-title">Get In Touch</div><div class="resource-desc">Ready to talk? Book a free 15-minute call.</div><div class="resource-link">Contact Lucy →</div></div>
    </a>
  </div>
</section>'''

# ============================================================== LEARNING HUB — free assessment (moved from /assessment/)
free_assessment_body = '''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Find your <em>starting point</em></h1>
  <p>Not sure where to begin? Start with a free, internationally recognised assessment.</p>
  <p style="margin-top:0.9rem;"><a href="/learning-hub/" style="color:var(--pink); font-weight:700; font-style:normal;">← Back to Learning Hub</a></p>
</div>

<section class="assessment">
  <p class="assess-intro reveal">Once you have your result, fill in the form below. I'll reach out via WhatsApp or email within 24 hours to book your free 15-minute discovery call, and we'll unpack exactly what your result means for your career path.</p>
  <div class="assess-grid">
    <div class="assess-card reveal">
      <div class="assess-emoji"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="12" r="6"/><circle cx="15" cy="12" r="6"/></svg></div>
      <div class="assess-name">16Personalities</div>
      <div class="assess-what">Personality Type</div>
      <div class="assess-desc">One of the most widely used personality frameworks in the world. Discover how you think, work and connect, and which careers align with your type.</div>
      <div class="assess-time">⏱ 10–12 minutes · Free</div>
      <a href="https://www.16personalities.com/" target="_blank" rel="noopener" class="btn-assess">Take Free Test →</a>
    </div>
    <div class="assess-card reveal">
      <div class="assess-emoji"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg></div>
      <div class="assess-name">DISC Assessment</div>
      <div class="assess-what">Work Style</div>
      <div class="assess-desc">Understand your dominant workplace behaviour style (Dominance, Influence, Steadiness or Conscientiousness) and how it shapes your career fit.</div>
      <div class="assess-time">⏱ 10 minutes · Free</div>
      <a href="https://www.123test.com/disc-personality-test/" target="_blank" rel="noopener" class="btn-assess">Take Free Test →</a>
    </div>
    <div class="assess-card reveal">
      <div class="assess-emoji"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg></div>
      <div class="assess-name">Holland Code</div>
      <div class="assess-what">Career Interests</div>
      <div class="assess-desc">Based on John Holland's RIASEC theory, the foundation of career psychology. Matches your interests to real career paths and fields where you're most likely to thrive.</div>
      <div class="assess-time">⏱ 10–15 minutes · Free</div>
      <a href="https://www.mynextmove.org/explore/ip" target="_blank" rel="noopener" class="btn-assess">Take Free Test →</a>
    </div>
  </div>
  <div class="assess-form-wrap reveal">
    <h3>Share your result, get your free call</h3>
    <p>Completed a test? Fill in your details below and I'll reach out within 24 hours to book your free 15-minute career discovery call.</p>
    <form name="career-assessment" netlify netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="career-assessment">
      <p style="display:none;"><label>Don't fill this out: <input name="bot-field"></label></p>
      <div class="form-row">
        <div class="form-field">
          <label for="fname">Full Name *</label>
          <input type="text" id="fname" name="name" placeholder="Your full name" required>
        </div>
        <div class="form-field">
          <label for="femail">Email Address *</label>
          <input type="email" id="femail" name="email" placeholder="your@email.com" required>
        </div>
      </div>
      <div class="form-row">
        <div class="form-field">
          <label for="fphone">Phone / WhatsApp *</label>
          <input type="tel" id="fphone" name="phone" placeholder="+27 82 000 0000" required>
        </div>
        <div class="form-field">
          <label for="ftest">Which test did you complete? *</label>
          <select id="ftest" name="test_taken" required>
            <option value="" disabled selected>Select a test</option>
            <option value="16Personalities">16Personalities</option>
            <option value="DISC">DISC Assessment</option>
            <option value="Holland Code">Holland Code (RIASEC)</option>
            <option value="Multiple">I completed more than one</option>
          </select>
        </div>
      </div>
      <div class="form-field">
        <label for="fresult">Your Result Type *</label>
        <input type="text" id="fresult" name="result_type" placeholder="e.g. INFJ, Dominant (D), Realistic-Investigative, etc." required>
      </div>
      <div class="form-field">
        <label for="fchallenge">What is your biggest career challenge right now? *</label>
        <textarea id="fchallenge" name="career_challenge" placeholder="Tell me what's holding you back or what you're trying to figure out..." required></textarea>
      </div>
      <button type="submit" class="btn-submit">Submit & Book My Free Discovery Call</button>
      <p class="form-note">By submitting, you agree to be contacted via WhatsApp or email within 24 hours. No spam, ever.</p>
    </form>
  </div>
</section>'''

# ============================================================== LEARNING HUB — cv-check
cv_check_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Check Your <em>CV</em>, Instantly</h1>
  <p>Paste your CV or upload a file to get free, instant pointers. Nothing leaves your browser.</p>
</div>

<section class="cv-tool">
  <div class="cv-tabs">
    <button class="cv-tab-btn active" id="tabPaste" type="button">Paste Text</button>
    <button class="cv-tab-btn" id="tabUpload" type="button">Upload File</button>
  </div>

  <div class="cv-input-panel active" id="panelPaste">
    <textarea class="cv-textarea" id="cvPasteInput" placeholder="Paste your CV text here..."></textarea>
  </div>

  <div class="cv-input-panel" id="panelUpload">
    <div class="cv-upload-zone" id="cvUploadZone">
      <div class="explore-icon" style="margin:0 auto 1rem;">{ICON['upload']}</div>
      <div class="cv-upload-label">Click to browse, or drag a file here</div>
      <div class="cv-upload-sub">.txt, .pdf, or .docx</div>
      <div class="cv-filename" id="cvFilename"></div>
      <input type="file" id="cvFileInput" accept=".txt,.pdf,.docx">
    </div>
  </div>

  <span class="cv-jd-toggle" id="jdToggle">+ Add a job description (optional, for keyword matching)</span>
  <div id="jdWrap" style="display:none;">
    <textarea class="cv-textarea" id="jdInput" style="min-height:140px;" placeholder="Paste the job description here to check how well your CV matches its key terms..."></textarea>
  </div>

  <div style="text-align:center;">
    <button class="btn-analyze" id="analyzeBtn" type="button">Check My CV</button>
    <div class="cv-privacy-note">Your CV never leaves your browser. Nothing is uploaded or stored.</div>
  </div>

  <div class="cv-results" id="cvResults"></div>
</section>'''

# ============================================================== LEARNING HUB — AI articles
CV_CTA_BUTTONS = '''<a href="/learning-hub/cv-check/" class="btn-pink">Try the Free CV Check</a>
        <a href="/contact/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5); color:var(--pink);">Book a Call</a>'''


def article_page(title, dek, body_html,
                 section_label="Learning Hub · Understand &amp; Use AI",
                 back_href="/learning-hub/learn-ai/", back_label="← Back to Understand &amp; Use AI",
                 byline="By Lucy Mukhethwa · AI Projects Manager &amp; Career Strategist",
                 cta_heading="Want this applied to your own CV?",
                 cta_text="Try the free CV Check, or book a call and we'll work through it together.",
                 cta_buttons=CV_CTA_BUTTONS):
    return f'''<div class="page-header">
  <div class="section-label">{section_label}</div>
  <h1>{title}</h1>
  <p>{dek}</p>
  <p style="margin-top:0.9rem;"><a href="{back_href}" style="color:var(--pink); font-weight:700; font-style:normal;">{back_label}</a></p>
</div>

<section class="article">
  <div class="article-inner">
    <div class="article-byline">{byline}</div>
    <div class="article-body">
{body_html}
    </div>
    <div class="article-cta">
      <h3 style="font-family:'Baloo 2',sans-serif; color:var(--white); font-size:1.3rem; font-weight:800; margin-bottom:0.6rem;">{cta_heading}</h3>
      <p>{cta_text}</p>
      <div class="cta-btns" style="justify-content:center;">
        {cta_buttons}
      </div>
    </div>
  </div>
</section>'''


article_what_is_ai = article_page(
    "What Is AI, Really?",
    "A clear, honest answer to a question everyone's asking.",
    '''      <p>"Artificial intelligence" gets thrown around so often it's started to feel like a buzzword rather than a real, useful idea. So let's strip away the hype and answer the actual question: what is AI, really?</p>
      <p>At its core, AI is a broad term for computer systems that can perform tasks that would normally require human intelligence: recognising patterns, making predictions, generating text or images, or making decisions based on data. That's it. It's not magic, and it's not a mind. It's very sophisticated pattern-matching, running at a scale no human could do by hand.</p>
      <h2>Why Everyone's Talking About It Now</h2>
      <p>AI itself isn't new. It's been part of everyday life for years, quietly powering things like spam filters, spell check, and the recommendations you see on streaming apps. What changed recently is the arrival of <strong>large language models</strong>, the technology behind tools like ChatGPT and Claude. They can hold a conversation, write in a natural voice, and help with tasks that used to require a human writer or researcher sitting next to you.</p>
      <h2>What AI Is Not</h2>
      <p>It's worth being clear about the limits, too. AI doesn't "understand" the world the way you do. It doesn't have opinions, memories of you between conversations (unless a tool is specifically built to keep them), or genuine judgement about what's true. It's excellent at generating plausible, well-structured text, which means it can also generate plausible-sounding <em>wrong</em> answers with total confidence. Treat it as a very capable assistant, not an authority.</p>
      <h2>Why This Matters for Your Career</h2>
      <p>Whether or not you ever touch a line of code, AI is already changing how work gets done: how CVs get screened, how job ads get written, how colleagues draft emails and reports. Understanding the basics isn't optional anymore; it's becoming as fundamental as knowing your way around a spreadsheet. The good news: you don't need to be technical to use it well. You just need to understand what it's doing, and that's what the rest of this series covers.</p>''',
)

article_how_ai_works = article_page(
    "How Tools Like ChatGPT &amp; Claude Actually Work",
    "A plain-language look under the hood, so you know what you're really working with.",
    '''      <p>Tools like ChatGPT and Claude can feel like magic: you type a question, and a thoughtful, well-written answer appears in seconds. Here's what's happening behind the scenes.</p>
      <h2>They Predict, They Don't "Know"</h2>
      <p>These tools are built on <strong>large language models</strong>, systems trained on enormous amounts of text to learn the patterns of language: which words and ideas tend to follow which others. When you ask a question, the model isn't looking up a stored answer. It's generating a response one piece at a time, predicting what should come next based on everything it learned during training.</p>
      <p>That's a subtle but important distinction. It means these tools are exceptional at producing fluent, well-structured, plausible-sounding text. But "plausible-sounding" and "correct" aren't always the same thing.</p>
      <h2>What They're Good At</h2>
      <ul>
        <li>Drafting and rewriting: turning a rough idea into a structured first draft</li>
        <li>Summarising long documents or explaining a complex topic simply</li>
        <li>Brainstorming: generating options quickly when you're stuck</li>
        <li>Editing: tightening wordy sentences, checking tone and clarity</li>
      </ul>
      <h2>Where They Fall Short</h2>
      <p>These tools can sometimes state incorrect information with total confidence (often called "hallucinating"). They don't automatically know about very recent events unless the tool is specifically connected to the internet. And they don't know <em>you</em> (your actual achievements, your voice, your context) unless you give it to them clearly.</p>
      <h2>The Practical Takeaway</h2>
      <p>Use these tools as a fast, capable first-draft partner, never as the final word. Always read critically, fact-check anything that matters, and make sure the final result still sounds like you. That's the difference between using AI well and letting it use you.</p>''',
)

article_prompting_101 = article_page(
    "Prompting 101",
    "The difference between a mediocre AI answer and a useful one usually comes down to how you ask.",
    '''      <p>Most people's first experience with AI chat tools is underwhelming: a vague question gets a vague, generic answer. The good news: getting dramatically better results isn't about learning to "code" or master some secret technique. It's about being a clearer communicator. Here's how.</p>
      <h2>1. Be Specific</h2>
      <p>"Write me a CV bullet point" will get you something generic. "Rewrite this bullet point to lead with a measurable result, in one sentence, for a customer service role" will get you something usable. The more specific your request, the less generic the output.</p>
      <h2>2. Give Context</h2>
      <p>Tell the tool who you are, what you're trying to achieve, and who the output is for. For example: "I'm applying for a graduate role in banking. Rewrite this paragraph to sound confident but not arrogant, for a recruiter reading dozens of applications."</p>
      <h2>3. Iterate: Don't Expect Perfection First Try</h2>
      <p>Treat the first response as a draft, not a final answer. Follow up with "make it shorter," "make it sound more like me," or "give me three alternative versions." Refining in conversation almost always beats trying to write the perfect prompt upfront.</p>
      <h2>4. Break Big Tasks Into Steps</h2>
      <p>Instead of "help me with my job search," try smaller, specific asks: "help me identify the top 5 keywords in this job ad," then "check if my CV includes those keywords," then "suggest where I could naturally work in the ones that are missing."</p>
      <h2>5. Always Fact-Check</h2>
      <p>Never take a specific fact, statistic, or claim from an AI response at face value if it matters. Verify it yourself before you rely on it or repeat it to someone else.</p>
      <h2>Try It Yourself</h2>
      <p>Next time you're stuck on a CV bullet or a LinkedIn line, try this prompt: <em>"Rewrite this to lead with a specific, quantified result, in one sentence, for a [your target role] application: [paste your text]."</em> Notice how much more useful the result is than just asking it to "make this better."</p>''',
)

article_free_ai_tools = article_page(
    "Free AI Tools Worth Trying",
    "The free tools worth your time, organised by what you're trying to do.",
    '''      <p>There's a new AI tool announced practically every week, and most people don't need to track any of that. What you need is a small, reliable toolkit for the handful of things AI does well. Here's a starting point, organised by task.</p>
      <h2>For Writing &amp; Drafting</h2>
      <p><strong>ChatGPT</strong> (OpenAI) and <strong>Claude</strong> (Anthropic) are both excellent general-purpose assistants for drafting emails, CV bullets, cover letters, and LinkedIn copy. Both have free tiers that are more than enough for everyday career-related use. Try both and see which one's tone you prefer. They do write a little differently.</p>
      <h2>For Research (With Sources)</h2>
      <p><strong>Perplexity</strong> is built specifically for research. It answers questions and shows you the sources it pulled from, which makes it easier to verify what it's telling you. Useful when researching a company before an interview, or checking facts about an industry you're moving into.</p>
      <h2>For Organising Your Own Notes</h2>
      <p><strong>NotebookLM</strong> (Google) is designed to work with documents you upload (your own notes, a set of job ads, your CV drafts) and helps you summarise and query them. Handy for pulling your own scattered career notes into something organised.</p>
      <h2>If You're Already in Google Workspace</h2>
      <p><strong>Gemini</strong> is built directly into Gmail, Docs, and Sheets, which makes it convenient if you're already living in those tools day to day. No need to copy-paste between apps.</p>
      <h2>A Word of Caution</h2>
      <p>Free tiers change, and new tools launch constantly, so treat any specific list (including this one) as a starting point, not gospel. The skill that doesn't go out of date is knowing <em>what</em> to ask these tools to do, and that's what the rest of this series is for.</p>''',
)

article_ai_for_cv = article_page(
    "Using AI to Sharpen Your CV &amp; LinkedIn (Without Losing Your Voice)",
    "AI is a great editor and a terrible ghostwriter. Here's how to use it as the former.",
    '''      <p>This is the question I get asked most often: "Can I just use AI to write my CV?" The honest answer: you can, but you shouldn't, at least not entirely. Here's the approach I recommend to clients.</p>
      <h2>Use It to Tighten, Not to Invent</h2>
      <p>AI is excellent at taking something you've already written and making it clearer and more concise. It is not a reliable source of your own achievements, so never let it invent or exaggerate results you didn't deliver. Start with your real experience, in your own words, then use AI to sharpen the language.</p>
      <h2>A Prompt Worth Stealing</h2>
      <p>Paste in a CV bullet and ask: <em>"Rewrite this to start with a strong action verb and include a measurable result if one is implied. Don't invent numbers I haven't given you: [paste your bullet]."</em> This forces the tool to improve structure and clarity without fabricating impact.</p>
      <h2>Check Keyword Alignment</h2>
      <p>Paste in a job description alongside your CV and ask which important keywords from the ad are missing from your CV. This is one of the fastest ways to improve how your CV performs against applicant tracking systems (ATS), as long as you really have the skill or experience being asked about.</p>
      <h2>Use It for Structure, Not Your Final Voice</h2>
      <p>AI is useful for suggesting a first-draft structure: what sections to include, what order to put them in. But the final wording should sound like you, not like a template. If a recruiter or interviewer meets you after reading an AI-polished-beyond-recognition CV, the mismatch is obvious and it undermines trust.</p>
      <h2>The Line I Tell Every Client</h2>
      <p>AI should sound like your best editor, not your ghostwriter. If you wouldn't say a sentence out loud in an interview, don't let it stay on your CV, no matter how good it looks on the page.</p>
      <p>Want a second pair of eyes on the real thing? Run your CV through the free CV Check tool below, or book a call and we'll sharpen it together, line by line.</p>''',
)

# ============================================================== GET HIRED WITH AI (paid digital kit)
# Buying starts with a WhatsApp message to Lucy until a payment link exists.
GH_BUY_LINK = "https://wa.me/27832610754?text=" + urllib.parse.quote(
    "Hi Lucy, I'd like to buy the Get Hired with AI kit (R149 founding price).")
get_hired_body = '''<div class="page-header gh-hero">
  <div class="section-label">Paid digital kit</div>
  <h1>Get Hired <em>with AI</em></h1>
  <p>The South African job-seeker's kit. Use free AI tools to build a CV that gets read, apply smarter and walk into interviews prepared, in 7 days.</p>
  <div class="gh-price"><strong>R149</strong><s>R249</s><small>Founding price for the first 50 buyers</small></div>
  <div class="gh-btns">
    <a href="BUY_LINK" class="btn-pink" target="_blank" rel="noopener">Get the kit →</a>
    <a href="#inside" class="btn-secondary">See what's inside</a>
  </div>
  <div class="gh-previews">
    <img class="tilt-l" src="/assets/get-hired/prompts-cover.jpg" alt="Cover of the Get Hired with AI prompt pack" width="170" height="240">
    <img src="/assets/get-hired/guide-cover.jpg" alt="Cover of the Get Hired with AI guide" width="170" height="240">
    <img class="tilt-r" src="/assets/get-hired/cv-modern.jpg" alt="The Modern CV template" width="170" height="240">
  </div>
</div>

<!-- WHAT'S IN THE KIT -->
<section id="inside">
  <div class="gh-section gh-center">
    <div class="section-label reveal">What's in the kit</div>
    <div class="section-title reveal">Everything you need, <em>nothing you don't</em></div>
    <div class="divider reveal"></div>
    <div class="gh-grid">
      <div class="service-card reveal">
        <div class="service-title">The 7-day guide</div>
        <div class="service-desc">A 22-page PDF. One short chapter a day, each ending with a "Do this today" task.</div>
      </div>
      <div class="service-card reveal">
        <div class="service-title">45 AI prompts</div>
        <div class="service-desc">Copy, paste and fill in the blanks. Prompts for your CV, LinkedIn, cover letters, applications and interviews.</div>
      </div>
      <div class="service-card reveal">
        <div class="service-title">3 CV templates</div>
        <div class="service-desc">Classic, Modern and Career changer, in Word. Built so screening software can read them cleanly.</div>
      </div>
      <div class="service-card reveal">
        <div class="service-title">Opportunities sheet</div>
        <div class="service-desc">40 South African job boards, youth programmes, SETAs and graduate programme pages, with every link checked.</div>
      </div>
      <div class="service-card reveal">
        <div class="service-title">7-day checklist</div>
        <div class="service-desc">Tick off your week and know exactly what to do next week.</div>
      </div>
      <div class="service-card reveal">
        <div class="service-title">Works on your phone</div>
        <div class="service-desc">Use it with the free versions of ChatGPT, Claude, Gemini or Copilot. No paid tools needed.</div>
      </div>
    </div>

    <div class="gh-inside">
      <figure class="reveal"><img src="/assets/get-hired/guide-inside.jpg" alt="A page from Chapter 1 of the guide" loading="lazy"><figcaption>The guide: clear steps, real examples</figcaption></figure>
      <figure class="reveal"><img src="/assets/get-hired/prompts-inside.jpg" alt="A page of the prompt pack" loading="lazy"><figcaption>The prompts: just fill in the pink blanks</figcaption></figure>
      <figure class="reveal"><img src="/assets/get-hired/cv-modern.jpg" alt="The Modern CV template with a sample CV" loading="lazy"><figcaption>The templates: a filled-in example to follow</figcaption></figure>
    </div>
  </div>
</section>

<!-- WHO IT'S FOR -->
<section style="background: var(--off-white); padding-top: 3rem;">
  <div class="gh-section gh-center">
    <div class="section-label reveal">Who it's for</div>
    <div class="section-title reveal">Applying a lot and <em>hearing nothing back?</em></div>
    <div class="divider reveal"></div>
    <div class="gh-for reveal">
      <span>Graduates</span><span>Matriculants looking for learnerships</span><span>Young professionals</span><span>Career changers</span><span>Anyone getting back into work</span>
    </div>
  </div>
</section>

<!-- 7 DAYS -->
<section style="background: var(--white);">
  <div class="gh-section gh-center">
    <div class="section-label reveal">How it works</div>
    <div class="section-title reveal">About an hour a day, <em>for one week</em></div>
    <div class="divider reveal"></div>
    <ol class="gh-days">
      <li class="reveal"><div><strong>How hiring really works</strong><span>What happens after you click "Apply", and a list of 10 roles to aim for.</span></div></li>
      <li class="reveal"><div><strong>AI basics</strong><span>Write prompts that work, and keep your personal details safe.</span></div></li>
      <li class="reveal"><div><strong>Build your CV</strong><span>Turn duties into achievements, then tailor your CV to one job in 20 minutes.</span></div></li>
      <li class="reveal"><div><strong>LinkedIn and cover letters</strong><span>A profile recruiters find, and a cover letter you can adapt.</span></div></li>
      <li class="reveal"><div><strong>Apply smarter</strong><span>Where to look, how to spot scams, and 3 tailored applications sent.</span></div></li>
      <li class="reveal"><div><strong>Ace the interview</strong><span>STAR answers, psychometric tests and a full mock interview with AI.</span></div></li>
      <li class="reveal"><div><strong>Review</strong><span>Tick off your checklist and plan the weeks ahead.</span></div></li>
    </ol>
  </div>
</section>

<!-- ABOUT LUCY -->
<section style="background: var(--off-white);">
  <div class="gh-about reveal">
    <img src="/assets/get-hired/logo.png" alt="Flow Corner logo" width="160" height="160">
    <div>
      <div class="section-label" style="justify-content:flex-start;">Made by Lucy Mukhethwa</div>
      <p>I studied Industrial and Organisational Psychology and Human Resources, and I'm now studying a Masters in Industrial &amp; Organisational Psychology, with my research focused on career psychology. Attending Harambee got me ready for work, and that opportunity opened doors for me.</p>
      <p>I have 6+ years in HR and operations, and I once owned an internet café where I helped people write CVs and apply for jobs. This kit is everything I'd tell you if we sat down together.</p>
    </div>
  </div>
</section>

<!-- BUY -->
<section class="founding" style="background: var(--white);" id="buy">
  <div class="gh-buy">
    <div class="section-label reveal">Founding price</div>
    <div class="section-title reveal">Get the kit for <em>R149</em></div>
    <div class="divider reveal" style="margin-left:auto;margin-right:auto;"></div>
    <div class="founding-what reveal">
      <div class="founding-item"><span>✦ The 7-day guide (PDF)</span></div>
      <div class="founding-item"><span>✦ 45 AI prompts (PDF)</span></div>
      <div class="founding-item"><span>✦ 3 CV templates (Word)</span></div>
      <div class="founding-item"><span>✦ South African opportunities sheet</span></div>
      <div class="founding-item"><span><strong>Total</strong></span><span class="founding-price"><strong>R149</strong> <s>R249</s></span></div>
    </div>
    <ol class="gh-steps reveal">
      <li>Tap the button to message me on WhatsApp.</li>
      <li>I'll send you the payment details.</li>
      <li>Once your payment reflects, I'll send your kit by WhatsApp or email.</li>
    </ol>
    <a href="BUY_LINK" class="btn-pink reveal" target="_blank" rel="noopener">Get the kit →</a>
  </div>
</section>

<!-- FAQ -->
<section style="background: var(--off-white);">
  <div class="gh-section gh-center">
    <div class="section-label reveal">Questions</div>
    <div class="section-title reveal">Good to <em>know</em></div>
    <div class="divider reveal"></div>
    <div class="gh-faq">
      <details class="reveal"><summary>Do I need to pay for an AI tool?</summary><p>No. Everything works with the free versions of ChatGPT, Claude, Gemini or Microsoft Copilot.</p></details>
      <details class="reveal"><summary>Can I use it on my phone?</summary><p>Yes. The guide and prompts are PDFs, and the CV templates open in Word or Google Docs on your phone or computer.</p></details>
      <details class="reveal"><summary>Will AI make things up on my CV?</summary><p>Not if you follow the kit. Every prompt tells the AI never to invent experience, and the guide shows you how to check what it writes.</p></details>
      <details class="reveal"><summary>I don't have much experience. Will it help me?</summary><p>Yes. There's a prompt and a section for first CVs, plus learnerships, internships and graduate programmes for people who are starting out.</p></details>
      <details class="reveal"><summary>Can you do my CV for me instead?</summary><p>Yes, that's a separate paid service. A <a href="/services/" style="color:var(--pink-deep);font-weight:700;">CV Revamp</a> starts from R100 and a LinkedIn Revamp from R150.</p></details>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta">
  <div class="section-title" style="color:var(--white);">Your next job starts <em style="color:var(--pink);">this week</em></div>
  <p style="color:rgba(255,255,255,0.8); margin: 0.6rem 0 2rem;">7 days. About an hour a day. R149 for the first 50 buyers.</p>
  <div class="cta-btns"><a href="BUY_LINK" class="btn-pink" target="_blank" rel="noopener">Get the kit →</a></div>
</section>'''.replace("BUY_LINK", GH_BUY_LINK)

# ============================================================== PAGES
services_body = services_body.replace("@@ROCKET@@", ICON["rocket"])

# ============================================================== LEARNING HUB — Start a Business
BIZ_ARTICLE = dict(
    section_label="Learning Hub · Start a Business",
    back_href="/learning-hub/start-a-business/",
    back_label="← Back to Start a Business",
    byline="By Lucy Mukhethwa · Career Strategist · Last reviewed October 2026",
    cta_heading="Want help with your business idea?",
    cta_text="Business Start-Up Support: a free intro call, then a quote based on what you need.",
    cta_buttons=f'''<a href="{biz.WA_BIZ}" class="btn-pink" target="_blank" rel="noopener">Book a Free Intro Call</a>
        <a href="/learning-hub/start-a-business/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5); color:var(--pink);">More Start-Up Guides</a>''',
)

start_business_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Start a <em>Business</em></h1>
  <p>Step-by-step guides, funding options and official links for anyone in South Africa who wants to start a small business.</p>
</div>

<section class="explore">
  <p style="max-width:680px; margin:0 auto 1rem; text-align:center; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">Starting a business is exciting, and confusing. These free guides take you from idea to first customer, with the funding that exists for young people and entrepreneurs, and the official places where each step happens. Plain language, no fees.</p>
  <div class="hub-category-label">Start here</div>
  <p class="hub-category-intro">Read them in order, or jump to what you need.</p>
  <div class="resource-grid">
    {resource_card("How to Start a Small Business in South Africa", "The full step-by-step guide: your idea, the right structure, registration, tax, money, customers, and what to do differently for each type of business.", "rocket", "/learning-hub/start-a-business/how-to-start-a-small-business/", label="Read the guide →")}
    {resource_card("Funding for Youth & Entrepreneurs", "Grants, loans and free support: what each programme is for, who qualifies, how to get funding-ready, and how to avoid scams.", "star", "/learning-hub/start-a-business/funding-for-youth-and-entrepreneurs/", label="Read the funding guide →")}
    {resource_card("Useful Links", "Every official site you will need, in one place: registration, tax, free advice, funding, tenders and permits.", "compass", "/learning-hub/start-a-business/useful-links/", label="See the links →")}
    {resource_card("Not sure what business suits you?", "Start with the free career assessment: it helps you see your strengths and what to build on.", "message", "/learning-hub/free-assessment/", label="Take the free test →")}
  </div>
</section>

<section class="cta">
  <h2 class="reveal">Want someone in your corner<br>while you <em>build it?</em></h2>
  <p class="reveal">Business Start-Up Support: a free intro call, then a quote based on what you need. I'll help you plan, prepare, and find the right official support.</p>
  <div class="cta-btns reveal">
    <a href="{biz.WA_BIZ}" class="btn-pink" target="_blank" rel="noopener">Book a Free Intro Call</a>
    <a href="/services/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5); color:var(--pink);">See All Services</a>
  </div>
</section>'''

article_how_to_start = article_page(
    "How to Start a Small Business in South Africa",
    "The full step-by-step guide: from idea to first customer, for every kind of business.",
    biz.guide_body(), **BIZ_ARTICLE)

article_funding = article_page(
    "Funding for Youth & Entrepreneurs",
    "Grants, loans and free support: who qualifies, how to apply, and how to avoid scams.",
    biz.funding_body(), **BIZ_ARTICLE)

useful_links_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub · Start a Business</div>
  <h1>Useful <em>Links</em></h1>
  <p>The official sites you will need, in one place. Last reviewed October 2026.</p>
  <p style="margin-top:0.9rem;"><a href="/learning-hub/start-a-business/" style="color:var(--pink); font-weight:700; font-style:normal;">← Back to Start a Business</a></p>
</div>

<section class="explore">
  <p style="max-width:680px; margin:0 auto 1.5rem; text-align:center; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">These are the official pages behind our guides. Funding programmes, fees and deadlines change, so always read the current details on each site. Applying to government funders is free: never pay anyone to apply for you.</p>
{biz.links_sections(resource_card)}
  <p style="text-align:center; margin-top:3rem; font-size:0.88rem; color:var(--charcoal);">Missing a link, or found one that no longer works? <a href="/contact/" style="color:var(--pink-deep); font-weight:700;">Let me know</a>.</p>
</section>'''

not_found_body = '''<div class="page-header">
  <div class="section-label">404</div>
  <h1>Page not <em>found</em></h1>
  <p>That page has moved or doesn't exist. Let's get you back on track.</p>
</div>

<section class="cta" style="padding-top: 4rem;">
  <div class="cta-btns">
    <a href="/" class="btn-pink">Go to Home</a>
    <a href="/learning-hub/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5); color:var(--pink);">Visit the Learning Hub</a>
  </div>
</section>'''

# ============================================================== ABOUT + WORK (merged)
# The old /work/ page now lives inside /about/ (nav was too crowded). Reuse its
# experience + portfolio sections; drop its own page header and closing CTA.
_work_main = work_body.split('</div>\n\n', 1)[1].rsplit('<section class="cta"', 1)[0]
_work_main = _work_main.replace(
    '<section class="experience">\n  <div class="exp-grid" style="margin-top: 0;">',
    '<section class="experience" id="experience">\n  <div class="section-label reveal" style="justify-content:center; display:flex;">Professional Experience</div>\n  <div class="section-title reveal" style="text-align:center;">Where I\'ve <em>worked</em></div>\n  <div class="divider reveal" style="margin-left:auto; margin-right:auto;"></div>\n  <p class="reveal" style="text-align:center; color:var(--charcoal); font-size:0.95rem; margin:0 auto 2.5rem; max-width:560px;">6+ years across BPO, HR, and career development.</p>\n  <div class="exp-grid" style="margin-top: 0;">', 1)
assert 'id="experience"' in _work_main
_about_cta = '<section class="cta" style="padding: 5rem 5%;">'
assert about_body.count(_about_cta) == 1
about_full = about_body.replace(_about_cta, _work_main + _about_cta, 1)

# ============================================================== ADMIN (private, noindex)
admin_body = '''<div class="page-header">
  <div class="section-label">Private</div>
  <h1>Flow Corner <em>admin</em></h1>
  <p>Manage jobs and opportunities, and read employer enquiries.</p>
</div>
<section class="adm-section">
  <noscript><p>This page needs JavaScript.</p></noscript>
  <div id="adminApp" class="adm-app"><p class="adm-msg">Loading…</p></div>
</section>'''

PAGES = [
    ("index.html", "Flow Corner | Free AI Career Tools & Guidance",
     "Free career guides, an instant CV check and job resources for South Africans, plus paid CV, LinkedIn and career roadmap services from career strategist Lucy Mukhethwa.",
     None, home_body, '<script src="/assets/hero-3d.js" defer></script>\n'),
    ("about/index.html", "About Lucy | Flow Corner",
     "Meet Lucy Mukhethwa, a career strategist and AI Projects Manager studying a Masters in Industrial & Organisational Psychology, plus 6+ years of HR, BPO and career development experience.",
     "/about/", about_full, ""),
    ("how-it-works/index.html", "How It Works | Flow Corner",
     "Three simple steps to a career that finally fits: a free discovery call, a tailored strategy, and a stronger professional presence.",
     "/how-it-works/", how_body, ""),
    ("services/index.html", "Services & Pricing | Flow Corner",
     "Paid CV revamps from R100, LinkedIn rewrites from R150 and career roadmaps, plus digital products and a founding-client offer.",
     "/services/", services_body, ""),
    ("contact/index.html", "Contact | Flow Corner",
     "Book a free 15-minute discovery call or message Lucy Mukhethwa on WhatsApp.",
     "/contact/", contact_body, ""),
    ("learning-hub/index.html", "Learning Hub | Flow Corner",
     "Free AI guides, South African job resources, an instant CV check, and personal guidance in one place.",
     "/learning-hub/", hub_body, ""),
    ("learning-hub/learn-ai/index.html", "Understand & Use AI | Flow Corner Learning Hub",
     "AI explained simply: the basics, and how to practically use AI tools to work smarter and sharpen your CV or LinkedIn.",
     "/learning-hub/", learn_ai_body, ""),
    ("learning-hub/find-a-job/index.html", "Find a Job | Flow Corner Learning Hub",
     "Where to search for jobs in South Africa, how to stand out, and how to get personal guidance from Lucy.",
     "/learning-hub/", find_job_body, ""),
    ("learning-hub/free-assessment/index.html", "Free Career Assessment | Flow Corner Learning Hub",
     "Take a free personality or career assessment and book a free discovery call to unpack your results.",
     "/learning-hub/", free_assessment_body, ""),
    ("learning-hub/cv-check/index.html", "Free CV Check | Flow Corner Learning Hub",
     "Paste or upload your CV for an instant, free, automated checklist. No sign-up, and nothing leaves your browser.",
     "/learning-hub/", cv_check_body, '<script src="/assets/cv-check.js" defer></script>\n'),
    ("learning-hub/learn-ai/what-is-ai/index.html", "What Is AI, Really? | Flow Corner Learning Hub",
     "A plain-English explainer of what AI is, written by career strategist and AI Projects Manager Lucy Mukhethwa.",
     "/learning-hub/", article_what_is_ai, ""),
    ("learning-hub/learn-ai/how-ai-chat-tools-work/index.html", "How ChatGPT & Claude Actually Work | Flow Corner Learning Hub",
     "A plain-language look at how large language models generate answers, what they're good at, and where they fall short.",
     "/learning-hub/", article_how_ai_works, ""),
    ("learning-hub/learn-ai/prompting-101/index.html", "Prompting 101 | Flow Corner Learning Hub",
     "A practical guide to getting better results from AI chat tools like ChatGPT and Claude.",
     "/learning-hub/", article_prompting_101, ""),
    ("learning-hub/learn-ai/free-ai-tools/index.html", "Free AI Tools Worth Trying | Flow Corner Learning Hub",
     "The free AI tools worth your time, organised by what you're trying to do.",
     "/learning-hub/", article_free_ai_tools, ""),
    ("learning-hub/learn-ai/ai-for-cv-linkedin/index.html", "Using AI to Sharpen Your CV & LinkedIn | Flow Corner Learning Hub",
     "How to use AI as a drafting assistant for your CV and LinkedIn without losing your own voice.",
     "/learning-hub/", article_ai_for_cv, ""),
    ("learning-hub/start-a-business/index.html", "Start a Business | Flow Corner Learning Hub",
     "Free guides, funding options and official links for anyone in South Africa starting a small business.",
     "/learning-hub/", start_business_body, ""),
    ("learning-hub/start-a-business/how-to-start-a-small-business/index.html", "How to Start a Small Business in South Africa | Flow Corner",
     "A step-by-step guide to starting a small business in South Africa: idea, structure, CIPC and SARS registration, money, customers and permits.",
     "/learning-hub/", article_how_to_start, ""),
    ("learning-hub/start-a-business/funding-for-youth-and-entrepreneurs/index.html", "Funding for Youth & Entrepreneurs in South Africa | Flow Corner",
     "NYDA, sefa, NEF, GEP and more: what each funder offers, who qualifies, how to get funding-ready and how to avoid scams.",
     "/learning-hub/", article_funding, ""),
    ("learning-hub/start-a-business/useful-links/index.html", "Start a Business: Useful Links | Flow Corner",
     "Official South African links for registering a business, tax, free advice, funding, tenders and permits.",
     "/learning-hub/", useful_links_body, ""),
    ("learning-hub/job-readiness/index.html", "How Job-Ready Are You? Free Check | Flow Corner Learning Hub",
     "Answer ten questions to get a job-readiness score out of 100, your biggest gaps and a practical action plan. Free, no sign-up.",
     "/learning-hub/", FT["job_readiness"], '<script src="/assets/job-readiness.js" defer></script>\n'),
    ("free-tools/index.html", "Free Career Tools | Flow Corner",
     "Free tools for South African job-seekers: job-readiness check, CV check, CV builder, cover letter generator, interview practice and an opportunities board.",
     "/free-tools/", FT["free_tools"], ""),
    ("free-tools/cv-builder/index.html", "Free CV Builder | Flow Corner",
     "Build a clean, recruiter-friendly CV in minutes and save it as a PDF. Free, no sign-up, and your details stay in your browser.",
     "/free-tools/", FT["cv_builder"], '<script src="/assets/cv-builder.js" defer></script>\n'),
    ("free-tools/cover-letter/index.html", "Free Cover Letter Generator | Flow Corner",
     "Answer a few questions and get a professional cover letter draft to edit and send. Free, and nothing leaves your browser.",
     "/free-tools/", FT["cover_letter"], '<script src="/assets/cover-letter.js" defer></script>\n'),
    ("free-tools/interview-practice/index.html", "Free Interview Practice | Flow Corner",
     "Practise common interview questions with a two-minute timer and the STAR method. Free, with tips for every question.",
     "/free-tools/", FT["interview"], '<script src="/assets/interview-practice.js" defer></script>\n'),
    ("opportunities/index.html", "Jobs & Opportunities in South Africa | Flow Corner",
     "South African job platforms, learnerships and youth programmes with the official link for each, plus where to find fresh openings.",
     "/opportunities/", FT["opportunities"], '<script src="/assets/opportunities.js" defer></script>\n'),
    ("for-business/index.html", "For Business | Hire Through Flow Corner",
     "Hiring in South Africa? Share your role with Flow Corner's job-seeker audience, or get career development support for your team.",
     "/for-business/", EMP["landing"], ""),
    ("for-business/hire/index.html", "Tell Us About Your Role | Flow Corner For Business",
     "Send Flow Corner your open role: company, province, how many people and how soon. Lucy replies within 24 hours.",
     "/for-business/", EMP["hire"], ""),
    ("for-business/services/index.html", "Business Services | Flow Corner For Business",
     "Feature your role, get help finding the right people, or book career development for your team. Quoted on request.",
     "/for-business/", EMP["services"], ""),
    ("privacy/index.html", "Privacy Notice | Flow Corner",
     "How Flow Corner collects, uses and protects your personal information under POPIA.",
     None, EMP["privacy"], ""),
    ("get-hired/index.html", "Get Hired with AI | Flow Corner",
     "The South African job-seeker's kit: a 7-day guide, 45 AI prompts, 3 CV templates and an opportunities sheet. R149 founding price.",
     None, get_hired_body, ""),
]

# Pages whose share image isn't the default
OG_IMAGE_OVERRIDES = {"get-hired/index.html": SITE_URL + "/assets/get-hired/guide-cover.jpg"}

# Pages generated but not listed in the sitemap
EXTRA_PAGES = [
    ("admin/index.html", "Admin | Flow Corner", "Private admin for Flow Corner.",
     None, admin_body, '<script src="/assets/admin.js" defer></script>\n', "noindex, nofollow"),
    ("for-business/thanks/index.html", "Thank you | Flow Corner For Business", "Your enquiry has been received.",
     "/for-business/", EMP["thanks"], "", "noindex"),
    ("404.html", "Page not found | Flow Corner", "This page doesn't exist. Head back to the Flow Corner home page or Learning Hub.",
     None, not_found_body, "", "noindex"),
]

def write(path, content):
    full_path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print("wrote", path)


if __name__ == "__main__":
    for path, title, desc, active, body, extra_scripts in PAGES:
        write(path, page(title, desc, active, body, extra_scripts=extra_scripts, path=path,
                         og_image=OG_IMAGE_OVERRIDES.get(path)))

    for path, title, desc, active, body, extra_scripts, robots in EXTRA_PAGES:
        write(path, page(title, desc, active, body, extra_scripts=extra_scripts, robots=robots))

    # sitemap.xml + robots.txt are generated from PAGES so they never drift
    from site_template import canonical_url
    urls = "\n".join(f"  <url><loc>{canonical_url(p[0])}</loc></url>" for p in PAGES)
    write("sitemap.xml", f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
''')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
