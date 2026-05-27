#!/usr/bin/env bash
set -euo pipefail

SECTIONS=(usermanual analyses data howto spss2jamovi)
OUTBASE="src/content/docs"

for section in "${SECTIONS[@]}"; do
  mkdir -p "${OUTBASE}/${section}"
  for rst in "${section}"/*.rst; do
    [ -f "$rst" ] || continue
    base=$(basename "$rst" .rst | tr '[:upper:]' '[:lower:]')
    out="${OUTBASE}/${section}/${base}.mdx"
    pandoc "$rst" \
      -f rst \
      -t markdown \
      --wrap=none \
      --markdown-headings=atx \
      -o "$out"
    echo "Converted: $rst → $out"
  done
done
echo "Done. Run python3 scripts/postprocess-mdx.py next."
