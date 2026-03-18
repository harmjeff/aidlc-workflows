# Code Generation (Lite)

**Purpose**: Generate working code in a single pass.

**No separate planning step.** Read the requirements and generate code directly.

## Prerequisites
- Requirements Analysis must be complete
- Requirements document must be available at `aidlc-docs/inception/requirements/requirements.md`
- Reverse engineering artifacts loaded (if brownfield)

## Step 1: Load Context

- Read `aidlc-docs/inception/requirements/requirements.md`
- Read `aidlc-docs/aidlc-state.md` for project type and workspace root
- **IF brownfield**: Read reverse engineering artifacts:
  - `aidlc-docs/inception/reverse-engineering/architecture.md`
  - `aidlc-docs/inception/reverse-engineering/code-structure.md`

## Step 2: Determine Code Location

- **Brownfield**: Use existing project structure (e.g., `src/main/java/`, `lib/`, `pkg/`)
- **Greenfield**: Create sensible structure at workspace root:
  - `src/` for application code
  - `tests/` for test code
  - Configuration files at workspace root
- **NEVER** put application code in `aidlc-docs/`

## Step 3: Generate Code

Generate all application code in a single pass:

1. **Project setup** (greenfield only):
   - Create project configuration (package.json, pom.xml, requirements.txt, etc.)
   - Set up directory structure
   - Add dependency declarations

2. **Application code**:
   - Generate all source files based on requirements
   - Use sensible defaults for architecture (no need to ask about patterns)
   - Follow standard conventions for the chosen language/framework
   - Keep it simple - this is a prototype

3. **Basic unit tests**:
   - Generate tests for core business logic
   - Focus on happy path and key edge cases
   - Don't aim for comprehensive coverage - basic verification is sufficient

4. **Configuration files**:
   - Environment configuration
   - Build configuration
   - Any necessary scaffolding

### Brownfield Rules
- Check if target file exists before generating
- If file exists: Modify it in-place (NEVER create copies like `ClassName_modified.java`)
- If file doesn't exist: Create new file
- Respect existing code style and patterns

### Automation-Friendly Code
When generating UI code, add `data-testid` attributes to interactive elements:
- Use consistent naming: `{component}-{element-role}` (e.g., `login-form-submit-button`)
- Avoid dynamic or auto-generated IDs

## Step 4: Update State

Update `aidlc-docs/aidlc-state.md`:
- Mark Code Generation as complete

## Step 5: Present Results

```markdown
# Code Generation Complete

**Files generated:**
- `[path/to/file1]` - [Purpose]
- `[path/to/file2]` - [Purpose]
- `[path/to/file3]` - [Purpose]
...

**What was built:**
- [Brief summary of what was implemented]

**What was NOT built (out of scope for prototype):**
- [Items deferred]

Would you like to make any changes, or shall I proceed to Build and Test?
```

## Step 6: Handle Response

- If user approves: Proceed to Build and Test
- If user requests changes: Make the changes and present updated results
- Iterate until user is satisfied
