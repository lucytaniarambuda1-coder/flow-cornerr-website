(function () {
  const pasteTab = document.getElementById('tabPaste');
  const uploadTab = document.getElementById('tabUpload');
  const pastePanel = document.getElementById('panelPaste');
  const uploadPanel = document.getElementById('panelUpload');
  const cvTextarea = document.getElementById('cvPasteInput');
  const fileInput = document.getElementById('cvFileInput');
  const uploadZone = document.getElementById('cvUploadZone');
  const filenameEl = document.getElementById('cvFilename');
  const jdToggle = document.getElementById('jdToggle');
  const jdWrap = document.getElementById('jdWrap');
  const jdInput = document.getElementById('jdInput');
  const analyzeBtn = document.getElementById('analyzeBtn');
  const resultsEl = document.getElementById('cvResults');

  let uploadedText = '';

  function setTab(which) {
    const isPaste = which === 'paste';
    pasteTab.classList.toggle('active', isPaste);
    uploadTab.classList.toggle('active', !isPaste);
    pastePanel.classList.toggle('active', isPaste);
    uploadPanel.classList.toggle('active', !isPaste);
  }
  pasteTab.addEventListener('click', () => setTab('paste'));
  uploadTab.addEventListener('click', () => setTab('upload'));

  jdToggle.addEventListener('click', () => {
    const open = jdWrap.style.display === 'block';
    jdWrap.style.display = open ? 'none' : 'block';
    jdToggle.textContent = open
      ? '+ Add a job description (optional, for keyword matching)'
      : '− Hide job description';
  });

  uploadZone.addEventListener('click', () => fileInput.click());
  uploadZone.addEventListener('dragover', (e) => { e.preventDefault(); uploadZone.classList.add('dragover'); });
  uploadZone.addEventListener('dragleave', () => uploadZone.classList.remove('dragover'));
  uploadZone.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadZone.classList.remove('dragover');
    if (e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]);
  });
  fileInput.addEventListener('change', () => {
    if (fileInput.files.length) handleFile(fileInput.files[0]);
  });

  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  async function extractPdfText(arrayBuffer) {
    const pdfjsLib = await import('https://cdnjs.cloudflare.com/ajax/libs/pdf.js/6.3.289/pdf.min.mjs');
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/6.3.289/pdf.worker.min.mjs';
    const doc = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
    let text = '';
    for (let i = 1; i <= doc.numPages; i++) {
      const page = await doc.getPage(i);
      const content = await page.getTextContent();
      text += content.items.map((it) => it.str).join(' ') + '\n';
    }
    return text;
  }

  async function extractDocxText(arrayBuffer) {
    if (!window.mammoth) {
      await loadScript('https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.12.3/mammoth.browser.min.js');
    }
    const result = await window.mammoth.extractRawText({ arrayBuffer });
    return result.value;
  }

  async function handleFile(file) {
    filenameEl.textContent = 'Reading ' + file.name + '...';
    analyzeBtn.disabled = true;
    const name = file.name.toLowerCase();
    try {
      if (name.endsWith('.txt')) {
        uploadedText = await file.text();
      } else if (name.endsWith('.pdf')) {
        uploadedText = await extractPdfText(await file.arrayBuffer());
      } else if (name.endsWith('.docx')) {
        uploadedText = await extractDocxText(await file.arrayBuffer());
      } else {
        filenameEl.textContent = 'Unsupported file type — please use .txt, .pdf, or .docx, or paste your text instead.';
        analyzeBtn.disabled = false;
        return;
      }
      const wc = uploadedText.trim().split(/\s+/).filter(Boolean).length;
      filenameEl.textContent = uploadedText.trim() ? (file.name + ' loaded (' + wc + ' words)') : (file.name + ' loaded, but no readable text was found — try pasting instead.');
    } catch (err) {
      filenameEl.textContent = 'Could not read that file. Try pasting your CV text instead.';
      uploadedText = '';
    }
    analyzeBtn.disabled = false;
  }

  analyzeBtn.addEventListener('click', () => {
    const isPaste = pastePanel.classList.contains('active');
    const text = isPaste ? cvTextarea.value : uploadedText;
    if (!text || text.trim().split(/\s+/).filter(Boolean).length < 20) {
      alert("Please paste or upload your CV first — there isn't enough text to check yet.");
      return;
    }
    const results = analyzeCv(text, jdInput.value);
    renderResults(results);
    resultsEl.classList.add('visible');
    resultsEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  // ---------------- Heuristic engine (all client-side, no AI/API) ----------------

  const STRONG_VERBS = ['led', 'built', 'created', 'launched', 'managed', 'delivered', 'increased', 'reduced',
    'improved', 'developed', 'designed', 'implemented', 'coordinated', 'achieved', 'drove', 'grew', 'saved',
    'negotiated', 'streamlined', 'spearheaded', 'established', 'executed', 'optimised', 'optimized', 'trained',
    'mentored', 'analysed', 'analyzed'];
  const WEAK_OPENERS = ['responsible for', 'helped with', 'worked on', 'involved in', 'tasked with', 'assisted with'];
  const STOPWORDS = new Set(['the', 'and', 'a', 'an', 'of', 'to', 'in', 'for', 'on', 'with', 'as', 'is', 'are',
    'was', 'were', 'be', 'by', 'at', 'or', 'that', 'this', 'it', 'from', 'will', 'you', 'your', 'we', 'our']);

  function analyzeCv(text, jdText) {
    const words = text.trim().split(/\s+/).filter(Boolean);
    const wordCount = words.length;
    const lower = text.toLowerCase();
    const lines = text.split(/\n+/).map((l) => l.trim()).filter(Boolean);

    const checks = { basics: [], structure: [], content: [], length: [] };

    if (wordCount < 150) {
      checks.length.push({ status: 'fail', text: `Your CV is only about <strong>${wordCount} words</strong> — that usually reads as incomplete. Aim for at least 300–600 words.` });
    } else if (wordCount < 250) {
      checks.length.push({ status: 'warn', text: `At <strong>${wordCount} words</strong>, your CV is on the sparse side. A bit more detail on your achievements would help.` });
    } else if (wordCount > 1300) {
      checks.length.push({ status: 'warn', text: `At <strong>${wordCount} words</strong>, your CV is quite long. Most recruiters expect 1–2 pages — consider trimming to your most relevant experience.` });
    } else {
      checks.length.push({ status: 'pass', text: `Length looks good — about <strong>${wordCount} words</strong>, roughly 1–2 pages.` });
    }

    const hasEmail = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/i.test(text);
    const hasPhone = /(\+?\d[\d\s\-()]{7,}\d)/.test(text);
    const hasLinkedIn = /linkedin\.com\/in\//i.test(text);
    checks.basics.push({ status: hasEmail ? 'pass' : 'fail', text: hasEmail ? 'Email address found.' : 'No email address found — make sure it\'s clearly visible near the top.' });
    checks.basics.push({ status: hasPhone ? 'pass' : 'fail', text: hasPhone ? 'Phone number found.' : 'No phone number found — add one so recruiters can reach you directly.' });
    checks.basics.push({ status: hasLinkedIn ? 'pass' : 'warn', text: hasLinkedIn ? 'LinkedIn profile linked.' : 'No LinkedIn link found — adding one gives recruiters a fuller picture of you.' });

    const sectionPatterns = {
      Summary: /\b(summary|profile|objective|about me)\b/i,
      Experience: /\b(experience|work history|employment)\b/i,
      Education: /\b(education|qualifications|academic)\b/i,
      Skills: /\b(skills|competenc(y|ies))\b/i,
    };
    for (const [label, pattern] of Object.entries(sectionPatterns)) {
      const found = pattern.test(text);
      const soft = label === 'Education' || label === 'Summary';
      checks.structure.push({
        status: found ? 'pass' : (soft ? 'warn' : 'fail'),
        text: found ? `${label} section found.` : `No clear <strong>${label}</strong> section found — consider adding one so it's easy to scan.`,
      });
    }

    const bulletLines = lines.filter((l) => /^[•\-*▪◦]/.test(l) || /^\d+[.)]/.test(l));
    if (bulletLines.length === 0) {
      checks.content.push({ status: 'warn', text: 'No bullet points detected — bulleted achievements are usually easier for recruiters to scan than paragraphs.' });
    } else {
      const strongCount = bulletLines.filter((l) => {
        const clean = l.toLowerCase().replace(/^[•\-*▪◦\d.)\s]+/, '');
        return STRONG_VERBS.some((v) => clean.startsWith(v));
      }).length;
      const weakCount = bulletLines.filter((l) => WEAK_OPENERS.some((w) => l.toLowerCase().includes(w))).length;
      if (weakCount > 0) {
        checks.content.push({ status: 'warn', text: `Found ${weakCount} bullet(s) starting with weak phrasing like "responsible for" — try swapping in strong action verbs (led, built, delivered...) instead.` });
      }
      if (strongCount >= Math.max(2, Math.floor(bulletLines.length * 0.4))) {
        checks.content.push({ status: 'pass', text: `Good use of strong action verbs across your ${bulletLines.length} bullet points.` });
      } else {
        checks.content.push({ status: 'warn', text: `Only ${strongCount} of your ${bulletLines.length} bullet points open with a strong action verb — starting each one that way makes your impact clearer.` });
      }
    }

    const meaningfulNumbers = (text.match(/\d+%|\bR\s?\d|\$\s?\d|\d+\s?(clients|projects|people|team|hours|months|years)/gi) || []).length;
    if (meaningfulNumbers === 0) {
      checks.content.push({ status: 'warn', text: 'No quantified achievements found (numbers, %, R amounts). Adding measurable results makes your impact concrete — e.g. "reduced turnaround time by 20%".' });
    } else {
      checks.content.push({ status: 'pass', text: `Found ${meaningfulNumbers} quantified result(s) — numbers make your achievements concrete, keep it up.` });
    }

    if (jdText && jdText.trim().split(/\s+/).filter(Boolean).length > 15) {
      const jdWords = jdText.toLowerCase().match(/[a-z][a-z0-9+#.]{2,}/g) || [];
      const freq = {};
      jdWords.forEach((w) => { if (!STOPWORDS.has(w)) freq[w] = (freq[w] || 0) + 1; });
      const topJdWords = Object.entries(freq).sort((a, b) => b[1] - a[1]).slice(0, 15).map(([w]) => w);
      const missing = topJdWords.filter((w) => !lower.includes(w));
      const overlapPct = topJdWords.length ? Math.round(((topJdWords.length - missing.length) / topJdWords.length) * 100) : 0;
      checks.content.push({
        status: overlapPct >= 60 ? 'pass' : overlapPct >= 35 ? 'warn' : 'fail',
        text: `Your CV overlaps with about <strong>${overlapPct}%</strong> of the job description's key terms.` + (missing.length ? ` Consider working in: <strong>${missing.slice(0, 8).join(', ')}</strong>.` : ''),
      });
    }

    const all = [...checks.basics, ...checks.structure, ...checks.content, ...checks.length];
    const fails = all.filter((c) => c.status === 'fail').length;
    const warns = all.filter((c) => c.status === 'warn').length;
    let tier;
    if (fails === 0 && warns <= 1) tier = 'great';
    else if (fails <= 1 && warns <= 3) tier = 'good';
    else tier = 'needs-work';

    return { checks, tier };
  }

  function iconFor(status) {
    if (status === 'pass') {
      return '<svg class="check-icon pass" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>';
    }
    if (status === 'warn') {
      return '<svg class="check-icon warn" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
    }
    return '<svg class="check-icon fail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>';
  }

  const TIER_LABEL = { great: 'Great — Just a Few Tweaks', good: 'Good — Some Quick Wins Here', 'needs-work': "Needs Work — Let's Fix This" };
  const TIER_CLASS = { great: 'cv-tier-great', good: 'cv-tier-good', 'needs-work': 'cv-tier-needs-work' };

  function groupHtml(title, items) {
    if (!items.length) return '';
    const rows = items.map((c) => `<div class="check-item">${iconFor(c.status)}<div class="check-text">${c.text}</div></div>`).join('');
    return `<div class="check-group"><div class="check-group-title">${title}</div>${rows}</div>`;
  }

  function renderResults({ checks, tier }) {
    let html = `<div class="cv-tier-badge ${TIER_CLASS[tier]}">${TIER_LABEL[tier]}</div>`;
    html += groupHtml('Contact & Basics', checks.basics);
    html += groupHtml('Structure', checks.structure);
    html += groupHtml('Content Strength', checks.content);
    html += groupHtml('Length', checks.length);
    html += `<div class="cv-cta-box">
      <h3>Want a professional to fix this with you?</h3>
      <p>These are automated pointers — a real CV Revamp gets it recruiter-ready, tailored to the roles you actually want.</p>
      <div class="cta-btns">
        <a href="/services/" class="btn-pink">Book the CV Revamp (R300)</a>
        <a href="https://wa.me/27832610754?text=Hi%20Lucy%2C%20I%20just%20used%20the%20free%20CV%20Check%20and%20would%20like%20help" class="btn-whatsapp" target="_blank" rel="noopener">Chat on WhatsApp</a>
      </div>
    </div>`;
    resultsEl.innerHTML = html;
  }
})();
