(function () {
  var QS = [
    // About you
    { c: 'About you', q: 'Tell me about yourself.', t: 'Keep it to about a minute: who you are professionally, one or two highlights, and why you\'re excited about this role.' },
    { c: 'About you', q: 'Why do you want this job?', t: 'Link something specific about the role or company to your strengths. Avoid "I need a job".' },
    { c: 'About you', q: 'Why should we hire you?', t: 'Name your top two strengths and back each with a short example or result.' },
    { c: 'About you', q: 'Where do you see yourself in five years?', t: 'Show you want to grow, ideally in a way that benefits the company. Be honest but ambitious.' },
    { c: 'About you', q: 'What do you know about our company?', t: 'Do your homework: look at their website and LinkedIn page the night before and mention one thing that genuinely interests you.' },
    // Strengths and weaknesses
    { c: 'Strengths & weaknesses', q: 'What are your greatest strengths?', t: 'Choose strengths that match the job ad and give an example for each.' },
    { c: 'Strengths & weaknesses', q: 'What is your biggest weakness?', t: 'Pick a real but fixable weakness, then explain what you are doing to improve it. Never say "I\'m a perfectionist".' },
    { c: 'Strengths & weaknesses', q: 'How do you handle pressure or tight deadlines?', t: 'Describe your method (prioritise, break the task down, communicate early) and give a quick example.' },
    { c: 'Strengths & weaknesses', q: 'How do you learn new things?', t: 'Mention a recent skill or system you picked up quickly, and how you did it.' },
    // Behavioural (STAR)
    { c: 'Tell me about a time…', q: 'Tell me about a time you solved a difficult problem.', t: 'Use STAR: Situation, Task, Action, Result. Spend most of your time on what you did.' },
    { c: 'Tell me about a time…', q: 'Tell me about a time you worked well in a team.', t: 'Say what your role was and how you helped the team reach the goal. Use "I" for your actions and "we" for the result.' },
    { c: 'Tell me about a time…', q: 'Tell me about a time you dealt with a difficult customer or colleague.', t: 'Show that you stayed calm, listened and found a solution. End with the outcome.' },
    { c: 'Tell me about a time…', q: 'Tell me about a mistake you made and what you learned.', t: 'Own it, explain what you did to fix it, and say what you do differently now.' },
    { c: 'Tell me about a time…', q: 'Tell me about a time you went above and beyond.', t: 'Choose an example where you took initiative without being asked, and end with the result.' },
    { c: 'Tell me about a time…', q: 'Tell me about a time you had to learn something quickly.', t: 'Show how fast you adapt: what you had to learn, how you did it, and what happened next.' },
    // Situational
    { c: 'What would you do if…', q: 'What would you do if you disagreed with your manager?', t: 'Show respect: you would listen, share your view calmly with facts, then follow the final decision.' },
    { c: 'What would you do if…', q: 'What would you do if you were given two urgent tasks at once?', t: 'Explain how you prioritise (deadline, impact), and that you would communicate with your manager early.' },
    { c: 'What would you do if…', q: 'What would you do if you did not know the answer to a customer\'s question?', t: 'Be honest, find out, and follow up. Guessing is the wrong answer.' },
    { c: 'What would you do if…', q: 'What would you do if you noticed a colleague breaking a rule?', t: 'Show integrity and tact: raise it with them or the right person, and focus on the facts.' },
    // Motivation and practical
    { c: 'Motivation & practical', q: 'What motivates you at work?', t: 'Be honest and link it to the role: helping people, solving problems, learning, or growing.' },
    { c: 'Motivation & practical', q: 'Why did you leave your last job, or why are you looking now?', t: 'Stay positive. Focus on what you are moving towards, not what you are running from.' },
    { c: 'Motivation & practical', q: 'How would your last manager or lecturer describe you?', t: 'Use two or three words with a short example, and keep it genuine.' },
    { c: 'Motivation & practical', q: 'Are you willing to work shifts, overtime or travel?', t: 'Be honest about what you can do. If it\'s a yes, say so clearly. If there are limits, state them politely.' },
    { c: 'Motivation & practical', q: 'What are your salary expectations?', t: 'Research the typical range for the role first. Give a range, and say you are open to discussion.' },
    // Closing
    { c: 'Your questions for them', q: 'Do you have any questions for us?', t: 'Always have two. Try: "What does success look like in this role in the first 3 months?" or "What do you enjoy most about working here?"' },
    { c: 'Your questions for them', q: 'Is there anything else you would like us to know?', t: 'Use this to add one strength you didn\'t get to mention, and say that you are keen on the role.' }
  ];

  var chipsHost = document.getElementById('ipChips');
  if (!chipsHost) return;
  var catEl = document.getElementById('ipCat'), qEl = document.getElementById('ipQ'), tipEl = document.getElementById('ipTip');
  var timerEl = document.getElementById('ipTimer'), startBtn = document.getElementById('ipStart');
  var nextBtn = document.getElementById('ipNext'), doneBtn = document.getElementById('ipDone'), countEl = document.getElementById('ipCount');

  var cats = ['All'];
  QS.forEach(function (x) { if (cats.indexOf(x.c) < 0) cats.push(x.c); });
  var active = 'All', pool = [], cur = null, practised = {}, timer = null, left = 120;

  function chip(label) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'ip-chip' + (label === 'All' ? ' active' : '');
    b.textContent = label;
    b.addEventListener('click', function () {
      active = label;
      Array.prototype.forEach.call(chipsHost.children, function (c) { c.classList.toggle('active', c === b); });
      next();
    });
    return b;
  }
  cats.forEach(function (c) { chipsHost.appendChild(chip(c)); });

  function fmt(s) { var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }

  function stopTimer() {
    if (timer) { clearInterval(timer); timer = null; }
    left = 120;
    timerEl.textContent = fmt(left);
    timerEl.classList.remove('ip-timer-low');
    startBtn.textContent = 'Start 2-minute answer';
  }

  function show(item) {
    cur = item;
    catEl.textContent = item.c;
    qEl.textContent = item.q;
    tipEl.textContent = 'Tip: ' + item.t;
    doneBtn.textContent = practised[item.q] ? '✓ Practised' : '✓ Mark as practised';
    stopTimer();
  }

  function next() {
    var list = QS.filter(function (x) { return active === 'All' || x.c === active; });
    if (!pool.length || pool.filter(function (x) { return list.indexOf(x) >= 0; }).length === 0) pool = list.slice();
    pool = pool.filter(function (x) { return list.indexOf(x) >= 0 && x !== cur; });
    if (!pool.length) pool = list.filter(function (x) { return x !== cur; });
    if (!pool.length) pool = list.slice();
    var i = Math.floor(Math.random() * pool.length);
    var item = pool.splice(i, 1)[0];
    show(item);
  }

  startBtn.addEventListener('click', function () {
    if (timer) { stopTimer(); return; }
    startBtn.textContent = 'Stop';
    timer = setInterval(function () {
      left -= 1;
      timerEl.textContent = fmt(left);
      if (left <= 20) timerEl.classList.add('ip-timer-low');
      if (left <= 0) { stopTimer(); timerEl.textContent = 'Time!'; }
    }, 1000);
  });
  nextBtn.addEventListener('click', next);
  doneBtn.addEventListener('click', function () {
    if (!cur) return;
    practised[cur.q] = true;
    doneBtn.textContent = '✓ Practised';
    var n = Object.keys(practised).length;
    countEl.textContent = n + ' of ' + QS.length + ' practised';
  });

  countEl.textContent = '0 of ' + QS.length + ' practised';
  next();
})();
