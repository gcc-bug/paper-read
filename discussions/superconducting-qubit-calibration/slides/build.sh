#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p build
if ! latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -outdir=build slides.tex > build/slides-build.log 2>&1; then
  tail -60 build/slides-build.log
  exit 1
fi
cp build/slides.pdf 0918-calibration-zh.pdf
printf '%s\n' 'Built 0918-calibration-zh.pdf (full deck, including appendix).'
