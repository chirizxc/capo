"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.application_id
    import capo_iotsitewise.types.workspace_name


class DescribeApplicationRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>Name of the workspace to associate with the underlying Application</p>"""
    id: "capo_iotsitewise.types.application_id.ApplicationId"
    """<p>ID of the Application</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeApplicationRequest:
    out: DescribeApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
