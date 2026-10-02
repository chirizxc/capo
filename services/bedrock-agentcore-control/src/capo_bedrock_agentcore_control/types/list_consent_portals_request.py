"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListConsentPortalsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListConsentPortalsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of consent portals to return in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to retrieve the next page of results. Use the value returned in a previous response to request the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConsentPortalsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConsentPortalsRequest:
    out: ListConsentPortalsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
