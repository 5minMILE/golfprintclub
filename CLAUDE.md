# Golf Print Club — Workspace Context

Owner: Parker Dewey
Business: DTC golf poster brand (parallel experiment to Run Culture)
Status: Pre-launch. Folder scaffolded 2026-06-30.
Shopify: not yet set up

## Why this brand exists

This is a parallel paid-acquisition test, not a separate business. Thesis: the poster machine that Run Culture is testing right now (Higgsfield AI artwork + Gelato POD + Shopify bundle LP + Meta ads at $50/day) should be portable to any high-spend hobby. Golf was chosen first because:

- Older, wealthier demographic than running.
- Strong identity culture (golfers love being golfers).
- Existing wall-art tradition for office/man-cave decor.
- Less competition for original golf art than running.
- Higher AOV tolerance and lower price sensitivity.

If the running posters show ROAS > 1.5x on a winning creative in the next 5-7 days, Golf Print Club launches with high confidence. If running posters don't work, this folder gets shelved.

## What's in this folder

```
Golf Print Club/
├── CLAUDE.md                 — this file
├── README.md                 — what's here, what's next
├── theme/                    — Shopify theme files (custom only, not a full theme)
│   ├── sections/
│   │   ├── section-wf-hero.liquid       — slideshow hero (cross-fade, 2 slides)
│   │   └── section-poster-bundle.liquid — bundle landing page section
│   └── templates/
│       ├── index.json                   — homepage (golf hero + bundle CTA)
│       ├── page.poster-bundle.json      — /pages/buy-2-get-1-free
│       └── product.poster.json          — golf poster product template
├── seo-toolkit/
│   ├── deploy.py                        — copy of the RNCLTR deploy script
│   └── .env.template                    — fill in once Shopify is created
├── designs/posters/                     — Higgsfield-generated artwork lands here
└── Knowledge Base/                      — brand docs, supplier info (TBD)
```

## How to brief a new Claude session

If you're a Claude instance starting fresh in this folder:

1. Read this file first (you already are).
2. Read `README.md` for the launch checklist.
3. The Run Culture sibling project lives at `~/Desktop/Claude Skills/RNCLTR/` and is the source the templates were forked from. Anything generic about the bundle LP, hero, or poster template behaves the same way; only the copy and collection handles change.
4. If the user hasn't set up the Shopify store yet, do NOT try to deploy. Work on theme files locally only.

## Brand identity (draft, not final)

- Voice: irreverent young golf, not country club. Think golf TikTok era, Bryson DeChambeau, Tiger Woods 2.0. Anti-stuffy.
- Tagline (working): "Wall art for golfers who actually play."
- Bundle offer: same as Run Culture. Buy 2, get the cheapest free, code `B2G1FREE` auto-applies.
- Price band: aim for $25-$35 ASP, same range as Run Culture posters.

## What this folder is NOT

- It is NOT a full Shopify theme. It contains only the custom files Run Culture built on top of Broadcast. When the Shopify store is created, install Broadcast first, then deploy these files on top.
- It is NOT a separate business yet. It's a paid-acquisition experiment. Treat operational decisions the same way you'd treat a feature flag, not a brand launch.

## What NOT to recommend

- Don't recommend turning this into a full ecommerce expansion (apparel, accessories, etc.) before the poster ROAS clears 1.5x.
- Don't recommend a separate brand voice document, style guide, or design system. Move fast, copy what works from Run Culture.
- Don't recommend hiring. Solo operation.

## Strategic context

See `~/Desktop/Claude Skills/RNCLTR/CLAUDE.md` for the umbrella business state. Golf Print Club's profitability bar is the same as Run Culture's: positive net contribution after Meta spend and Gelato COGS within 14 days of launch.
