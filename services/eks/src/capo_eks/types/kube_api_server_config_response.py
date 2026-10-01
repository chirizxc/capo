"""Generated from Smithy shape ``com.amazonaws.eks#KubeApiServerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.service_node_port_range
    import capo_eks.types.string


class KubeApiServerConfigResponse(TypedDict, closed=True):
    event_ttl: NotRequired["capo_eks.types.string.String"]
    """<p>The duration that Kubernetes events are retained.</p>"""
    service_node_port_range: NotRequired[
        "capo_eks.types.service_node_port_range.ServiceNodePortRange"
    ]
    """<p>The port range for NodePort services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubeApiServerConfigResponse) -> dict:
    out: dict = {}
    if "event_ttl" in value:
        out["eventTtl"] = value["event_ttl"]
    if "service_node_port_range" in value:
        import capo_eks.types.service_node_port_range

        out["serviceNodePortRange"] = (
            capo_eks.types.service_node_port_range.serialize_json(
                value["service_node_port_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubeApiServerConfigResponse:
    out: KubeApiServerConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("eventTtl") is not None:
        out["event_ttl"] = data["eventTtl"]
    if data.get("serviceNodePortRange") is not None:
        import capo_eks.types.service_node_port_range

        out["service_node_port_range"] = (
            capo_eks.types.service_node_port_range.deserialize_json(
                data["serviceNodePortRange"]
            )
        )
    return out
