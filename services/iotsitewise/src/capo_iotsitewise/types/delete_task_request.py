"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.workspace_name


class DeleteTaskRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the task to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTaskRequest:
    out: DeleteTaskRequest = {}  # type: ignore[typeddict-item]
    return out
