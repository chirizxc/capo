"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListenerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_arn
    import capo_vpc_lattice.types.listener_id
    import capo_vpc_lattice.types.listener_name
    import capo_vpc_lattice.types.listener_protocol
    import capo_vpc_lattice.types.port
    import capo_vpc_lattice.types.timestamp


class ListenerSummary(TypedDict, closed=True):
    arn: NotRequired["capo_vpc_lattice.types.listener_arn.ListenerArn"]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    id: NotRequired["capo_vpc_lattice.types.listener_id.ListenerId"]
    """<p>The ID of the listener.</p>"""
    name: NotRequired["capo_vpc_lattice.types.listener_name.ListenerName"]
    """<p>The name of the listener.</p>"""
    protocol: NotRequired["capo_vpc_lattice.types.listener_protocol.ListenerProtocol"]
    """<p>The listener protocol.</p>"""
    port: NotRequired["capo_vpc_lattice.types.port.Port"]
    """<p>The listener port.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "port" in value:
        out["port"] = value["port"]
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ListenerSummary:
    out: ListenerSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("createdAt") is not None:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
