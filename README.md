# nanoheal-site

Static homepage for Nanoheal. Plain HTML/CSS — no build step, no dependencies.

```
index.html                    the homepage (self-contained; Google Fonts is the only external request)
404.html                      not-found page
sitemap.xml                   XML sitemap — only "/" is live; the rest is commented out
robots.txt
SITEMAP.md                    the information architecture + positioning rationale
.github/workflows/pages.yml   deploys to GitHub Pages on every push to main
```

## Deploying

```bash
git init && git branch -M main
git add -A && git commit -m "Nanoheal homepage"
git remote add origin git@github.com:<org>/nanoheal-site.git
git push -u origin main
```

Then in the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions.**
The workflow runs on push and publishes to `https://<org>.github.io/nanoheal-site/`.

### Custom domain

Add a file named `CNAME` at the repo root containing one line:

```
nanoheal.com
```

Then point DNS at GitHub:

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<org>.github.io` |

Enable **Enforce HTTPS** in Settings → Pages once the certificate is issued (usually
a few minutes; occasionally up to 24 hours).

> Verify these IPs against GitHub's current documentation before you cut DNS over —
> apex records for Pages have changed before.

## Before this becomes the production nanoheal.com

Three things this repo does not solve, in priority order:

1. **Lead capture.** The "Schedule a Demo" buttons are `#demo` anchors. They need to
   point at a real form (HubSpot/Marketo embed, or Calendly) and fire attribution.
   Nothing on this page converts until that is wired.
2. **Editability.** Every copy change is a commit. If marketing needs to revise the
   hero without an engineer, this belongs in a CMS.
3. **Hosting fit.** GitHub's usage limits say Pages "is not intended for or allowed to
   be used as a free web hosting service to run your online business." A SaaS marketing
   site sits in a grey area. Cloudflare Pages / Vercel / Netlify take these exact files,
   cost nothing at this volume, and add branch previews, redirects and form handling.

Use Pages to get the positioning in front of people this week. Decide the real stack
after the messaging has survived a few customer conversations.

## Editing

Everything is in `index.html`. Design tokens are CSS custom properties in the `:root`
block at the top — colour, radius and the light/dark palettes. There are three theme
states to keep in sync: bare `:root` (light), `@media (prefers-color-scheme: dark)`
guarded by `:root:not([data-theme="light"])`, and `:root[data-theme="dark"]`.

The hero's carved-plaster texture is generated in a `<canvas>` at the bottom of the
file — no image asset. Swap it for a real photograph by replacing `<canvas class="plaster">`
with an `<img>`; the reference direction wants a warm stone or plaster relief.
