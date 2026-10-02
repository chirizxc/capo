"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class DescribeTaskRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the task.</p>"""
    task_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The version number of the task to retrieve. If not specified, returns the latest version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTaskRequest:
    out: DescribeTaskRequest = {}  # type: ignore[typeddict-item]
    return out
