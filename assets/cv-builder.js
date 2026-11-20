(function () {
  var KEY = 'fc-cv-builder-draft';
  var paper = document.getElementById('cvPaper');
  if (!paper) return;

  var SIMPLE = ['name', 'title', 'email', 'phone', 'loc', 'link', 'summary', 'skills', 'other'];
  var expList = document.getElementById('expList');
  var eduList = document.getElementById('eduList');

  function $(id) { return document.getElementById(id); }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  // ---- dynamic blocks (static markup only; user text is never injected as HTML)
  function addExp(v) {
    v = v || {};
    var b = el('div', 'ft-block');
    b.innerHTML =
      '<div class="ft-row"><label class="ft-field">Job title<input data-k="role" placeholder="Customer Service Agent"></label>' +
      '<label class="ft-field">Company<input data-k="company" placeholder="Company name"></label></div>' +
      '<div class="ft-row"><label class="ft-field">From – To<input data-k="dates" placeholder="Jan 2023 – Present"></label>' +
      '<label class="ft-field">Town (optional)<input data-k="place" placeholder="Johannesburg"></label></div>' +
      '<label class="ft-field">What you did (one bullet per line)<textarea data-k="bullets" rows="4" placeholder="Handled 60+ inbound calls a day&#10;Resolved 92% of queries on first contact"></textarea></label>' +
      '<button type="button" class="ft-remove">Remove this job</button>';
    ['role', 'company', 'dates', 'place', 'bullets'].forEach(function (k) {
      var f = b.querySelector('[data-k="' + k + '"]');
      if (v[k]) f.value = v[k];
    });
    b.querySelector('.ft-remove').addEventListener('click', function () { b.remove(); update(); });
    expList.appendChild(b);
  }

  function addEdu(v) {
    v = v || {};
    var b = el('div', 'ft-block');
    b.innerHTML =
      '<div class="ft-row"><label class="ft-field">Qualification<input data-k="qual" placeholder="National Senior Certificate"></label>' +
      '<label class="ft-field">School / institution<input data-k="school" placeholder="Name of school or college"></label></div>' +
      '<div class="ft-row"><label class="ft-field">Year completed<input data-k="year" placeholder="2021"></label><div></div></div>' +
      '<button type="button" class="ft-remove">Remove</button>';
    ['qual', 'school', 'year'].forEach(function (k) {
      var f = b.querySelector('[data-k="' + k + '"]');
      if (v[k]) f.value = v[k];
    });
    b.querySelector('.ft-remove').addEventListener('click', function () { b.remove(); update(); });
    eduList.appendChild(b);
  }

  function readBlocks(list, keys) {
    return Array.prototype.map.call(list.querySelectorAll('.ft-block'), function (b) {
      var o = {};
      keys.forEach(function (k) { o[k] = b.querySelector('[data-k="' + k + '"]').value.trim(); });
      return o;
    });
  }

  function lines(text) {
    return (text || '').split('\n').map(function (s) { return s.replace(/^[\s\-•*·]+/, '').trim(); }).filter(Boolean);
  }

  function state() {
    var s = {};
    SIMPLE.forEach(function (k) { s[k] = $('f_' + k).value.trim(); });
    s.exp = readBlocks(expList, ['role', 'company', 'dates', 'place', 'bullets']);
    s.edu = readBlocks(eduList, ['qual', 'school', 'year']);
    return s;
  }

  // ---- preview
  function section(title) {
    var s = el('div', 'cvp-section');
    s.appendChild(el('div', 'cvp-heading', title));
    return s;
  }

  function render(s) {
    paper.textContent = '';
    var empty = !s.name && !s.title && !s.summary && !s.skills && !s.exp.some(function (e) { return e.role || e.company; });
    if (empty) {
      paper.appendChild(el('p', 'cvp-placeholder', 'Start typing on the left and your CV appears here.'));
      return;
    }
    paper.appendChild(el('div', 'cvp-name', s.name || 'Your Name'));
    if (s.title) paper.appendChild(el('div', 'cvp-title', s.title));
    var contact = [s.phone, s.email, s.loc, s.link].filter(Boolean).join('  ·  ');
    if (contact) paper.appendChild(el('div', 'cvp-contact', contact));

    if (s.summary) {
      var p = section('Profile');
      p.appendChild(el('p', 'cvp-text', s.summary));
      paper.appendChild(p);
    }
    if (s.skills) {
      var sk = section('Skills');
      var list = s.skills.split(',').map(function (x) { return x.trim(); }).filter(Boolean).join('  ·  ');
      sk.appendChild(el('p', 'cvp-text', list));
      paper.appendChild(sk);
    }
    var exp = s.exp.filter(function (e) { return e.role || e.company || e.bullets; });
    if (exp.length) {
      var ex = section('Work Experience');
      exp.forEach(function (e) {
        var row = el('div', 'cvp-row');
        row.appendChild(el('span', 'cvp-role', [e.role, e.company].filter(Boolean).join(', ')));
        row.appendChild(el('span', 'cvp-dates', e.dates));
        ex.appendChild(row);
        if (e.place) ex.appendChild(el('div', 'cvp-place', e.place));
        var bl = lines(e.bullets);
        if (bl.length) {
          var ul = el('ul', 'cvp-list');
          bl.forEach(function (b) { ul.appendChild(el('li', null, b)); });
          ex.appendChild(ul);
        }
      });
      paper.appendChild(ex);
    }
    var edu = s.edu.filter(function (e) { return e.qual || e.school; });
    if (edu.length) {
      var ed = section('Education & Training');
      edu.forEach(function (e) {
        var row = el('div', 'cvp-row');
        row.appendChild(el('span', 'cvp-role', [e.qual, e.school].filter(Boolean).join(', ')));
        row.appendChild(el('span', 'cvp-dates', e.year));
        ed.appendChild(row);
      });
      paper.appendChild(ed);
    }
    var other = lines(s.other);
    if (other.length) {
      var ot = section('Additional');
      var ul2 = el('ul', 'cvp-list');
      other.forEach(function (b) { ul2.appendChild(el('li', null, b)); });
      ot.appendChild(ul2);
      paper.appendChild(ot);
    }
    var refs = section('References');
    refs.appendChild(el('p', 'cvp-text', 'Available on request.'));
    paper.appendChild(refs);
  }

  // ---- draft storage (this device only)
  function save(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* storage unavailable */ }
  }
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { return null; }
  }

  function update() {
    var s = state();
    render(s);
    save(s);
  }

  // ---- init
  var saved = load();
  if (saved) {
    SIMPLE.forEach(function (k) { if (saved[k]) $('f_' + k).value = saved[k]; });
    (saved.exp || []).forEach(addExp);
    (saved.edu || []).forEach(addEdu);
  }
  if (!expList.children.length) addExp();
  if (!eduList.children.length) addEdu();

  document.getElementById('cbForm').addEventListener('input', update);
  $('addExp').addEventListener('click', function () { addExp(); });
  $('addEdu').addEventListener('click', function () { addEdu(); });
  $('cbPrint').addEventListener('click', function () { window.print(); });
  $('cbClear').addEventListener('click', function () {
    if (!window.confirm('Clear everything you have typed?')) return;
    SIMPLE.forEach(function (k) { $('f_' + k).value = ''; });
    expList.textContent = ''; eduList.textContent = '';
    addExp(); addEdu();
    try { localStorage.removeItem(KEY); } catch (e) { /* ignore */ }
    update();
  });
  window.addEventListener('beforeprint', function () { document.body.classList.add('print-cv'); });
  window.addEventListener('afterprint', function () { document.body.classList.remove('print-cv'); });
  update();
})();
