/* Opens the recorded tour window over the current page. The window is the page /tour-window/ in a full-screen frame;
   it asks to be closed with a message, so nothing else on the page is touched. Any button marked data-ilit-tour-start
   (and window.ilitTour.start()) opens it; Exit, Done and Escape close it again. */
(function () {
  if (window.ilitTour) return;
  var holder = null, frame = null, opener = null, scrollLock = '';

  function build() {
    holder = document.createElement('div');
    holder.id = 'ilitTourWindow';
    holder.setAttribute('role', 'dialog');
    holder.setAttribute('aria-modal', 'true');
    holder.setAttribute('aria-label', 'Site tour');
    holder.style.cssText = 'position:fixed;left:0;top:0;right:0;bottom:0;z-index:2147483000;background:#f1efe8;display:none';
    frame = document.createElement('iframe');
    frame.title = 'Site tour';
    frame.style.cssText = 'position:absolute;left:0;top:0;width:100%;height:100%;border:0;background:#f1efe8';
    holder.appendChild(frame);
    document.body.appendChild(holder);
  }

  function start() {
    if (!holder) build();
    opener = document.activeElement;
    scrollLock = document.documentElement.style.overflow;
    document.documentElement.style.overflow = 'hidden';
    frame.src = '/tour-window/?embed=1';          // a fresh start at step 1 every time
    holder.style.display = 'block';
    frame.focus();
  }

  function exit() {
    if (!holder || holder.style.display === 'none') return;
    holder.style.display = 'none';
    frame.src = 'about:blank';
    document.documentElement.style.overflow = scrollLock;
    if (opener && opener.focus) { try { opener.focus(); } catch (e) {} }
  }

  window.addEventListener('message', function (event) {
    if (event.origin === location.origin && event.data && event.data.ilitTour === 'close') exit();
  });
  document.addEventListener('click', function (event) {
    var button = event.target.closest && event.target.closest('[data-ilit-tour-start]');
    if (button) { event.preventDefault(); start(); }
  });
  window.ilitTour = { start: start, exit: exit };
})();
