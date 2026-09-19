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
import sys

sys.path.insert(0, os.path.dirname(__file__))
from site_template import page  # noqa: E402

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
    "upload": '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14.9A5 5 0 0 1 6 5.3 6.5 6.5 0 0 1 19 8a4.5 4.5 0 0 1-1 8.9"/><path d="M12 12v9"/><path d="m8 16 4-4 4 4"/></svg>',
}

WHATSAPP_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:-3px; margin-right:0.3em;"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.8 14.06c-.24.68-1.4 1.3-1.93 1.38-.5.08-1.11.11-1.79-.11-.41-.13-.95-.31-1.63-.6-2.87-1.24-4.74-4.12-4.88-4.31-.14-.19-1.17-1.56-1.17-2.98 0-1.42.74-2.12 1-2.41.26-.29.57-.36.76-.36.19 0 .38 0 .55.01.18.01.41-.07.64.49.24.58.81 2 .88 2.14.07.14.12.31.02.5-.09.19-.14.31-.28.48-.14.17-.29.37-.42.5-.14.14-.28.29-.12.57.16.28.71 1.17 1.52 1.89 1.05.93 1.93 1.22 2.21 1.36.28.14.44.12.6-.07.16-.19.68-.79.87-1.06.19-.27.37-.22.63-.13.26.09 1.63.77 1.91.91.28.14.47.21.54.33.07.12.07.68-.17 1.36z"/></svg>'

# ============================================================== HOME
home_body = f'''<!-- HERO -->
<section class="hero">
  <div class="hero-blob-yellow"></div>
  <div class="hero-text">
    <div class="hero-tag">Free AI Learning Hub · CV Check · Career Guidance</div>
    <h1>Find Your <em>Flow.</em></h1>
    <p>You've sent the applications. You have the skills. But your CV isn't getting through, and your LinkedIn isn't showing up when it counts. <em style="color:var(--pink); font-style:normal;">That changes today.</em></p>
    <p>This is a free space built to help you find direction — AI explained simply, real job-search resources, an instant CV check, and guidance from a real person when you're ready for it.</p>
    <div class="hero-btns">
      <a href="/learning-hub/cv-check/" class="btn-primary">Try the Free CV Check</a>
      <a href="/learning-hub/" class="btn-secondary">Explore Learning Hub</a>
    </div>
  </div>
  <div class="hero-visual">
    <div class="hero-card">
      <div class="label">What We Do</div>
      <div class="value" style="font-size:1.25rem;">Find Your Flow</div>
      <div class="sub">Career Clarity · Purpose · Direction</div>
    </div>
    <div class="stats-row">
      <div class="hero-card">
        <div class="label">Free Tools</div>
        <div class="value" style="font-size:1.1rem;">CV Check + Tests</div>
        <div class="sub">Instant, No Sign-Up</div>
      </div>
      <div class="hero-card">
        <div class="label">Learning Hub</div>
        <div class="value" style="font-size:1.1rem;">AI · Jobs · Careers</div>
        <div class="sub">Curated & Growing</div>
      </div>
    </div>
  </div>
</section>

<!-- FLOW BRAND BAR -->
<div class="flow-bar">
  <p>Flow is that feeling when work stops feeling like work — when your purpose, your skills, and your career finally line up. <strong>We built this space to help you get there:</strong> free AI-powered tools, curated resources, and real guidance when you need it.</p>
</div>

<!-- EXPLORE -->
<section class="explore">
  <div class="section-label reveal">Find Your Way Around</div>
  <div class="section-title reveal">Explore <em>Flow Corner</em></div>
  <div class="divider reveal"></div>
  <div class="explore-grid">
    <a href="/learning-hub/" class="explore-card reveal">
      <div class="explore-icon">{ICON['book']}</div>
      <div class="explore-title">Learning Hub</div>
      <div class="explore-desc">Free AI tools, curated resources, and a CV check — the best place to start.</div>
      <span class="explore-arrow">Start here →</span>
    </a>
    <a href="/services/" class="explore-card reveal">
      <div class="explore-icon">{ICON['briefcase']}</div>
      <div class="explore-title">Services & Pricing</div>
      <div class="explore-desc">CV, LinkedIn & career roadmaps — plus a limited founding-client offer.</div>
      <span class="explore-arrow">See services →</span>
    </a>
    <a href="/about/" class="explore-card reveal">
      <div class="explore-icon">{ICON['person']}</div>
      <div class="explore-title">About Lucy</div>
      <div class="explore-desc">My story, credentials, and the principles behind how I coach.</div>
      <span class="explore-arrow">Meet Lucy →</span>
    </a>
    <a href="/work/" class="explore-card reveal">
      <div class="explore-icon">{ICON['folder']}</div>
      <div class="explore-title">Experience & Work</div>
      <div class="explore-desc">6+ years across BPO, HR, and career development — the highlights.</div>
      <span class="explore-arrow">See the work →</span>
    </a>
  </div>
</section>

<!-- CTA -->
<section class="cta">
  <h2 class="reveal">Your career should feel<br>like <em>flow.</em></h2>
  <p class="reveal">Stop being overlooked. Your skills are real — let's make sure the world can see them. Book your free 15-minute discovery call today.</p>
  <div class="cta-btns reveal">
    <a href="mailto:hello@lucymukhethwa.co.za" class="btn-pink">Book My Free Call</a>
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%20would%20like%20to%20enquire%20about%20your%20services" class="btn-whatsapp" target="_blank" rel="noopener">{WHATSAPP_SVG}Chat on WhatsApp</a>
  </div>
</section>'''

