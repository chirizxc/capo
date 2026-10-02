"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.query_filter
    import capo_iotsitewise.types.query_list_next_token
    import capo_iotsitewise.types.query_max_results
    import capo_iotsitewise.types.workspace_name


class ListQueriesRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace to list queries for.</p>"""
    filter: NotRequired["capo_iotsitewise.types.query_filter.QueryFilter"]
    """<p>An optional filter to return only queries with the specified status. The value must be one of the supported query statuses: SUBMITTED, RUNNING, COMPLETED, FAILED, CANCELED, or CANCELING.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.query_max_results.QueryMaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""
    next_token: NotRequired[
        "capo_iotsitewise.types.query_list_next_token.QueryListNextToken"
    ]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueriesRequest:
    out: ListQueriesRequest = {}  # type: ignore[typeddict-item]
    return out
