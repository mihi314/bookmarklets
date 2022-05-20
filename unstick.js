javascript: (function () {
  let elements = document.querySelectorAll("body *");
  for (let i = 0; i < elements.length; i++) {
    const style = getComputedStyle(elements[i]);
    if (style.position === "fixed" || style.position === "sticky") {
      elements[i].parentNode.removeChild(elements[i]);
    }
  }
  document.querySelector("html").style.overflow = "visible";
  document.querySelector("body").style.overflow = "visible";
})();
