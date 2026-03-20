# Community Extensions

Optional AI-DLC extensions that aren't shipped with the core rules. Browse this folder, pick what fits your project, and install to your local rule set.

---

## For Users: Installing an Extension

Each extension lives in a subfolder with its own `README.md` explaining what it does and when to use it.

To install an extension:

1. Read the extension's `README.md` to confirm it fits your use case
2. Copy the `.md` rule files (everything **except** `README.md`) into your project's extensions directory:

| Platform | Target path |
|---|---|
| Kiro | `.kiro/aws-aidlc-rule-details/extensions/<category>/` |
| Amazon Q Developer | `.amazonq/aws-aidlc-rule-details/extensions/<category>/` |
| Cursor / Cline / Claude Code / GitHub Copilot | `.aidlc-rule-details/extensions/<category>/` |

3. Start a new AI-DLC session — the extension is auto-detected

The extension's `README.md` includes copy-paste install commands for each platform.

---

## For Authors: Writing an Extension

### File Structure

An extension lives in a named folder under the appropriate category:

```
**Cross-cutting extension** (security, compliance, accessibility):
```
community-extensions/
└── <category>/
    └── <extension-name>/
        ├── README.md                      <- installation guide (stays in repo, not copied)
        ├── <extension-name>.opt-in.md     <- opt-in question presented at Requirements Analysis
        └── <extension-name>.md            <- the rules
```

**Project-type extension** (brownfield, greyfield, or any new project type):
```
community-extensions/
└── project-type/
    └── <type-name>/
        ├── README.md                      <- installation guide (stays in repo, not copied)
        └── <type-name>.md                 <- rules file containing BOTH ## Project Type Registration
                                              AND ## Opt-In Prompt sections (no separate opt-in file)
```

The `README.md` stays in this repo for documentation. The `.md` rule files are what users copy into their projects.

Use `compliance/nist-800-53/` as a reference for cross-cutting extensions and `project-type/brownfield/` for project-type extensions.

---

### Opt-In Prompts — Every Extension Must Have One

Every extension must include an `## Opt-In Prompt` section so users can see exactly when and how they will be asked whether to enable it. Where that prompt lives depends on the extension type:

| Extension type | Where opt-in is defined | When presented to user |
|---|---|---|
| Cross-cutting (security, compliance, accessibility) | Separate `*.opt-in.md` file | Requirements Analysis |
| Project-type | `## Opt-In Prompt` section inside the rules `.md` file | Workspace Detection |

**Cross-cutting extensions** use a separate `*.opt-in.md` file. This allows the loader to scan and present opt-in questions without loading the full rules file (context efficiency).

**Project-type extensions** include the `## Opt-In Prompt` section directly in their rules file, alongside a `## Project Type Registration` section. Workspace Detection reads both sections to build the project type question and load the correct extension. There is no separate `.opt-in.md` file.

See `project-type/brownfield/brownfield.md` for a project-type example and `compliance/nist-800-53/nist-800-53.opt-in.md` for a cross-cutting example.

---

### Cross-Cutting Opt-In File Format

For cross-cutting extensions, create a `*.opt-in.md` file containing a `## Opt-In Prompt` section. This question is automatically included in the Requirements Analysis clarifying questions file.

```markdown
# <Extension Name> — Opt-In

**Extension**: <Extension Name>

## Opt-In Prompt

The following question is automatically included during Requirements Analysis:

\`\`\`markdown
## Question: <Extension Name>
<Question text — describe what enabling this extension does>

A) Yes — <describe enforcement behavior>
B) No — skip all <extension name> rules
X) Other (please describe after [Answer]: tag below)

[Answer]:
\`\`\`
```

See `compliance/nist-800-53/nist-800-53.opt-in.md` for a complete example.

---

### Rules File Format

The rules file (`<extension-name>.md`) should follow this structure:

```markdown
# <Extension Name> Rules

## Overview
[What this extension does and when it applies. One short paragraph.]

## Added Stages (if any)
[List any new workflow stages this extension introduces, with a reference to the
stage file. Specify where in the workflow the stage runs.]

## Stage Addendums (if any)
[Per-stage additions that inject into existing stage logic when this extension
is loaded. Keep each addendum short — a paragraph or a focused list.]

### <Stage Name> Addendum
[Content to add to this stage]

## Rules (if any)
### RULE-PREFIX-01: <Rule Name>
**Rule**: [Single, specific requirement]
**Verification**:
- [Concrete check the AI evaluates against the artifact]
- [Another concrete check]
```

---

### New Stages vs. Stage Addendums

**Add a new stage** when your extension introduces an entirely new workflow activity that has no equivalent in the core — for example, analyzing external resources, running a compliance pre-check, or generating a threat model. New stages reference a dedicated stage file (a `.md` file in the extension folder).

**Use a stage addendum** when your extension adds focused considerations to an existing core stage — for example, adding multi-package coordination to Workflow Planning or adding constraint checks to Code Generation. Addendums are short and reference the extension file, not a separate stage file.

---

### Rule Optimization Guidelines

- **One concern per rule**: Each rule ID addresses exactly one requirement. Don't bundle multiple concerns under one ID.
- **Verifiable criteria only**: Write Verification items that the AI can evaluate concretely against the artifacts it just produced. Avoid vague guidance like "ensure security is considered."
- **Reference, don't repeat**: If a core stage file already covers something, reference it. Don't copy its content into your extension.
- **Keep addendums short**: A stage addendum should be a paragraph or a short list, not a full stage rewrite. If it grows large, it belongs in a dedicated stage file instead.
- **Fail-fast blocking rules**: If your extension has blocking rules, define the exact condition that constitutes non-compliance so the AI can make a binary compliant/non-compliant determination without ambiguity.
- **Stage relevance**: Mark rules as N/A for stages where they genuinely don't apply — don't force every rule to evaluate at every stage.
