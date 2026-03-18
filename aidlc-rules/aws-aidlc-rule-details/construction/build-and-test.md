# Build and Test (Lite)

**Purpose**: Verify the generated code builds and basic tests pass.

Lite mode focuses on build verification and unit tests only. No integration tests, performance tests, security tests, or e2e tests.

## Prerequisites
- Code Generation must be complete
- All code artifacts must be generated

## Step 1: Generate Build Instructions

Create `aidlc-docs/construction/build-and-test/build-instructions.md`:

```markdown
# Build Instructions

## Prerequisites
- **Runtime**: [Language runtime and version]
- **Build Tool**: [Tool name and version]
- **Dependencies**: [How to install]

## Build Steps

### 1. Install Dependencies
\`\`\`bash
[Command to install dependencies]
\`\`\`

### 2. Build
\`\`\`bash
[Command to build]
\`\`\`

### 3. Run
\`\`\`bash
[Command to run the application]
\`\`\`
```

## Step 2: Generate Unit Test Instructions

Create `aidlc-docs/construction/build-and-test/unit-test-instructions.md`:

```markdown
# Unit Test Instructions

## Run Tests
\`\`\`bash
[Command to run unit tests]
\`\`\`

## Expected Results
- **Total Tests**: [Number]
- **Expected**: All pass
```

## Step 3: Execute Build and Tests (If Possible)

If the AI has the ability to execute commands:
1. Run the build command
2. Run the unit tests
3. Report results

If the AI cannot execute commands:
1. Present the build and test instructions for the user to run
2. Ask user to report any issues

## Step 4: Update State

Update `aidlc-docs/aidlc-state.md`:
- Mark Build and Test as complete

## Step 5: Present Results

```markdown
# Build and Test Complete

**Build**: [Success/Failed/Instructions provided]
**Tests**: [X passed, Y failed / Instructions provided]

**To get started:**
1. [Install command]
2. [Build command]
3. [Run command]

Your prototype is ready! You can iterate on it by asking for changes.
```

## Completion

The AI-DLC Lite workflow is now complete. The user has:
- A requirements document
- Working application code
- Basic unit tests
- Build and run instructions

The user can now iterate on the prototype by requesting changes directly.
