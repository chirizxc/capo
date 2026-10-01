"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.workspace_name


class DescribeWorkspaceRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceRequest:
    out: DescribeWorkspaceRequest = {}  # type: ignore[typeddict-item]
    return out
