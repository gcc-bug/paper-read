#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p build
for entry in slides main; do
  if ! latexmk -xelatex -interaction=nonstopmode -halt-on-error \
    -outdir=build "${entry}.tex" > "build/${entry}-build.log" 2>&1; then
    tail -60 "build/${entry}-build.log"
    exit 1
  fi
done
cp build/slides.pdf 0918-calibration-zh.pdf
cp build/main.pdf 0918-calibration-main-zh.pdf
printf '%s\n' 'Built 0918-calibration-main-zh.pdf and 0918-calibration-zh.pdf.'
