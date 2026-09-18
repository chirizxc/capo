"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeNetworkOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.protocol


class AddBridgeNetworkOutputRequest(TypedDict, closed=True):
    ip_address: NotRequired["str"]
    """<p> The network output IP Address. </p>"""
    name: NotRequired["str"]
    """<p> The network output name. This name is used to reference the output and must be unique among outputs in this bridge. </p>"""
    network_name: NotRequired["str"]
    """<p> The network output's gateway network name. </p>"""
    port: NotRequired["int"]
    """<p> The network output port. </p>"""
    protocol: NotRequired["capo_mediaconnect.types.protocol.Protocol"]
    """<p> The network output protocol. </p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>"""
    ttl: NotRequired["int"]
    """<p> The network output TTL. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeNetworkOutputRequest) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "name" in value:
        out["name"] = value["name"]
    if "network_name" in value:
        out["networkName"] = value["network_name"]
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        import capo_mediaconnect.types.protocol

        out["protocol"] = capo_mediaconnect.types.protocol.serialize_json(
            value["protocol"]
        )
    if "ttl" in value:
        out["ttl"] = value["ttl"]
    return out


def deserialize_json(data: dict) -> AddBridgeNetworkOutputRequest:
    out: AddBridgeNetworkOutputRequest = {}  # type: ignore[typeddict-item]
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("networkName") is not None:
        out["network_name"] = data["networkName"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("protocol") is not None:
        import capo_mediaconnect.types.protocol

        out["protocol"] = capo_mediaconnect.types.protocol.deserialize_json(
            data["protocol"]
        )
    if data.get("ttl") is not None:
        out["ttl"] = data["ttl"]
    return out
