# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec for design-reviewer
#
# Bundles:
#   - config/patterns/   (15 architectural pattern markdown files)
#   - config/prompts/    (critique/alternatives/gap prompt markdown files)
#   - reporting/templates/ (Jinja2 .jinja2 templates, loaded via importlib.resources)
#
# Build:
#   uv run pyinstaller design-reviewer.spec
#   or: pyinstaller design-reviewer.spec
#
# Output: dist/design-reviewer  (single-file executable)

import os
from pathlib import Path

src_root = Path("src/design_reviewer")

datas = [
    # Config data files shipped alongside the package
    ("config/patterns", "config/patterns"),
    ("config/prompts", "config/prompts"),
    # Jinja2 templates — importlib.resources resolves these as package data,
    # so they must live under the package path inside the bundle.
    (str(src_root / "reporting/templates"), "design_reviewer/reporting/templates"),
]

a = Analysis(
    ["src/design_reviewer/cli/cli.py"],
    pathex=["src"],
    binaries=[],
    datas=datas,
    hiddenimports=[
        # strands-agents uses dynamic plugin loading
        "strands",
        # pydantic v2 validators are loaded lazily
        "pydantic.v1",
        # boto3/botocore endpoint data
        "botocore",
        "boto3",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="design-reviewer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    codesign_identity=None,
    entitlements_file=None,
)
