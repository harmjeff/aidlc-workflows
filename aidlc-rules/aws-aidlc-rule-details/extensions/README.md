# Extensions

This folder is read by the AI-DLC rules loader at workflow start. Place installed extension files here — the AI will automatically detect and load them.

**This README file is not processed by the extensions loader.** The loader scans subdirectories only.

---

## This Folder Is Empty by Default

No extensions ship with the core AI-DLC rules. Install only what your project needs.

---

## Finding Extensions

Browse the `community-extensions/` folder in the AI-DLC repository. Each extension has its own subfolder with a README describing what it does and when to use it.

Available extension categories:
- `community-extensions/project-type/` — project type extensions (brownfield, greyfield)
- `community-extensions/security/` — security and compliance rules

---

## Installing an Extension

Each extension's README includes copy-paste install commands. The general pattern is to copy the extension's rule files (`.md` files, not the README) into the matching subfolder here, preserving the category structure.

Example — installing the security baseline:
```bash
mkdir -p extensions/security/baseline
cp community-extensions/security/baseline/security-baseline.md extensions/security/baseline/
cp community-extensions/security/baseline/security-baseline.opt-in.md extensions/security/baseline/
```

Then start a new AI-DLC session to load the extension.

---

## How the Loader Works

At workflow start, the AI scans subdirectories under `extensions/`:

- A subfolder containing a `*.opt-in.md` file is an **opt-in extension** — the user is asked during Requirements Analysis whether to enable it for this project
- A subfolder with rule `.md` files but no `*.opt-in.md` is **always enforced** — its rules are loaded immediately at workflow start
- The `project-type/` subfolder is **excluded from this scan** — project-type extensions are loaded by Workspace Detection based on the user's project type selection, not by the standard opt-in mechanism
