#!/usr/bin/env python3
"""
Content for the "Start a Business" section of the Learning Hub.

Imported by generate.py. Kept in its own file because the guides are long.
Every external link below was checked (HTTP 200) in October 2026, and every
rule or figure comes from an official or government source. Where sources
disagree (funding caps, tax thresholds, application windows) the copy says
so and sends the reader to the official page instead of quoting a number.

To re-check links after a change: python3 tools/check_links.py
"""

REVIEWED = "October 2026"

# Official links. SEDA/SEFA are switched here in one place if their own sites are down.
URL = {
    "cipc": "https://www.cipc.co.za",
    "bizportal": "https://www.bizportal.gov.za",
    "bizportal_guide": "https://www.bizportal.gov.za/files/company_reg_guide.pdf",
    "gov_register": "https://www.gov.za/services/services-organisations/register-business-or-organisation/register-your-company",
    "gov_start": "https://www.gov.za/issues/starting-your-own-business-0",
    "gov_smallbiz": "https://www.gov.za/about-government/small-business-development",
    "dsbd": "https://www.dsbd.gov.za",
    "sars_small": "https://www.sars.gov.za/businesses-and-employers/small-businesses-taxpayers/",
    "sars_vat": "https://www.sars.gov.za/businesses-and-employers/small-businesses-taxpayers/small-businesses-and-vat/",
    "sars_tot": "https://www.sars.gov.za/faq/faq-what-are-the-requirements-for-a-micro-business-to-qualify-for-turnover-tax/",
    "csd": "https://www.csd.gov.za",
    "dtic": "https://www.thedtic.gov.za",
    "labour_guide": "https://www.labour.gov.za/DocumentCenter/Publications/Public%20Employment%20Services/Entrepreneurship_Starting%20and%20Running%20your%20own%20business_.pdf",
    "nyda_grant": "https://www.nyda.gov.za/Products-Services/NYDA-Grant-Programme.html",
    "nyda": "https://www.nyda.gov.za",
    "nyda_guide": "https://www.vukuzenzele.gov.za/guide-get-nyda-funding",
    "nyda_training": "https://www.vukuzenzele.gov.za/business-management-training-entrepreneurs",
    "funding_overview": "https://www.vukuzenzele.gov.za/funding-small-business-development",
    # sefa.org.za has an expired TLS certificate (Dec 2025) and seda.org.za did not load in Oct 2026,
    # so these two point to government pages that describe them. Switch back when their sites are healthy.
    "sefa": "https://www.vukuzenzele.gov.za/funding-small-business-development",
    "seda": "https://www.gov.za/about-government/small-business-development",
    "nef": "https://www.nefcorp.co.za/products-services/imbewu-fund/1-entrepreneurship-finance/",
    "gep": "https://www.gep.co.za/who-we-are/our-mandate/",
    "idc": "https://www.idc.co.za",
    "business_partners": "https://www.businesspartners.co.za",
    "absa": "https://www.absa.africa/absa-youth-entrepreneurship-fund/",
    "mrprice": "https://www.mrpricefoundation.org/uplift/",
    "yes": "https://www.yes4youth.co.za",
    "spaza": "https://www.sanews.gov.za/features-south-africa/guide-register-spaza-shops",
    "fasa": "https://fasa.co.za",
    "cidb": "https://www.cidb.org.za",
}

WA_BIZ = "https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%27d%20like%20help%20starting%20a%20business"


def a(key, text=None):
    """External link to an official page, opens in a new tab."""
    return f'<a href="{URL[key]}" target="_blank" rel="noopener">{text or URL[key]}</a>'


DISCLAIMER = '''      <div class="callout">
        <div class="callout-title">Good to know</div>
        <p>This guide is general information to help you get started. It is not legal, tax or financial advice, and rules, fees and funding change. Last reviewed: October 2026. Always confirm the details on the official page linked in each section, and speak to an accountant or attorney for anything that affects your money or liability. Applying to government agencies is free: never pay anyone to "fast-track" a grant or registration.</p>
      </div>'''


