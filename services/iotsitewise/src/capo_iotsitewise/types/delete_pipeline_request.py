"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeletePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.workspace_name


class DeletePipelineRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePipelineRequest:
    out: DeletePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
