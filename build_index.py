#!/usr/bin/env python3
"""Build a lightweight index.json for The Open Stacks so the frontend loads
in ONE request instead of ~2000 individual GitHub raw fetches.
Index carries all list/detail metadata + short desc, but NOT the full body.
Bodies are lazy-fetched per book only when opened."""
import glob, re, json, os

ROOT = os.environ.get("OS_ROOT", ".")
md_files = sorted(glob.glob(ROOT + "/books/**/*.md", recursive=True))


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
    })

with open(ROOT + "/index.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))

sz = os.path.getsize(ROOT + "/index.json")
print(f"books indexed: {len(out)}")
print(f"index.json size: {sz/1e6:.2f} MB")
