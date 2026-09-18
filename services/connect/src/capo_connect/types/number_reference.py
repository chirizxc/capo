"""Generated from Smithy shape ``com.amazonaws.connect#NumberReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.reference_key
    import capo_connect.types.reference_value


class NumberReference(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.reference_key.ReferenceKey"]
    """<p>Identifier of the number reference.</p>"""
    value: NotRequired["capo_connect.types.reference_value.ReferenceValue"]
    """<p>A valid number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> NumberReference:
    out: NumberReference = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
