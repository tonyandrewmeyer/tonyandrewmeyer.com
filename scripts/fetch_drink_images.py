#!/usr/bin/env python3
"""Download product images for the drinks tracker.

Reads scripts/drinks_manifest.txt (lines of `<post-slug>\\t<product-url>`),
fetches each product page, extracts og:image, downloads it to
static/uploads/drinks/<slug>.<ext>, and updates the matching post in
content/posts/ to point its drink.photo field at the saved file.

Run from a network that can reach the producer sites (Cloudflare blocks the
Claude web sandbox). Re-runnable; skips already-downloaded files but always
rewrites the photo field so extensions stay in sync.
"""
import mimetypes
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "scripts" / "drinks_manifest.txt"
DEST_DIR = ROOT / "static" / "uploads" / "drinks"
POSTS_DIR = ROOT / "content" / "posts"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"

OG_RE = re.compile(
    r"""<meta[^>]+property=["']og:image["'][^>]*content=["']([^"']+)["']""",
    re.IGNORECASE,
)
OG_RE_ALT = re.compile(
    r"""<meta[^>]+content=["']([^"']+)["'][^>]+property=["']og:image["']""",
    re.IGNORECASE,
)


def fetch(url: str) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read(), r.headers.get("Content-Type", "")


def og_image(html: str, base: str) -> str | None:
    m = OG_RE.search(html) or OG_RE_ALT.search(html)
    if not m:
        return None
    src = m.group(1)
    if src.startswith("//"):
        src = "https:" + src
    elif src.startswith("/"):
        from urllib.parse import urljoin
        src = urljoin(base, src)
    # Strip Shopify-style query-string size hints so we get the original.
    return src.split("?", 1)[0]


def ext_for(content_type: str, url: str) -> str:
    ct = content_type.split(";", 1)[0].strip().lower()
    ext = mimetypes.guess_extension(ct) if ct else None
    if not ext:
        # Fall back to URL extension, then .jpg.
        _, _, tail = url.rpartition("/")
        if "." in tail:
            ext = "." + tail.rsplit(".", 1)[1].lower()
        else:
            ext = ".jpg"
    if ext == ".jpe":
        ext = ".jpg"
    return ext


PHOTO_LINE_RE = re.compile(r"^(?P<indent>\s+)photo:\s*.*$", re.MULTILINE)
DRINK_BLOCK_RE = re.compile(r"^drink:\s*$", re.MULTILINE)


def update_post(slug: str, photo_path: str) -> bool:
    """Set drink.photo on the post whose filename ends with -<slug>.md."""
    matches = list(POSTS_DIR.glob(f"*-{slug}.md"))
    if not matches:
        print(f"WARN no post for slug {slug!r}", file=sys.stderr)
        return False
    if len(matches) > 1:
        print(f"WARN multiple posts for slug {slug!r}: {matches}", file=sys.stderr)
        return False
    post = matches[0]
    text = post.read_text()
    new_line_value = f'"{photo_path}"'
    if PHOTO_LINE_RE.search(text):
        text = PHOTO_LINE_RE.sub(lambda m: f"{m.group('indent')}photo: {new_line_value}", text, count=1)
    else:
        # Insert `  photo: "..."` immediately after the `drink:` line.
        m = DRINK_BLOCK_RE.search(text)
        if not m:
            print(f"WARN no drink: block in {post.name}", file=sys.stderr)
            return False
        insert_at = m.end()
        text = text[:insert_at] + f"\n  photo: {new_line_value}" + text[insert_at:]
    post.write_text(text)
    return True


def main() -> int:
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    ok = skipped = failed = 0
    for line in MANIFEST.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        slug, _, url = line.partition("\t")
        slug, url = slug.strip(), url.strip()
        if not slug or not url:
            print(f"skip malformed line: {line!r}", file=sys.stderr)
            continue

        existing = list(DEST_DIR.glob(f"{slug}.*"))
        if existing:
            dest = existing[0]
            print(f"skip {dest.relative_to(ROOT)} (already downloaded)")
            skipped += 1
            update_post(slug, "/" + str(dest.relative_to(ROOT / "static")))
            continue

        try:
            page, _ = fetch(url)
            img_url = og_image(page.decode("utf-8", "replace"), url)
            if not img_url:
                print(f"FAIL {slug}: no og:image on {url}", file=sys.stderr)
                failed += 1
                continue
            img_bytes, ct = fetch(img_url)
            ext = ext_for(ct, img_url)
            dest = DEST_DIR / f"{slug}{ext}"
            dest.write_bytes(img_bytes)
            print(f"ok   {dest.relative_to(ROOT)} ({len(img_bytes):,} bytes)")
            update_post(slug, "/" + str(dest.relative_to(ROOT / "static")))
            ok += 1
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
            print(f"FAIL {slug}: {e}", file=sys.stderr)
            failed += 1

    print(f"downloaded={ok} skipped={skipped} failed={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
