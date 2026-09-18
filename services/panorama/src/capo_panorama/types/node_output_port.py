"""Generated from Smithy shape ``com.amazonaws.panorama#NodeOutputPort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.description
    import capo_panorama.types.port_name
    import capo_panorama.types.port_type


class NodeOutputPort(TypedDict, closed=True):
    name: NotRequired["capo_panorama.types.port_name.PortName"]
    """<p>The output port's name.</p>"""
    description: NotRequired["capo_panorama.types.description.Description"]
    """<p>The output port's description.</p>"""
    type: NotRequired["capo_panorama.types.port_type.PortType"]
    """<p>The output port's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputPort) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> NodeOutputPort:
    out: NodeOutputPort = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
