#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p build/early-control-work
if ! latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -outdir=build/early-control-work early-control-work.tex \
  > build/early-control-work/build.log 2>&1; then
  tail -60 build/early-control-work/build.log
  exit 1
fi
cp build/early-control-work/early-control-work.pdf early-control-work-zh.pdf
printf '%s\n' 'Built early-control-work-zh.pdf (main talk and appendix).'
