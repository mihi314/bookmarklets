javascript: (function () {
  for (let elem of document.querySelectorAll("iframe")) {
    elem.parentNode.removeChild(elem);
  }
})();
