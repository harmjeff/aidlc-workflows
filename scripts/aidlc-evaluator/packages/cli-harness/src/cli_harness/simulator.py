"""Shared Human Simulator — Anthropic SDK-based reviewer for CLI adapter workflows.

Used by both the kiro-cli adapter (after each kiro turn) and the claude-code-sdk
adapter (on each handoff_to_simulator tool call).  Backed by the same system prompt
as the Strands two-agent swarm via build_simulator_system_prompt().
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import anthropic
import boto3

# Import shared prompt builder from execution package
_EXEC_SRC = Path(__file__).resolve().parents[5] / "execution" / "src"
if str(_EXEC_SRC) not in sys.path:
    sys.path.insert(0, str(_EXEC_SRC))
from aidlc_runner.agents.simulator import build_simulator_system_prompt  # noqa: E402

logger = logging.getLogger(__name__)

_SIMULATOR_TOOLS = [
    {
        "name": "read_file",
        "description": "Read the contents of a file in the run folder.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "File path relative to the run folder.",
                }
            },
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Write content to a file in the run folder.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "list_files",
        "description": "List files and directories within a path in the run folder.",
        "input_schema": {
            "type": "object",
            "properties": {
                "directory": {"type": "string", "default": "."},
            },
            "required": [],
        },
    },
]


def _resolve_safe(base: Path, relative: str) -> Path:
    resolved = (base / relative).resolve()
    if not str(resolved).startswith(str(base.resolve())):
        raise ValueError(f"Path traversal denied: {relative}")
    return resolved


def _exec_file_tool(name: str, tool_input: dict, run_folder: Path) -> str:
    try:
        if name == "read_file":
            path = tool_input["path"]
            target = _resolve_safe(run_folder, path)
            if not target.exists():
                return f"Error: File not found: {path}"
            return target.read_text(encoding="utf-8")

        elif name == "write_file":
            path = tool_input["path"]
            content = tool_input.get("content", "")
            target = _resolve_safe(run_folder, path)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            return f"Written: {path} ({len(content)} chars)"

        elif name == "list_files":
            directory = tool_input.get("directory", ".")
            target = _resolve_safe(run_folder, directory)
            if not target.is_dir():
                return f"Error: Not a directory: {directory}"
            entries = sorted(target.iterdir())
            lines = [
                f"  {e.relative_to(run_folder)}{'/' if e.is_dir() else ''}"
                for e in entries
            ]
            return "\n".join(lines) if lines else f"(empty: {directory})"

        return f"[error: unknown tool: {name}]"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        logger.exception("File tool %r failed", name)
        return f"[error: {e}]"


class HumanSimulator:
    """Anthropic SDK-based human simulator for CLI adapter review gates.

    Wraps a single stateless call: given a message from the executor (e.g.
    the output of a kiro turn, or a handoff_to_simulator tool call), runs
    a short simulator conversation and returns the simulator's text response.
    """

    def __init__(
        self,
        client: anthropic.AnthropicBedrock,
        model: str,
        system_prompt: str,
        run_folder: Path,
    ):
        self._client = client
        self._model = model
        self._system_prompt = system_prompt
        self._run_folder = run_folder

    @classmethod
    def from_adapter_config(
        cls,
        run_folder: Path,
        vision_content: str,
        tech_env_content: str | None,
        openapi_content: str | None,
        aws_profile: str | None,
        aws_region: str | None,
        model: str,
    ) -> "HumanSimulator":
        """Construct a HumanSimulator from the pieces available in an AdapterConfig."""
        system_prompt = build_simulator_system_prompt(
            vision_content=vision_content,
            tech_env_content=tech_env_content,
            openapi_content=openapi_content,
        )

        session_kwargs: dict = {}
        if aws_profile:
            session_kwargs["profile_name"] = aws_profile
        boto_session = boto3.Session(**session_kwargs)
        frozen = boto_session.get_credentials().get_frozen_credentials()
        client = anthropic.AnthropicBedrock(
            aws_access_key=frozen.access_key,
            aws_secret_key=frozen.secret_key,
            aws_session_token=frozen.token,
            aws_region=aws_region or "us-east-1",
        )

        return cls(
            client=client,
            model=model,
            system_prompt=system_prompt,
            run_folder=run_folder,
        )

    def respond(self, message: str, max_iterations: int = 50) -> str:
        """Run one simulator turn and return the final text response.

        The simulator may make file tool calls before responding — this loop
        handles those transparently.
        """
        messages: list[dict] = [{"role": "user", "content": message}]

        for _ in range(max_iterations):
            response = self._client.messages.create(
                model=self._model,
                max_tokens=8192,
                system=self._system_prompt,
                tools=_SIMULATOR_TOOLS,
                messages=messages,
            )

            tool_uses = [b for b in response.content if b.type == "tool_use"]
            text_blocks = [b for b in response.content if b.type == "text"]

            if not tool_uses:
                return "\n".join(b.text for b in text_blocks).strip() or "(no response)"

            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for tu in tool_uses:
                result_text = _exec_file_tool(tu.name, tu.input, self._run_folder)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu.id,
                    "content": result_text,
                })
            messages.append({"role": "user", "content": tool_results})

        return "[error: simulator exceeded max iterations]"
