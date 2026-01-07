#!/bin/bash
# Generate Agent Skills format from source of truth
#
# Usage: ./scripts/generate-skills.sh <version>
# Example: ./scripts/generate-skills.sh 1.2.0

set -e

VERSION="${1:-0.0.0}"
SOURCE_DIR="aidlc-rules/aws-aidlc-rule-details"
SKILLS_DIR="dist/skills/ai-dlc-methodology"
TEMPLATE_FILE="scripts/templates/SKILL.md.template"

echo "Generating Agent Skills format (version $VERSION)"

# Create skills directory structure
mkdir -p "$SKILLS_DIR/references/common"
mkdir -p "$SKILLS_DIR/references/inception"
mkdir -p "$SKILLS_DIR/references/construction"
mkdir -p "$SKILLS_DIR/references/operations"

# Generate SKILL.md from template with version
sed "s/{{VERSION}}/$VERSION/g" "$TEMPLATE_FILE" > "$SKILLS_DIR/SKILL.md"

# Copy core workflow
cp "aidlc-rules/aws-aidlc-rules/core-workflow.md" "$SKILLS_DIR/references/core-workflow.md"

# Copy phase files
for phase in common inception construction operations; do
  for file in "$SOURCE_DIR/$phase"/*.md; do
    if [ -f "$file" ]; then
      cp "$file" "$SKILLS_DIR/references/$phase/"
    fi
  done
done

echo "Skills directory generated at $SKILLS_DIR"
find "$SKILLS_DIR" -type f | wc -l | xargs echo "Total files:"
