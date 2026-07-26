#!/usr/bin/env python3
"""Convert a WordPress.com WXR export into a Hugo content tree.

Outputs:
  content/posts/<date>-<slug>.md   one file per post (drafts flagged)
  content/<slug>.md                standalone pages
  data/comments/<post_id>.json     approved comments per post (threaded by template)
  data/menu_extra.json             nav menu (external links)
  scripts/media_manifest.txt       original media URLs -> local /uploads paths
"""

import json
import os
import re
import sys
from datetime import datetime
from html import unescape
from xml.etree import ElementTree as ET

import markdownify

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_HOST = "tonyandrewmeyer.com"

media_map = {}  # original_url -> local_path


def txt(el, path):
    """Return the text of the first child matching path, or an empty string."""
    node = el.find(path, NS)
    return node.text if node is not None and node.text is not None else ""


def slugify(value):
    """Convert a title into a URL-safe slug."""
    value = re.sub(r"[^\w\s-]", "", value.lower()).strip()
    value = re.sub(r"[\s_-]+", "-", value)
    return value or "post"


def rewrite_media(html):
    """Rewrite wp-content/uploads URLs to local /uploads paths; record them."""

    def repl(m):
        url = m.group(0)
        base = url.split("?", 1)[0].split("#", 1)[0]  # drop resize/query params
        path = re.sub(r"^https?://[^/]+/wp-content/uploads/", "/uploads/", base)
        if path == base:  # not an uploads URL on this host
            return url
        media_map[base] = path  # download the full-res original
        return path

    # match full upload URLs on the blog host
    pattern = re.compile(
        r"https?://(?:[a-z0-9.-]*\.)?"
        + re.escape(SITE_HOST)
        + r"/wp-content/uploads/[^\s\"'<>)]+",
        re.I,
    )
    return pattern.sub(repl, html)


def strip_blocks(html):
    """Remove Gutenberg block delimiter comments, keep inner HTML."""
    return re.sub(r"<!--\s*/?wp:.*?-->", "", html, flags=re.S)


def html_to_md(html):
    """Convert post HTML into Markdown."""
    if not html.strip():
        return ""
    html = strip_blocks(html)
    html = rewrite_media(html)
    md = markdownify.markdownify(
        html,
        heading_style="ATX",
        bullets="-",
        code_language="",
        escape_asterisks=False,
        escape_underscores=False,
    )
    # collapse 3+ blank lines
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md


