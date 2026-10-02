"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class DescribeDatasetRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace that contains the dataset.</p>"""
    dataset_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The version of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
