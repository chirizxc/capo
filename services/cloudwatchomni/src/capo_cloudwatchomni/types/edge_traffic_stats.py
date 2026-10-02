"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#EdgeTrafficStats``."""

from typing_extensions import NotRequired, TypedDict


class EdgeTrafficStats(TypedDict, closed=True):
    bytes: NotRequired["int"]
    """Total bytes observed across the edge."""
    packets: NotRequired["int"]
    """Total packets observed across the edge."""
    flows: NotRequired["int"]
    """Total network flows observed across the edge."""
    sent_bytes: NotRequired["int"]
    """Total bytes sent to the destination."""
    received_bytes: NotRequired["int"]
    """Total bytes received from the destination."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EdgeTrafficStats) -> dict:
    out: dict = {}
    if "bytes" in value:
        out["bytes"] = value["bytes"]
    if "packets" in value:
        out["packets"] = value["packets"]
    if "flows" in value:
        out["flows"] = value["flows"]
    if "sent_bytes" in value:
        out["sentBytes"] = value["sent_bytes"]
    if "received_bytes" in value:
        out["receivedBytes"] = value["received_bytes"]
    return out


def deserialize_cbor(data: dict) -> EdgeTrafficStats:
    out: EdgeTrafficStats = {}  # type: ignore[typeddict-item]
    if data.get("bytes") is not None:
        out["bytes"] = data["bytes"]
    if data.get("packets") is not None:
        out["packets"] = data["packets"]
    if data.get("flows") is not None:
        out["flows"] = data["flows"]
    if data.get("sentBytes") is not None:
        out["sent_bytes"] = data["sentBytes"]
    if data.get("receivedBytes") is not None:
        out["received_bytes"] = data["receivedBytes"]
    return out