def yaml_quote(s):
    """Quote a string for safe use as a YAML scalar."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_wp_date(s):
    """Parse a WordPress timestamp, returning None when absent or zeroed."""
    s = s.strip()
    if not s or s.startswith("0000"):
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def main(xml_path):
    """Convert a WordPress export at xml_path into Hugo content."""
    tree = ET.parse(xml_path)  # noqa: S314
    channel = tree.getroot().find("channel")

    posts = pages = comments_total = pingbacks_total = 0
    menu = []

    for item in channel.findall("item"):
        ptype = txt(item, "wp:post_type")
        status = txt(item, "wp:status")

        if ptype == "nav_menu_item":
            meta = {}
            for pm in item.findall("wp:postmeta", NS):
                meta[txt(pm, "wp:meta_key")] = txt(pm, "wp:meta_value")
            url = meta.get("_menu_item_url", "").strip()
            label = unescape(txt(item, "title")).strip()
            order = int(txt(item, "wp:menu_order") or 0)
            if url and label:
                menu.append({"name": label, "url": url, "weight": order})
            continue

        if ptype not in ("post", "page"):
            continue  # skip attachments, styles, navigation, etc.

        title = unescape(txt(item, "title")).strip() or "Untitled"
        post_id = txt(item, "wp:post_id")
        name = txt(item, "wp:post_name").strip()
        date = parse_wp_date(txt(item, "wp:post_date"))
        content_html = txt(item, "content:encoded")
        excerpt_html = txt(item, "excerpt:encoded")

        slug = name or slugify(title)
        body = html_to_md(content_html)
        excerpt = html_to_md(excerpt_html)

        cats, tags = [], []
        for c in item.findall("category"):
            domain = c.get("domain")
            val = unescape(c.text or "").strip()
            if not val:
                continue
            if domain == "category" and val.lower() != "uncategorized":
                cats.append(val)
            elif domain == "post_tag":
                tags.append(val)

        # comments (approved only); pingbacks/trackbacks kept separately
        clist = []
        plist = []
        for c in item.findall("wp:comment", NS):
            if txt(c, "wp:comment_approved") != "1":
                continue
            cdate = parse_wp_date(txt(c, "wp:comment_date"))
            ctype = txt(c, "wp:comment_type")
            if ctype in ("pingback", "trackback"):
                plist.append(
                    {
                        "title": unescape(txt(c, "wp:comment_author").strip()),
                        "url": txt(c, "wp:comment_author_url").strip(),
                        "date": cdate.strftime("%Y-%m-%dT%H:%M:%S+12:00") if cdate else "",
                        "kind": ctype,
                    }
                )
                continue
            clist.append(
                {
                    "id": int(txt(c, "wp:comment_id") or 0),
                    "author": unescape(txt(c, "wp:comment_author").strip()),
                    "author_url": txt(c, "wp:comment_author_url").strip(),
                    "date": cdate.strftime("%Y-%m-%dT%H:%M:%S+12:00") if cdate else "",
                    "parent": int(txt(c, "wp:comment_parent") or 0),
                    "content": html_to_md(txt(c, "wp:comment_content")),
                }
            )
        if clist:
            clist.sort(key=lambda x: x["id"])
            with open(
                os.path.join(ROOT, "data/comments", f"{post_id}.json"), "w", encoding="utf-8"
            ) as fh:
                json.dump(clist, fh, ensure_ascii=False, indent=1)
            comments_total += len(clist)
        if plist:
            plist.sort(key=lambda x: x["date"])
            with open(
                os.path.join(ROOT, "data/pingbacks", f"{post_id}.json"), "w", encoding="utf-8"
            ) as fh:
                json.dump(plist, fh, ensure_ascii=False, indent=1)
            pingbacks_total += len(plist)

        # front matter
        fm = ["---"]
        fm.append(f"title: {yaml_quote(title)}")
        if date:
            fm.append(f"date: {date.strftime('%Y-%m-%dT%H:%M:%S+12:00')}")
        fm.append(f"slug: {yaml_quote(slug)}")
        if status == "draft":
            fm.append("draft: true")
        if excerpt:
            fm.append(f"summary: {yaml_quote(excerpt)}")
        if cats:
            fm.append("categories:")
            fm += [f"  - {yaml_quote(c)}" for c in cats]
        if tags:
            fm.append("tags:")
            fm += [f"  - {yaml_quote(t)}" for t in tags]
        if clist:
            fm.append(f"comment_id: {yaml_quote(post_id)}")
            fm.append(f"comment_count: {len(clist)}")
        if plist:
            fm.append(f"pingback_id: {yaml_quote(post_id)}")
            fm.append(f"pingback_count: {len(plist)}")
        fm.append("---\n")
        out = "\n".join(fm) + body + "\n"

        if ptype == "page":
            path = os.path.join(ROOT, "content", f"{slug}.md")
            pages += 1
        else:
            prefix = date.strftime("%Y-%m-%d-") if date else ""
            path = os.path.join(ROOT, "content/posts", f"{prefix}{slug}.md")
            posts += 1
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(out)

    # menu data
    menu.sort(key=lambda m: m["weight"])
    with open(os.path.join(ROOT, "data/menu_extra.json"), "w", encoding="utf-8") as fh:
        json.dump(menu, fh, ensure_ascii=False, indent=1)

    # media manifest
    with open(os.path.join(ROOT, "scripts/media_manifest.txt"), "w", encoding="utf-8") as fh:
        for url in sorted(media_map):
            fh.write(f"{url}\t{media_map[url]}\n")

    print(
        f"posts={posts} pages={pages} comments={comments_total} "
        f"pingbacks={pingbacks_total} menu={len(menu)} media_refs={len(media_map)}"
    )


if __name__ == "__main__":
    main(sys.argv[1])
