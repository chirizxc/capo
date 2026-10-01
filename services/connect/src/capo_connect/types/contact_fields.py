"""Generated from Smithy shape ``com.amazonaws.connect#ContactFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_field

ContactFields: TypeAlias = list["capo_connect.types.contact_field.ContactField"]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFields) -> list:
    import capo_connect.types.contact_field

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFields:
    import capo_connect.types.contact_field

    out: ContactFields = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.contact_field.deserialize_json(item))
    return out
