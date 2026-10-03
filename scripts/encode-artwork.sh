#!/usr/bin/env bash
# Erzeugt die WebP-Dateien eines Gemäldes nach docs/handbuch.md, Kapitel „Bilder“.
# Aufruf: scripts/encode-artwork.sh <id> <originaldatei>
# Ergebnis: web/public/art/<id>-{480,800,1200}.webp. Originale gehören nicht ins Repository.
# Voraussetzungen: ImageMagick 7 (`magick`) und ein sRGB-Profil (Standard: Ghostscript, sonst SRGB_PROFILE setzen).
set -euo pipefail

id="$1"
src="$2"
out="$(dirname "$0")/../web/public/art"
srgb="${SRGB_PROFILE:-/usr/share/ghostscript/iccprofiles/srgb.icc}"

# Eingebettete Nicht-sRGB-Profile (etwa Adobe RGB, eciRGB) vor dem Entfernen der Metadaten umrechnen.
profile=$(magick identify -format '%[icc:description]' "$src" 2>/dev/null || true)
convert_args=()
if [[ -n "$profile" && "$profile" != *sRGB* ]]; then
  convert_args=(-profile "$srgb")
fi

original_width=$(magick identify -format '%w' "$src")
if ((original_width < 1200)); then
  echo "Original ist nur ${original_width} px breit; das Handbuch verlangt mindestens 1200 px." >&2
  exit 1
fi
for width in 480 800 1200; do
  magick "$src" -auto-orient "${convert_args[@]}" -strip -resize "${width}x" -quality 83 \
    "$out/$id-$width.webp"
done

echo "$id: Profil „${profile:-keins}“, umgerechnet: $([[ ${#convert_args[@]} -gt 0 ]] && echo ja || echo nein)"
echo "SHA-256 des Originals: $(sha256sum "$src" | cut -d' ' -f1)"
echo "Mittlere Farbe: #$(magick "$out/$id-800.webp" -resize '1x1!' -format '%[hex:p{0,0}]' info:)"
