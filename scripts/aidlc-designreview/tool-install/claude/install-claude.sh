#!/usr/bin/env bash
# AIDLC Design Review - Claude Code Agent Installer
# Version: 1.0
#
# Installs the design reviewer as a Claude Code subagent.
# The subagent uses Claude's built-in Read/Glob/Write tools to discover
# design artifacts and produce the review entirely within Claude Code —
# no external CLI or AWS credentials required.
#
# Usage:
#   ./scripts/aidlc-designreview/tool-install/claude/install-claude.sh

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
echo -e "${BLUE}║     AIDLC Design Review - Claude Code Agent Installer         ║${NC}"
echo -e "${BLUE}║                     Version 1.0                               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

WORKSPACE_DIR="$(find_workspace_root)"
CLAUDE_DIR="${WORKSPACE_DIR}/.claude"
AGENTS_DIR="${CLAUDE_DIR}/agents"
DR_DIR="${CLAUDE_DIR}/design-reviewer"

print_info "Detected workspace: $WORKSPACE_DIR"
print_info "Agents target:      $AGENTS_DIR"
echo ""

# ---- Create directory structure ----

print_info "Creating .claude directory structure..."
mkdir -p "$AGENTS_DIR"
mkdir -p "${DR_DIR}/patterns"
mkdir -p "${DR_DIR}/prompts"
print_success "Directories created"

# ---- Install subagent definition ----

print_info "Installing subagent definition..."
cp "${SCRIPT_DIR}/design-reviewer.md" "${AGENTS_DIR}/aidlc-design-reviewer.md"
print_success "Copied .claude/agents/aidlc-design-reviewer.md"

# ---- Install patterns ----

print_info "Installing architectural patterns..."
cp "${TOOL_INSTALL_DIR}/patterns/"*.md "${DR_DIR}/patterns/"
PATTERN_COUNT=$(ls "${DR_DIR}/patterns/"*.md 2>/dev/null | wc -l | tr -d ' ')
print_success "Copied $PATTERN_COUNT pattern files to .claude/design-reviewer/patterns/"

# ---- Install prompts ----

print_info "Installing agent prompts..."
cp "${TOOL_INSTALL_DIR}/prompts/"*.md "${DR_DIR}/prompts/"
PROMPT_COUNT=$(ls "${DR_DIR}/prompts/"*.md 2>/dev/null | wc -l | tr -d ' ')
print_success "Copied $PROMPT_COUNT prompt files to .claude/design-reviewer/prompts/"

# ---- Validation ----

echo ""
print_info "Validating installation..."
ERRORS=0

for f in \
    ".claude/agents/aidlc-design-reviewer.md" \
    ".claude/design-reviewer/prompts/critique-v1.md" \
    ".claude/design-reviewer/prompts/alternatives-v1.md" \
    ".claude/design-reviewer/prompts/gap-v1.md"; do
    if [ -f "${WORKSPACE_DIR}/${f}" ]; then
        print_success "$f"
    else
        print_error "Missing: $f"
        ERRORS=$((ERRORS + 1))
    fi
done

if [ "$PATTERN_COUNT" -gt 0 ]; then
    print_success ".claude/design-reviewer/patterns/ ($PATTERN_COUNT files)"
else
    print_error ".claude/design-reviewer/patterns/ is empty or missing"
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
echo "The AIDLC Design Reviewer is now available as a Claude Code subagent."
echo "No AWS credentials or external tools required — Claude performs the"
echo "review entirely within its own session using Read, Glob, and Write."
echo ""
echo -e "${BLUE}Usage:${NC}"
echo "  Claude will invoke the subagent automatically when you say:"
echo "    \"review my design\""
echo "    \"run the design review\""
echo "    \"check my design artifacts\""
echo ""
echo "  Or invoke it explicitly with:"
echo "    @\"aidlc-design-reviewer (agent)\" review my design"
echo ""
echo -e "${BLUE}Subagent:${NC}  ${AGENTS_DIR}/aidlc-design-reviewer.md"
echo -e "${BLUE}Patterns:${NC}  ${DR_DIR}/patterns/ ($PATTERN_COUNT files)"
echo -e "${BLUE}Prompts:${NC}   ${DR_DIR}/prompts/ ($PROMPT_COUNT files)"
echo -e "${BLUE}Reports:${NC}   aidlc-docs/review/ (markdown)"
echo ""
echo -e "${YELLOW}Note:${NC} HTML reports require the Python CLI tool (design-reviewer)."
echo "  Install with: pip install -e scripts/aidlc-designreview"
echo ""
echo -e "${GREEN}Done!${NC}"
echo ""
