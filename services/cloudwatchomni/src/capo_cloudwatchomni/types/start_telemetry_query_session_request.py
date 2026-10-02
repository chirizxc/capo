"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#StartTelemetryQuerySessionRequest``."""

from typing_extensions import NotRequired, TypedDict


class StartTelemetryQuerySessionRequest(TypedDict, closed=True):
    session_name: NotRequired["str"]
    """A human-readable name for the session. Names under `/aws/` are reserved for service integrations."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartTelemetryQuerySessionRequest) -> dict:
    out: dict = {}
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    return out


def deserialize_cbor(data: dict) -> StartTelemetryQuerySessionRequest:
    out: StartTelemetryQuerySessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("sessionName") is not None:
        out["session_name"] = data["sessionName"]
    return out
