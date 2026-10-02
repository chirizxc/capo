"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetQueryResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.query_id
    import capo_iotsitewise.types.query_max_results
    import capo_iotsitewise.types.query_next_token
    import capo_iotsitewise.types.workspace_name


class GetQueryResultsRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace associated with the query.</p>"""
    query_id: "capo_iotsitewise.types.query_id.QueryId"
    """<p>The unique identifier for the query execution.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.query_max_results.QueryMaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.query_next_token.QueryNextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryResultsRequest:
    out: GetQueryResultsRequest = {}  # type: ignore[typeddict-item]
    return out
