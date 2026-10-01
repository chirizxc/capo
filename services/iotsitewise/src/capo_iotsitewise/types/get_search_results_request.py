"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetSearchResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.get_search_results_request_max_results_integer
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.search_id
    import capo_iotsitewise.types.workspace_name


class GetSearchResultsRequest(TypedDict, closed=True):
    search_id: "capo_iotsitewise.types.search_id.SearchId"
    """<p>The identifier of the search whose results are retrieved.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace the search belongs to.</p>"""
    max_results: NotRequired[
        "capo_iotsitewise.types.get_search_results_request_max_results_integer.GetSearchResultsRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return in a single page. Valid range is 1 to 10,000; if omitted, a service-defined default is used.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The pagination token returned by a previous GetSearchResults call. Provide it to retrieve the next page of results; omit it to retrieve the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSearchResultsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSearchResultsRequest:
    out: GetSearchResultsRequest = {}  # type: ignore[typeddict-item]
    return out
