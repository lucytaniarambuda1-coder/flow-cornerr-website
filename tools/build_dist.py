#!/usr/bin/env python3
"""
Copies the deployable site into dist/ for Netlify, leaving out source and
config (tools/, .git, netlify.toml and so on) so only public files are served.
Netlify runs this as the build command; see netlify.toml.

The HTML is already generated and committed, so no generate step is needed.
Run  python3 tools/generate.py  yourself before committing page changes.
"""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
EXCLUDE = {".git", ".github", "tools", "dist", "netlify", "src", "node_modules", ".DS_Store",
           "netlify.toml", "package.json", "package-lock.json", "README.md", ".gitignore"}

if os.path.isdir(DIST):
    shutil.rmtree(DIST)
os.makedirs(DIST)

count = 0
for name in sorted(os.listdir(ROOT)):
    if name in EXCLUDE or name.startswith("."):
        continue
    src = os.path.join(ROOT, name)
    dst = os.path.join(DIST, name)
    if os.path.isdir(src):
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".DS_Store"))
    else:
        shutil.copy2(src, dst)
    count += 1
print(f"dist/ ready: {count} top-level entries")
