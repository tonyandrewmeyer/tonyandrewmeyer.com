#!/usr/bin/env bash
# Download the media files referenced by posts into static/uploads/.
# Run this from a network that can reach tonyandrewmeyer.com (the Claude web
# sandbox blocks that host, so run it locally). Re-runnable; skips existing files.
set -euo pipefail
cd "$(dirname "$0")/.."
manifest="scripts/media_manifest.txt"
ok=0; fail=0
while IFS=$'\t' read -r url path; do
  [ -z "$url" ] && continue
  dest="static${path}"
  if [ -f "$dest" ]; then continue; fi
  mkdir -p "$(dirname "$dest")"
  if curl -fsSL "$url" -o "$dest"; then
    echo "ok   $path"; ok=$((ok+1))
  else
    echo "FAIL $url"; rm -f "$dest"; fail=$((fail+1))
  fi
done < "$manifest"
echo "downloaded=$ok failed=$fail"
