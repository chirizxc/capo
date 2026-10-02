"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetDataSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class ListDatasetDataSegmentsRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the dataset.</p>"""
    dataset_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The version of the dataset to list data segments for.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request. Default: 50.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetDataSegmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetDataSegmentsRequest:
    out: ListDatasetDataSegmentsRequest = {}  # type: ignore[typeddict-item]
    return out