# ============================================================== ABOUT
about_body = f'''<div class="page-header">
  <div class="section-label">About Me</div>
  <h1>Purpose-driven. <em>People-first.</em></h1>
  <div class="hero-tag" style="margin:0.5rem auto 1.6rem;">Career Strategist · CV & LinkedIn Specialist · I&O Psychology</div>
  <div class="stats-row" style="max-width:420px; margin:0 auto 1.8rem;">
    <div class="hero-card">
      <div class="label">Experience</div>
      <div class="value">6+ yrs</div>
      <div class="sub">HR & Operations</div>
    </div>
    <div class="hero-card">
      <div class="label">Credentials</div>
      <div class="value" style="font-size:1.1rem;">Masters</div>
      <div class="sub">I&O Psychology</div>
    </div>
  </div>
  <p>"Passion. Purpose. Peace — three words that define how I show up every single day." <span style="opacity:0.6;">— Philippians 4:4</span></p>
</div>

<section class="about">
  <div class="about-grid">
    <div>
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
      <p>I'm Lucy Mukhethwa — a South African career strategist based near Johannesburg. I currently support C-suite operations at a global BPO organisation, working directly with the COO across multi-country strategic initiatives.</p>
      <p>My background spans HR and administration — progressing from HR Assistant through to Generalist and into my current operational leadership-support role. Along the way, I've developed strong working knowledge of AI tools and automation technologies that are reshaping how modern workplaces operate.</p>
      <p>I'm also a student of Industrial &amp; Organisational Psychology, and a Christian living author completing final review ahead of publication. My mission is simple: to help people operate with more clarity, more confidence, and more impact in their careers.</p>
    </div>
  </div>
</section>

<!-- WHY LUCY -->
<section class="whylucy">
  <div class="section-label reveal">Why Choose Lucy</div>
  <div class="section-title reveal">What makes this <em>different</em></div>
  <div class="divider reveal"></div>
  <div class="why-grid">
    <div class="why-card reveal">
      <div class="why-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5"/><path d="M22 10v6"/></svg></div>
      <h3>Academic Rigour</h3>
      <p>Currently completing a Masters in Industrial &amp; Organisational Psychology — specialising in career psychology. My coaching is grounded in validated theory, not guesswork.</p>
    </div>
    <div class="why-card reveal">
      <div class="why-icon">{ICON['briefcase']}</div>
      <h3>C-Suite Insider Knowledge</h3>
      <p>6+ years supporting executive leadership at a global BPO. I know exactly what decision-makers look for — and I build that into every CV, LinkedIn profile, and career plan I create.</p>
    </div>
    <div class="why-card reveal">
      <div class="why-icon">{ICON['compass']}</div>
      <h3>Purpose-Led, Not Just Career-Led</h3>
      <p>I believe your career is part of a bigger story. My approach connects your professional goals to your purpose — so the work we do together has meaning beyond the job title.</p>
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
  <h1>Three steps to your <em>next chapter</em></h1>
  <p>A simple, guided path from "overlooked" to "in demand."</p>
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
      <div class="step-desc">CV, LinkedIn, career roadmap — or all three. I craft a tailored approach that positions you powerfully for the opportunities you actually want.</div>
    </div>
    <div class="step-card reveal">
      <div class="step-number">03</div>
      <div class="step-title">You Show Up Differently</div>
      <div class="step-desc">Armed with a compelling story, a professional presence, and a clear direction — you stop being overlooked and start attracting the right doors.</div>
    </div>
  </div>
  <div style="text-align:center; margin-top:2.5rem; display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
    <a href="/contact/" class="btn-primary" style="display:inline-block;">Book My Free Call</a>
    <a href="/learning-hub/free-assessment/" class="btn-secondary" style="display:inline-block;">Take Free Assessment First →</a>
  </div>
  <p style="text-align:center; margin-top:1.3rem; font-size:0.85rem; color:var(--charcoal);">Not ready to book? <a href="/learning-hub/cv-check/" style="color:var(--pink-deep); font-weight:700;">Try the free CV Check</a> first.</p>
</section>'''

