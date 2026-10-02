"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.max_results_type
    import capo_drs.types.pagination_token


class ListRecoveryPlansRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_drs.types.max_results_type.MaxResultsType"]
    """<p>Maximum number of results to return.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlansRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlansRequest:
    out: ListRecoveryPlansRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
