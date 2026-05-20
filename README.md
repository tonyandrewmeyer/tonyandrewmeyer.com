# tonyandrewmeyer.com

Static site (Hugo) migrated from WordPress.com. Posts are markdown; old
comments are preserved read-only; permalinks match the original site.

## Local development

```sh
hugo server          # http://localhost:1313/
```

Install Hugo **extended** (>= 0.148): https://gohugo.io/installation/

## Layout

| Path | Contents |
|------|----------|
| `content/posts/` | 187 posts, one markdown file each (`YYYY-MM-DD-slug.md`) |
| `content/archive.md` | full chronological archive page |
| `data/comments/*.json` | preserved comments, keyed by original post id |
| `data/menu_extra.json` | external "Elsewhere" links (footer) |
| `layouts/` | the theme (hand-rolled, no external dependency) |
| `static/uploads/` | media (see below) |
| `scripts/convert.py` | the WXR-to-Hugo converter, kept for reference |
| `scripts/media_manifest.txt` | list of media URLs -> local paths |
| `scripts/fetch_media.sh` | downloads the media into `static/uploads/` |

## Media — one step still needed

The WordPress export does **not** include the image files, only links to
them. Run this from a machine/network that can reach `tonyandrewmeyer.com`
(while the WordPress site is still up):

```sh
bash scripts/fetch_media.sh
git add static/uploads && git commit -m "Add migrated media"
```

There are 18 referenced files. After that the site is fully self-contained
and you can let the WordPress.com hosting lapse.

## Writing a new post

```sh
hugo new content posts/2026-05-21-my-title.md
```

Edit the front matter (`title`, `date`, `slug`) and write markdown. New
posts don't need a `comment_id`.

## Deployment (GitHub Pages + custom domain)

1. Create repo `tonyandrewmeyer/tonyandrewmeyer.com` and push this tree to
   the `main` branch.
2. Repo **Settings -> Pages -> Build and deployment -> Source: GitHub Actions**.
   The included workflow (`.github/workflows/deploy.yml`) builds and deploys
   on every push to `main`.
3. The `static/CNAME` file sets the custom domain. In your DNS, point the
   apex `tonyandrewmeyer.com` at GitHub Pages:
   - `A` records to `185.199.108.153`, `.109.153`, `.110.153`, `.111.153`
   - or an `ALIAS`/`ANAME` to `tonyandrewmeyer.github.io`
   GitHub provisions HTTPS automatically once DNS resolves.

Until DNS is cut over, the site is also reachable at the
`*.github.io` URL for testing.
