"""gatsby2hugo

Walk a content directory and update markdown files in-place to be more Hugo-friendly.

What it does:
- Reads each Markdown file under the provided directory (recursive).
- Extracts YAML front matter (delimited by leading and trailing "---").
- Converts an `itemtype:` key like `Item/Page/Article` into `type: article`.
- Converts `date: YYYY-MM-DD HH:MM:SS` into `date: YYYY-MM-DDTHH:MM:SSZ`.
- Converts simple inline HTML to Markdown: `<strong>`/`<b>` -> `**...**`,
  `<em>`/`<i>` -> `*...*`, `<a href="...">text</a>` -> `[text](...)`.
- Writes the updated front matter and content back to the file.

This implementation avoids external YAML libraries by editing the front
matter lines directly (safe for simple transformations described above).

Usage:
        python bin/gatsby2hugo.py /path/to/content
"""

from __future__ import annotations

import argparse
import os
import re
from datetime import datetime
from typing import Optional, Tuple


def split_front_matter(text: str) -> Tuple[Optional[str], str]:
    """Return (front_matter, content). If no front matter, front_matter is None."""
    if text.startswith("---\n"):
        # find the closing --- on its own line
        m = re.search(r"\n---\s*\n", text)
        if m:
            fm = text[
                4 : m.start() + 1
            ]  # between the two '---' lines (include trailing \n)
            content = text[m.end() :]
            return fm, content
    return None, text


def transform_front_matter(fm_text: str) -> str:
    """Apply itemtype -> type and date conversions to front matter text."""
    lines = fm_text.splitlines()
    out_lines = []
    date_re = re.compile(r"^(\s*date\s*:\s*)(['\"]?)(.+?)(['\"]?)\s*$", re.I)
    itemtype_re = re.compile(r"^(\s*itemtype\s*:\s*)(['\"]?)(.+?)(['\"]?)\s*$", re.I)

    for line in lines:
        m_item = itemtype_re.match(line)
        if m_item:
            value = m_item.group(3).strip()
            # take last segment after / and lowercase
            last = value.split("/")[-1]
            new = f"type: {last.lower()}"
            out_lines.append(new)
            continue

        m_date = date_re.match(line)
        if m_date:
            raw = m_date.group(3).strip()
            # if it looks like 'YYYY-MM-DD HH:MM' convert to ISO with Z
            if re.match(r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}$", raw):
                try:
                    dt = datetime.strptime(raw, "%Y-%m-%d %H:%M")
                    iso = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                    out_lines.append(f"date: {iso}")
                    continue
                except Exception:
                    pass
            # otherwise, leave as-is
            out_lines.append(line)
            continue

        out_lines.append(line)

    return "\n".join(out_lines) + "\n"


def html_to_markdown(text: str) -> str:
    """Convert simple inline HTML tags to markdown equivalents."""

    # Convert anchors: <a href="url">text</a> -> [text](url)
    def a_repl(m: re.Match) -> str:
        href = m.group("href")
        txt = m.group("text")
        return f"[{txt}]({href})"

    text = re.sub(
        r"<a\s+[^>]*href=[\"']?(?P<href>[^\"' >]+)[\"']?[^>]*>(?P<text>.*?)</a>",
        a_repl,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # strong/b tags -> **text**
    text = re.sub(
        r"<(?:strong|b)>(.*?)</(?:strong|b)>",
        r"**\1**",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # em/i tags -> *text*
    text = re.sub(
        r"<(?:em|i)>(.*?)</(?:em|i)>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL
    )

    return text


def process_file(path: str) -> bool:
    """Process single markdown file. Return True if file changed."""
    with open(path, "r", encoding="utf-8") as f:
        orig = f.read()

    fm, content = split_front_matter(orig)
    changed = False
    new_fm_text = None

    if fm is not None:
        new_fm_text = transform_front_matter(fm)
        if new_fm_text != fm:
            changed = True

    new_content = html_to_markdown(content)
    if new_content != content:
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            if new_fm_text is not None:
                f.write("---\n")
                f.write(new_fm_text)
                f.write("---\n")
            f.write(new_content)
    return changed


def crawl_and_process(root: str) -> int:
    """Walk directory and process markdown files. Returns number of files changed."""
    changed_count = 0
    for dirpath, dirs, files in os.walk(root):
        for name in files:
            if name.lower().endswith((".md", ".markdown")):
                full = os.path.join(dirpath, name)
                try:
                    if process_file(full):
                        changed_count += 1
                        print(f"Updated: {full}")
                except Exception as e:
                    print(f"Error processing {full}: {e}")
    return changed_count


def main() -> None:
    p = argparse.ArgumentParser(
        description="Convert Gatsby-style markdown to Hugo-friendly format"
    )
    p.add_argument("path", help="Content directory to process")
    args = p.parse_args()

    root = args.path
    if not os.path.isdir(root):
        print(f"Not a directory: {root}")
        raise SystemExit(2)

    changed = crawl_and_process(root)
    print(f"Done. Files updated: {changed}")


if __name__ == "__main__":
    main()
