"""Generated from Smithy shape ``com.amazonaws.eks#KubeApiServerVersionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.duration_parameter_config
    import capo_eks.types.port_range_parameter_config


class KubeApiServerVersionConfig(TypedDict, closed=True):
    event_ttl: NotRequired[
        "capo_eks.types.duration_parameter_config.DurationParameterConfig"
    ]
    """<p>The event TTL configuration with default value and constraints.</p>"""
    service_node_port_range: NotRequired[
        "capo_eks.types.port_range_parameter_config.PortRangeParameterConfig"
    ]
    """<p>The service node port range configuration with default value and constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubeApiServerVersionConfig) -> dict:
    out: dict = {}
    if "event_ttl" in value:
        import capo_eks.types.duration_parameter_config

        out["eventTtl"] = capo_eks.types.duration_parameter_config.serialize_json(
            value["event_ttl"]
        )
    if "service_node_port_range" in value:
        import capo_eks.types.port_range_parameter_config

        out["serviceNodePortRange"] = (
            capo_eks.types.port_range_parameter_config.serialize_json(
                value["service_node_port_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubeApiServerVersionConfig:
    out: KubeApiServerVersionConfig = {}  # type: ignore[typeddict-item]
    if data.get("eventTtl") is not None:
        import capo_eks.types.duration_parameter_config

        out["event_ttl"] = capo_eks.types.duration_parameter_config.deserialize_json(
            data["eventTtl"]
        )
    if data.get("serviceNodePortRange") is not None:
        import capo_eks.types.port_range_parameter_config

        out["service_node_port_range"] = (
            capo_eks.types.port_range_parameter_config.deserialize_json(
                data["serviceNodePortRange"]
            )
        )
    return out
