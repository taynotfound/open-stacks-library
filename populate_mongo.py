#!/usr/bin/env python3
"""
populate_mongo.py
-----------------
Full initial population of MongoDB 'open-stacks'.'books' collection
from the open-stacks-library index.json.

Usage:
    MONGODB_URI="mongodb+srv://..." python populate_mongo.py
"""

import os
import sys
import urllib.request
import json

# ---------------------------------------------------------------------------
# 1. Dependency check / install
# ---------------------------------------------------------------------------
try:
    import pymongo
except ImportError:
    import subprocess
    print("[setup] pymongo / dnspython not found – installing …")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymongo", "dnspython"])
    import pymongo

from pymongo import MongoClient, UpdateOne, ASCENDING, TEXT
from pymongo.errors import BulkWriteError

# ---------------------------------------------------------------------------
# 2. Config
# ---------------------------------------------------------------------------
INDEX_URL   = "https://raw.githubusercontent.com/taynotfound/open-stacks-library/main/index.json"
DB_NAME     = "open-stacks"
COLL_NAME   = "books"
BATCH_SIZE  = 500          # how many upserts to send per bulk_write call
LOG_EVERY   = 1000         # print progress every N documents processed

# ---------------------------------------------------------------------------
# 3. Connect
# ---------------------------------------------------------------------------
mongodb_uri = os.environ.get("MONGODB_URI")
if not mongodb_uri:
    print("[error] MONGODB_URI environment variable is not set.", file=sys.stderr)
    sys.exit(1)

print(f"[mongo] Connecting …")
client     = MongoClient(mongodb_uri)
db         = client[DB_NAME]
collection = db[COLL_NAME]
print(f"[mongo] Connected – using db='{DB_NAME}' collection='{COLL_NAME}'")

# ---------------------------------------------------------------------------
# 4. Fetch index.json
# ---------------------------------------------------------------------------
print(f"[fetch] Loading index from {INDEX_URL} …")
with urllib.request.urlopen(INDEX_URL) as resp:
    data = json.loads(resp.read().decode("utf-8"))

# Support both a bare list and {"books": [...]} shapes
if isinstance(data, list):
    entries = data
elif isinstance(data, dict):
    # Try common wrapper keys
    entries = data.get("books") or data.get("entries") or data.get("data") or list(data.values())[0]
else:
    print("[error] Unexpected JSON shape.", file=sys.stderr)
    sys.exit(1)

total = len(entries)
print(f"[fetch] {total} entries loaded.")

# ---------------------------------------------------------------------------
# 5. Upsert (bulk)
# ---------------------------------------------------------------------------
upserted   = 0
modified   = 0
errors     = 0
processed  = 0
batch: list[UpdateOne] = []

def flush_batch(batch: list) -> tuple[int, int]:
    """Send a bulk_write batch; returns (upserted, modified) counts."""
    if not batch:
        return 0, 0
    try:
        result = collection.bulk_write(batch, ordered=False)
        return result.upserted_count, result.modified_count
    except BulkWriteError as bwe:
        details = bwe.details
        # partial results still available
        return details.get("nUpserted", 0), details.get("nModified", 0)

for entry in entries:
    slug = entry.get("slug")
    if not slug:
        errors += 1
        processed += 1
        continue

    batch.append(
        UpdateOne(
            filter={"slug": slug},
            update={"$set": entry},
            upsert=True,
        )
    )

    if len(batch) >= BATCH_SIZE:
        u, m = flush_batch(batch)
        upserted += u
        modified += m
        batch = []

    processed += 1
    if processed % LOG_EVERY == 0:
        print(f"[progress] {processed}/{total} processed  |  upserted={upserted}  modified={modified}  errors={errors}")

# flush remainder
if batch:
    u, m = flush_batch(batch)
    upserted += u
    modified += m

print(f"\n[done] {processed}/{total} processed  |  upserted={upserted}  modified={modified}  skipped/errors={errors}")

# ---------------------------------------------------------------------------
# 6. Indexes
# ---------------------------------------------------------------------------
print("\n[indexes] Creating indexes …")

# Unique index on slug
collection.create_index([("slug", ASCENDING)], unique=True, name="slug_unique")
print("  ✓ slug (unique)")

# Compound text index on title + author
collection.create_index(
    [("title", TEXT), ("author", TEXT)],
    name="title_author_text",
    default_language="english",
)
print("  ✓ title + author (text)")

# Regular ascending indexes for filtering / sorting
for field in ("category", "sourceName", "hasBody", "added"):
    collection.create_index([(field, ASCENDING)], name=f"{field}_asc")
    print(f"  ✓ {field} (ascending)")

print("\n[indexes] All indexes created.")

# ---------------------------------------------------------------------------
# 7. Final summary
# ---------------------------------------------------------------------------
doc_count = collection.estimated_document_count()
print(f"\n{'='*55}")
print(f"  Population complete!")
print(f"  Documents in collection : {doc_count}")
print(f"  Entries in index.json   : {total}")
print(f"  Upserted (new)          : {upserted}")
print(f"  Modified (existing)     : {modified}")
print(f"  Skipped / errors        : {errors}")
print(f"{'='*55}")

client.close()

# ---------------------------------------------------------------------------
# 8. Print GitHub Actions workflow YAML
# ---------------------------------------------------------------------------
WORKFLOW_YAML = """\
# .github/workflows/populate-mongo.yml
# ------------------------------------
# Manual trigger only.
# Populates (or re-syncs) the MongoDB 'open-stacks'.'books' collection
# from the latest index.json in this repository.

name: Populate MongoDB

on:
  workflow_dispatch:   # manual trigger only

jobs:
  populate:
    name: Populate MongoDB from index.json
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install pymongo dnspython

      - name: Run populate_mongo.py
        env:
          MONGODB_URI: ${{ secrets.MONGODB_URI }}
        run: python populate_mongo.py
"""

print("\n" + "="*55)
print("  GitHub Actions Workflow YAML")
print("="*55)
print(WORKFLOW_YAML)
