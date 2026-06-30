# Golf Print Club — Shopify Theme

This repo IS the Shopify theme. Theme folders (`assets`, `config`, `layout`, `locales`, `sections`, `snippets`, `templates`) live at the root so Shopify's GitHub integration can connect directly to this repo.

Forked from Run Culture's Broadcast-based theme and rebranded for golf posters.

## Connect this repo to Shopify (one-time setup)

1. Spin up the Shopify store (`golfprintclub.myshopify.com`, $39/mo basic plan).
2. In Shopify Admin → **Online Store → Themes** → **Add theme** → **Connect from GitHub**.
3. Authorize Shopify to access GitHub (one-time).
4. Pick the repo: `5minMILE/golfprintclub`. Branch: `main`.
5. Shopify imports the theme. Set it as a preview (NOT live) initially.
6. From this point on, every `git push` to main auto-syncs into Shopify. No manual zips.

## What you still need to do post-connection

1. Upload golf hero images via theme editor (current image refs point at Run Culture's CDN)
2. Create the `golf-posters` collection in Shopify Admin
3. Add golf poster products (via Gelato POD)
4. Set up the `B2G1FREE` automatic discount (Buy X get Y, 3 posters, cheapest free, scoped to `golf-posters` collection)
5. Replace logo + favicon
6. Hide apparel-specific collection templates (`collection.main-running.json`, `collection.layer-1.json`, etc.) that won't render on a poster-only store
7. Update "About" / "Our Story" page with golf-specific founder narrative
8. Update social media handles in footer (currently `@golfprintclub` but those handles need to be created on IG/TikTok/etc.)

## Repo layout

```
.                                  ← repo root (= Shopify theme root)
├── assets/                        — CSS, JS, SVG icons, images
├── config/                        — theme settings schema + data
├── layout/                        — theme.liquid wrapper
├── locales/                       — translations
├── sections/                      — Liquid sections (including custom golf ones)
├── snippets/                      — reusable Liquid fragments
├── templates/                     — page templates (JSON + Liquid)
│
├── CLAUDE.md                      — Claude's project context
├── README.md                      — this file
└── _meta/                         — non-theme files (Shopify ignores)
    ├── seo-toolkit/               — deploy script (legacy, mostly unused now that GitHub is the deploy path)
    │   ├── deploy.py
    │   └── .env.template
    ├── designs/                   — Higgsfield poster artwork (TBD)
    └── Knowledge Base/            — brand docs (TBD)
```

## Iteration workflow

Once Shopify is connected to this repo:

1. Claude (or you) makes changes locally
2. `git push origin main`
3. Shopify auto-syncs within ~30 seconds
4. Refresh the preview theme to see the change

You no longer need to manually zip or upload. The repo IS the source of truth.