# ============================================================== SERVICES
services_body = '''<div class="page-header">
  <div class="section-label">Services</div>
  <h1>How I can <em>help you</em></h1>
  <p>Straightforward, ATS-aware career support — priced for the professionals it's built for.</p>
</div>

<section class="services">
  <div class="services-grid">
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></div>
      <div class="service-title">LinkedIn Profile Revamp</div>
      <div class="service-desc">I rewrite your headline, summary, and experience using strategic keywords that attract recruiters and the right opportunities.</div>
      <div class="service-price">Starting from R350</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/><path d="M9 13h6"/><path d="M9 17h6"/></svg></div>
      <div class="service-title">CV Revamp</div>
      <div class="service-desc">A professionally restructured, ATS-friendly CV that positions you for the roles you actually want — tailored to your industry and career level.</div>
      <div class="service-price">Starting from R300</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg></div>
      <div class="service-title">Career Development Roadmap</div>
      <div class="service-desc">A personalised career roadmap including skills gap analysis, goal setting, and a clear action plan to get you where you want to be.</div>
      <div class="service-price">Starting from R500</div>
    </div>
  </div>
  <p style="text-align:center; margin-top:2rem; font-size:0.88rem; color:var(--charcoal);">Not ready to book? <a href="/learning-hub/cv-check/" style="color:var(--pink-deep); font-weight:700;">Try our free CV Check</a> first — it's instant and it's free.</p>
</section>

<!-- ALSO AVAILABLE -->
<section class="extra-services">
  <div class="extra-services-inner">
    <div class="extra-services-label">Also Available</div>
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
  <div class="section-title reveal">Be part of the <em>beginning</em></div>
  <div class="divider reveal"></div>
  <div class="founding-content">
    <p class="reveal">I'm currently taking on <strong>3 founding clients</strong> at a significantly reduced rate — in exchange for an honest, detailed testimonial once we've worked together.</p>
    <p class="reveal">You get professional career support at a fraction of the normal price, and I get a genuine testimonial to build on.</p>
    <div class="founding-what reveal" style="background: var(--white);">
      <div class="founding-item"><span>✦ CV Revamp</span><span class="founding-price"><strong>R150</strong> <s>R300</s></span></div>
      <div class="founding-item"><span>✦ LinkedIn Revamp</span><span class="founding-price"><strong>R175</strong> <s>R350</s></span></div>
      <div class="founding-item"><span>✦ Career Roadmap</span><span class="founding-price"><strong>R250</strong> <s>R500</s></span></div>
      <p style="font-size:0.82rem; color:rgba(15,32,68,0.5); margin-top:0.9rem; text-align:left;">Each service includes one full delivery + one revision round. Once complete, I'll follow up with a short testimonial request.</p>
    </div>
    <p class="founding-note reveal">Only 3 spots available. First come, first served.</p>
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%27d%20like%20to%20apply%20as%20a%20founding%20client" class="btn-pink reveal" target="_blank" rel="noopener">Apply as a Founding Client →</a>
  </div>
</section>'''