# =====================================================================
# 1. THE FLAGSHIP GUIDE
# =====================================================================
def guide_body():
    return f'''{DISCLAIMER}

      <div class="toc">
        <div class="toc-title">In this guide</div>
        <ol>
          <li><a href="#ready">Are you ready? A quick self-check</a></li>
          <li><a href="#idea">Find and test your idea</a></li>
          <li><a href="#types">How it works for different types of business</a></li>
          <li><a href="#plan">Write a simple business plan</a></li>
          <li><a href="#structure">Choose a legal structure</a></li>
          <li><a href="#register">Register your business and tax</a></li>
          <li><a href="#money">Set up your money properly</a></li>
          <li><a href="#customers">Get your first customers</a></li>
          <li><a href="#funding">Funding, in one paragraph</a></li>
          <li><a href="#mistakes">Common mistakes</a></li>
          <li><a href="#ninety">Your first 90 days checklist</a></li>
          <li><a href="#help">Where to get free help</a></li>
        </ol>
      </div>

      <p>Starting a business is one of the most exciting things you can do with your skills, and one of the easiest to get tangled up in. Between the paperwork, the tax rules and the money, many people never start. This guide walks you through the whole path, in order, for the kinds of businesses most South Africans actually start, with real links to the official places where each step happens.</p>
      <p>If you are not sure whether you want a business or a job, that is a fair place to be. Start with the <a href="/learning-hub/free-assessment/">free career assessment</a>, and come back when you know.</p>

      <h2 id="ready">1. Are you ready? A quick self-check</h2>
      <p>You do not need to feel ready. You need to be honest about where you are. Answer these for yourself, on paper:</p>
      <ol class="step-list">
        <li><strong>What problem am I solving, and for whom?</strong> If you cannot name the person, you are not ready to price or promote it.</li>
        <li><strong>Do people already pay for this?</strong> Someone paying a competitor is good news: it means the market exists.</li>
        <li><strong>What skills do I already have, and what am I missing?</strong> List both. Missing skills can be learned, hired or partnered for.</li>
        <li><strong>How much money do I need to start, and how long can I last without income?</strong> Work out a number, even a rough one.</li>
        <li><strong>How many hours a week can I really give it?</strong> Many successful businesses start part-time alongside a job.</li>
        <li><strong>Who will support me, and who will challenge me?</strong> You need both.</li>
      </ol>

      <h2 id="idea">2. Find and test your idea</h2>
      <p>Before spending money, test whether anyone wants what you are offering.</p>
      <ul>
        <li><strong>Talk to ten possible customers.</strong> Ask what they do now, what annoys them, and what they pay. Do not pitch. Listen.</li>
        <li><strong>Pre-sell.</strong> Offer your product or service to a few people before it fully exists: a WhatsApp message with a price and a date is enough. Real orders beat compliments.</li>
        <li><strong>Start small.</strong> One product, one service, one area. You can widen it once it works.</li>
        <li><strong>Check the competition.</strong> Note who they are, what they charge and what customers complain about. That complaint is your opening.</li>
      </ul>

      <h2 id="types">3. How it works for different types of business</h2>
      <p>The legal steps in sections 4 to 7 apply to every business, but what you need to <em>start</em> differs a lot by type. Find yours below. Many rules (especially permits and health rules) are set by your local municipality, so always ask them before you spend money on premises or equipment.</p>

      <h3>Service business or freelancing</h3>
      <p>Examples: consulting, cleaning, tutoring, photography, design, bookkeeping, writing, event planning.</p>
      <ul>
        <li><strong>Start-up needs:</strong> usually the lowest of any type: skills, a phone, data, and perhaps a laptop.</li>
        <li><strong>First steps:</strong> define one clear offer and a price; build a small portfolio or three case studies (offer your first jobs at a discount in exchange for a testimonial); set up a simple invoice and a one-page contract.</li>
        <li><strong>Watch out for:</strong> underpricing, working without a deposit, and mixing client money with your own. Most service businesses start as a sole proprietor and register a company later.</li>
      </ul>

      <h3>Retail, spaza and township trade</h3>
      <p>Examples: spaza shops, tuck shops, general dealers, clothing and accessories, airtime and data resellers.</p>
      <ul>
        <li><strong>Start-up needs:</strong> stock, premises or a stall, a way to track stock, and often a refrigerator or equipment.</li>
        <li><strong>Rules to check first:</strong> spaza shops and other food-selling outlets are required to register with their municipality. Municipalities typically ask for a business licence, zoning approval, a food-safety certificate and an ID, and some also ask for company and tax registration. Requirements differ by municipality, so contact your local business-licensing and environmental health offices. See the government's <a href="{URL['spaza']}" target="_blank" rel="noopener">guide to registering spaza shops</a>.</li>
        <li><strong>First steps:</strong> pick a location with foot traffic and permission to trade; buy only the fast-moving stock you can sell in a week; keep a daily cash book; learn your margins before you set prices.</li>
        <li><strong>Watch out for:</strong> over-stocking, extending credit you cannot collect, and selling expired or unsafe food.</li>
      </ul>

      <h3>Food and catering</h3>
      <p>Examples: home baking, catering, food stalls, a food truck, a small restaurant.</p>
      <ul>
        <li><strong>Start-up needs:</strong> equipment, ingredients, packaging, transport, and a hygienic place to prepare food.</li>
        <li><strong>Rules to check first:</strong> a food business generally needs a Certificate of Acceptability from your municipality's environmental health department before you trade. An inspector checks your premises against the national food-hygiene regulation (R638). It is issued for specific premises and is not transferable. This usually applies to a home kitchen, a stall and a delivery vehicle as well as a restaurant. A business licence is a separate municipal permit.</li>
        <li><strong>First steps:</strong> contact your municipality's environmental health office; get the application form; prepare your premises to the standard they will inspect; start with a small, simple menu.</li>
        <li><strong>Watch out for:</strong> trading before you have the certificate (fines or closure are possible), and pricing without counting your own time.</li>
      </ul>

      <h3>Online business and e-commerce</h3>
      <p>Examples: online shops, reselling, digital products, social-media services, courses, apps.</p>
      <ul>
        <li><strong>Start-up needs:</strong> a product or service, a way to take payment, delivery or a way to deliver digitally, and an online presence (social page, WhatsApp Business, or a simple website).</li>
        <li><strong>Rules to check first:</strong> if you collect customers' personal information (names, phone numbers, addresses) you must handle it responsibly under the Protection of Personal Information Act (POPIA). The Consumer Protection Act also covers returns, honest advertising and clear prices.</li>
        <li><strong>First steps:</strong> test with a handful of orders through WhatsApp or Instagram before you build a store; work out delivery cost per order; set a clear returns policy.</li>
        <li><strong>Watch out for:</strong> paying for stock you have not tested, hidden delivery costs, and chasing followers instead of buyers.</li>
      </ul>

      <h3>Farming and agriculture</h3>
      <p>Examples: vegetables, poultry, livestock, urban farming, agro-processing.</p>
      <ul>
        <li><strong>Start-up needs:</strong> land or access to it, water, inputs (seed, feed), equipment, and a buyer for what you produce.</li>
        <li><strong>First steps:</strong> secure a buyer or market <em>before</em> you plant or buy animals; start on a small area to learn the costs; ask your provincial Department of Agriculture about extension officers and training; ask the funders in our <a href="/learning-hub/start-a-business/funding-for-youth-and-entrepreneurs/">funding guide</a> about agricultural support.</li>
        <li><strong>Watch out for:</strong> weather and disease risk, long delays before income, and selling at low prices because you have no storage or transport.</li>
      </ul>

      <h3>Trades and construction</h3>
      <p>Examples: electrical, plumbing, building, painting, welding, carpentry, security.</p>
      <ul>
        <li><strong>Start-up needs:</strong> tools, transport, insurance, and proof you can do the work.</li>
        <li><strong>Rules to check first:</strong> some trades are regulated. For example, electrical and plumbing work often requires a registered person and a compliance certificate, and construction businesses bidding for public-sector work register with the <a href="{URL['cidb']}" target="_blank" rel="noopener">Construction Industry Development Board (CIDB)</a>. Check what applies to your trade before you quote.</li>
        <li><strong>First steps:</strong> get your trade qualification and any required registration; start with small jobs for referrals; get a written quote and deposit for every job.</li>
        <li><strong>Watch out for:</strong> working without the right registration, unpaid invoices, and quoting without counting materials and transport.</li>
      </ul>

      <h3>Buying a franchise</h3>
      <p>A franchise gives you a proven brand and system in return for fees and rules.</p>
      <ul>
        <li><strong>Know your rights:</strong> under the Consumer Protection Act regulations, a franchisor must give you a signed disclosure document at least 14 days before you sign, and you have a 10-business-day cooling-off period after signing. Confirm the current wording with a franchise attorney before you commit.</li>
        <li><strong>First steps:</strong> talk to current franchisees (not only the ones the franchisor picks); work out the <em>total</em> cost including fees and royalties; check whether the franchisor belongs to the <a href="{URL['fasa']}" target="_blank" rel="noopener">Franchise Association of South Africa (FASA)</a>.</li>
        <li><strong>Watch out for:</strong> promised profits you cannot verify, and agreements you do not fully understand.</li>
      </ul>

      <h3>A side hustle growing into a business</h3>
      <p>If you already sell on the side, you are ahead of most people. Keep your job while you track your sales for three months, separate the money, and register once you have steady customers or a client who asks for a tax invoice.</p>

      <h2 id="plan">4. Write a simple business plan</h2>
      <p>A business plan does not need to be long. The government's small-business guidance says it should state what you will do, how, when, and why you expect to succeed, backed by research. One to three pages is enough to start. Cover:</p>
      <ul>
        <li><strong>What you sell</strong> and who buys it.</li>
        <li><strong>Why you</strong>: your skills and experience.</li>
        <li><strong>Your costs and prices:</strong> start-up costs, monthly running costs, price per sale, and how many sales you need to break even.</li>
        <li><strong>A 12-month cash-flow estimate:</strong> money in and money out, month by month.</li>
        <li><strong>How you will find customers.</strong></li>
        <li><strong>How much funding you need, and what for.</strong></li>
      </ul>
      <p>Seda helps entrepreneurs write business plans free of charge, and the Department of Employment and Labour publishes a practical <a href="{URL['labour_guide']}" target="_blank" rel="noopener">guide to starting and running your own business</a> (PDF) with templates. You can also read the government's own page on <a href="{URL['gov_start']}" target="_blank" rel="noopener">starting your own business</a>.</p>

      <h2 id="structure">5. Choose a legal structure</h2>
      <p>This decides how you are taxed, who is responsible if things go wrong, and how funders see you.</p>
      <p class="table-hint">Swipe sideways to see the whole table →</p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Structure</th><th>Registration</th><th>Personal liability</th><th>Good for</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Sole proprietor</strong></td><td>None with CIPC. Register with SARS as a taxpayer.</td><td>Unlimited: your personal assets can be used to pay business debts.</td><td>Starting small and testing the idea; freelancers; side hustles.</td></tr>
            <tr><td><strong>Partnership</strong></td><td>None with CIPC. Put a written agreement in place.</td><td>Unlimited, and you can be responsible for your partner's business debts.</td><td>Two or more people starting together. Only with a written agreement.</td></tr>
            <tr><td><strong>Private company (Pty) Ltd</strong></td><td>CIPC, online through BizPortal.</td><td>Generally limited: the company is a separate legal entity.</td><td>Most growing businesses; tenders; funding applications.</td></tr>
            <tr><td><strong>Non-profit company (NPC)</strong></td><td>CIPC.</td><td>Generally limited.</td><td>Community and charitable work. Get advice first: the rules are different.</td></tr>
            <tr><td><strong>Co-operative</strong></td><td>CIPC, with a minimum number of members (check the current rule).</td><td>Generally limited.</td><td>A group producing, buying or selling together.</td></tr>
          </tbody>
        </table>
      </div>
      <p>The old "close corporation" (CC) is no longer registered for new businesses, so a (Pty) Ltd is the usual choice once you outgrow a sole proprietorship. Many people start as a sole proprietor and register a company once the business is earning steadily.</p>

      <h2 id="register">6. Register your business and tax</h2>
      <h3>Register a company (if you chose a (Pty) Ltd)</h3>
      <ol class="step-list">
        <li><strong>Create an account on {a('bizportal', 'BizPortal')}.</strong> You sign in with your South African ID.</li>
        <li><strong>Optionally reserve a name.</strong> You can register without one and use the registration number as your name until you choose.</li>
        <li><strong>Enter your director details.</strong> BizPortal checks each director's ID against Home Affairs, so spell names exactly as on the ID. A company needs at least one director.</li>
        <li><strong>Pay the fee.</strong> At the time of writing BizPortal lists R125 without a name and R175 with a name; confirm the current fee on the site. BizPortal's own <a href="{URL['bizportal_guide']}" target="_blank" rel="noopener">step-by-step guide</a> shows each screen.</li>
        <li><strong>Keep your documents.</strong> Once registered, you must file annual returns with {a('cipc', 'CIPC')}.</li>
      </ol>
      <h3>Register for tax with SARS</h3>
      <ul>
        <li><strong>Companies:</strong> registering a company with CIPC automatically creates an income-tax reference number with SARS. You then register on eFiling to submit returns.</li>
        <li><strong>Sole proprietors:</strong> register yourself with SARS as a taxpayer; you may need to pay provisional tax during the year.</li>
        <li><strong>Turnover Tax:</strong> an optional, simpler tax for micro businesses. SARS's Budget 2026 guidance says the turnover limit rises from R1 million to R2.3 million from 1 April 2026. Confirm the current limit on the <a href="{URL['sars_tot']}" target="_blank" rel="noopener">SARS Turnover Tax page</a>.</li>
        <li><strong>VAT:</strong> compulsory once your taxable sales pass the threshold, and optional below it. The 2026 Budget announced a rise in the compulsory threshold to R2.3 million and the voluntary threshold to R120,000, but SARS's small-business VAT page still shows R1 million and R50,000, so check the current figures on the <a href="{URL['sars_vat']}" target="_blank" rel="noopener">SARS VAT page</a> before you decide.</li>
        <li><strong>More from SARS:</strong> the <a href="{URL['sars_small']}" target="_blank" rel="noopener">small businesses section</a> and its <a href="{URL['sars_tot']}" target="_blank" rel="noopener">Turnover Tax requirements</a>.</li>
      </ul>
      <h3>If you will employ people</h3>
      <p>Register as an employer: UIF and the Compensation Fund (COIDA) can both be registered through BizPortal if you have employees, and PAYE and the Skills Development Levy apply once your payroll reaches the thresholds. Ask an accountant or Seda adviser which apply to you, and what a contract must contain.</p>
      <h3>Local and industry permits</h3>
      <p>Your municipality may require a business licence, zoning approval for your premises, or health and fire approvals. Ask the business-licensing office before you sign a lease. If you want to supply government, register on the {a('csd', 'Central Supplier Database')} (it is free).</p>

      <h2 id="money">7. Set up your money properly</h2>
      <ul>
        <li><strong>Open a separate business bank account.</strong> Banks offer starter accounts for small businesses. Never run the business through your personal account.</li>
        <li><strong>Record every rand.</strong> A simple spreadsheet or a free bookkeeping app is enough at the start: date, what, who, in, out.</li>
        <li><strong>Price properly.</strong> Price = your costs + your time + a profit. Do not copy a competitor's price without knowing their costs.</li>
        <li><strong>Pay yourself a small, regular amount</strong> and leave the rest in the business until you are stable.</li>
        <li><strong>Keep a tax pot.</strong> Move a percentage of every sale into a separate savings account for tax.</li>
        <li><strong>Get an accountant for the first year-end</strong>, even if you do the rest yourself.</li>
      </ul>

      <h2 id="customers">8. Get your first customers</h2>
      <ul>
        <li><strong>Tell everyone you know,</strong> clearly, what you do and who it is for. First customers are usually people who already trust you.</li>
        <li><strong>Use WhatsApp Business and a single social page</strong> instead of five half-finished ones. Post proof: results, photos, testimonials.</li>
        <li><strong>Claim your Google Business Profile</strong> if customers search for a local service.</li>
        <li><strong>Ask for referrals</strong> after every job, and say thank you.</li>
        <li><strong>A simple website helps</strong> once you have something to show. It does not need to be big or expensive.</li>
        <li><strong>Be consistent.</strong> Post, follow up and ask every week, not only when it is quiet.</li>
      </ul>

      <h2 id="funding">9. Funding, in one paragraph</h2>
      <p>Most small businesses start with savings, a small loan from family, or a first customer's deposit, and then apply for outside funding once they have a registered business, a plan and some sales. For young people there are real options, including the NYDA grant, sefa loans, and several private programmes. Each has its own requirements. Read our full <a href="/learning-hub/start-a-business/funding-for-youth-and-entrepreneurs/">funding guide for youth and entrepreneurs</a>, and be careful with anyone who asks you to pay a fee to "unlock" a grant.</p>

      <h2 id="mistakes">10. Common mistakes</h2>
      <ul>
        <li>Spending on a logo, website and stock before testing demand.</li>
        <li>Mixing personal and business money.</li>
        <li>Pricing too low and trying to make it up in volume.</li>
        <li>Skipping registrations and permits, then losing a contract or paying a fine.</li>
        <li>Doing everything alone. A mentor, an adviser or a partner saves expensive mistakes.</li>
        <li>Giving up in month three. Most businesses take longer than expected to find their footing.</li>
      </ul>

      <h2 id="ninety">11. Your first 90 days checklist</h2>
      <div class="callout">
        <div class="callout-title">Days 1 to 30: prove it</div>
        <ul>
          <li>Talk to ten possible customers</li>
          <li>Pre-sell to at least three</li>
          <li>Write your one-page business plan and cash flow</li>
          <li>Decide your structure and price</li>
        </ul>
        <div class="callout-title">Days 31 to 60: set it up</div>
        <ul>
          <li>Register (CIPC and SARS) or register as a taxpayer if a sole proprietor</li>
          <li>Open the business bank account</li>
          <li>Check municipal permits for your type of business</li>
          <li>Set up records and a simple invoice</li>
        </ul>
        <div class="callout-title">Days 61 to 90: sell it</div>
        <ul>
          <li>Serve your first customers and collect testimonials</li>
          <li>Ask each customer for a referral</li>
          <li>Review your numbers: what sold, what cost, what profit</li>
          <li>Book a free session with Seda or NYDA, and check funding options</li>
        </ul>
      </div>

      <h2 id="help">12. Where to get free help</h2>
      <ul>
        <li><strong>Seda</strong> (Small Enterprise Development Agency): free advice, business plans, training and mentoring through its branches. Seda is being merged with sefa into a new agency, so check the Department of Small Business Development site for current branch details: {a('dsbd', 'dsbd.gov.za')}.</li>
        <li><strong>NYDA:</strong> business management training and grants for ages 18 to 35, through the {a('nyda', 'NYDA website')}, its branches, or the call centre on 0800 58 58 58.</li>
        <li><strong>Local municipality:</strong> business licensing, zoning and environmental health.</li>
        <li><strong>Business Partners and sefa:</strong> small-business finance and mentorship. See the <a href="/learning-hub/start-a-business/funding-for-youth-and-entrepreneurs/">funding guide</a>.</li>
        <li><strong>Our <a href="/learning-hub/start-a-business/useful-links/">useful links page</a></strong> collects every official site mentioned in this guide.</li>
      </ul>
      <p>And if you want a person on your side while you work through it, that is what Business Start-Up Support is for.</p>'''


