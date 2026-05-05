#!/usr/bin/env bash
# Build the design-reviewer standalone executable with PyInstaller.
#
# Usage:
#   ./build.sh          # build to dist/design-reviewer
#   ./build.sh --clean  # remove build/ and dist/ first, then build
#
# Requirements: uv must be installed (https://docs.astral.sh/uv/)
# PyInstaller is listed in [dependency-groups] dev in pyproject.toml.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [[ "${1:-}" == "--clean" ]]; then
    echo "Cleaning build artifacts..."
    rm -rf build dist
fi

echo "Building design-reviewer..."
uv run pyinstaller design-reviewer.spec

echo ""
echo "Build complete: dist/design-reviewer"
echo "Test with: ./dist/design-reviewer --help"
