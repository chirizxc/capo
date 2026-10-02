"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListSpacesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.next_token


class ListSpacesInput(TypedDict, closed=True):
    domain_id: NotRequired["capo_cloudwatchomni.types.domain_id.DomainId"]
    """Filter by domain ID."""
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results. Supply the same filters used on the request that returned it. Tokens expire after 24 hours."""
    max_results: NotRequired["int"]
    """The maximum number of spaces to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSpacesInput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListSpacesInput:
    out: ListSpacesInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
