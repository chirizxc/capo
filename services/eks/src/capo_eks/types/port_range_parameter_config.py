"""Generated from Smithy shape ``com.amazonaws.eks#PortRangeParameterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.port_range_constraints
    import capo_eks.types.service_node_port_range


class PortRangeParameterConfig(TypedDict, closed=True):
    default_value: NotRequired[
        "capo_eks.types.service_node_port_range.ServiceNodePortRange"
    ]
    """<p>The default port range value.</p>"""
    constraints: NotRequired[
        "capo_eks.types.port_range_constraints.PortRangeConstraints"
    ]
    """<p>The constraints for the port range parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortRangeParameterConfig) -> dict:
    out: dict = {}
    if "default_value" in value:
        import capo_eks.types.service_node_port_range

        out["defaultValue"] = capo_eks.types.service_node_port_range.serialize_json(
            value["default_value"]
        )
    if "constraints" in value:
        import capo_eks.types.port_range_constraints

        out["constraints"] = capo_eks.types.port_range_constraints.serialize_json(
            value["constraints"]
        )
    return out


def deserialize_json(data: dict) -> PortRangeParameterConfig:
    out: PortRangeParameterConfig = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        import capo_eks.types.service_node_port_range

        out["default_value"] = capo_eks.types.service_node_port_range.deserialize_json(
            data["defaultValue"]
        )
    if data.get("constraints") is not None:
        import capo_eks.types.port_range_constraints

        out["constraints"] = capo_eks.types.port_range_constraints.deserialize_json(
            data["constraints"]
        )
    return out
