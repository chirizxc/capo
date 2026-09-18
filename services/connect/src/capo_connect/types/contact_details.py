"""Generated from Smithy shape ``com.amazonaws.connect#ContactDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_detail_description
    import capo_connect.types.contact_detail_name


class ContactDetails(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.contact_detail_name.ContactDetailName"]
    """<p>The name of the contact details.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_detail_description.ContactDetailDescription"
    ]
    """<p>Teh description of the contact details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ContactDetails:
    out: ContactDetails = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
