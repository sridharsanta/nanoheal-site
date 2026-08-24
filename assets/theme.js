// Light/dark toggle. The early inline script in <head> applies any saved
// preference before first paint (avoids a flash); this just handles clicks.
(function () {
  var btn = document.getElementById("theme-toggle");
  if (!btn) return;

  function current() {
    var t = document.documentElement.getAttribute("data-theme");
    if (t === "dark" || t === "light") return t;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  btn.addEventListener("click", function () {
    var next = current() === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("nh-theme", next); } catch (e) {}
    // plaster.js redraws its canvas on resize; reuse that hook so the hero
    // texture repaints in the new theme's colours too.
    window.dispatchEvent(new Event("resize"));
  });
})();
