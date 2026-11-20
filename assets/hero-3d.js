(function () {
  var hero = document.querySelector('.hero');
  var stack = document.getElementById('heroStack');
  if (!hero || !stack || !window.matchMedia) return;
  // Subtle mouse tilt on laptops only; skipped for touch, small screens and reduced-motion users.
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (window.matchMedia('(max-width: 900px)').matches) return;
  if (!window.matchMedia('(hover: hover)').matches) return;
  hero.addEventListener('mousemove', function (e) {
    var r = hero.getBoundingClientRect();
    var x = (e.clientX - r.left) / r.width - 0.5;
    var y = (e.clientY - r.top) / r.height - 0.5;
    stack.style.setProperty('--ry', (-9 + x * 9).toFixed(2) + 'deg');
    stack.style.setProperty('--rx', (4 - y * 7).toFixed(2) + 'deg');
  });
  hero.addEventListener('mouseleave', function () {
    stack.style.removeProperty('--ry');
    stack.style.removeProperty('--rx');
  });
})();
