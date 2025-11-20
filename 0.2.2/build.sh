#!/usr/bin/env bash
set -euo pipefail

# Minimal in-place build script for habitat-sim-api 0.2.2
# This script is intentionally static: uses committed pyproject.toml / setup.cfg / MANIFEST.in
# Usage: ./build.sh [--no-build]

VERSION="0.2.2"
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTDIR_DEFAULT="$SELF_DIR/dist"
DO_BUILD=1
OUTDIR="$OUTDIR_DEFAULT"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-build)
      DO_BUILD=0; shift;;
    --outdir)
      OUTDIR="$2"; shift 2;;
    --help|-h)
      sed -n '1,160p' "${BASH_SOURCE[0]}"; exit 0;;
    *)
      echo "Unknown arg: $1"; exit 2;;
  esac
done

mkdir -p "$OUTDIR"

if [[ $DO_BUILD -eq 1 ]]; then
  echo "Building in-place: python -m build --sdist --wheel --outdir $OUTDIR"
  (cd "$SELF_DIR" && python -m build --sdist --wheel --outdir "$OUTDIR")
  echo "Artifacts placed in $OUTDIR"
else
  echo "Prepared package in $SELF_DIR. To build manually: cd $SELF_DIR && python -m build --sdist --wheel --outdir $OUTDIR"
fi

# Remove temporary build directory created during packaging
rm -rf "$SELF_DIR/build"

exit 0
