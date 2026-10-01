"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListApplicationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>Maximum number of results to return</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>Next Page Token</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
