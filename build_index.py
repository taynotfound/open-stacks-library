#!/usr/bin/env python3
"""Build a lightweight index.json for The Open Stacks so the frontend loads
in ONE request instead of ~2000 individual GitHub raw fetches.
Index carries all list/detail metadata + short desc, but NOT the full body.
Bodies are lazy-fetched per book only when opened."""
import glob, re, json, os, subprocess, html, time

ROOT = os.environ.get("OS_ROOT", ".")
SITE = "https://theopenstacks.apolochees.me"
md_files = sorted(glob.glob(ROOT + "/books/**/*.md", recursive=True))


def git_added_dates():
    """Map books/<cat>/<slug>.md -> unix timestamp of first (Add) commit.
    One git pass; falls back to filesystem mtime if git is unavailable."""
    dates = {}
    try:
        p = subprocess.run(
            ["git", "-C", ROOT, "log", "--diff-filter=A", "--name-only",
             "--format=%at", "--", "books/"],
            capture_output=True, text=True, timeout=120)
        cur = None
        for ln in p.stdout.splitlines():
            ln = ln.strip()
            if not ln:
                continue
            if ln.isdigit():
                cur = int(ln)
            elif ln.endswith(".md") and cur and ln not in dates:
                dates[ln] = cur  # first time we see it = newest add (git log is newest-first)
    except Exception:
        pass
    return dates

ADDED = git_added_dates()


def unq(s):
    s = s.strip()
    if len(s) >= 2 and s[0] in "\"'" and s[-1] == s[0]:
        s = s[1:-1]
    return s.replace('\\"', '"')


def parse_front(md):
    m = re.match(r'^---\n([\s\S]*?)\n---', md)
    if not m:
        return {}, md
    body = md[m.end():].strip()
    lines = m.group(1).split("\n")
    meta = {"tags": [], "files": [], "images": [], "links": []}
    mode = None
    cur = None
    for ln in lines:
        if re.match(r'^tags:\s*$', ln): mode = "tags"; continue
        if re.match(r'^files:\s*$', ln): mode = "files"; continue
        if re.match(r'^images:\s*$', ln): mode = "images"; continue
        if re.match(r'^links:\s*$', ln): mode = "links"; continue
        if re.match(r'^(files|tags|images|links):\s*\[\]', ln): mode = None; continue
        if mode == "tags" and re.match(r'^\s*-\s', ln):
            meta["tags"].append(unq(re.sub(r'^\s*-\s*', '', ln))); continue
        if mode == "images" and re.match(r'^\s*-\s', ln):
            meta["images"].append(unq(re.sub(r'^\s*-\s*', '', ln))); continue
        if mode == "links":
            if re.match(r'^\s*-\s*url:', ln):
                cur = {}; meta["links"].append(cur)
                cur["url"] = unq(ln.split("url:", 1)[1]); continue
            lm = re.match(r'^\s+(text):\s*(.*)$', ln)
            if lm and cur is not None:
                cur["text"] = unq(lm.group(2)); continue
        if mode == "files":
            if re.match(r'^\s*-\s*name:', ln):
                cur = {}; meta["files"].append(cur)
                cur["name"] = unq(ln.split("name:", 1)[1]); continue
            fm = re.match(r'^\s+(type|url|hosted):\s*(.*)$', ln)
            if fm and cur is not None:
                if fm.group(1) == "hosted":
                    cur["hosted"] = bool(re.search(r'true', fm.group(2)))
                else:
                    cur[fm.group(1)] = unq(fm.group(2)); continue
                continue
        kv = re.match(r'^(\w+):\s*(.*)$', ln)
        if kv:
            mode = None
            meta[kv.group(1)] = unq(kv.group(2))
    return meta, body


def first_para(body):
    import re as _re
    body = _re.sub(r'^>\s*\*Translated to English from[^\n]*\n?', '', body, flags=_re.M).strip()
    for l in body.split("\n"):
        t = l.strip()
        if t and not t.startswith(("#", "**", "- ", "[", ">")):
            return t
    return ""


def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower())
    return re.sub(r'^-|-$', '', s)[:80]


