# Extensions

This folder is read by the AI-DLC rules loader at workflow start. Place installed extension files here — the AI will automatically detect and load them.

**This README file is not processed by the extensions loader.** The loader scans subdirectories only.

---

## Available Extensions

| Extension | Category | Description |
|---|---|---|
| `security/baseline/` | security | OWASP-mapped security rules |
| `testing/property-based/` | testing | Property-based testing rules |

---

## How the Loader Works

At workflow start, the AI scans subdirectories under `extensions/`:

1. A subfolder containing a `*.opt-in.md` file is an **opt-in extension** — during Requirements Analysis, a consolidated selection menu is presented listing all available extensions for the user to choose from
2. A subfolder with rule `.md` files but no `*.opt-in.md` is **always enforced** — its rules are loaded immediately at workflow start
3. The `project-type/` subfolder is **excluded from this scan** — project-type extensions are loaded by Workspace Detection

---

## Installing Community Extensions

Community extensions are hosted in external repositories and listed in `community-extensions-index.yaml` at the repo root. To install one, copy its rule files into the matching category subdirectory here:

```bash
mkdir -p extensions/<category>/<extension-name>
cp <source>/*.opt-in.md <source>/*-rules.md extensions/<category>/<extension-name>/
```

Then start a new AI-DLC session to load the extension.

---
