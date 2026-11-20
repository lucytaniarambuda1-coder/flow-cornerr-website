#!/usr/bin/env python3
"""
Page bodies for the free tools: job-readiness check, CV builder, cover letter
generator, interview practice, the /free-tools/ hub and the /opportunities/ board.

generate.py imports build(ICON, WHATSAPP_SVG) and registers the returned pages.
The opportunities board is rendered from tools/opportunities.json, so adding a
listing means editing that file and re-running tools/generate.py.
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/27832610754?text="


def esc(s):
    return html.escape(s or "", quote=True)


def load_opportunities():
    with open(os.path.join(HERE, "opportunities.json")) as f:
        return json.load(f)


def build(ICON, WHATSAPP_SVG):
    pages = {}

    # ------------------------------------------------------------ JOB READINESS
    pages["job_readiness"] = f'''<div class="page-header">
  <div class="section-label">Learning Hub</div>
  <h1>How <em>Job-Ready</em> Are You?</h1>
  <p>Ten quick questions. Get a score out of 100, your biggest gaps and a plan for fixing them. Free, no sign-up, and your answers never leave your browser.</p>
  <p style="margin-top:0.9rem;"><a href="/learning-hub/" style="color:var(--pink); font-weight:700; font-style:normal;">← Back to Learning Hub</a></p>
</div>

<section class="ft-section">
  <div class="ft-wrap">
    <form id="jrForm" novalidate>
      <div class="jr-progress" aria-live="polite"><span id="jrCount">0</span> of 10 answered<div class="jr-bar"><div id="jrBarFill"></div></div></div>
      <div id="jrQuestions"></div>
      <div style="text-align:center;">
        <button class="btn-analyze" id="jrSubmit" type="submit">See My Score</button>
        <div class="cv-privacy-note" id="jrError" role="alert"></div>
      </div>
    </form>
    <div id="jrResults" class="jr-results" aria-live="polite"></div>
  </div>
</section>'''

    # ------------------------------------------------------------ CV BUILDER
    pages["cv_builder"] = f'''<div class="page-header">
  <div class="section-label">Free Tools</div>
  <h1>Free <em>CV Builder</em></h1>
  <p>Fill in the form and watch a clean, recruiter-friendly CV build itself. Save it as a PDF when you're done.</p>
  <p style="margin-top:0.9rem;"><a href="/free-tools/" style="color:var(--pink); font-weight:700; font-style:normal;">← Back to Free Tools</a></p>
</div>

<section class="ft-section">
  <div class="ft-wrap ft-wide">
    <div class="ft-split">
      <div class="ft-form" id="cbForm">
        <div class="ft-note">Your details stay in your browser. They are saved on this device only so you don't lose your work, so use <strong>Clear form</strong> if this is a shared computer.</div>

        <h2 class="ft-h">About you</h2>
        <div class="ft-row"><label class="ft-field">Full name<input id="f_name" autocomplete="name" placeholder="e.g. Thandi Nkosi"></label>
        <label class="ft-field">Job title you want<input id="f_title" placeholder="e.g. Customer Service Agent"></label></div>
        <div class="ft-row"><label class="ft-field">Email<input id="f_email" type="email" autocomplete="email" placeholder="you@email.com"></label>
        <label class="ft-field">Phone<input id="f_phone" type="tel" autocomplete="tel" placeholder="082 000 0000"></label></div>
        <div class="ft-row"><label class="ft-field">Town / city<input id="f_loc" placeholder="e.g. Soweto, Johannesburg"></label>
        <label class="ft-field">LinkedIn (optional)<input id="f_link" placeholder="linkedin.com/in/your-name"></label></div>

        <h2 class="ft-h">Profile</h2>
        <label class="ft-field">2–3 sentences about who you are and what you offer<textarea id="f_summary" rows="4" placeholder="Reliable, friendly customer service professional with 2 years' call-centre experience. Calm under pressure, quick to learn systems, and committed to resolving issues first time."></textarea></label>

        <h2 class="ft-h">Skills</h2>
        <label class="ft-field">Separate with commas<textarea id="f_skills" rows="2" placeholder="Customer service, MS Excel, Typing 45 wpm, Problem solving, Isixhosa, English"></textarea></label>

        <h2 class="ft-h">Work experience</h2>
        <p class="ft-help">One bullet per line. Start with an action word and add a number where you can (e.g. "Handled 60+ calls a day with a 92% satisfaction score").</p>
        <div id="expList"></div>
        <button type="button" class="ft-add" id="addExp">+ Add another job</button>

        <h2 class="ft-h">Education &amp; training</h2>
        <div id="eduList"></div>
        <button type="button" class="ft-add" id="addEdu">+ Add education</button>

        <h2 class="ft-h">Anything else</h2>
        <label class="ft-field">Certificates, driver's licence, volunteering (optional, one per line)<textarea id="f_other" rows="3" placeholder="Code 08 driver's licence&#10;First Aid Level 1"></textarea></label>

        <div class="ft-actions">
          <button type="button" class="btn-analyze" id="cbPrint">Download as PDF</button>
          <button type="button" class="ft-ghost" id="cbClear">Clear form</button>
        </div>
        <p class="ft-help">In the print window, choose <strong>Save as PDF</strong> as the destination. Turn off "Headers and footers" for the cleanest result.</p>
      </div>

      <div class="ft-preview-col">
        <div class="ft-preview-label">Live preview</div>
        <div class="cv-paper" id="cvPaper" aria-live="polite"></div>
      </div>
    </div>

    <div class="cv-cta-box" style="margin-top:3rem;">
      <h3>Want it checked and polished by a person?</h3>
      <p>Run it through the free CV Check first, or have me revamp it properly, with ATS-friendly wording and a design that stands out.</p>
      <div class="cta-btns" style="justify-content:center;">
        <a href="/learning-hub/cv-check/" class="btn-pink">Free CV Check</a>
        <a href="/services/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5);">CV Revamp from R100</a>
      </div>
    </div>
  </div>
</section>'''

    # ------------------------------------------------------------ COVER LETTER
    pages["cover_letter"] = f'''<div class="page-header">
  <div class="section-label">Free Tools</div>
  <h1>Cover Letter <em>Generator</em></h1>
  <p>Answer a few questions and get a clear, professional cover letter draft to edit and make your own.</p>
  <p style="margin-top:0.9rem;"><a href="/free-tools/" style="color:var(--pink); font-weight:700; font-style:normal;">← Back to Free Tools</a></p>
</div>

<section class="ft-section">
  <div class="ft-wrap ft-wide">
    <div class="ft-split">
      <div class="ft-form" id="clForm">
        <div class="ft-note">Nothing you type leaves your browser. This builds a draft from a proven structure. Always edit it so it sounds like you.</div>
        <h2 class="ft-h">You</h2>
        <div class="ft-row"><label class="ft-field">Full name<input id="c_name" autocomplete="name" placeholder="Thandi Nkosi"></label>
        <label class="ft-field">Email / phone<input id="c_contact" placeholder="thandi@email.com · 082 000 0000"></label></div>
        <label class="ft-field">In one line, who are you professionally?<input id="c_who" placeholder="a customer service professional with two years of call-centre experience"></label>

        <h2 class="ft-h">The job</h2>
        <div class="ft-row"><label class="ft-field">Job title<input id="c_role" placeholder="Customer Service Consultant"></label>
        <label class="ft-field">Company<input id="c_company" placeholder="Company name"></label></div>
        <div class="ft-row"><label class="ft-field">Hiring manager's name (optional)<input id="c_manager" placeholder="Ms Dlamini"></label>
        <label class="ft-field">Where did you see the job? (optional)<input id="c_source" placeholder="LinkedIn"></label></div>

        <h2 class="ft-h">Why you</h2>
        <p class="ft-help">Three things you'd bring, ideally with a result or number.</p>
        <label class="ft-field">Strength or achievement 1<textarea id="c_a1" rows="2" placeholder="Resolved 92% of customer queries on the first call"></textarea></label>
        <label class="ft-field">Strength or achievement 2<textarea id="c_a2" rows="2" placeholder="Trained 4 new agents on our CRM system"></textarea></label>
        <label class="ft-field">Strength or achievement 3 (optional)<textarea id="c_a3" rows="2" placeholder="Maintained a 98% attendance record over 18 months"></textarea></label>
        <label class="ft-field">Why this company? (optional, 1–2 sentences)<textarea id="c_why" rows="2" placeholder="I admire your focus on service quality and would love to grow with a team that values it."></textarea></label>

        <div class="ft-actions">
          <button type="button" class="btn-analyze" id="clMake">Write My Letter</button>
        </div>
      </div>

      <div class="ft-preview-col">
        <div class="ft-preview-label">Your letter <span style="font-weight:500; text-transform:none; letter-spacing:0;">(editable)</span></div>
        <textarea class="cv-textarea cl-output" id="clOutput" aria-label="Your cover letter" placeholder="Your letter will appear here. Fill in the form and press &quot;Write My Letter&quot;."></textarea>
        <div class="ft-actions" style="margin-top:1rem;">
          <button type="button" class="btn-analyze" id="clCopy" style="margin-top:0;">Copy text</button>
          <button type="button" class="ft-ghost" id="clPrint">Download as PDF</button>
          <span class="ft-copied" id="clCopied" role="status"></span>
        </div>
        <div class="cl-print" id="clPrint_div"></div>
      </div>
    </div>

    <div class="cv-cta-box" style="margin-top:3rem;">
      <h3>Need a CV to go with it?</h3>
      <p>Build one free in minutes, or check the one you have.</p>
      <div class="cta-btns" style="justify-content:center;">
        <a href="/free-tools/cv-builder/" class="btn-pink">Free CV Builder</a>
        <a href="/learning-hub/cv-check/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5);">Free CV Check</a>
      </div>
    </div>
  </div>
</section>'''

    # ------------------------------------------------------------ INTERVIEW PRACTICE
    pages["interview"] = f'''<div class="page-header">
  <div class="section-label">Free Tools</div>
  <h1>Interview <em>Practice</em></h1>
  <p>Common interview questions, a two-minute answer timer and a simple structure for answering. Say your answers out loud.</p>
  <p style="margin-top:0.9rem;"><a href="/free-tools/" style="color:var(--pink); font-weight:700; font-style:normal;">← Back to Free Tools</a></p>
</div>

<section class="ft-section">
  <div class="ft-wrap">
    <div class="ip-chips" id="ipChips" role="group" aria-label="Question type"></div>

    <div class="ip-card" id="ipCard">
      <div class="ip-cat" id="ipCat"></div>
      <div class="ip-q" id="ipQ" aria-live="polite"></div>
      <div class="ip-tip" id="ipTip"></div>
      <div class="ip-timer" id="ipTimer" aria-label="Answer timer">2:00</div>
      <div class="ft-actions" style="justify-content:center;">
        <button type="button" class="btn-analyze" id="ipStart" style="margin-top:0;">Start 2-minute answer</button>
        <button type="button" class="ft-ghost" id="ipNext">Next question →</button>
      </div>
      <div class="ip-meta"><button type="button" class="ft-ghost ft-small" id="ipDone">✓ Mark as practised</button> <span id="ipCount">0 practised</span></div>
    </div>

    <div class="ip-star">
      <h2 class="ft-h" style="margin-top:0;">The STAR method</h2>
      <p>For "tell me about a time…" questions, answer in four short steps:</p>
      <ol>
        <li><strong>Situation:</strong> set the scene in one sentence.</li>
        <li><strong>Task:</strong> what was your responsibility or goal?</li>
        <li><strong>Action:</strong> what did <em>you</em> do? This is the longest part.</li>
        <li><strong>Result:</strong> what changed? Use a number if you can.</li>
      </ol>
      <p>Prepare 3 stories (a challenge you solved, a time you worked in a team, a time you learned fast) and you can answer most behavioural questions.</p>
    </div>

    <div class="cv-cta-box" style="margin-top:2.5rem;">
      <h3>Want mock-interview feedback from a person?</h3>
      <p>Book a free 15-minute call and we'll talk through where you're stuck.</p>
      <div class="cta-btns" style="justify-content:center;">
        <a href="/contact/" class="btn-pink">Book a Free Call</a>
        <a href="/get-hired/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5);">Get Hired with AI kit · R149</a>
      </div>
    </div>
  </div>
</section>'''

    # ------------------------------------------------------------ FREE TOOLS HUB
    def tool_card(title, desc, icon, href, label):
        return f'''<a href="{href}" class="hub-card reveal">
      <div class="explore-icon">{ICON[icon]}</div>
      <div class="hub-card-title">{title}</div>
      <div class="hub-card-desc">{desc}</div>
      <span class="hub-card-arrow">{label}</span>
    </a>'''

    pages["free_tools"] = f'''<div class="page-header">
  <div class="section-label">Free Tools</div>
  <h1>Free <em>Career Tools</em></h1>
  <p>Check it. Build it. Find it. Practise it. Everything here is free, needs no sign-up, and runs in your browser.</p>
</div>

<section class="explore">
  <div class="hub-grid">
    {tool_card("Job-Readiness Check", "Ten questions, a score out of 100, your biggest gaps and a plan to close them.", "zap", "/learning-hub/job-readiness/", "Get my score →")}
    {tool_card("CV Check", "Paste or upload your CV for an instant checklist of what's working and what isn't.", "filecheck", "/learning-hub/cv-check/", "Check my CV →")}
    {tool_card("CV Builder", "Don't have a CV? Build a clean, recruiter-friendly one and save it as a PDF.", "folder", "/free-tools/cv-builder/", "Build my CV →")}
    {tool_card("Cover Letter Generator", "Answer a few questions and get a professional draft you can edit and send.", "message", "/free-tools/cover-letter/", "Write my letter →")}
    {tool_card("Interview Practice", "Common questions, a two-minute timer and the STAR method for strong answers.", "star", "/free-tools/interview-practice/", "Start practising →")}
    {tool_card("Opportunities Board", "Where to find jobs, learnerships and youth programmes in South Africa, in one place.", "search", "/opportunities/", "See opportunities →")}
  </div>
</section>

<section class="why-free">
  <div class="why-free-inner reveal">
    <div class="section-label">Why it's free</div>
    <h2>The basics shouldn't cost you anything.</h2>
    <p>Job hunting is expensive enough: data, transport, printing. Nobody should have to pay just to find out where they stand, or to get a CV that doesn't embarrass them. So these tools are free, with no sign-up and no email trap, and what you type never leaves your device.</p>
    <p>What you pay for is my time. If you want me to rewrite your CV, fix your LinkedIn or build your career roadmap with you, that's the paid work, and it's what keeps the free tools going.</p>
    <a href="/services/" class="fp-link">See paid services →</a>
  </div>
</section>'''

    # ------------------------------------------------------------ OPPORTUNITIES
    data = load_opportunities()
    items = data["items"]
    types = sorted({i["type"] for i in items})
    provinces = sorted({i.get("province", "National") for i in items})

    cards = []
    for it in items:
        closing = it.get("closing", "")
        closing_label = "Always open" if not closing else "Closes " + closing
        prov = it.get("province", "National")
        cards.append(f'''<article class="opp-card reveal" data-type="{esc(it['type'])}" data-province="{esc(prov)}" data-closing="{esc(closing)}" data-text="{esc((it['title'] + ' ' + it['org'] + ' ' + it['desc'] + ' ' + ' '.join(it.get('tags', []))).lower())}">
      <div class="opp-top"><span class="opp-type">{esc(it['type'])}</span><span class="opp-close" data-label="{esc(closing_label)}">{esc(closing_label)}</span></div>
      <h3 class="opp-title">{esc(it['title'])}</h3>
      <div class="opp-org">{esc(it['org'])} · {esc(prov)}</div>
      <p class="opp-desc">{esc(it['desc'])}</p>
      <a href="{esc(it['url'])}" class="opp-link" target="_blank" rel="noopener">{esc(it.get('cta', 'Visit the official page'))} →</a>
    </article>''')

    type_chips = "".join(f'<button type="button" class="ip-chip" data-type="{esc(t)}">{esc(t)}</button>' for t in types)
    province_filter = ""
    if len(provinces) > 1:
        opts = "".join(f'<option value="{esc(p)}">{esc(p)}</option>' for p in provinces)
        province_filter = f'<select id="oppProvince" aria-label="Province"><option value="">All provinces</option>{opts}</select>'

    pages["opportunities"] = f'''<div class="page-header">
  <div class="section-label">Open Now</div>
  <h1>Jobs &amp; <em>Opportunities</em></h1>
  <p>South African job platforms, learnerships and youth programmes, with the official link for each. New openings with closing dates are posted on Instagram first.</p>
  <p style="margin-top:0.9rem;"><a href="/free-tools/" style="color:var(--pink); font-weight:700; font-style:normal;">← Back to Free Tools</a></p>
</div>

<section class="ft-section">
  <div class="ft-wrap ft-wide">
    <a href="https://www.instagram.com/flow_cornerr/" target="_blank" rel="noopener" class="opp-banner reveal">
      <strong>Looking for fresh openings?</strong>
      <span>New jobs, learnerships and internships with closing dates are posted on @flow_cornerr. Follow so you don't miss one →</span>
    </a>

    <div class="opp-filters">
      <input type="search" id="oppSearch" placeholder="Search by name, topic or keyword…" aria-label="Search opportunities">
      {province_filter}
    </div>
    <div class="ip-chips" id="oppChips" role="group" aria-label="Opportunity type">
      <button type="button" class="ip-chip active" data-type="">All</button>{type_chips}
    </div>
    <div class="opp-count" id="oppCount" aria-live="polite"></div>
    <div class="opp-grid" id="oppGrid">
      {"".join(cards)}
    </div>
    <p class="opp-empty" id="oppEmpty" style="display:none;">Nothing matches that search. Try a different word or clear the filters.</p>
    <p class="opp-foot">Last checked: {esc(data['updated'])}. Always apply through the official page, and never pay to apply for a job or learnership. If someone asks you to, it's a scam.</p>

    <div class="cv-cta-box" style="margin-top:2.5rem;">
      <h3>Found one? Make sure your CV is ready.</h3>
      <p>Check your CV free, or find out how job-ready you are before you apply.</p>
      <div class="cta-btns" style="justify-content:center;">
        <a href="/learning-hub/cv-check/" class="btn-pink">Free CV Check</a>
        <a href="/learning-hub/job-readiness/" class="btn-secondary" style="border-color: rgba(255,111,165,0.5);">Job-Readiness Check</a>
      </div>
    </div>
  </div>
</section>'''

    return pages