# =====================================================================
# 2. THE FUNDING GUIDE
# =====================================================================
def funding_body():
    return f'''{DISCLAIMER}

      <p>Funding is one of the biggest questions for anyone starting a business. This guide explains the main kinds of funding, then lists the main programmes open to South African youth and entrepreneurs, what each is for, and where to apply. We do not quote amounts that different sources disagree on, because caps and deadlines change. Check the official page for the current figures.</p>

      <h2>Grants, loans, equity and savings: what is the difference?</h2>
      <ul>
        <li><strong>Grant:</strong> money you do not pay back, usually for a specific use, with conditions and reporting.</li>
        <li><strong>Loan:</strong> money you repay, with interest. Funders look hard at whether the business can repay.</li>
        <li><strong>Equity:</strong> an investor gets a share of your business. Less common for very small businesses.</li>
        <li><strong>Your own money:</strong> savings, a family loan or a customer's deposit. Often where the first rand comes from, and funders like to see you have put something in.</li>
      </ul>

      <div class="callout">
        <div class="callout-title">Avoid funding scams</div>
        <p>Applying to government funders is free. Never pay anyone who promises you a grant, "guaranteed" approval or a "fast track". Apply only through the funder's official website, branch or call centre, and be careful with sites that only repeat funding information, because their amounts and dates are often out of date.</p>
      </div>

      <h2>The main programmes</h2>
      <p>Programmes change: always confirm eligibility, amounts, and whether applications are open on the official page. Last reviewed: October 2026.</p>
      <p class="table-hint">Swipe sideways to see the whole table →</p>
      <div class="table-wrap">
        <table class="funding-table">
          <thead>
            <tr><th>Programme</th><th>Who it is for</th><th>Type</th><th>Good to know</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>{a('nyda_grant', 'NYDA Grant Programme')}</strong></td><td>South Africans aged 18 to 35 with a youth-owned business</td><td>Grant (not repaid)</td><td>You complete NYDA business management training first, give a short pitch, and submit documents such as ID, a business plan and supplier quotes. NYDA excludes businesses above a turnover limit, and the maximum and age rule have changed over time, so check the current figures. Call centre: 0800 58 58 58.</td></tr>
            <tr><td><strong>{a('sefa', 'sefa')}</strong> (Small Enterprise Finance Agency)</td><td>Small businesses and co-operatives, including start-ups and expansion</td><td>Loans</td><td>Products include bridging loans, revolving credit and term loans for equipment. You usually need a business plan, a fixed address, tax compliance and the ability to repay. sefa is being merged with Seda.</td></tr>
            <tr><td><strong>{a('seda', 'Seda')}</strong> (Small Enterprise Development Agency)</td><td>Anyone starting or growing a small business</td><td>Free support (not money)</td><td>Business plans, registration help, training, mentoring and help getting ready for funding. A good first stop because it is free.</td></tr>
            <tr><td><strong>{a('nef', 'National Empowerment Fund (NEF)')}</strong></td><td>Majority black-owned businesses, including start-ups</td><td>Loans</td><td>Entrepreneurship Finance supports start-up and expansion. You need a registered legal entity, a viable business case and, if you lack experience, the NEF may require mentorship.</td></tr>
            <tr><td><strong>{a('gep', 'Gauteng Enterprise Propeller (GEP)')}</strong></td><td>Gauteng small businesses and township entrepreneurs, with priority for youth, women and people with disabilities</td><td>Finance and business support</td><td>Includes the Township Economy Partnership Fund, business development support and pitching events. Older criteria asked for CIPC registration, SARS compliance and a trading history, so check what is open now. Relevant if you are in Soweto or elsewhere in Gauteng.</td></tr>
            <tr><td><strong>{a('absa', 'Absa Youth Entrepreneurship Fund')}</strong></td><td>Young South African entrepreneurs (age range and ownership criteria on its page)</td><td>Grant (not repaid)</td><td>Run in yearly application rounds with a closing date, run with the Tshiamo Foundation. Check the page for the current round.</td></tr>
            <tr><td><strong>{a('mrprice', 'Mr Price Foundation (Uplift)')}</strong></td><td>Youth entrepreneurs in its programme</td><td>Development programme and seed support</td><td>An accelerator-style programme. Check the page for how and when to apply.</td></tr>
            <tr><td><strong>{a('business_partners', 'Business Partners')}</strong></td><td>Established small and medium businesses</td><td>Finance and support</td><td>A specialist SME financier. Check what it funds and its minimum amounts on its website.</td></tr>
            <tr><td><strong>{a('idc', 'Industrial Development Corporation (IDC)')}</strong></td><td>Larger industrial and business projects</td><td>Development finance</td><td>Usually for bigger funding needs, so more likely a later-stage option.</td></tr>
            <tr><td><strong>{a('dtic', 'The dtic')}</strong> (Department of Trade, Industry and Competition)</td><td>Businesses in qualifying sectors</td><td>Incentives and support</td><td>Incentive schemes for certain sectors (such as manufacturing and exporting). Usually for established businesses.</td></tr>
            <tr><td><strong>{a('yes', 'Youth Employment Service (YES)')}</strong></td><td>Young people looking for work experience</td><td>Not funding</td><td>A 12-month paid work experience programme. It does not fund businesses, but it is a good way to build skills and savings first.</td></tr>
          </tbody>
        </table>
      </div>
      <p>For a plain-English overview of government funding for small businesses, see the government's article on <a href="{URL['funding_overview']}" target="_blank" rel="noopener">funding for small business development</a>.</p>

      <h2>How to get funding-ready</h2>
      <p>Most funders look for the same things. Work through this list before you apply:</p>
      <ol class="step-list">
        <li><strong>A registered business.</strong> Some funders accept sole proprietors, but many want a registered entity. See <a href="/learning-hub/start-a-business/how-to-start-a-small-business/#register">how to register</a>.</li>
        <li><strong>Tax compliance.</strong> A registered SARS profile and up-to-date returns.</li>
        <li><strong>A clear business plan</strong> with a cash-flow forecast and what you will spend the money on.</li>
        <li><strong>Quotations</strong> from suppliers for anything you plan to buy (often three).</li>
        <li><strong>Bank statements</strong> from a business account, and certified copies of your ID.</li>
        <li><strong>A practised pitch.</strong> Ten minutes: who you serve, what you sell, how it makes money, what you need.</li>
        <li><strong>Evidence of sales or demand:</strong> orders, invoices, letters of intent, testimonials.</li>
      </ol>

      <h2>If you are applying to the NYDA</h2>
      <ol class="step-list">
        <li>Register on the NYDA portal or visit a branch; the call centre is 0800 58 58 58.</li>
        <li>Complete the NYDA business management training. See the government's page on <a href="{URL['nyda_training']}" target="_blank" rel="noopener">business management training for entrepreneurs</a>.</li>
        <li>Prepare your documents and application form (see the <a href="{URL['nyda_guide']}" target="_blank" rel="noopener">step-by-step guide on Vuk'uzenzele</a>).</li>
        <li>Give your pitch and go through the due-diligence assessment.</li>
        <li>Apply well before your 35th birthday: the NYDA sets a minimum lead time, and sources quote different periods, so confirm it with them.</li>
      </ol>

      <h2>Before you apply: your checklist</h2>
      <div class="callout">
        <ul>
          <li>I read the <em>official</em> page for this programme, not a summary on another site.</li>
          <li>I meet the age, ownership and turnover rules.</li>
          <li>I know whether applications are open, and the closing date.</li>
          <li>My documents are certified and up to date.</li>
          <li>I am not paying anyone to apply for me.</li>
          <li>I have a plan for what the money will do and how I will show results.</li>
        </ul>
      </div>
      <p>Want a second pair of eyes on your plan or pitch before you apply? That is exactly what <a href="/services/">Business Start-Up Support</a> is for. You can also start with the <a href="/learning-hub/start-a-business/how-to-start-a-small-business/">full step-by-step guide</a>.</p>'''


