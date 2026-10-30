#!/usr/bin/env python3
"""Consistency checks for BasicScienceVault.

Run from the vault root:   python scripts/check_vault.py
Exit code 0 = all checks passed, 1 = errors found (used by GitHub Actions).

Checks
  1. note names are unique (Obsidian links by name)
  2. every [[wikilink]] points to an existing note (code blocks are ignored)
  3. every topic note has a "- Worksheet" and a "- Solutions" note
  4. every note has YAML front matter with tags
  5. Markdown tables have the same number of columns in every row
  6. worksheets contain at most one 🧮 and at most one 💻 task
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".obsidian", ".github", ".trash", "node_modules", "_attachments"}
SKIP_FILES = {"README.md", "CONTRIBUTING.md", "CHANGELOG.md", "CODE_OF_CONDUCT.md"}
TEMPLATE_DIR = "_Templates"
TOPIC_RE = re.compile(r"^(?:[A-E]\d+|Ph\d\d|Ch\d\d|Bio\d\d|Meth\d\d|CS\d\d|Prog\d\d|Py\d\d|R\d\d|MAT\d\d|Doc\d\d) ")
OVERVIEW_RE = re.compile(r"^(?:[A-E]0|Py00|R00|MAT00|Doc00) ")
LINK_RE = re.compile(r"\[\[([^\]\|#\\]+)(?:#[^\]\|]*)?(?:\\?\|[^\]]*)?\]\]")


def strip_code(text):
    # fenced code blocks, also when the fence starts on a list item line ("1. ```r")
    text = re.sub(r"(?ms)^[ \t]*(?:(?:\d+\.|[-*+])[ \t]+)?(`{3,}|~{3,}).*?^[ \t]*\1[ \t]*$", "", text)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def table_errors(lines):
    errors, header, in_code = [], None, False
    for i, line in enumerate(lines, 1):
        if re.match(r"^\s*(?:(?:\d+\.|[-*+])\s+)?(```|~~~)", line):
            in_code, header = not in_code, None
            continue
        if in_code:
            continue
        if line.strip().startswith("|"):
            cells = re.split(r"(?<!\\)\|", line.strip())[1:-1]
            if header is None:
                header = len(cells)
            elif len(cells) != header:
                errors.append(f"line {i}: {len(cells)} columns, header has {header}")
        else:
            header = None
    return errors


def main():
    notes = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(".md") and f not in SKIP_FILES:
                notes.setdefault(f[:-3], []).append(os.path.join(dirpath, f))
    errors = []

    for name, paths in notes.items():
        if len(paths) > 1:
            errors.append(f"duplicate note name '{name}': {paths}")

    n_links = 0
    for name, paths in notes.items():
        for path in paths:
            rel = os.path.relpath(path, ROOT)
            text = open(path, encoding="utf-8").read()
            in_templates = rel.startswith(TEMPLATE_DIR)
            if not in_templates and not rel.startswith("setup"):
                for target in LINK_RE.findall(strip_code(text)):
                    n_links += 1
                    if target.strip() not in notes:
                        errors.append(f"{rel}: broken link [[{target.strip()}]]")
                if not re.match(r"^---\n(.*?\n)?tags:", text, re.S):
                    errors.append(f"{rel}: missing YAML front matter with tags")
            for e in table_errors(text.split("\n")):
                errors.append(f"{rel}: table {e}")
            if name.endswith(" - Worksheet"):
                for sym in ("🧮", "💻"):
                    tasks = [l for l in text.split("\n") if sym in l and re.match(r"^\s*\d+\.", l)]
                    if len(tasks) > 1:
                        errors.append(f"{rel}: {len(tasks)} tasks marked {sym} (max. 1)")

    for name in notes:
        if TOPIC_RE.match(name) and not OVERVIEW_RE.match(name) \
                and not name.endswith((" - Worksheet", " - Solutions")) and "MOC" not in name:
            for suffix in (" - Worksheet", " - Solutions"):
                if name + suffix not in notes:
                    errors.append(f"'{name}' has no '{name}{suffix}'")

    print(f"{sum(len(p) for p in notes.values())} notes, {n_links} links checked")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        return 1
    print("All checks passed ✔")
    return 0


if __name__ == "__main__":
    sys.exit(main())
