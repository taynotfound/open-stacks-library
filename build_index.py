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
    for l in body.split("\n"):
        t = l.strip()
        if t and not t.startswith(("#", "**", "- ", "[")):
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
    for fl in meta["files"]:
        if fl.get("hosted"):
            fl["size"] = file_size(fl)
    hosted_files = [x for x in meta["files"] if x.get("hosted")]
    if linked_only:
        state = "none"
    elif has_body or hosted_files:
        state = "full"
    elif meta["files"]:
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
        "atRisk": bool(re.search(r'true', meta.get("at_risk", ""), re.I)),
        "desc": desc,
        "slug": slugify(title),
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
