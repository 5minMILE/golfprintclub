"""
Deploy one or more theme assets to the live Golf Print Club theme.

USAGE:
    cd "/Users/parkerdewey/Desktop/Claude Skills/Golf Print Club/seo-toolkit"
    python3 deploy.py sections/section-poster-bundle.liquid templates/page.poster-bundle.json ...

Paths are relative to the theme root ("../theme").
Reads creds from .env (copy .env.template to .env and fill in once Shopify is set up).
"""
import json, urllib.request, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
THEME_ROOT = os.path.abspath(os.path.join(HERE, '..', 'theme'))

ENV = {}
env_path = os.path.join(HERE, '.env')
if not os.path.exists(env_path):
    print("ERROR: .env not found. Copy .env.template to .env and fill in your Shopify credentials.")
    sys.exit(1)
with open(env_path) as f:
    for line in f:
        if '=' in line and not line.startswith('#'):
            k, v = line.strip().split('=', 1); ENV[k.strip()] = v.strip()
SHOP = ENV['SHOPIFY_DOMAIN']
THEME_ID = ENV['THEME_ID']

def get_token():
    body = json.dumps({'client_id': ENV['SHOPIFY_CLIENT_ID'], 'client_secret': ENV['SHOPIFY_CLIENT_SECRET'], 'grant_type': 'client_credentials'}).encode()
    req = urllib.request.Request(f'https://{SHOP}/admin/oauth/access_token', data=body, headers={'Content-Type': 'application/json'}, method='POST')
    return json.loads(urllib.request.urlopen(req).read())['access_token']

TOKEN = get_token()

def deploy(key):
    path = os.path.join(THEME_ROOT, key)
    with open(path) as f:
        value = f.read()
    payload = json.dumps({'asset': {'key': key, 'value': value}}).encode()
    req = urllib.request.Request(f'https://{SHOP}/admin/api/2024-10/themes/{THEME_ID}/assets.json',
        data=payload, headers={'Content-Type': 'application/json', 'X-Shopify-Access-Token': TOKEN}, method='PUT')
    res = json.loads(urllib.request.urlopen(req).read())
    print(f"  deployed {key} -> live @ {res['asset']['updated_at']}")

if __name__ == '__main__':
    keys = sys.argv[1:]
    if not keys:
        print("usage: python3 deploy.py <asset-key> [<asset-key> ...]"); sys.exit(1)
    for k in keys:
        deploy(k)
    print(f"Done ({len(keys)} asset(s)).")
