#!/usr/bin/env bash
set -euo pipefail

# Build script for habitat-sim-api 0.2.2 supporting flavor selection
# Usage: ./build.sh --with-all-types|--with-public-types|--with-packages

VERSION="0.2.2"
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTDIR="$SELF_DIR/dist"
FLAVOR=""
FLAVOR_COUNT=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-all-types)
      FLAVOR="with-all-types"; FLAVOR_COUNT=$((FLAVOR_COUNT+1)); shift;;
    --with-public-types)
      FLAVOR="with-public-types"; FLAVOR_COUNT=$((FLAVOR_COUNT+1)); shift;;
    --with-packages)
      FLAVOR="with-packages"; FLAVOR_COUNT=$((FLAVOR_COUNT+1)); shift;;
    --help|-h)
      echo "Usage: $0 --with-all-types|--with-public-types|--with-packages"; exit 0;;
    *)
      echo "Unknown arg: $1"; exit 2;;
  esac
done

if [[ $FLAVOR_COUNT -gt 1 ]]; then
  echo "Error: Only one flavor can be selected." >&2
  exit 2
fi
if [[ $FLAVOR_COUNT -eq 0 ]]; then
  echo "Error: You must specify exactly one flavor: --with-all-types, --with-public-types, or --with-packages." >&2
  exit 2
fi

# Clean previous temp build dir if exists
rm -rf "$SELF_DIR/habitat_sim_api_temp"

# Copy selected flavor to temp build dir
cp -r "$SELF_DIR/$FLAVOR" "$SELF_DIR/habitat_sim_api_temp"

mkdir -p "$OUTDIR"

echo "Building flavor: $FLAVOR (python -m build --sdist --wheel --outdir $OUTDIR)"
(cd "$SELF_DIR" && PYTHONPATH="$SELF_DIR/habitat_sim_api_temp" python -m build --sdist --wheel --outdir "$OUTDIR")
echo "Artifacts placed in $OUTDIR"

# Clean up temp build dir
rm -rf "$SELF_DIR/habitat_sim_api_temp"
# Remove temporary build directory created during packaging
rm -rf "$SELF_DIR/build"

exit 0
