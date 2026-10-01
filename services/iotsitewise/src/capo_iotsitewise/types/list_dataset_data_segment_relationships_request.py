"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetDataSegmentRelationshipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.workspace_name


class ListDatasetDataSegmentRelationshipsRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the session dataset to list data segment relationships for.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the dataset.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request. Default: 50.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetDataSegmentRelationshipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetDataSegmentRelationshipsRequest:
    out: ListDatasetDataSegmentRelationshipsRequest = {}  # type: ignore[typeddict-item]
    return out