# ============================================================== WORK
work_body = f'''<div class="page-header">
  <div class="section-label">Professional Experience</div>
  <h1>Where I've <em>made an impact</em></h1>
  <p>6+ years across BPO, HR, and career development.</p>
</div>

<section class="experience">
  <div class="exp-grid" style="margin-top: 0;">
    <div class="exp-card reveal">
      <div class="exp-role">Administrative Coordinator</div>
      <div class="exp-area">Dash BPO · Johannesburg, South Africa</div>
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
      <div class="exp-desc">Progressive HR career spanning employee relations, policy development, onboarding design, workforce engagement, and compliance — building a strong foundation in people operations across multiple industries.</div>
      <div class="exp-tags">
        <span class="exp-tag">HR Operations</span>
        <span class="exp-tag">Policy Development</span>
        <span class="exp-tag">Employee Relations</span>
        <span class="exp-tag">Compliance</span>
      </div>
    </div>
    <div class="exp-card reveal">
      <div class="exp-role">AI & Automation Practitioner</div>
      <div class="exp-area">AI Tools User & Practitioner</div>
      <div class="exp-desc">Working knowledge of AI tools including ChatGPT, Claude, Perplexity, NotebookLM, and Gemini. Experienced in environments where voice bots, chatbots, and automation strategies are deployed — with hands-on use of these tools to enhance operational and administrative efficiency.</div>
      <div class="exp-tags">
        <span class="exp-tag">ChatGPT</span>
        <span class="exp-tag">Claude</span>
        <span class="exp-tag">Perplexity</span>
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
  <p class="reveal" style="text-align:center; color:rgba(255,255,255,0.6); font-size:0.9rem; max-width:580px; margin:0 auto 2.5rem; line-height:1.8;">Drawn from 6+ years across BPO, HR, and career development — highlights of what I've contributed and built.</p>
  <div class="portfolio-grid">
    <div class="port-card reveal">
      <div class="port-icon">{ICON['filecheck']}</div>
      <div class="port-title">Cross-Border Legal Documentation</div>
      <div class="port-desc">Adapted employment frameworks across different legal jurisdictions, ensuring full compliance with local labour laws and regulatory requirements.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15 15 0 0 1 0 20a15 15 0 0 1 0-20"/></svg></div>
      <div class="port-title">Global Expansion Support</div>
      <div class="port-desc">Supported multi-country office and operational expansion — from research and cost analysis through to stakeholder coordination and documentation.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg></div>
      <div class="port-title">AI-First Workflow Projects</div>
      <div class="port-desc">Contributed to AI adoption initiatives including voice bot deployment, chatbot integration, and agent augmentation projects within contact centre environments.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg></div>
      <div class="port-title">Brand & Digital Asset Development</div>
      <div class="port-desc">Designed professional brand books, presentations, and digital collateral — maintaining visual consistency and quality across organisational deliverables.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg></div>
      <div class="port-title">Executive Presentations & Reporting</div>
      <div class="port-desc">Produced board-level presentations and strategic reports, synthesising complex information into clear, decision-ready formats for senior leadership.</div>
    </div>
    <div class="port-card reveal">
      <div class="port-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div>
      <div class="port-title">Book — Coming Soon</div>
      <div class="port-desc">Authored a Christian living book end-to-end — from manuscript to cover design and editorial review. Currently under final review ahead of publication. Title: Passion. Purpose. Peace. — Becoming Whole in Christ.</div>
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
  <p>Stop being overlooked. Your skills are real — let's make sure the world can see them.</p>
</div>

<section class="cta" style="padding-top: 5rem;">
  <h2 class="reveal">Book your free 15-minute<br>discovery call <em>today.</em></h2>
  <p class="reveal">Prefer WhatsApp? Message me directly and I'll respond within 24 hours.</p>
  <div class="cta-btns reveal">
    <a href="mailto:hello@lucymukhethwa.co.za" class="btn-pink">Book My Free Call</a>
    <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%20would%20like%20to%20enquire%20about%20your%20services" class="btn-whatsapp" target="_blank" rel="noopener">''' + WHATSAPP_SVG + '''Chat on WhatsApp</a>
  </div>
</section>

<section class="about" style="text-align:center;">
  <div class="section-label reveal" style="justify-content:center; display:flex;">Not Ready to Talk Yet?</div>
  <div class="section-title reveal">Start with a <em>free assessment</em></div>
  <div class="divider reveal" style="margin-left:auto; margin-right:auto;"></div>
  <p class="reveal" style="max-width:560px; margin:0 auto 2rem; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">Take a free career test first, share your result, and I'll reach out to book your call.</p>
  <a href="/learning-hub/free-assessment/" class="btn-primary reveal" style="display:inline-block;">Take Free Assessment</a>
</section>'''

