"""Generated from Smithy shape ``com.amazonaws.eks#ServiceNodePortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.integer


class ServiceNodePortRange(TypedDict, closed=True):
    min_port: "capo_eks.types.integer.Integer"
    """<p>The minimum port number in the range.</p>"""
    max_port: "capo_eks.types.integer.Integer"
    """<p>The maximum port number in the range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNodePortRange) -> dict:
    out: dict = {}
    out["minPort"] = value.get("min_port", 0)
    out["maxPort"] = value.get("max_port", 0)
    return out


def deserialize_json(data: dict) -> ServiceNodePortRange:
    out: ServiceNodePortRange = {}  # type: ignore[typeddict-item]
    if data.get("minPort") is not None:
        out["min_port"] = data["minPort"]
    else:
        out["min_port"] = 0
    if data.get("maxPort") is not None:
        out["max_port"] = data["maxPort"]
    else:
        out["max_port"] = 0
    return out
