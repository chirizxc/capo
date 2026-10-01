"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListTelemetryQuerySessionsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListTelemetryQuerySessionsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of sessions to return per page."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTelemetryQuerySessionsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListTelemetryQuerySessionsRequest:
    out: ListTelemetryQuerySessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
