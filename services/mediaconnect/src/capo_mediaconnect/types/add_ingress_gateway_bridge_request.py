"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddIngressGatewayBridgeRequest``."""

from typing_extensions import NotRequired, TypedDict


class AddIngressGatewayBridgeRequest(TypedDict, closed=True):
    max_bitrate: NotRequired["int"]
    """<p> The maximum expected bitrate (in bps) of the ingress bridge. </p>"""
    max_outputs: NotRequired["int"]
    """<p> The maximum number of expected outputs on the ingress bridge. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddIngressGatewayBridgeRequest) -> dict:
    out: dict = {}
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "max_outputs" in value:
        out["maxOutputs"] = value["max_outputs"]
    return out


def deserialize_json(data: dict) -> AddIngressGatewayBridgeRequest:
    out: AddIngressGatewayBridgeRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("maxOutputs") is not None:
        out["max_outputs"] = data["maxOutputs"]
    return out
