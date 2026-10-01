"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListIntermediateTableVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token


class ListIntermediateTableVersionsInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table for which to list versions.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntermediateTableVersionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIntermediateTableVersionsInput:
    out: ListIntermediateTableVersionsInput = {}  # type: ignore[typeddict-item]
    return out
