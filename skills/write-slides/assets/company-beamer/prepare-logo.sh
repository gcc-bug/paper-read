#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
# Convert the horizontal second artboard without rasterizing the artwork.
brand_tmp="$(mktemp -d)"
trap 'rm -rf -- "$brand_tmp"' EXIT
mutool merge -o "$brand_tmp/page.pdf" 'brand/弧光量子 源文件.ai' 2
pdfcrop --margins 4 "$brand_tmp/page.pdf" "$brand_tmp/logo.pdf"
cp "$brand_tmp/logo.pdf" brand/logo.pdf
