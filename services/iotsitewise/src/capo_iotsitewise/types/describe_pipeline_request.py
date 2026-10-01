"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class DescribePipelineRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline.</p>"""
    pipeline_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The version number of the pipeline to retrieve. If not specified, returns the latest version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePipelineRequest:
    out: DescribePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
