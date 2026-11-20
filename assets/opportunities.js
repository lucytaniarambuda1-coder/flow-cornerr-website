(function () {
  var grid = document.getElementById('oppGrid');
  if (!grid) return;

  // The list is managed from /admin/. If the live list can't be loaded, the page keeps the
  // cards that were built into the HTML, so it always works.
  function loadLive() {
    if (!window.fetch) return Promise.resolve(null);
    var ctl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctl) ctl.abort(); }, 4000);
    return fetch('/api/jobs', { signal: ctl ? ctl.signal : undefined })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { return d && Array.isArray(d.items) && d.items.length ? d.items : null; })
      .catch(function () { return null; })
      .then(function (items) { clearTimeout(timer); return items; });
  }

  function node(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function renderLive(items) {
    var types = [], provinces = [];
    grid.textContent = '';
    items.forEach(function (it) {
      var prov = it.province || 'National';
      if (types.indexOf(it.type) < 0) types.push(it.type);
      if (provinces.indexOf(prov) < 0) provinces.push(prov);
      var label = it.closing ? 'Closes ' + it.closing : 'Always open';
      var a = node('article', 'opp-card reveal visible');
      a.setAttribute('data-type', it.type);
      a.setAttribute('data-province', prov);
      a.setAttribute('data-closing', it.closing || '');
      a.setAttribute('data-text', (it.title + ' ' + it.org + ' ' + it.desc + ' ' + (it.tags || []).join(' ')).toLowerCase());
      var top = node('div', 'opp-top');
      top.appendChild(node('span', 'opp-type', it.type));
      var close = node('span', 'opp-close', label);
      close.setAttribute('data-label', label);
      top.appendChild(close);
      a.appendChild(top);
      a.appendChild(node('h3', 'opp-title', it.title));
      a.appendChild(node('div', 'opp-org', it.org + ' · ' + prov));
      a.appendChild(node('p', 'opp-desc', it.desc));
      var link = node('a', 'opp-link', (it.cta || 'Visit the official page') + ' →');
      if (/^https?:\/\//i.test(it.url)) link.href = it.url;
      link.target = '_blank';
      link.rel = 'noopener';
      a.appendChild(link);
      grid.appendChild(a);
    });

    types.sort();
    var chipBox = document.getElementById('oppChips');
    if (chipBox) {
      chipBox.textContent = '';
      var all = node('button', 'ip-chip active', 'All');
      all.type = 'button'; all.setAttribute('data-type', '');
      chipBox.appendChild(all);
      types.forEach(function (t) {
        var b = node('button', 'ip-chip', t);
        b.type = 'button'; b.setAttribute('data-type', t);
        chipBox.appendChild(b);
      });
    }

    provinces.sort();
    var sel = document.getElementById('oppProvince');
    if (provinces.length > 1) {
      if (!sel) {
        sel = document.createElement('select');
        sel.id = 'oppProvince';
        sel.setAttribute('aria-label', 'Province');
        var box = document.querySelector('.opp-filters');
        if (box) box.appendChild(sel);
      }
      sel.textContent = '';
      var first = node('option', null, 'All provinces'); first.value = '';
      sel.appendChild(first);
      provinces.forEach(function (p) { var o = node('option', null, p); o.value = p; sel.appendChild(o); });
    } else if (sel) {
      sel.parentNode.removeChild(sel);
    }
  }

  function setup() {
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.opp-card'));
    var search = document.getElementById('oppSearch');
    var province = document.getElementById('oppProvince');
    var chips = document.querySelectorAll('#oppChips .ip-chip');
    var countEl = document.getElementById('oppCount');
    var emptyEl = document.getElementById('oppEmpty');
    var type = '';

    var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var today = new Date(); today.setHours(0, 0, 0, 0);

    // Time-bound listings: hide once closed, flag when closing within 7 days, show a readable date.
    cards.forEach(function (c) {
      var iso = c.getAttribute('data-closing');
      if (!iso) return;
      var d = new Date(iso + 'T00:00:00');
      if (isNaN(d)) return;
      var days = Math.round((d - today) / 86400000);
      var label = c.querySelector('.opp-close');
      if (days < 0) { c.setAttribute('data-expired', '1'); return; }
      label.textContent = (days === 0 ? 'Closes today' : 'Closes ' + d.getDate() + ' ' + MONTHS[d.getMonth()]);
      if (days <= 7) label.classList.add('opp-soon');
    });

    // Closing-soonest first, always-open last.
    cards.sort(function (a, b) {
      var x = a.getAttribute('data-closing') || '9999', y = b.getAttribute('data-closing') || '9999';
      return x < y ? -1 : x > y ? 1 : 0;
    }).forEach(function (c) { grid.appendChild(c); });

    function apply() {
      var q = (search.value || '').trim().toLowerCase();
      var p = province ? province.value : '';
      var shown = 0;
      cards.forEach(function (c) {
        var ok = !c.getAttribute('data-expired') &&
          (!type || c.getAttribute('data-type') === type) &&
          (!p || c.getAttribute('data-province') === p || c.getAttribute('data-province') === 'National') &&
          (!q || c.getAttribute('data-text').indexOf(q) >= 0);
        c.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      countEl.textContent = shown + (shown === 1 ? ' opportunity' : ' opportunities');
      emptyEl.style.display = shown ? 'none' : 'block';
    }

    Array.prototype.forEach.call(chips, function (b) {
      b.addEventListener('click', function () {
        type = b.getAttribute('data-type') || '';
        Array.prototype.forEach.call(chips, function (x) { x.classList.toggle('active', x === b); });
        apply();
      });
    });
    search.addEventListener('input', apply);
    if (province) province.addEventListener('change', apply);
    apply();
  }

  loadLive().then(function (items) {
    if (items) renderLive(items);
    setup();
  });
})();
