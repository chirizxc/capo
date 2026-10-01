"""Generated from Smithy shape ``com.amazonaws.securityagent#ListPrivateConnectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token


class ListPrivateConnectionsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of private connections to return in a single response.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivateConnectionsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrivateConnectionsInput:
    out: ListPrivateConnectionsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
