"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateIngressGatewayBridgeRequest``."""

from typing_extensions import NotRequired, TypedDict


class UpdateIngressGatewayBridgeRequest(TypedDict, closed=True):
    max_bitrate: NotRequired["int"]
    """<p> The maximum expected bitrate (in bps).</p>"""
    max_outputs: NotRequired["int"]
    """<p> The maximum number of expected outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngressGatewayBridgeRequest) -> dict:
    out: dict = {}
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "max_outputs" in value:
        out["maxOutputs"] = value["max_outputs"]
    return out


def deserialize_json(data: dict) -> UpdateIngressGatewayBridgeRequest:
    out: UpdateIngressGatewayBridgeRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("maxOutputs") is not None:
        out["max_outputs"] = data["maxOutputs"]
    return out
