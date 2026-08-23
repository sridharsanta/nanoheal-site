#!/usr/bin/env python3
"""
Local preview server with save-back.

    python3 serve.py          →  http://localhost:8000

Serves the built site, and accepts edits from the in-page editor: press E in
the browser, click a block, type, and the change is written back into pages.py
and the site rebuilt. LOCAL ONLY — never deploy this; GitHub Pages serves the
static files and ignores this file entirely.

Each save writes pages.py.bak first, so the last edit is always recoverable.
"""
import http.server
import json
import re
import socketserver
import subprocess
import sys
import shutil
import pathlib

ROOT = pathlib.Path(__file__).parent.resolve()
SRC = ROOT / "pages.py"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

# Characters the source may carry as HTML entities. When matching the browser's
# view of the text against the Python source, either form has to count.
ENTS = {
    "—": ["&mdash;"], "–": ["&ndash;"], "·": ["&middot;"],
    "→": ["&rarr;"], "←": ["&larr;"], "…": ["&hellip;"],
    "’": ["&rsquo;", "&#39;"], "‘": ["&lsquo;"],
    "“": ["&ldquo;"], "”": ["&rdquo;"],
    "™": ["&trade;"], " ": ["&nbsp;"],
    "&": ["&amp;"], "<": ["&lt;"], ">": ["&gt;"],
}


_TAGWILD = r'(?:\s*</?(?:div|span)\b[^>]*>\s*)?'


def pattern_for(fragment):
    """Whitespace-, entity- and wrapper-tolerant regex for an HTML fragment.

    A \\0 in `fragment` (from clean_for_match's div/span stripping) becomes an
    optional match for ONE div/span wrapper tag, rather than requiring its
    absence -- the source may legitimately have one there (e.g. a highlighted
    <span class="q">) even though clean_for_match removed it from the text
    being compared. Each \\0 gets its own group rather than collapsing
    consecutive ones into a single repeated (`*`) group: a repeated group can
    match a whole *chain* of unrelated adjacent tags in the source (e.g.
    </div><div class="x"><div class="y"><span class="z">), pulling the match
    start back into a previous, untouched element and deleting it on splice.
    One bounded group per stripped tag means the match can never reach back
    further than the number of tags actually stripped from `before`.
    """
    out = []
    for ch in fragment:
        if ch == "\x00":
            out.append(_TAGWILD)
        elif ch.isspace():
            if out and out[-1] == r"\s+":
                continue
            out.append(r"\s+")
        elif ch in ENTS:
            alts = [re.escape(ch)] + [re.escape(e) for e in ENTS[ch]]
            out.append("(?:" + "|".join(alts) + ")")
        else:
            out.append(re.escape(ch))
    return re.compile("".join(out))


def clean(html):
    """Strip what contenteditable tends to inject. Used for the replacement
    text that actually gets written into pages.py, so div/span wrappers and
    editor-only attributes are dropped outright here."""
    html = re.sub(r"<br\s*/?>", " ", html)
    html = re.sub(r"</?(div|span)(\s[^>]*)?>", "", html)
    html = re.sub(r'\s(style|class|data-dm|contenteditable|spellcheck)="[^"]*"', "", html)
    return re.sub(r"[ \t]+", " ", html).strip()


def clean_for_match(html):
    """Like clean(), but marks stripped div/span wrappers with a \\0 sentinel
    instead of deleting them outright, so pattern_for() can treat them as
    optional. Only editor-only attributes (contenteditable/spellcheck/data-dm)
    get dropped here -- class/style on a surviving tag (an icon's <svg
    class="..."> for instance) is kept, since the source is expected to carry
    that attribute verbatim."""
    html = re.sub(r"<br\s*/?>", " ", html)
    html = re.sub(r"</?(div|span)(\s[^>]*)?>", "\x00", html)
    html = re.sub(r'\s(contenteditable|spellcheck|data-dm)="[^"]*"', "", html)
    return re.sub(r"[ \t]+", " ", html).strip()


def apply_edit(before, after):
    src = SRC.read_text(encoding="utf-8")
    pat = pattern_for(clean_for_match(before))
    hits = list(pat.finditer(src))
    if len(hits) == 0:
        return False, ("Couldn't find that block in pages.py — it probably contains "
                       "markup the editor rewrote. Copy its code instead and ask in chat.")
    if len(hits) > 1:
        return False, ("That exact text appears %d times in pages.py, so saving would be "
                       "ambiguous. Ask in chat and name the page." % len(hits))
    shutil.copyfile(SRC, SRC.with_suffix(".py.bak"))
    m = hits[0]
    SRC.write_text(src[:m.start()] + clean(after) + src[m.end():], encoding="utf-8")
    r = subprocess.run([sys.executable, "build.py"], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        shutil.copyfile(SRC.with_suffix(".py.bak"), SRC)
        return False, "Build failed, change reverted:\n" + (r.stderr or "")[:400]
    return True, "Saved to pages.py and rebuilt."


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def _json(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/__save":
            return self._json(404, {"ok": False, "error": "no such endpoint"})
        if self.client_address[0] not in ("127.0.0.1", "::1"):
            return self._json(403, {"ok": False, "error": "local requests only"})
        try:
            n = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(n) or b"{}")
            ok, msg = apply_edit(data.get("before", ""), data.get("after", ""))
            print(("  saved: " if ok else "  REJECTED: ") + msg.split("\n")[0])
            return self._json(200 if ok else 409, {"ok": ok, "message": msg})
        except Exception as e:      # noqa: BLE001 - surfaced to the browser
            return self._json(500, {"ok": False, "error": repr(e)})

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        if args and "__save" in str(args[0]):
            super().log_message(fmt, *args)


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    subprocess.run([sys.executable, "build.py"], cwd=ROOT)
    print("\n  Nanoheal preview  →  http://localhost:%d" % PORT)
    print("  Press E in the browser to edit. Ctrl-C to stop.\n")
    with Server(("127.0.0.1", PORT), Handler) as s:
        try:
            s.serve_forever()
        except KeyboardInterrupt:
            print("\n  stopped\n")
