javascript: (function () {
  for (let elem of document.querySelectorAll("html, body")) {
    elem.style.setProperty("touch-action", "auto", "important");
  }
})();