# =====================================================================
# 3. LINKS DIRECTORY (uses resource_card)
# =====================================================================
def links_sections(resource_card):
    def c(title, desc, icon, key):
        return resource_card(title, desc, icon, URL[key])

    groups = [
        ("Register your business", "The official places where a business becomes real.", [
            c("BizPortal", "Register a company online, reserve a name, and register for UIF and the Compensation Fund if you employ people.", "briefcase", "bizportal"),
            c("CIPC", "The Companies and Intellectual Property Commission: company records, annual returns and name searches.", "filecheck", "cipc"),
            c("Register your company (gov.za)", "The government's own step-by-step overview of company registration.", "book", "gov_register"),
        ]),
        ("Tax", "Tax is simpler when you know the options early.", [
            c("SARS: small businesses", "Everything SARS publishes for small business owners, in one place.", "briefcase", "sars_small"),
            c("SARS: Turnover Tax", "The simplified tax regime for micro businesses, and who qualifies.", "filecheck", "sars_tot"),
            c("SARS: small businesses and VAT", "When you must register for VAT, and when you may.", "search", "sars_vat"),
        ]),
        ("Free advice, plans and training", "Free help is available. Use it.", [
            c("Start your own business (gov.za)", "The government's guide to planning and starting a business.", "compass", "gov_start"),
            c("Starting and running your own business (PDF)", "A practical guide and templates from the Department of Employment and Labour.", "book", "labour_guide"),
            c("Department of Small Business Development", "The department that oversees Seda and sefa, with links to support.", "briefcase", "dsbd"),
            c("NYDA", "Business management training and support for young entrepreneurs aged 18 to 35.", "person", "nyda"),
        ]),
        ("Funding", "Official pages for the programmes in our funding guide. Always check current eligibility and open calls.", [
            c("NYDA Grant Programme", "Non-repayable grants for young entrepreneurs, with requirements and how to apply.", "star", "nyda_grant"),
            c("Funding for small business development (gov.za)", "A government overview of the funders available to small businesses.", "book", "funding_overview"),
            c("National Empowerment Fund", "Entrepreneurship Finance for majority black-owned start-ups and expansions.", "zap", "nef"),
            c("Gauteng Enterprise Propeller", "Finance and business support for Gauteng and township entrepreneurs.", "compass", "gep"),
            c("Absa Youth Entrepreneurship Fund", "Annual grant rounds for young entrepreneurs. Check the current deadline.", "star", "absa"),
            c("Mr Price Foundation Uplift", "A development programme for youth entrepreneurs.", "bulb", "mrprice"),
            c("Business Partners", "Small and medium business finance and mentorship.", "briefcase", "business_partners"),
            c("Industrial Development Corporation", "Development finance for larger industrial and business projects.", "zap", "idc"),
        ]),
        ("Customers and contracts", "Where to find your first bigger customers.", [
            c("Central Supplier Database", "Free registration that lets you supply goods and services to government.", "search", "csd"),
            c("The dtic", "Information on incentives and support for qualifying sectors.", "briefcase", "dtic"),
            c("CIDB", "Registration for construction businesses that bid for public-sector work.", "filecheck", "cidb"),
        ]),
        ("Rules for specific businesses", "Permits and rules that depend on what you sell.", [
            c("Registering a spaza shop", "A government guide to what spaza and food outlets must register.", "briefcase", "spaza"),
            c("Franchise Association of South Africa", "Information for people thinking of buying a franchise.", "search", "fasa"),
        ]),
        ("Learn more", "Plain-English guides worth reading.", [
            c("A guide to getting NYDA funding", "Vuk'uzenzele's step-by-step guide for NYDA grant applicants.", "book", "nyda_guide"),
            c("Business management training for entrepreneurs", "What the NYDA training involves and why it matters.", "person", "nyda_training"),
            c("Youth Employment Service", "A 12-month paid work experience programme for young people.", "star", "yes"),
        ]),
    ]
    out = []
    for label, intro, cards in groups:
        out.append(f'''  <div class="hub-category-label">{label}</div>
  <p class="hub-category-intro">{intro}</p>
  <div class="resource-grid">
    {chr(10).join("    " + x for x in cards).strip()}
  </div>
''')
    return "\n".join(out)