def human_size(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return (f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}")
        n /= 1024.0


def file_size(f):
    """Bytes on disk for a hosted file, matched by the basename of its URL
    (the URL points at files/<realname>; the `name` field is only a label)."""
    from urllib.parse import unquote
    url = f.get("url", "")
    name = unquote(url.rsplit("/", 1)[-1]) if url else (f.get("name") or "")
    if not name:
        return 0
    for cand in (os.path.join(ROOT, "files", name),
                 os.path.join(ROOT, "files", "img", name)):
        try:
            return os.path.getsize(cand)
        except OSError:
            continue
    return 0


LANG_NAMES = {
    "en": "English", "de": "Deutsch", "fr": "Francais", "es": "Espanol",
    "it": "Italiano", "pt": "Portugues", "zh": "Chinese", "ru": "Russian",
    "bg": "Bulgarian", "nl": "Nederlands", "pl": "Polski",
}
# filename-prefix (sister-mirror slugs) -> language code
_PREFIX_LANG = {"de": "de", "fr": "fr", "es": "es", "it": "it",
                "pt": "pt", "zh": "zh", "ru": "ru", "bg": "bg", "talde": "de"}


def derive_lang(meta, rel):
    """Language code for an item. Priority: explicit front-matter `language`,
    then sister-mirror filename prefix (books/<cat>/<code>-slug.md), then
    source_name host prefix, then native-language tag, else English."""
    explicit = (meta.get("language") or meta.get("lang") or "").strip().lower()
    if explicit:
        return explicit[:2]
    base = os.path.basename(rel)
    pre = base.split("-", 1)[0].lower()
    if pre in _PREFIX_LANG:
        return _PREFIX_LANG[pre]
    sn = (meta.get("source_name") or "").lower()
    m = re.match(r'(de|fr|es|it|pt|zh|ru|bg)\.anarchist', sn)
    if m:
        return m.group(1)
    tagset = {t.lower() for t in meta.get("tags", [])}
    for code, nm in (("de", "deutsch"), ("fr", "francais"), ("es", "espanol"),
                     ("it", "italiano"), ("pt", "portugues")):
        if nm in tagset:
            return code
    return "en"


out = []
for f in md_files:
    txt = open(f, encoding="utf-8").read()
    meta, body = parse_front(txt)
    rel = os.path.relpath(f, ROOT)  # e.g. books/anarchism/foo.md
    title = meta.get("title") or os.path.basename(f)
    desc = meta.get("description") or first_para(body)
    if len(desc) > 400:
        desc = desc[:400]
    # Derive state from what we ACTUALLY hold, not the (often wrong) front-matter.
    # full = we have a readable copy here (full archived body OR a self-hosted file)
    # partial = we hold some files but not the full text
    # none = we only link out; no body, no hosted files
    # linked_only: true forces "none" — for curated pointer entries whose body is
    # just a short editorial blurb + source link, NOT an archived full copy.
    linked_only = bool(re.search(r'true', meta.get("linked_only", ""), re.I))
    has_body = len(body) > 40
    # Attach byte sizes to hosted files (so the frontend can show "12.4 MB").
    for fl in meta.get("files", []):
        if fl.get("hosted"):
            fl["size"] = file_size(fl)
    hosted_files = [x for x in meta.get("files", []) if x.get("hosted")]
    if linked_only:
        state = "none"
    elif has_body or hosted_files:
        state = "full"
    elif meta.get("files"):
        state = "partial"
    else:
        state = "none"
    out.append({
        "title": title,
        "author": meta.get("author", ""),
        "category": meta.get("category") or (rel.split("/")[1] if "/" in rel else "general"),
        "state": state,
        "tags": meta["tags"],
        "files": meta["files"],
        "images": meta["images"],
        "links": meta["links"],
        "pageType": meta.get("page_type", ""),
        "source": meta.get("source", ""),
        "cover": meta.get("cover", ""),
        "sourceName": meta.get("source_name", ""),
        "language": derive_lang(meta, rel),
        "translatedType": meta.get("translatedType") or meta.get("translatedtype") or "",
        "translatedFrom": meta.get("translatedFrom") or meta.get("translatedfrom") or "",
        "originalSlug": meta.get("originalSlug") or meta.get("originalslug") or "",
        "atRisk": bool(re.search(r'true', meta.get("at_risk", ""), re.I)),
        "desc": desc,
        "slug": (slugify(title) + "-" + meta.get("language","en")) if (meta.get("originalSlug") or meta.get("originalslug")) else slugify(title),
        "path": rel,
        "hasBody": len(body) > 40,
        "added": ADDED.get(rel, int(os.path.getmtime(f))),
    })

# newest first for recently-added surfacing
out.sort(key=lambda e: e.get("added", 0), reverse=True)

with open(ROOT + "/index.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))

sz = os.path.getsize(ROOT + "/index.json")
total_hosted_bytes = sum(fl.get("size", 0) for e in out for fl in e["files"] if fl.get("hosted"))
n_hosted = sum(1 for e in out for fl in e["files"] if fl.get("hosted"))
print(f"books indexed: {len(out)}")
print(f"index.json size: {sz/1e6:.2f} MB")
print(f"self-hosted files: {n_hosted} · {human_size(total_hosted_bytes)}")


# ---------------------------------------------------------------------------
# Secondary artifacts, all built from `out`, all committed by the same Action:
#   feed.xml          - RSS 2.0 of the 50 most recently ADDED items
#   opds.xml          - OPDS 1.2 catalog (Atom) for e-reader apps
#   search-index.json - flat docs for Lunr.js full-text search on the client
# ---------------------------------------------------------------------------
def xesc(s):
    return html.escape(str(s or ""), quote=True)

def item_url(e):
    kind = "gallery" if (e.get("pageType") == "gallery" or (e.get("images") and not e.get("files"))) else "book"
    return f"{SITE}/{kind}/{e['slug']}"

now_http = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

# ---- RSS feed: newest 50 additions (out is already newest-first) ----
rss_items = []
for e in out[:50]:
    pub = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(e.get("added", 0)))
    url = item_url(e)
    desc = e.get("desc") or f"{e['title']} archived on The Open Stacks."
    cats = "".join(f"<category>{xesc(t)}</category>" for t in (e.get("tags") or [])[:6])
    rss_items.append(
        f"<item><title>{xesc(e['title'])}</title>"
        f"<link>{xesc(url)}</link><guid isPermaLink=\"true\">{xesc(url)}</guid>"
        f"<pubDate>{pub}</pubDate>"
        f"{'<author>'+xesc(e['author'])+'</author>' if e.get('author') else ''}"
        f"{cats}<description>{xesc(desc)}</description></item>")

rss = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
       f'<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
       f'<title>The Open Stacks - recently added</title>'
       f'<link>{SITE}/</link>'
       f'<atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>'
       f'<description>Newest additions to The Open Stacks, an anti-censorship library.</description>'
       f'<language>en</language><lastBuildDate>{now_http}</lastBuildDate>'
       + "".join(rss_items) + "</channel></rss>")
