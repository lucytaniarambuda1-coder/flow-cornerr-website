(function () {
  // Five areas x two questions x max 10 points = 100.
  var AREAS = {
    cv: {
      name: 'Your CV',
      headline: 'Your CV is the first filter',
      tips: [
        'Tailor the top third of your CV (profile and key skills) to every job ad, using words from the advert itself.',
        'Keep it to 2 pages, one simple column, no photo, no tables or graphics. Many recruiting systems can\'t read them.',
        'Replace duties with results: "Handled 60+ calls a day at 92% satisfaction" beats "Answered phones".'
      ],
      links: [['Free CV Check', '/learning-hub/cv-check/'], ['Free CV Builder', '/free-tools/cv-builder/']]
    },
    online: {
      name: 'Online presence',
      headline: 'Make LinkedIn work while you sleep',
      tips: [
        'Add a clear photo and a headline with the role you want, not just your current job title.',
        'Write a 3-line summary and list 10+ relevant skills, because recruiters search by keyword.',
        'Switch on "Open to work" for recruiters and connect with people in the industry you want.'
      ],
      links: [['AI for your CV & LinkedIn', '/learning-hub/learn-ai/ai-for-cv-linkedin/'], ['LinkedIn Revamp from R150', '/services/']]
    },
    search: {
      name: 'Job search',
      headline: 'Search wider, apply sharper',
      tips: [
        'Use at least three sources: a job board, LinkedIn and company websites. Set job alerts so roles come to you.',
        'Aim for a few well-matched applications each week instead of dozens of random ones.',
        'Tell people you\'re looking. Many jobs are filled through referrals before they\'re advertised.'
      ],
      links: [['Opportunities board', '/opportunities/'], ['Where to search', '/learning-hub/find-a-job/']]
    },
    interview: {
      name: 'Interview readiness',
      headline: 'Practise before it counts',
      tips: [
        'Write down 3 achievements with results, and practise telling each as a short story (the STAR method).',
        'Rehearse your answer to "Tell me about yourself" out loud until it takes about a minute.',
        'Prepare two questions to ask them. It shows genuine interest.'
      ],
      links: [['Interview Practice', '/free-tools/interview-practice/'], ['Get Hired with AI kit', '/get-hired/']]
    },
    direction: {
      name: 'Direction & skills',
      headline: 'Get clear on your target',
      tips: [
        'Pick one or two job titles to aim at. A focused CV beats one that says "anything".',
        'Take a free career-interest test to see which roles fit how you work.',
        'Learn to use AI as a drafting assistant for applications, then edit everything so it sounds like you.'
      ],
      links: [['Free career assessment', '/learning-hub/free-assessment/'], ['Understand & use AI', '/learning-hub/learn-ai/']]
    }
  };

  var QUESTIONS = [
    { area: 'cv', q: 'How recently did you update your CV?', o: [['In the last 3 months', 10], ['3 to 12 months ago', 7], ['More than a year ago', 3], ['I don\'t have a CV yet', 0]] },
    { area: 'cv', q: 'Does your CV match the jobs you apply for?', o: [['I tailor it for every application', 10], ['I have one CV and tweak it sometimes', 6], ['I send the same CV everywhere', 3], ['I\'m not sure', 1]] },
    { area: 'online', q: 'What does your LinkedIn profile look like?', o: [['Complete: photo, headline, summary and skills', 10], ['It exists but is half-filled', 5], ['I haven\'t touched it in ages', 2], ['I don\'t have one', 0]] },
    { area: 'online', q: 'If a recruiter searched for your target job title, would they find you?', o: [['Yes, my profile uses the right keywords', 10], ['Maybe', 5], ['I don\'t think so', 2], ['I\'ve never checked', 1]] },
    { area: 'search', q: 'How do you find job openings?', o: [['Several sources: boards, LinkedIn, company sites and people', 10], ['One or two job sites', 6], ['Only when someone sends me a link', 3], ['I\'m not actively looking yet', 1]] },
    { area: 'search', q: 'How many targeted applications do you send in a typical week?', o: [['5 or more', 10], ['2 to 4', 7], ['1 or fewer', 3], ['None right now', 0]] },
    { area: 'interview', q: 'If you got an interview invitation for tomorrow, how would you feel?', o: [['Ready: I\'ve practised my answers', 10], ['Fairly ready: I know the basics', 6], ['Very nervous', 3], ['I\'d panic', 1]] },
    { area: 'interview', q: 'Can you describe three achievements, with results, from your work, studies or volunteering?', o: [['Yes, I have them ready', 10], ['I can think of one or two', 6], ['With some time to think', 3], ['Not really', 1]] },
    { area: 'direction', q: 'How clear are you on the kind of role you want?', o: [['Very: I know the titles and industries', 10], ['I have a general idea', 6], ['I\'ll take anything', 3], ['I have no idea yet', 1]] },
    { area: 'direction', q: 'Are you using AI tools to help with your applications?', o: [['Yes, as a drafting helper, and I edit the result', 10], ['I\'ve tried it once or twice', 6], ['I\'ve heard of it but haven\'t tried', 3], ['I don\'t know how to start', 1]] }
  ];

  var form = document.getElementById('jrForm');
  var host = document.getElementById('jrQuestions');
  var results = document.getElementById('jrResults');
  var errorEl = document.getElementById('jrError');
  var countEl = document.getElementById('jrCount');
  var barFill = document.getElementById('jrBarFill');
  if (!form) return;

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  var lastArea = null;
  QUESTIONS.forEach(function (item, qi) {
    if (item.area !== lastArea) {
      host.appendChild(el('div', 'jr-area', AREAS[item.area].name));
      lastArea = item.area;
    }
    var fs = el('fieldset', 'jr-q');
    fs.setAttribute('data-q', qi);
    fs.appendChild(el('legend', 'jr-legend', (qi + 1) + '. ' + item.q));
    item.o.forEach(function (opt, oi) {
      var label = el('label', 'jr-opt');
      var input = document.createElement('input');
      input.type = 'radio';
      input.name = 'q' + qi;
      input.value = String(opt[1]);
      input.id = 'q' + qi + '_' + oi;
      label.appendChild(input);
      label.appendChild(el('span', null, opt[0]));
      fs.appendChild(label);
    });
    host.appendChild(fs);
  });

  function answered() {
    var n = 0;
    QUESTIONS.forEach(function (_, qi) {
      if (form.querySelector('input[name="q' + qi + '"]:checked')) n++;
    });
    return n;
  }

  form.addEventListener('change', function (ev) {
    var n = answered();
    countEl.textContent = n;
    barFill.style.width = (n * 10) + '%';
    errorEl.textContent = '';
    var fs = ev.target && ev.target.closest ? ev.target.closest('.jr-q') : null;
    if (fs) fs.classList.remove('jr-missing');
  });

  function tier(score) {
    if (score >= 80) return ['Job-ready', 'jr-tier-great', 'You\'re in a strong position. Focus on volume and polish: apply widely and keep practising.'];
    if (score >= 60) return ['Almost there', 'jr-tier-good', 'You have a good base. Close the gaps below and your applications will start to land.'];
    if (score >= 40) return ['Building', 'jr-tier-mid', 'You\'ve started, and a few focused fixes will make a big difference. Start with the first gap below.'];
    return ['Starting point', 'jr-tier-low', 'Everyone starts somewhere. Pick one thing from the plan below and do it this week.'];
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var firstMissing = null;
    var totals = {};
    var score = 0;
    QUESTIONS.forEach(function (item, qi) {
      var checked = form.querySelector('input[name="q' + qi + '"]:checked');
      var fs = form.querySelector('.jr-q[data-q="' + qi + '"]');
      if (!checked) {
        fs.classList.add('jr-missing');
        if (!firstMissing) firstMissing = fs;
        return;
      }
      var pts = parseInt(checked.value, 10);
      totals[item.area] = (totals[item.area] || 0) + pts;
      score += pts;
    });
    if (firstMissing) {
      errorEl.textContent = 'Please answer every question to see your score.';
      firstMissing.scrollIntoView({ behavior: 'smooth', block: 'center' });
      return;
    }
    render(score, totals);
  });

  function render(score, totals) {
    results.textContent = '';
    var t = tier(score);

    var head = el('div', 'jr-head');
    head.appendChild(el('div', 'jr-score', String(score)));
    head.appendChild(el('div', 'jr-outof', 'out of 100'));
    head.appendChild(el('div', 'cv-tier-badge ' + t[1], t[0]));
    head.appendChild(el('p', 'jr-lead', t[2]));
    results.appendChild(head);

    var order = Object.keys(AREAS).sort(function (a, b) { return (totals[a] || 0) - (totals[b] || 0); });

    var bars = el('div', 'jr-bars');
    bars.appendChild(el('div', 'check-group-title', 'Your score by area'));
    Object.keys(AREAS).forEach(function (k) {
      var row = el('div', 'jr-barrow');
      row.appendChild(el('span', 'jr-barname', AREAS[k].name));
      var track = el('div', 'jr-track');
      var fill = el('div', 'jr-fill');
      fill.style.width = ((totals[k] || 0) * 5) + '%';
      track.appendChild(fill);
      row.appendChild(track);
      row.appendChild(el('span', 'jr-barval', (totals[k] || 0) + '/20'));
      bars.appendChild(row);
    });
    results.appendChild(bars);

    var plan = el('div', 'jr-plan');
    plan.appendChild(el('div', 'check-group-title', 'Your action plan: fix these first'));
    order.slice(0, 3).forEach(function (k, i) {
      var a = AREAS[k];
      var card = el('div', 'jr-gap');
      card.appendChild(el('div', 'jr-gap-num', String(i + 1)));
      var body = el('div', 'jr-gap-body');
      body.appendChild(el('h3', null, a.headline));
      var ul = el('ul');
      a.tips.forEach(function (tip) { ul.appendChild(el('li', null, tip)); });
      body.appendChild(ul);
      var links = el('div', 'jr-links');
      a.links.forEach(function (l) {
        var link = el('a', null, l[0] + ' →');
        link.href = l[1];
        links.appendChild(link);
      });
      body.appendChild(links);
      card.appendChild(body);
      plan.appendChild(card);
    });
    results.appendChild(plan);

    var cta = el('div', 'cv-cta-box');
    cta.appendChild(el('h3', null, 'Want me to go through your results with you?'));
    cta.appendChild(el('p', null, 'Book a free 15-minute call. We\'ll pick your next step together.'));
    var btns = el('div', 'cta-btns');
    btns.style.justifyContent = 'center';
    var b1 = el('a', 'btn-pink', 'Book My Free Call'); b1.href = '/contact/';
    var b2 = el('a', 'btn-secondary', 'Take the test again'); b2.href = '/learning-hub/job-readiness/';
    b2.style.borderColor = 'rgba(255,111,165,0.5)';
    btns.appendChild(b1); btns.appendChild(b2);
    cta.appendChild(btns);
    results.appendChild(cta);

    results.classList.add('visible');
    results.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
})();
