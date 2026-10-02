"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListIntermediateTablesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token


class ListIntermediateTablesInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership for which to list intermediate tables.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntermediateTablesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIntermediateTablesInput:
    out: ListIntermediateTablesInput = {}  # type: ignore[typeddict-item]
    return out
