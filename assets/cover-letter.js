(function () {
  var out = document.getElementById('clOutput');
  if (!out) return;
  function v(id) { return document.getElementById(id).value.trim(); }
  function cap(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }

  function today() {
    try {
      return new Date().toLocaleDateString('en-ZA', { day: 'numeric', month: 'long', year: 'numeric' });
    } catch (e) { return ''; }
  }

  function make() {
    var name = v('c_name'), contact = v('c_contact'), who = v('c_who');
    var role = v('c_role') || 'the advertised',
        company = v('c_company'), manager = v('c_manager'), source = v('c_source'), why = v('c_why');
    var wins = [v('c_a1'), v('c_a2'), v('c_a3')].filter(Boolean);

    var L = [];
    if (name) L.push(name);
    if (contact) L.push(contact);
    if (name || contact) L.push('');
    var d = today();
    if (d) { L.push(d); L.push(''); }

    L.push(manager ? 'Dear ' + manager + ',' : 'Dear Hiring Manager,');
    L.push('');
    L.push('Application for ' + role + ' position' + (company ? ' at ' + company : ''));
    L.push('');

    var first = 'I am writing to apply for the ' + role + ' position' + (company ? ' at ' + company : '');
    if (source) first += ', which I saw advertised on ' + source;
    first += '.';
    if (who) first += ' I am ' + who.replace(/^(i am|i'm)\s+/i, '').replace(/\.$/, '') + ', and I believe my background makes me a strong fit for this role.';
    else first += ' I believe my skills and experience make me a strong fit for this role.';
    L.push(first);
    L.push('');

    if (wins.length) {
      L.push('Here is some of what I would bring to your team:');
      wins.forEach(function (w) { L.push('• ' + cap(w.replace(/^[•\-*\s]+/, '').replace(/\.$/, '')) + '.'); });
      L.push('');
    }

    if (why) {
      L.push(cap(why.replace(/^[•\-*\s]+/, '')) + (/[.!?]$/.test(why) ? '' : '.'));
      L.push('');
    }

    L.push('I would welcome the opportunity to discuss how I can contribute' + (company ? ' to ' + company : '') + '. Thank you for your time and consideration. I look forward to hearing from you.');
    L.push('');
    L.push(manager ? 'Yours sincerely,' : 'Yours faithfully,');
    L.push(name || '[Your name]');

    out.value = L.join('\n');
    out.focus();
  }

  document.getElementById('clMake').addEventListener('click', make);

  var copied = document.getElementById('clCopied');
  function flash(msg) {
    copied.textContent = msg;
    setTimeout(function () { copied.textContent = ''; }, 2500);
  }
  document.getElementById('clCopy').addEventListener('click', function () {
    if (!out.value.trim()) { flash('Write your letter first.'); return; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(out.value).then(function () { flash('Copied!'); }, function () { out.select(); flash('Press Ctrl/Cmd+C to copy.'); });
    } else {
      out.select();
      flash('Press Ctrl/Cmd+C to copy.');
    }
  });

  document.getElementById('clPrint').addEventListener('click', function () {
    if (!out.value.trim()) { flash('Write your letter first.'); return; }
    window.print();
  });
  window.addEventListener('beforeprint', function () {
    document.getElementById('clPrint_div').textContent = out.value;
    document.body.classList.add('print-cl');
  });
  window.addEventListener('afterprint', function () { document.body.classList.remove('print-cl'); });
})();