# ============================================================== LEARNING HUB — landing
hub_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Your Free <em>Career Toolkit</em></h1>
  <p>AI explained simply, real job-search resources, and tools to help you move forward — free, no sign-up required.</p>
</div>

<section class="explore">
  <p style="max-width:680px; margin:0 auto 1rem; text-align:center; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">AI is changing how people find work — from writing a standout CV to discovering roles you didn't know existed. This hub exists to make that useful for you, for free.</p>
  <div class="hub-grid">
    <a href="/learning-hub/learn-ai/" class="hub-card reveal">
      <div class="explore-icon">{ICON['bulb']}</div>
      <div class="hub-card-title">Understand & Use AI</div>
      <div class="hub-card-desc">What AI actually is, and how to use it to write better, work smarter, and stand out — no jargon.</div>
      <span class="hub-card-arrow">Start learning →</span>
    </a>
    <a href="/learning-hub/find-a-job/" class="hub-card reveal">
      <div class="explore-icon">{ICON['search']}</div>
      <div class="hub-card-title">Find a Job</div>
      <div class="hub-card-desc">Where South African job-seekers actually find roles, plus how to stand out once you do.</div>
      <span class="hub-card-arrow">Start searching →</span>
    </a>
    <a href="/learning-hub/cv-check/" class="hub-card reveal">
      <div class="explore-icon">{ICON['filecheck']}</div>
      <div class="hub-card-title">Check Your CV Instantly</div>
      <div class="hub-card-desc">Paste or upload your CV and get instant, free pointers — nothing leaves your browser.</div>
      <span class="hub-card-arrow">Check my CV →</span>
    </a>
    <a href="/learning-hub/free-assessment/" class="hub-card reveal">
      <div class="explore-icon">{ICON['message']}</div>
      <div class="hub-card-title">Get Personalised Guidance</div>
      <div class="hub-card-desc">Take a free career assessment and I'll personally follow up with guidance for your situation.</div>
      <span class="hub-card-arrow">Take the test →</span>
    </a>
  </div>
  <p style="text-align:center; margin-top:3rem; font-size:0.88rem; color:var(--charcoal);">Want to talk to a real person instead? <a href="/contact/" style="color:var(--pink-deep); font-weight:700;">Get in touch</a>.</p>
