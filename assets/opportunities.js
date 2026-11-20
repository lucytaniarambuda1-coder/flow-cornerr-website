(function () {
  var grid = document.getElementById('oppGrid');
  if (!grid) return;
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
})();
