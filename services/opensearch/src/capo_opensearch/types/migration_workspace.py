"""Generated from Smithy shape ``com.amazonaws.opensearch#MigrationWorkspace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.string


class MigrationWorkspace(TypedDict, closed=True):
    workspace_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The unique identifier of an existing workspace to use as the migration target. Specify either this parameter or <code>createWorkspace</code>.</p>"""
    create_workspace: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Specifies whether to create a new workspace as the migration target. If <code>true</code>, you must also specify <code>name</code>.</p>"""
    name: NotRequired["capo_opensearch.types.string.String"]
    """<p>The name of the new workspace to create. Required when <code>createWorkspace</code> is <code>true</code>.</p>"""
    type: NotRequired["capo_opensearch.types.string.String"]
    """<p>The type of the new workspace to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationWorkspace) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["workspaceId"] = value["workspace_id"]
    if "create_workspace" in value:
        out["createWorkspace"] = value["create_workspace"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> MigrationWorkspace:
    out: MigrationWorkspace = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    if data.get("createWorkspace") is not None:
        out["create_workspace"] = data["createWorkspace"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
