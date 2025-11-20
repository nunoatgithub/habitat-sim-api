#!/usr/bin/env bash
set -euo pipefail

# Build script for habitat-sim-api 0.3.3 supporting flavor selection
# Usage: ./build.sh [--with-all-types|--with-public-types|--with-packages] [--no-build] [--outdir DIR]

VERSION="0.3.3"
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTDIR_DEFAULT="$SELF_DIR/dist"
DO_BUILD=1
OUTDIR="$OUTDIR_DEFAULT"
FLAVOR="with-all-types"
FLAVOR_COUNT=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-all-types)
      FLAVOR="with-all-types"; FLAVOR_COUNT=$((FLAVOR_COUNT+1)); shift;;
    --with-public-types)
      FLAVOR="with-public-types"; FLAVOR_COUNT=$((FLAVOR_COUNT+1)); shift;;
    --with-packages)
      FLAVOR="with-packages"; FLAVOR_COUNT=$((FLAVOR_COUNT+1)); shift;;
    --no-build)
      DO_BUILD=0; shift;;
    --outdir)
      OUTDIR="$2"; shift 2;;
    --help|-h)
      echo "Usage: $0 [--with-all-types|--with-public-types|--with-packages] [--no-build] [--outdir DIR]"; exit 0;;
    *)
      echo "Unknown arg: $1"; exit 2;;
  esac
done

if [[ $FLAVOR_COUNT -gt 1 ]]; then
  echo "Error: Only one flavor can be selected." >&2
  exit 2
fi

# Clean previous temp build dir if exists
rm -rf "$SELF_DIR/habitat_sim_api_temp"

# Copy selected flavor to temp build dir
cp -r "$SELF_DIR/$FLAVOR" "$SELF_DIR/habitat_sim_api_temp"

# Patch pyproject.toml/setup.cfg/MANIFEST.in if needed (not required for static flavors)

mkdir -p "$OUTDIR"

if [[ $DO_BUILD -eq 1 ]]; then
  echo "Building flavor: $FLAVOR (python -m build --sdist --wheel --outdir $OUTDIR)"
  (cd "$SELF_DIR" && PYTHONPATH="$SELF_DIR/habitat_sim_api_temp" python -m build --sdist --wheel --outdir "$OUTDIR")
  echo "Artifacts placed in $OUTDIR"
else
  echo "Prepared package in $SELF_DIR. To build manually: cd $SELF_DIR && python -m build --sdist --wheel --outdir $OUTDIR"
fi

# Clean up temp build dir
rm -rf "$SELF_DIR/habitat_sim_api_temp"
# Remove temporary build directory created during packaging
rm -rf "$SELF_DIR/build"

exit 0