with open(ROOT + "/feed.xml", "w", encoding="utf-8") as fh:
    fh.write(rss)

# ---- OPDS 1.2 catalog (acquisition feed) for e-reader apps ----
MIME = {"pdf": "application/pdf", "epub": "application/epub+zip",
        "mobi": "application/x-mobipocket-ebook", "azw3": "application/vnd.amazon.ebook",
        "html": "text/html", "htm": "text/html", "txt": "text/plain"}
def file_mime(f):
    src = (f.get("name", "") + " " + f.get("url", "")).lower()
    m = re.search(r"\.(pdf|epub|mobi|azw3|html?|txt)(\?|#|$)", src)
    return MIME.get(m.group(1).replace("htm", "html"), "application/octet-stream") if m else "application/octet-stream"

opds_entries = []
n_acq = 0
for e in out:
    acq = []
    for f in (e.get("files") or []):
        if f.get("hosted") and f.get("url"):
            acq.append(f'<link rel="http://opds-spec.org/acquisition" '
                       f'href="{xesc(f["url"])}" type="{file_mime(f)}"/>')
    if not acq:
        continue
    n_acq += 1
    upd = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(e.get("added", 0)))
    author = f"<author><name>{xesc(e['author'])}</name></author>" if e.get("author") else ""
    cats = "".join(f'<category term="{xesc(t)}"/>' for t in (e.get("tags") or [])[:6])
    summ = xesc(e.get("desc") or e["title"])
    opds_entries.append(
        f"<entry><title>{xesc(e['title'])}</title>"
        f"<id>{xesc(item_url(e))}</id><updated>{upd}</updated>{author}{cats}"
        f'<link rel="alternate" href="{xesc(item_url(e))}" type="text/html"/>'
        f"<summary type=\"text\">{summ}</summary>" + "".join(acq) + "</entry>")

opds = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<feed xmlns="http://www.w3.org/2005/Atom" '
        f'xmlns:opds="http://opds-spec.org/2010/catalog">'
        f'<id>{SITE}/opds.xml</id>'
        f'<title>The Open Stacks</title><updated>{now_iso}</updated>'
        f'<author><name>The Open Stacks</name><uri>{SITE}/</uri></author>'
        f'<link rel="self" href="{SITE}/opds.xml" type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>'
        f'<link rel="start" href="{SITE}/opds.xml" type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>'
        + "".join(opds_entries) + "</feed>")
with open(ROOT + "/opds.xml", "w", encoding="utf-8") as fh:
    fh.write(opds)

# ---- Lunr search docs: title/author/tags/text (full body when we hold it) ----
docs = []
for e in out:
    body = ""
    if e.get("hasBody"):
        try:
            with open(os.path.join(ROOT, e["path"]), encoding="utf-8") as bf:
                raw = bf.read()
            mm = re.search(r"^---\n.*?\n---\n?", raw, re.S)
            body = raw[mm.end():] if mm else raw
            body = re.sub(r"\s+", " ", body)[:1800]  # cap per-doc to keep the client index lean
        except Exception:
            body = ""
    docs.append({
        "slug": e["slug"],
        "title": e["title"],
        "author": e.get("author", ""),
        "tags": " ".join(e.get("tags") or []),
        "text": (e.get("desc", "") + " " + body).strip(),
    })
with open(ROOT + "/search-index.json", "w", encoding="utf-8") as fh:
    json.dump({"docs": docs}, fh, ensure_ascii=False, separators=(",", ":"))

print(f"feed.xml: {len(rss_items)} items · opds.xml: {n_acq} acquirable · search-index.json: {len(docs)} docs")
