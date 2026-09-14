"""Generated from Smithy shape ``com.amazonaws.connect#EmailReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.reference_key
    import capo_connect.types.reference_value


class EmailReference(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.reference_key.ReferenceKey"]
    """<p>Identifier of the email reference.</p>"""
    value: NotRequired["capo_connect.types.reference_value.ReferenceValue"]
    """<p>A valid email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EmailReference:
    out: EmailReference = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
