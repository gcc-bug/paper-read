#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"

compile_deck() {
  local source_file="$1"
  local output_file="$2"
  local build_dir="$3"
  local stem="${source_file%.tex}"

  mkdir -p "$build_dir"
  if ! latexmk -xelatex -interaction=nonstopmode -halt-on-error \
    -outdir="$build_dir" "$source_file" > "$build_dir/$stem-build.log" 2>&1; then
    tail -60 "$build_dir/$stem-build.log"
    return 1
  fi
  cp "$build_dir/$stem.pdf" "$output_file"
  printf 'Built %s (main talk and appendix).\n' "$output_file"
}

compile_deck slides.tex 0918-calibration-zh.pdf build
compile_deck early-control-work.tex early-control-work-zh.pdf build/early-control-work
