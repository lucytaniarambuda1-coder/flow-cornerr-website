#!/usr/bin/env python3
"""
Page bodies for the "For Business" area (/for-business/) and the privacy page.

This is separate from business_pages.py, which is the Start-a-Business guide
for job-seekers. Everything here is aimed at companies and people who hire.

build(WHATSAPP_SVG) returns {name: html_body}; generate.py registers the pages.
Prices are deliberately "quoted on request" until Lucy sets them.
"""

WA = "https://wa.me/27832610754"


def _wa(text):
    import urllib.parse
    return f"{WA}?text={urllib.parse.quote(text)}"


def build(WHATSAPP_SVG):
    pages = {}

    # ------------------------------------------------------------ LANDING
    pages["landing"] = f'''<div class="page-header">
  <div class="section-label">For Business</div>
  <h1>Hire people who are <em>ready to work</em></h1>
  <p>Flow Corner helps South African job-seekers get CV-ready. If you are hiring, tell me about your roles and I'll help you reach them.</p>
  <div class="hero-btns" style="justify-content:center; margin-top:1.8rem; position:relative;">
    <a href="/for-business/hire/" class="btn-pink">Tell me about your role</a>
    <a href="/for-business/services/" class="btn-secondary" style="border-color:rgba(255,111,165,0.5); color:var(--pink);">See how we can work together</a>
  </div>
</div>

<section class="services">
  <div class="section-label reveal">How it works for employers</div>
  <div class="section-title reveal">Three simple <em>steps</em></div>
  <div class="services-grid">
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg></div>
      <div class="service-title">1. Tell me what you need</div>
      <div class="service-desc">Send the role, the province and how soon you need someone. It takes about two minutes.</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>
      <div class="service-title">2. I review and agree a plan</div>
      <div class="service-desc">I get back to you within 24 hours to agree how the role is shared and what, if anything, it costs.</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>
      <div class="service-title">3. Your role gets seen</div>
      <div class="service-desc">Approved roles are shared with job-seekers who use Flow Corner's free tools and guides.</div>
    </div>
  </div>
</section>

<section class="about" style="background:var(--off-white);">
  <div class="section-label reveal">Why Flow Corner</div>
  <div class="section-title reveal">Built around <em>job-seekers</em>, so you meet them where they are</div>
  <div class="divider reveal"></div>
  <p class="reveal" style="max-width:680px; color:var(--charcoal); font-size:0.95rem; line-height:1.85;">Flow Corner started as free career help for South Africans: CV checks, a CV builder, interview practice and an opportunities board. The people here are actively working on getting hired. If you have a role to fill, or a team that could use career development, this is a place to reach them.</p>
  <p class="reveal" style="max-width:680px; color:var(--charcoal); font-size:0.95rem; line-height:1.85; margin-top:1rem;">Flow Corner is new, and I'd rather be straight with you than oversell it. Every employer enquiry is handled by me personally.</p>
</section>

<section class="cta" style="padding-top:5rem;">
  <h2 class="reveal">Hiring? <em>Let's talk.</em></h2>
  <p class="reveal">Send your role through the form, or message me on WhatsApp.</p>
  <div class="cta-btns reveal">
    <a href="/for-business/hire/" class="btn-pink">Tell me about your role</a>
    <a href="{_wa("Hi Lucy, I'm hiring and would like to find out more about Flow Corner for business")}" class="btn-whatsapp" target="_blank" rel="noopener">{WHATSAPP_SVG}Chat on WhatsApp</a>
  </div>
</section>'''

    # ------------------------------------------------------------ SERVICES
    pages["services"] = f'''<div class="page-header">
  <div class="section-label">For Business</div>
  <h1>How we can <em>work together</em></h1>
  <p>Pricing depends on the role and the support you need, so I quote each one. Tell me what you have in mind and I'll come back within 24 hours.</p>
</div>

<section class="services">
  <div class="services-grid">
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div>
      <div class="service-title">Feature your role</div>
      <div class="service-desc">Your open position shared with Flow Corner's job-seeker audience, with a clear description and a way to apply.</div>
      <div class="service-price">Quoted on request</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/><path d="m9 15 2 2 4-4"/></svg></div>
      <div class="service-title">Help finding the right people</div>
      <div class="service-desc">I help you write a role that attracts the right applicants and point you to candidates with strong, well-presented CVs.</div>
      <div class="service-price">Quoted on request</div>
    </div>
    <div class="service-card reveal">
      <div class="service-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg></div>
      <div class="service-title">Career development for your team</div>
      <div class="service-desc">One-on-one or small-group career development sessions for your staff: goals, skills gaps and a clear action plan.</div>
      <div class="service-price">Quoted on request</div>
    </div>
  </div>
  <p style="text-align:center; margin-top:2rem; font-size:0.88rem; color:var(--charcoal);">Looking for help for yourself instead? See <a href="/services/" style="color:var(--pink-deep); font-weight:700;">CV, LinkedIn and career roadmap services</a> for individuals.</p>
</section>

<section class="cta" style="padding-top:5rem;">
  <h2 class="reveal">Tell me what <em>you need</em></h2>
  <p class="reveal">No obligation. I'll reply within 24 hours.</p>
  <div class="cta-btns reveal">
    <a href="/for-business/hire/" class="btn-pink">Tell me about your role</a>
    <a href="{_wa("Hi Lucy, I'd like a quote for Flow Corner business services")}" class="btn-whatsapp" target="_blank" rel="noopener">{WHATSAPP_SVG}Chat on WhatsApp</a>
  </div>
</section>'''

    # ------------------------------------------------------------ ENQUIRY FORM
    pages["hire"] = f'''<div class="page-header">
  <div class="section-label">For Business</div>
  <h1>Tell me about <em>your role</em></h1>
  <p>Share a few details and I'll get back to you within 24 hours.</p>
</div>

<section class="about">
  <div class="assess-form-wrap reveal">
    <h3>Employer enquiry</h3>
    <p>Fill in what you can. Nothing is published until we've agreed it together.</p>
    <form name="employer-enquiry" method="POST" action="/for-business/thanks/" netlify netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="employer-enquiry">
      <p style="display:none;"><label>Don't fill this out: <input name="bot-field"></label></p>
      <div class="form-row">
        <div class="form-field">
          <label for="ecompany">Company *</label>
          <input type="text" id="ecompany" name="company" placeholder="Company name" required>
        </div>
        <div class="form-field">
          <label for="ename">Your name *</label>
          <input type="text" id="ename" name="contact_name" placeholder="Your full name" required>
        </div>
      </div>
      <div class="form-row">
        <div class="form-field">
          <label for="eemail">Email *</label>
          <input type="email" id="eemail" name="email" placeholder="you@company.co.za" required>
        </div>
        <div class="form-field">
          <label for="ephone">Phone / WhatsApp *</label>
          <input type="tel" id="ephone" name="phone" placeholder="+27 82 000 0000" required>
        </div>
      </div>
      <div class="form-row">
        <div class="form-field">
          <label for="erole">Role you're hiring for *</label>
          <input type="text" id="erole" name="role" placeholder="e.g. Admin Clerk" required>
        </div>
        <div class="form-field">
          <label for="eprovince">Province *</label>
          <select id="eprovince" name="province" required>
            <option value="" disabled selected>Select a province</option>
            <option>Gauteng</option><option>Western Cape</option><option>KwaZulu-Natal</option>
            <option>Eastern Cape</option><option>Free State</option><option>Limpopo</option>
            <option>Mpumalanga</option><option>North West</option><option>Northern Cape</option>
            <option>Remote</option>
          </select>
        </div>
      </div>
      <div class="form-row">
        <div class="form-field">
          <label for="ecount">How many people?</label>
          <input type="text" id="ecount" name="how_many" placeholder="e.g. 1, or 5 to 10">
        </div>
        <div class="form-field">
          <label for="ewhen">How soon do you need them? *</label>
          <select id="ewhen" name="urgency" required>
            <option value="" disabled selected>Select</option>
            <option>As soon as possible</option>
            <option>Within a month</option>
            <option>In the next few months</option>
            <option>Just exploring</option>
          </select>
        </div>
      </div>
      <div class="form-field">
        <label for="emsg">Anything else I should know?</label>
        <textarea id="emsg" name="message" placeholder="Skills needed, salary range, how to apply, closing date..."></textarea>
      </div>
      <div class="form-field" style="flex-direction:row; align-items:flex-start; gap:0.7rem;">
        <input type="checkbox" id="econsent" name="consent" value="yes" required style="margin-top:0.25rem; flex-shrink:0;">
        <label for="econsent" style="text-transform:none; letter-spacing:0; font-size:0.78rem; font-weight:500; color:rgba(255,255,255,0.7); line-height:1.6;">I agree that Flow Corner may use these details to reply to my enquiry. See the <a href="/privacy/" style="color:var(--pink);">privacy notice</a>.</label>
      </div>
      <button type="submit" class="btn-submit">Send my enquiry</button>
      <p class="form-note">I reply within 24 hours on WhatsApp or email. No spam, ever.</p>
    </form>
  </div>
</section>'''

    # ------------------------------------------------------------ THANKS
    pages["thanks"] = f'''<div class="page-header">
  <div class="section-label">For Business</div>
  <h1>Thank <em>you</em></h1>
  <p>I've got your enquiry and will reply within 24 hours.</p>
</div>

<section class="cta" style="padding-top:4rem;">
  <p class="reveal">Want to speak sooner? Message me on WhatsApp.</p>
  <div class="cta-btns reveal">
    <a href="{_wa("Hi Lucy, I just sent an employer enquiry on Flow Corner")}" class="btn-whatsapp" target="_blank" rel="noopener">{WHATSAPP_SVG}Chat on WhatsApp</a>
    <a href="/for-business/" class="btn-secondary" style="border-color:rgba(255,111,165,0.5); color:var(--pink);">Back to For Business</a>
  </div>
</section>'''

    # ------------------------------------------------------------ PRIVACY
    pages["privacy"] = '''<div class="page-header">
  <div class="section-label">Privacy</div>
  <h1>Privacy <em>notice</em></h1>
  <p>How Flow Corner handles your personal information. Last updated November 2026.</p>
</div>

<section class="article">
  <div class="article-inner">
    <h2>Who is responsible</h2>
    <p>Flow Corner is run by Lucy Mukhethwa in Johannesburg, South Africa. I am the responsible party for the personal information described here, under the Protection of Personal Information Act (POPIA).</p>

    <h2>What I collect, and why</h2>
    <p>When you fill in a form on this site (the free assessment or the employer enquiry), I collect the details you type in, such as your name, email, phone number and what you tell me about your career or hiring needs. I use them only to reply to you, deliver the service you asked about and keep a record of our conversation.</p>
    <p>The free tools (CV check, CV builder, cover letter and interview practice) run in your browser. What you type into them stays on your device and is not sent to me.</p>

    <h2>Who sees it</h2>
    <p>Only me. Form submissions are stored with the site's hosting provider, Netlify, and I may contact you by WhatsApp or email. I do not sell your information or share it with advertisers.</p>

    <h2>How long I keep it</h2>
    <p>I keep enquiry details for as long as needed to help you, and for a reasonable period after, then delete them.</p>

    <h2>Your rights</h2>
    <p>You can ask to see, correct or delete the information I hold about you at any time. Message me on <a href="https://wa.me/27832610754" target="_blank" rel="noopener">WhatsApp</a> and I will deal with it promptly. If you are unhappy, you can complain to the Information Regulator of South Africa.</p>

    <h2>Changes</h2>
    <p>If this notice changes, the new version will be published on this page.</p>
  </div>
</section>'''

    return pages
