javascript: (function () {
  for (let elem of document.querySelectorAll("body *")) {
    const style = getComputedStyle(elem);
    if (style.position === "fixed" || style.position === "sticky") {
      elem.parentNode.removeChild(elem);
    }
  }
  for (let elem of document.querySelectorAll("html, body")) {
    elem.style.setProperty("overflow", "visible", "important");
    elem.style.setProperty("position", "static", "important");
  }
})();
