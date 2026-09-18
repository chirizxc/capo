"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListReplicationSetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.max_results
    import capo_ssm_incidents.types.next_token


class ListReplicationSetsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_ssm_incidents.types.max_results.MaxResults"]
    """<p>The maximum number of results per page. </p>"""
    next_token: NotRequired["capo_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplicationSetsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReplicationSetsInput:
    out: ListReplicationSetsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
