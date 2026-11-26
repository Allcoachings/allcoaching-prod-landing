/* /tutorials: mark episodes not yet released, and play the picked episode in the main player */
(function () {
  var d = document, now = Date.now();
  [].forEach.call(d.querySelectorAll('.tu-ep'), function (li) {
    var up = Date.parse(li.getAttribute('data-up'));
    if (up && up > now && !li.hasAttribute('data-live')) li.classList.add('soon');
  });
  // capture phase: runs before the shared switcher in x.js
  d.addEventListener('click', function (e) {
    var b = e.target.closest('.tu-play'); if (!b) return;
    var li = b.closest('.tu-ep');
    if (li.classList.contains('soon')) { e.stopImmediatePropagation(); e.preventDefault(); li.classList.add('nudge'); setTimeout(function () { li.classList.remove('nudge'); }, 600); return; }
    var ep = b.getAttribute('data-ep');
    setTimeout(function () {
      var main = d.querySelector('.xyt');
      if (!main) return;
      d.querySelector('.tu-player').scrollIntoView({behavior: 'smooth', block: 'center'});
      [].forEach.call(d.querySelectorAll('.tu-ep'), function (x) { x.classList.toggle('on', x === li); });
      var cap = d.querySelector('.tu-now span'); if (cap) cap.textContent = 'Now playing · EP ' + ep;
      main.click();
    }, 30);
  }, true);
})();
