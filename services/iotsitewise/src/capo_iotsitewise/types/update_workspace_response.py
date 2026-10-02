"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.workspace_status


class UpdateWorkspaceResponse(TypedDict, closed=True):
    workspace_status: "capo_iotsitewise.types.workspace_status.WorkspaceStatus"
    """<p>The status of the workspace after the update, which is <code>UPDATING</code> when the operation returns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.workspace_status

    out["workspaceStatus"] = capo_iotsitewise.types.workspace_status.serialize_json(
        value["workspace_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceResponse:
    out: UpdateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceStatus") is not None:
        import capo_iotsitewise.types.workspace_status

        out["workspace_status"] = (
            capo_iotsitewise.types.workspace_status.deserialize_json(
                data["workspaceStatus"]
            )
        )
    else:
        raise DeserializationError("UpdateWorkspaceResponse.workspace_status required")
    return out
