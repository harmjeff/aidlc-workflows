"""Adapter registry — discover and instantiate CLI adapters by name."""

from __future__ import annotations

from cli_harness.adapter import CLIAdapter


# Built-in adapters — always available
_ADAPTER_MAP: dict[str, str] = {
    "kiro-cli": "cli_harness.adapters.kiro_cli.KiroCLIAdapter",
    "claude-code": "cli_harness.adapters.claude_code.ClaudeCodeAdapter",
    "claude-code-sdk": "cli_harness.adapters.claude_code_sdk.ClaudeCodeSDKAdapter",
}


def register_adapter(name: str, fqn: str) -> None:
    """Register an adapter by name and fully-qualified class path.

    Allows external code (config loaders, plugins) to add adapters without
    modifying framework code.  Built-in adapters can be overridden by name.

    Args:
        name: Adapter name as used on the CLI (e.g. 'my-tool').
        fqn:  Fully-qualified class path (e.g. 'mypackage.adapters.MyAdapter').
    """
    _ADAPTER_MAP[name.lower().strip()] = fqn


def load_adapters_from_config(cfg_data: dict) -> None:
    """Register adapters declared under ``cli.adapters`` in a config dict.

    Config shape::

        cli:
          adapters:
            my-tool: "mypackage.adapters.MyToolAdapter"

    Each entry calls :func:`register_adapter` so the adapter is available
    for the current process without any framework code changes.
    """
    for adapter_name, fqn in cfg_data.get("cli", {}).get("adapters", {}).items():
        register_adapter(adapter_name, fqn)


def list_adapters() -> list[str]:
    """Return sorted list of registered adapter names."""
    return sorted(_ADAPTER_MAP.keys())


def get_adapter(name: str) -> CLIAdapter:
    """Instantiate an adapter by name.

    Raises KeyError if the adapter is not registered.
    Raises ImportError if the adapter module cannot be loaded.
    """
    key = name.lower().strip()
    if key not in _ADAPTER_MAP:
        raise KeyError(
            f"Unknown adapter '{name}'. Available: {', '.join(list_adapters())}"
        )

    fqn = _ADAPTER_MAP[key]
    module_path, class_name = fqn.rsplit(".", 1)

    import importlib
    # nosemgrep: non-literal-import - module_path validated against _ADAPTER_MAP whitelist
    module = importlib.import_module(module_path)
    cls = getattr(module, class_name)
    return cls()
