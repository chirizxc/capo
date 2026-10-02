"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_source_type
    import capo_iotsitewise.types.dataset_type_enum
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.workspace_name


class ListDatasetsRequest(TypedDict, closed=True):
    source_type: "capo_iotsitewise.types.dataset_source_type.DatasetSourceType"
    """<p>The type of data source for the dataset.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace to filter datasets by.</p>"""
    dataset_type: NotRequired[
        "capo_iotsitewise.types.dataset_type_enum.DatasetTypeEnum"
    ]
    """<p>The type of dataset to filter by: a session dataset, a curated dataset, or a connection to an external datasource.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    return out
