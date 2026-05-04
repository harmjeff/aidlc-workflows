# Extensions

This folder is read by the AI-DLC rules loader at workflow start. Place installed extension files here — the AI will automatically detect and load them.

**This README file is not processed by the extensions loader.** The loader scans subdirectories only.

---

## Available Extensions

| Extension | Category | Description |
|---|---|---|
| `security/baseline/` | security | OWASP-mapped security rules |
| `testing/property-based/` | testing | Property-based testing rules |
| `compliance/nist-800-53/` | compliance | NIST 800-53 controls mapped to AWS Control Tower, Config Rules, Security Hub, and GuardDuty |

---

## NIST 800-53 Compliance Controls

**Version**: 0.2.0

Maps ~90 NIST 800-53 controls to specific AWS mechanisms. When enabled, the workflow enforces applicable controls at each stage.

**Coverage:**
- **AC** (Access Control): AC-3, AC-4, AC-6, AC-12, AC-17, AC-22 + enhancements
- **AU** (Audit & Accountability): AU-2, AU-3, AU-5(2), AU-6, AU-12
- **CA** (Assessment & Monitoring): CA-3, CA-7

**Control Types**: Preventive (SCP, Declarative Policy), Proactive (CF Hook), Detective (Config Rule, Security Hub)

**Files:**
- `compliance/nist-800-53/nist-800-53-controls.md` — Full control mappings
- `compliance/nist-800-53/nist-800-53.opt-in.md` — Opt-in metadata

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
