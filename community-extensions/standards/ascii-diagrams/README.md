# ASCII Diagram Standards

Reference guide for drawing ASCII diagrams in AI-DLC artifacts. Install this if your project produces architecture diagrams, flow diagrams, or other visual content in markdown files and you want consistent, validated ASCII art.

---

## What It Provides

- Allowed character set (`+` `-` `|` `^` `v` `<` `>` and spaces only — no Unicode box-drawing)
- Character width rule (all lines in a box must be the same width)
- Standard patterns for boxes, nested boxes, arrows, horizontal flows, and vertical flows with labels
- Validation checklist

The core AI-DLC content validation rules (`common/content-validation.md`) already enforce the essential ASCII constraints inline. This file provides the full pattern library and examples.

---

## Installing This Extension

Copy `ascii-diagram-standards.md` into your project's `common/` rule-details directory so the AI can reference it when generating diagrams.

**Kiro:**
```bash
cp ascii-diagram-standards.md .kiro/aws-aidlc-rule-details/common/
```

**Amazon Q Developer:**
```bash
cp ascii-diagram-standards.md .amazonq/aws-aidlc-rule-details/common/
```

**Cursor / Cline / Claude Code / GitHub Copilot:**
```bash
cp ascii-diagram-standards.md .aidlc-rule-details/common/
```

Once installed, `content-validation.md` will automatically load it when validating ASCII diagrams.
