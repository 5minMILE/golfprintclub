# Golf Print Club — Launch Checklist

This folder is the scaffold for a Run Culture sibling brand focused on golf posters. Templates are copied and adapted; Shopify store is not yet created.

## What's already done

- Folder structure mirrored from Run Culture.
- `theme/sections/section-wf-hero.liquid` — slideshow hero (same one that runs on Run Culture).
- `theme/sections/section-poster-bundle.liquid` — bundle landing page section (1100+ lines, no edits needed).
- `theme/templates/page.poster-bundle.json` — bundle page template with golf-adapted copy.
- `theme/templates/index.json` — minimal homepage with the slideshow set up for golf.
- `theme/templates/product.poster.json` — poster product template (copy of Run Culture's).
- `seo-toolkit/deploy.py` — same deploy script as RNCLTR, reads creds from `.env`.

## What you do next

### 1. Pick the final brand name

Working name is **Golf Print Club**. If you want to change, pick one and search for:
- Available domain (`golfprintclub.com`, `golfprintclub.co`, `tee-culture.com`, etc.)
- Available IG handle
- Available Shopify subdomain

Alternates I'd accept without argument: **Fore Culture**, **Mulligan Culture**, **The Links Co.**

### 2. Spin up the Shopify store

- Register on shopify.com under the new brand.
- Pick the cheapest plan ($39/mo) for the first 60 days.
- Install the **Broadcast theme** (paid theme, ~$320 one-time) to match Run Culture's foundation. Or duplicate Run Culture's theme via Shopify's theme export/import to save the theme fee.
- Once Broadcast is installed, deploy the custom files in `theme/` on top via `seo-toolkit/deploy.py`.

### 3. Install the custom Shopify app for API access

- Shopify Admin → Settings → Apps → Develop apps → Create app.
- Grant the same scopes as Run Culture's app (read/write products, themes, orders).
- Copy client ID and client secret into `seo-toolkit/.env` (rename `.env.template`).
- Find theme ID (Online Store → Themes → ... → Edit code → URL contains the theme_id).

### 4. Generate posters

- Use Higgsfield (the same workflow as Run Culture's poster designs).
- Save raw outputs to `designs/posters/`.
- Suggested first batch: 10 designs covering the obvious moments and aesthetics. Iconic course shots, equipment art, era-defining moments, identity posters ("Make Your Office Look Like A Clubhouse" style copy).

### 5. Link products to Gelato

- Gelato has a separate store connection per Shopify store. Connect Golf Print Club's Shopify to a new Gelato store.
- Upload poster artwork, set print sizes (12x18, 16x24, 24x36).
- Link to Shopify products.

### 6. Set up the discount + bundle

- Shopify Admin → Discounts → Create automatic discount.
- Buy X get Y, code `B2G1FREE` (matches the LP), 3 posters from the `golf-posters` collection, cheapest free.
- Apply at checkout automatically.

### 7. Set up Meta ad account

- Create new Business Manager ad account scoped to Golf Print Club.
- Install Meta Pixel + Conversions API on the new Shopify store.
- Plan: write off the first $300-500 of spend as pixel warmup. Run the same campaign structure as Run Culture ($50/day CBO, 1 ad set, 10 creatives).

## Deploy commands once Shopify is live

From `/Users/parkerdewey/Desktop/Claude Skills/Golf Print Club/seo-toolkit/`:

```bash
python3 deploy.py sections/section-wf-hero.liquid sections/section-poster-bundle.liquid templates/index.json templates/page.poster-bundle.json templates/product.poster.json
```

## Why these specific copies

- The bundle section is 1100+ lines of working configurator UI. There's no reason to rewrite it. Brand-specific copy is exposed via section settings in the JSON template, not hardcoded in the liquid.
- The hero section is also reused as-is. Slideshow logic is brand-neutral.
- The poster product template (`product.poster.json`) carries the same configurator layout as Run Culture's posters. Just point it at golf products.

## What to skip

- Don't copy the full Run Culture theme. It's ~200 files of Broadcast plus custom sections that won't all be relevant. The minimum custom set is what's already in `theme/`. Everything else comes from a fresh Broadcast install.
- Don't try to make this a separate Shopify Plus store. Basic plan is fine for the experiment.
