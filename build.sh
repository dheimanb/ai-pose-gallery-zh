#!/usr/bin/env bash
# Assemble the Cloudflare Pages publish directory dist/ from the repo root.
# The site is static: no generation step. Only files the site serves are copied.
set -euo pipefail
cd "$(dirname "$0")"

DST="${DST:-dist}"
rm -rf "$DST"
mkdir -p "$DST"

cp index.html _headers "$DST/"
[ -f robots.txt ] && cp robots.txt "$DST/"
[ -f sitemap.xml ] && cp sitemap.xml "$DST/"
[ -f og-cover.jpg ] && cp og-cover.jpg "$DST/"
for d in data img thumbs; do
  [ -d "$d" ] && cp -R "$d" "$DST/"
done

echo "dist ready: $DST"
du -sh "$DST"
find "$DST" -type f | wc -l
