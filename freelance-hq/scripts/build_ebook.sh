#!/usr/bin/env bash
# Build EPUB (+ PDF if an engine exists) from ebooks/<slug>/manuscript/*.md
# Usage: bash scripts/build_ebook.sh ebooks/<slug>
# Needs: pandoc (https://pandoc.org). Optional for PDF: typst, or a LaTeX engine (xelatex).
set -euo pipefail
[ $# -ge 1 ] || { echo "Usage: $0 ebooks/<slug>"; exit 1; }
dir="${1%/}"
command -v pandoc >/dev/null || { echo "pandoc not found. Install it: https://pandoc.org/installing.html"; exit 1; }
ms="$dir/manuscript"
[ -d "$ms" ] || { echo "Missing $ms (put chapters there as 01-name.md, 02-name.md ...)"; exit 1; }
meta="$dir/metadata.yaml"
[ -f "$meta" ] || { echo "Missing $meta. Example:"; printf -- '---\ntitle: "Your Title"\nsubtitle: "Your subtitle"\nauthor: "Your Name"\nlang: en\nrights: "(c) 2026 Your Name. All rights reserved."\n---\n'; exit 1; }
out="$dir/build"; mkdir -p "$out"
shopt -s nullglob
files=("$ms"/*.md)
[ ${#files[@]} -gt 0 ] || { echo "No chapters in $ms"; exit 1; }
args=(--toc --toc-depth=2 --metadata-file="$meta")
[ -f "$dir/cover.jpg" ] && args+=(--epub-cover-image="$dir/cover.jpg")
pandoc "${files[@]}" "${args[@]}" -o "$out/book.epub"
echo "EPUB: $out/book.epub"
if command -v typst >/dev/null; then
  pandoc "${files[@]}" "${args[@]}" --pdf-engine=typst -o "$out/book.pdf" && echo "PDF: $out/book.pdf"
elif command -v xelatex >/dev/null; then
  pandoc "${files[@]}" "${args[@]}" --pdf-engine=xelatex -o "$out/book.pdf" && echo "PDF: $out/book.pdf"
else
  echo "No PDF engine (typst/xelatex) found; skipped PDF."
fi
echo "Next: validate EPUB (EPUBCheck / Kindle Previewer) and test on a device."