</section>'''

# ============================================================== LEARNING HUB — learn-ai
def resource_card(title, desc, icon_key="bulb", href="#", placeholder=True):
    note = '<div class="resource-placeholder-note">Link to be added — verified before launch</div>' if placeholder else ''
    return f'''<a href="{href}" class="resource-card reveal"{' target="_blank" rel="noopener"' if not placeholder else ''}>
      <div class="resource-icon">{ICON[icon_key]}</div>
      <div>
        <div class="resource-title">{title}</div>
        <div class="resource-desc">{desc}</div>
        <div class="resource-link">{'Read more →' if not placeholder else 'Coming soon'}</div>
        {note}
      </div>
    </a>'''


learn_ai_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Understand & Use <em>AI</em></h1>
  <p>No jargon — just what AI actually is, and how to put it to work for your career.</p>
</div>

<section class="explore">
  <div class="hub-category-label">AI Basics</div>
  <p class="hub-category-intro">New to AI? Start here — these break down what AI actually is, without the hype.</p>
  <div class="resource-grid">
    {resource_card("What Is AI, Really?", "A beginner-friendly explainer of what AI actually is — no jargon, no hype.", "bulb")}
    {resource_card("How Tools Like ChatGPT & Claude Work", "A plain-language look at how modern AI chat tools actually work under the hood.", "zap")}
  </div>

  <div class="hub-category-label">Using AI Practically</div>
  <p class="hub-category-intro">Ready to put it to work? These focus on real, everyday use.</p>
  <div class="resource-grid">
    {resource_card("Prompting 101", "A beginner's guide to getting better, more useful results from AI chat tools.", "message")}
    {resource_card("Free AI Tools Worth Trying", "A roundup of genuinely useful, free AI tools for everyday work and study.", "star")}
    {resource_card("Using AI to Sharpen Your CV & LinkedIn", "How to use AI as a drafting assistant — not a replacement for your own voice.", "filecheck")}
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
    {resource_card("LinkedIn Jobs", "One of the most active platforms for professional roles in South Africa.", "search")}
    {resource_card("Indeed South Africa", "A large general job board covering roles across every industry.", "search")}
    {resource_card("PNet", "A long-standing, popular South African job board.", "search")}
  </div>

  <div class="hub-category-label">How to Stand Out</div>
  <p class="hub-category-intro">Getting found is only step one — here's how to make an impression once you are.</p>
  <div class="resource-grid">
    <a href="/services/" class="resource-card reveal">
      <div class="resource-icon">{ICON['briefcase']}</div>
      <div>
        <div class="resource-title">LinkedIn Profile Revamp</div>
        <div class="resource-desc">Let's rewrite your headline and summary so recruiters actually notice you.</div>
        <div class="resource-link">See the service →</div>
      </div>
    </a>
    {resource_card("Interview Prep Basics", "A solid, free starting point for common interview questions and how to answer them.", "star")}
  </div>

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
  <p class="assess-intro reveal">Once you have your result, fill in the form below — I'll reach out via WhatsApp or email within 24 hours to book your free 15-minute discovery call — and we'll unpack exactly what your result means for your career path.</p>
  <div class="assess-grid">
    <div class="assess-card reveal">
      <div class="assess-emoji"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="12" r="6"/><circle cx="15" cy="12" r="6"/></svg></div>
      <div class="assess-name">16Personalities</div>
      <div class="assess-what">Personality Type</div>
      <div class="assess-desc">One of the most widely used personality frameworks in the world. Discover how you think, work, and connect — and what careers align with your type.</div>
      <div class="assess-time">⏱ 10–12 minutes · Free</div>
      <a href="https://www.16personalities.com/" target="_blank" rel="noopener" class="btn-assess">Take Free Test →</a>
    </div>
    <div class="assess-card reveal">
      <div class="assess-emoji"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg></div>
      <div class="assess-name">DISC Assessment</div>
      <div class="assess-what">Work Style</div>
      <div class="assess-desc">Understand your dominant workplace behaviour style — Dominance, Influence, Steadiness, or Conscientiousness — and how it shapes your career fit.</div>
      <div class="assess-time">⏱ 10 minutes · Free</div>
      <a href="https://www.123test.com/disc-personality-test/" target="_blank" rel="noopener" class="btn-assess">Take Free Test →</a>
    </div>
    <div class="assess-card reveal">
      <div class="assess-emoji"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg></div>
      <div class="assess-name">Holland Code</div>
      <div class="assess-what">Career Interests</div>
      <div class="assess-desc">Based on John Holland's RIASEC theory — the foundation of career psychology. Matches your interests to real career paths and fields where you're most likely to thrive.</div>
      <div class="assess-time">⏱ 10–15 minutes · Free</div>
      <a href="https://www.mynextmove.org/explore/ip" target="_blank" rel="noopener" class="btn-assess">Take Free Test →</a>
    </div>
  </div>
  <div class="assess-form-wrap reveal">
    <h3>Share your result — get your free call</h3>
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
      <p class="form-note">By submitting, you agree to be contacted via WhatsApp or email within 24 hours. No spam — ever.</p>
    </form>
  </div>
</section>'''

