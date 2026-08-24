/* ─────────────────────────────────────────────────────────────────────────
   Edit-mode overlay — LOCAL PREVIEW ONLY.

   Self-gates to localhost / 127.0.0.1 / file:// (or an explicit ?edit=1),
   so it stays inert on nanoheal.com and on GitHub Pages. Nothing it does
   touches the page's own markup or styling.

   Press E to toggle. Click any outlined block to copy its code + text,
   then paste that into the chat so the exact block is unambiguous.
   ───────────────────────────────────────────────────────────────────────── */
(function () {
  var host = location.hostname;
  var local = host === "localhost" || host === "127.0.0.1" ||
              host === "" || host === "[::1]";
  var forced = /[?&]edit=1\b/.test(location.search);
  if (!local && !forced) return;

  var SEL = [
    "h1", "h2", "h3",
    "p.lede", "p.sub", "p.lead", "p.note", "p.fine", ".pull",
    ".prose p", ".prose ul",
    ".tile", ".pane", ".cap", ".st", ".badge", ".verdict",
    ".ps > div", ".loop-legend > div", ".linkrow", ".next a",
    "table.spec tbody tr", ".chip", ".btn", ".loop",
    ".scope-glabel", ".scope-card-text", ".scope-pill", ".scope-stat-label", ".scope-bracket span",
    ".os-cap-title", ".os-cap-desc", ".sig-step", ".chain-node"
  ].join(",");

  var on = false, marks = [], toast;

  function sectionKey(el) {
    var s = el.closest("section, .trust, footer, header");
    if (!s) return "PAGE";
    if (s.id) return s.id.toUpperCase().replace(/[^A-Z0-9]+/g, "");
    if (s.tagName === "FOOTER") return "FOOTER";
    if (s.tagName === "HEADER") return "NAV";
    if (s.classList.contains("trust")) return "PROOF";
    if (s.classList.contains("phero")) return "HERO";
    var all = [].slice.call(document.querySelectorAll("section"));
    return "SEC" + (all.indexOf(s) + 1);
  }

  function pageKey() {
    var p = location.pathname.replace(/\/index\.html$/, "").replace(/^\/|\/$/g, "");
    if (!p) return "home";
    return p.split("/").pop();
  }

  function label(el) {
    var t = (el.innerText || "").trim().replace(/\s+/g, " ");
    return t.length > 70 ? t.slice(0, 70) + "…" : t;
  }

  function build() {
    clear();
    var counts = {};
    var els = [].slice.call(document.querySelectorAll(SEL));
    els.forEach(function (el) {
      if (el.closest(".dm-ui")) return;
      var r = el.getBoundingClientRect();
      if (r.width < 12 || r.height < 8) return;
      var k = sectionKey(el);
      counts[k] = (counts[k] || 0) + 1;
      var code = k + "-" + counts[k];
      el.setAttribute("data-dm", code);

      var box = document.createElement("div");
      box.className = "dm-box dm-ui";
      box.style.cssText =
        "position:absolute;pointer-events:auto;cursor:pointer;z-index:2147483000;" +
        "border:1px dashed rgba(4,115,126,.55);border-radius:3px;" +
        "left:" + (r.left + scrollX - 2) + "px;top:" + (r.top + scrollY - 2) + "px;" +
        "width:" + (r.width + 4) + "px;height:" + (r.height + 4) + "px;";

      var tag = document.createElement("span");
      tag.textContent = code;
      // Flip the badge below the block when it would clip off the top edge.
      var flip = (r.top < 20);
      tag.style.cssText =
        "position:absolute;left:-1px;" + (flip ? "top:100%;" : "top:-15px;") + "font:500 10px/14px ui-monospace,Menlo,monospace;" +
        "letter-spacing:.04em;background:#04737E;color:#fff;padding:0 5px;border-radius:2px;" +
        "white-space:nowrap;pointer-events:none;";
      box.appendChild(tag);

      box.addEventListener("mouseenter", function () {
        box.style.background = "rgba(4,115,126,.10)";
        box.style.borderStyle = "solid";
      });
      box.addEventListener("mouseleave", function () {
        box.style.background = "transparent";
        box.style.borderStyle = "dashed";
      });
      box.addEventListener("click", function (e) {
        e.preventDefault(); e.stopPropagation();
        if (e.altKey) {
          copy("[" + pageKey() + " · " + code + "] " + label(el));
          say("Copied  " + code + "  — paste it into the chat");
          return;
        }
        edit(el, code, box);
      });

      document.body.appendChild(box);
      marks.push(box);
    });
    say("Edit mode — " + marks.length + " blocks. Click to edit · Alt-click copies a code · E exits");
  }


  /* ── inline editing ─────────────────────
     Click a block to edit it in place. The original innerHTML is kept so the
     save endpoint can locate that exact fragment inside pages.py. Enter (or
     clicking away) saves; Escape cancels; Alt-click copies the code instead. */
  var active = null;

  function edit(el, code, box) {
    if (active) { finish(true); }
    var before = el.innerHTML;
    active = { el: el, code: code, before: before, box: box };

    clear();                       // outlines would sit on top of the caret
    el.setAttribute("contenteditable", "true");
    el.setAttribute("spellcheck", "true");
    el.style.outline = "2px solid #04737E";
    el.style.outlineOffset = "3px";
    el.style.borderRadius = "3px";
    el.focus();

    var sel = window.getSelection();
    if (sel && sel.rangeCount === 0) {
      var r = document.createRange();
      r.selectNodeContents(el); r.collapse(false); sel.addRange(r);
    }
    say("Editing " + code + " — Enter saves, Esc cancels");

    el.addEventListener("keydown", onKeys);
    el.addEventListener("blur", onBlur);
  }

  function onKeys(e) {
    if (e.key === "Escape") { e.preventDefault(); finish(false); }
    else if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); finish(true); }
    e.stopPropagation();           // so typing "e" doesn't toggle edit mode
  }
  function onBlur() { if (active) finish(true); }

  function finish(save) {
    if (!active) return;
    var a = active; active = null;
    a.el.removeEventListener("keydown", onKeys);
    a.el.removeEventListener("blur", onBlur);
    a.el.removeAttribute("contenteditable");
    a.el.removeAttribute("spellcheck");
    a.el.style.outline = ""; a.el.style.outlineOffset = "";

    var after = a.el.innerHTML;
    if (!save || after === a.before) {
      a.el.innerHTML = a.before;
      say(save ? "No change" : "Cancelled");
      if (on) build();
      return;
    }

    say("Saving " + a.code + "…");
    fetch("/__save", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ before: a.before, after: after })
    }).then(function (r) { return r.json(); }).then(function (res) {
      if (res.ok) {
        say("Saved " + a.code + " — reloading");
        setTimeout(function () { location.reload(); }, 350);
      } else {
        a.el.innerHTML = a.before;
        copy("[" + pageKey() + " · " + a.code + "] " + label(a.el));
        say("Couldn't save — code copied, ask in chat. (" +
            (res.message || res.error || "") + ")");
        if (on) build();
      }
    }).catch(function () {
      a.el.innerHTML = a.before;
      say("No save server — run  python3 serve.py  (not http.server)");
      if (on) build();
    });
  }

  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).catch(function () { fallback(text); });
    } else { fallback(text); }
  }
  function fallback(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.cssText = "position:fixed;top:-1000px;left:-1000px;";
    document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (err) {}
    document.body.removeChild(ta);
  }

  function say(msg) {
    if (!toast) {
      toast = document.createElement("div");
      toast.className = "dm-ui";
      toast.style.cssText =
        "position:fixed;left:16px;bottom:16px;z-index:2147483600;max-width:420px;" +
        "font:500 12.5px/1.5 ui-monospace,Menlo,monospace;background:#1A1716;color:#EFEDEB;" +
        "padding:10px 13px;border-radius:4px;box-shadow:0 8px 28px rgba(0,0,0,.35);";
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.display = "block";
    clearTimeout(toast._t);
    toast._t = setTimeout(function () {
      if (on) { toast.textContent = "Edit mode — click to edit · Alt-click copies · E exits"; }
      else { toast.style.display = "none"; }
    }, 2600);
  }

  function clear() {
    marks.forEach(function (m) { m.remove(); });
    marks = [];
  }

  function toggle() {
    on = !on;
    if (on) { build(); }
    else {
      clear();
      if (toast) { toast.textContent = "Edit mode off"; setTimeout(function(){ toast.style.display="none"; }, 1200); }
    }
  }

  var rt;
  function reflow() {
    if (!on) return;
    clearTimeout(rt);
    rt = setTimeout(build, 120);
  }
  addEventListener("resize", reflow);
  addEventListener("scroll", reflow, { passive: true });
  // CSS-only tab panels (.ostabs) change which content is visible without a
  // resize/scroll event, so overlay boxes on the newly-shown panel would
  // otherwise stay stale until the next reflow trigger.
  addEventListener("change", function (e) {
    if (e.target && e.target.name === "ostab") reflow();
  });

  addEventListener("keydown", function (e) {
    if (e.key !== "e" && e.key !== "E") return;
    var t = e.target;
    if (t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.isContentEditable)) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    toggle();
  });

  // Small always-visible hint so the feature is discoverable.
  addEventListener("DOMContentLoaded", function () {
    var hint = document.createElement("div");
    hint.className = "dm-ui";
    hint.textContent = "press E to edit";
    hint.style.cssText =
      "position:fixed;right:14px;bottom:14px;z-index:2147483500;cursor:pointer;" +
      "font:500 11px/1 ui-monospace,Menlo,monospace;letter-spacing:.04em;" +
      "background:rgba(26,23,22,.82);color:#EFEDEB;padding:7px 10px;border-radius:3px;";
    hint.addEventListener("click", toggle);
    document.body.appendChild(hint);
  });
})();
