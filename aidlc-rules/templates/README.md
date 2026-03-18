# AIDLC Workflow Templates

This directory contains reusable templates for the AIDLC workflow. These templates are referenced throughout the workflow detail files to reduce duplication and maintain consistency.

## Template Files

### Core Templates

1. **audit-log-entry.md** - Standard format for all audit log entries
   - Used in: All stages
   - Purpose: Consistent logging of all workflow interactions

2. **question-format.md** - Standard format for all questions
   - Used in: All stages that collect user input
   - Purpose: Structured question collection with [Answer]: tags

3. **completion-message-2-option.md** - Standardized completion message
   - Used in: All construction stages
   - Purpose: Consistent 2-option completion format (Request Changes / Continue)

4. **plan-structure.md** - Standard structure for plan files
   - Used in: All stages that create plans
   - Purpose: Consistent plan file structure with checkboxes

5. **approval-prompt.md** - Standard format for approval requests
   - Used in: All stages that require user approval
   - Purpose: Consistent approval request format

## Usage Guidelines

### Referencing Templates

When referencing a template in a detail file, use this format:

```markdown
**See Template:** `templates/[template-name].md` for the standard format.
```

Or for inline reference:

```markdown
**Format:** See `templates/audit-log-entry.md` for the standard audit log format.
```

### Template Consistency

All templates follow these principles:
- Clear purpose statement
- Usage instructions
- Field descriptions
- Complete examples
- Critical rules
- Common pitfalls to avoid

### Updating Templates

When updating a template:
1. Ensure changes are backward compatible
2. Update all references in detail files
3. Document the change in this README
4. Test with actual workflow execution

## Template Categories

### Logging Templates
- audit-log-entry.md

### User Interaction Templates
- question-format.md
- approval-prompt.md
- completion-message-2-option.md

### Planning Templates
- plan-structure.md

## Benefits of Templates

1. **Consistency:** All stages use the same formats
2. **Maintainability:** Update once, apply everywhere
3. **Reduced File Size:** Detail files reference templates instead of duplicating content
4. **Clarity:** Templates provide clear examples and rules
5. **Quality:** Standardized formats prevent errors and omissions

## Template Versioning

Templates are versioned with the workflow. When making breaking changes:
1. Create a new template version
2. Update references gradually
3. Deprecate old templates with migration guide
4. Remove old templates after migration complete

## Future Templates

Potential templates to add:
- Artifact structure templates (per artifact type)
- State tracking format
- Error handling format
- Session continuity format
- Mermaid diagram templates

## Questions or Issues

If you have questions about templates or find issues:
1. Check the template file for detailed usage instructions
2. Review examples in the template
3. Check detail files for reference examples
4. Consult the core workflow documentation
