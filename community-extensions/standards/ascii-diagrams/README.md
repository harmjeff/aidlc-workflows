# ASCII Diagram Standards

Reference guide for drawing ASCII diagrams in AI-DLC artifacts. Install this if your project produces architecture diagrams, flow diagrams, or other visual content in markdown files and you want consistent, validated ASCII art.

---

## What It Provides

- Allowed character set (`+` `-` `|` `^` `v` `<` `>` and spaces only — no Unicode box-drawing)
- Character width rule (all lines in a box must be the same width)
- Standard patterns for boxes, nested boxes, arrows, horizontal flows, and vertical flows with labels
- Validation checklist

The core AI-DLC content validation rules (`common/content-validation.md`) already enforce the essential ASCII constraints inline. This extension provides the full pattern library, examples, and an opt-in question that enables strict enforcement during Requirements Analysis.

---

## How It Works

When installed, the opt-in question is presented during Requirements Analysis asking whether to enforce full ASCII diagram standards. If opted in, the full pattern library is loaded when generating diagrams. If opted out, the basic inline rules in `content-validation.md` still apply.

---

## Installing This Extension

Copy both files into your project's `extensions/standards/ascii-diagrams/` rule-details directory.

**Kiro:**
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/standards/ascii-diagrams
cp ascii-diagram-standards.md ascii-diagram-standards.opt-in.md .kiro/aws-aidlc-rule-details/extensions/standards/ascii-diagrams/
```

**Amazon Q Developer:**
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/standards/ascii-diagrams
cp ascii-diagram-standards.md ascii-diagram-standards.opt-in.md .amazonq/aws-aidlc-rule-details/extensions/standards/ascii-diagrams/
```

**Cursor / Cline / Claude Code / GitHub Copilot:**
```bash
mkdir -p .aidlc-rule-details/extensions/standards/ascii-diagrams
cp ascii-diagram-standards.md ascii-diagram-standards.opt-in.md .aidlc-rule-details/extensions/standards/ascii-diagrams/
```

Then start a new AI-DLC session. During Requirements Analysis you will be asked whether to enforce ASCII diagram standards for this project.
