"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StageEndpoints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.stage_endpoint


class StageEndpoints(TypedDict, closed=True):
    events: NotRequired["capo_ivs_realtime.types.stage_endpoint.StageEndpoint"]
    """<p>Events endpoint.</p>"""
    whip: NotRequired["capo_ivs_realtime.types.stage_endpoint.StageEndpoint"]
    """<p>The endpoint to be used for IVS real-time streaming using the WHIP protocol.</p>"""
    rtmp: NotRequired["capo_ivs_realtime.types.stage_endpoint.StageEndpoint"]
    """<p>The endpoint to be used for IVS real-time streaming using the RTMP protocol.</p>"""
    rtmps: NotRequired["capo_ivs_realtime.types.stage_endpoint.StageEndpoint"]
    """<p>The endpoint to be used for IVS real-time streaming using the RTMPS protocol.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StageEndpoints) -> dict:
    out: dict = {}
    if "events" in value:
        out["events"] = value["events"]
    if "whip" in value:
        out["whip"] = value["whip"]
    if "rtmp" in value:
        out["rtmp"] = value["rtmp"]
    if "rtmps" in value:
        out["rtmps"] = value["rtmps"]
    return out


def deserialize_json(data: dict) -> StageEndpoints:
    out: StageEndpoints = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        out["events"] = data["events"]
    if data.get("whip") is not None:
        out["whip"] = data["whip"]
    if data.get("rtmp") is not None:
        out["rtmp"] = data["rtmp"]
    if data.get("rtmps") is not None:
        out["rtmps"] = data["rtmps"]
    return out
