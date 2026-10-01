"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListSpacesForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.next_token


class ListSpacesForOrganizationInput(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results. Tokens expire after 24 hours."""
    max_results: NotRequired["int"]
    """The maximum number of spaces to return per page. Defaults to 100."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSpacesForOrganizationInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListSpacesForOrganizationInput:
    out: ListSpacesForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
