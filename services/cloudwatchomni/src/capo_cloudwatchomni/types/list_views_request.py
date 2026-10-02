"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListViewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.view_type


class ListViewsRequest(TypedDict, closed=True):
    type: NotRequired["capo_cloudwatchomni.types.view_type.ViewType"]
    """Return only views of this ownership category."""
    max_results: NotRequired["int"]
    """The maximum number of views to return per page."""
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListViewsRequest) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_cloudwatchomni.types.view_type

        out["type"] = capo_cloudwatchomni.types.view_type.serialize_cbor(value["type"])
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListViewsRequest:
    out: ListViewsRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_cloudwatchomni.types.view_type

        out["type"] = capo_cloudwatchomni.types.view_type.deserialize_cbor(data["type"])
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
