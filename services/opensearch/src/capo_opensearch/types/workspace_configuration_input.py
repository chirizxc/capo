"""Generated from Smithy shape ``com.amazonaws.opensearch#WorkspaceConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.string


class WorkspaceConfigurationInput(TypedDict, closed=True):
    name: "capo_opensearch.types.string.String"
    """<p>The name of the workspace to create. Must be between 1 and 40 characters and can contain alphanumeric characters, parentheses, brackets, hyphens, underscores, and spaces.</p>"""
    workspace_type: "capo_opensearch.types.string.String"
    """<p>The type of workspace to create, which determines the use-case features enabled for the workspace. Valid values are <code>OBSERVABILITY</code>, <code>SECURITY_ANALYTICS</code>, and <code>SEARCH</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceConfigurationInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["workspaceType"] = value["workspace_type"]
    return out


def deserialize_json(data: dict) -> WorkspaceConfigurationInput:
    out: WorkspaceConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkspaceConfigurationInput.name required")
    if data.get("workspaceType") is not None:
        out["workspace_type"] = data["workspaceType"]
    else:
        raise DeserializationError(
            "WorkspaceConfigurationInput.workspace_type required"
        )
    return out