# ============================================================== LEARNING HUB — cv-check
cv_check_body = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>Check Your <em>CV</em>, Instantly</h1>
  <p>Paste your CV or upload a file — get free, instant pointers. Nothing leaves your browser.</p>
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
    <div class="cv-privacy-note">Your CV never leaves your browser — nothing is uploaded or stored.</div>
  </div>

  <div class="cv-results" id="cvResults"></div>
</section>'''

# ============================================================== PAGES
PAGES = [
    ("index.html", "Flow Corner — Free AI Career Tools & Guidance",
     "A free platform helping South Africans find career direction with AI-powered tools, a Learning Hub, and real guidance from career strategist Lucy Mukhethwa.",
     None, home_body, ""),
    ("about/index.html", "About Lucy — Flow Corner",
     "Meet Lucy Mukhethwa, a career strategist and HR professional pursuing a Masters in Industrial & Organisational Psychology.",
     "/about/", about_body, ""),
    ("how-it-works/index.html", "How It Works — Flow Corner",
     "Three simple steps to a career that finally fits: a free discovery call, a tailored strategy, and a stronger professional presence.",
     "/how-it-works/", how_body, ""),
    ("services/index.html", "Services & Pricing — Flow Corner",
     "CV revamps, LinkedIn profile rewrites, and career roadmaps — plus a limited founding-client offer.",
     "/services/", services_body, ""),
    ("work/index.html", "Experience & Work — Flow Corner",
     "6+ years of HR, BPO, and career development experience — professional highlights from Lucy Mukhethwa.",
     "/work/", work_body, ""),
    ("contact/index.html", "Contact — Flow Corner",
     "Book a free 15-minute discovery call or message Lucy Mukhethwa on WhatsApp.",
     "/contact/", contact_body, ""),
    ("learning-hub/index.html", "Learning Hub — Flow Corner",
     "Free AI tools, curated career resources, an instant CV check, and personalised guidance — all in one place.",
     "/learning-hub/", hub_body, ""),
    ("learning-hub/learn-ai/index.html", "Understand & Use AI — Flow Corner Learning Hub",
     "AI explained simply: the basics, and how to practically use AI tools to work smarter and sharpen your CV or LinkedIn.",
     "/learning-hub/", learn_ai_body, ""),
    ("learning-hub/find-a-job/index.html", "Find a Job — Flow Corner Learning Hub",
     "Where to search for jobs in South Africa, how to stand out, and how to get personal guidance from Lucy.",
     "/learning-hub/", find_job_body, ""),
    ("learning-hub/free-assessment/index.html", "Free Career Assessment — Flow Corner Learning Hub",
     "Take a free personality or career assessment and book a free discovery call to unpack your results.",
     "/learning-hub/", free_assessment_body, ""),
    ("learning-hub/cv-check/index.html", "Free CV Check — Flow Corner Learning Hub",
     "Paste or upload your CV for an instant, free, automated checklist — no sign-up, nothing leaves your browser.",
     "/learning-hub/", cv_check_body, '<script src="/assets/cv-check.js" defer></script>\n'),
]

if __name__ == "__main__":
    for path, title, desc, active, body, extra_scripts in PAGES:
        full_path = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(page(title, desc, active, body, extra_scripts=extra_scripts))
        print("wrote", path)
