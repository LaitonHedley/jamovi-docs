#!/usr/bin/env bash
# Convert GIF animations to WebM + MP4 for use with <video> elements.
# Requires: ffmpeg
set -euo pipefail

IMAGES_DIR="public/images"

for gif in "${IMAGES_DIR}"/*.gif; do
  base="${gif%.gif}"
  name=$(basename "$base")

  # WebM (VP9) — best compression, supported by all modern browsers
  ffmpeg -i "$gif" \
    -c:v libvpx-vp9 -b:v 0 -crf 33 \
    -vf "split[s0][s1];[s0]palettegen=reserve_transparent=0[p];[s1][p]paletteuse" \
    -an -loop 0 \
    "${base}.webm" -y

  # MP4 (H.264) — Safari fallback
  ffmpeg -i "$gif" \
    -c:v libx264 -pix_fmt yuv420p -movflags faststart \
    -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" \
    -an \
    "${base}.mp4" -y

  echo "Converted: $name.gif → $name.webm + $name.mp4"
done
echo "Done."
