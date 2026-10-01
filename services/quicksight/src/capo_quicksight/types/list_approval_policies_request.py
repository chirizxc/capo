"""Generated from Smithy shape ``com.amazonaws.quicksight#ListApprovalPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.max_results
    import capo_quicksight.types.pagination_token


class ListApprovalPoliciesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_quicksight.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. If you don't specify a value, the service returns a default number of results. Use the <code>NextToken</code> value in the response to retrieve additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApprovalPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApprovalPoliciesRequest:
    out: ListApprovalPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
