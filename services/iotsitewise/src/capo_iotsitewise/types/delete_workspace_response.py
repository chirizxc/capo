"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.workspace_status


class DeleteWorkspaceResponse(TypedDict, closed=True):
    workspace_status: "capo_iotsitewise.types.workspace_status.WorkspaceStatus"
    """<p>The status of the workspace after the deletion request, which is <code>DELETING</code> when the operation returns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.workspace_status

    out["workspaceStatus"] = capo_iotsitewise.types.workspace_status.serialize_json(
        value["workspace_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceResponse:
    out: DeleteWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceStatus") is not None:
        import capo_iotsitewise.types.workspace_status

        out["workspace_status"] = (
            capo_iotsitewise.types.workspace_status.deserialize_json(
                data["workspaceStatus"]
            )
        )
    else:
        raise DeserializationError("DeleteWorkspaceResponse.workspace_status required")
    return out
