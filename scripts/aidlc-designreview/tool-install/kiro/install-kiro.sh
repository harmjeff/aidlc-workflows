#!/usr/bin/env bash
# AIDLC Design Review - Kiro Installer
# Version: 1.0
#
# Installs the design reviewer as a Kiro steering-file agent.
# The steering file teaches Kiro's AI to invoke design-reviewer when asked.
#
# Usage:
#   ./scripts/aidlc-designreview/tool-install/kiro/install-kiro.sh

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOL_INSTALL_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

print_success() { echo -e "${GREEN}✓${NC} $1"; }
print_error()   { echo -e "${RED}✗${NC} $1"; }
print_warning() { echo -e "${YELLOW}⚠${NC} $1"; }
print_info()    { echo -e "${BLUE}ℹ${NC} $1"; }

# ============================================================================
# Workspace Root Detection (same priority algorithm as install-mac.sh)
# ============================================================================

find_workspace_root() {
    local current_dir="$SCRIPT_DIR"
    local max_depth=10
    local depth=0
    local fallback_dir=""

    while [ "$current_dir" != "/" ] && [ $depth -lt $max_depth ]; do
        if [ -d "$current_dir/.git" ] || [ -d "$current_dir/aidlc-rules" ]; then
            echo "$current_dir"
            return 0
        fi
        if [ -f "$current_dir/pyproject.toml" ] && [ -z "$fallback_dir" ]; then
            fallback_dir="$current_dir"
        fi
        current_dir="$(cd "$current_dir/.." && pwd)"
        depth=$((depth + 1))
    done

    [ -n "$fallback_dir" ] && echo "$fallback_dir" && return 0
    echo "$(cd "${SCRIPT_DIR}/../.." && pwd)"
}

# ============================================================================
# Main
# ============================================================================

echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     AIDLC Design Review - Kiro Agent Installer                ║${NC}"
echo -e "${BLUE}║                     Version 1.0                               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

WORKSPACE_DIR="$(find_workspace_root)"
KIRO_DIR="${WORKSPACE_DIR}/.kiro"
STEERING_DIR="${KIRO_DIR}/steering"

print_info "Detected workspace: $WORKSPACE_DIR"
print_info "Steering target:    $STEERING_DIR"
echo ""

# ---- Dependency check ----

if command -v design-reviewer &>/dev/null; then
    print_success "design-reviewer CLI found"
else
    print_warning "design-reviewer not found in PATH"
    echo "  Install with: pip install -e scripts/aidlc-designreview"
fi
echo ""

# ---- Install steering file ----

print_info "Installing steering file..."
mkdir -p "$STEERING_DIR"
cp "${SCRIPT_DIR}/design-reviewer.md" "${STEERING_DIR}/design-reviewer.md"
print_success "Copied .kiro/steering/design-reviewer.md"

# ---- Install patterns ----

print_info "Installing architectural patterns..."
mkdir -p "${KIRO_DIR}/patterns"
cp "${TOOL_INSTALL_DIR}/patterns/"*.md "${KIRO_DIR}/patterns/"
print_success "Copied $(ls "${TOOL_INSTALL_DIR}/patterns/"*.md | wc -l | tr -d ' ') pattern files to .kiro/patterns/"

# ---- Install config (preserve existing) ----

CONFIG_TARGET="${KIRO_DIR}/review-config.yaml"
if [ ! -f "$CONFIG_TARGET" ]; then
    print_info "Installing default configuration..."
    cp "${TOOL_INSTALL_DIR}/review-config.yaml.example" "$CONFIG_TARGET"
    print_success "Copied .kiro/review-config.yaml"
else
    print_info "Existing .kiro/review-config.yaml preserved"
fi

echo ""

# ---- Validation ----

print_info "Validating installation..."
ERRORS=0

for f in \
    ".kiro/steering/design-reviewer.md" \
    ".kiro/review-config.yaml"; do
    if [ -f "${WORKSPACE_DIR}/${f}" ]; then
        print_success "$f"
    else
        print_error "Missing: $f"
        ERRORS=$((ERRORS + 1))
    fi
done

PATTERN_COUNT=$(ls "${KIRO_DIR}/patterns/"*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$PATTERN_COUNT" -gt 0 ]; then
    print_success ".kiro/patterns/ ($PATTERN_COUNT files)"
else
    print_error ".kiro/patterns/ is empty or missing"
    ERRORS=$((ERRORS + 1))
fi

echo ""
if [ "$ERRORS" -gt 0 ]; then
    print_error "Installation completed with $ERRORS error(s)"
    exit 1
fi
print_success "Validation passed"
echo ""

# ---- Summary ----

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Installation Complete!${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Kiro now knows how to run the AIDLC Design Reviewer."
echo "In Kiro, just ask: \"review my design\" or \"run the design review\""
echo ""
echo -e "${BLUE}Steering file:${NC}  ${STEERING_DIR}/design-reviewer.md"
echo -e "${BLUE}Patterns:${NC}       ${KIRO_DIR}/patterns/ ($PATTERN_COUNT files)"
echo -e "${BLUE}Configuration:${NC}  ${CONFIG_TARGET}"
echo -e "${BLUE}Reports:${NC}        aidlc-docs/review/"
echo ""
echo -e "${GREEN}Done!${NC}"
echo ""
