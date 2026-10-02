"""Generated from Smithy shape ``com.amazonaws.customerprofiles#KeyValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255

KeyValuesList: TypeAlias = list[
    "capo_customer_profiles.types.string1_to255.string1To255"
]


# --- restJson1 ser/de ---
def serialize_json(value: KeyValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> KeyValuesList:
    return [item for item in data if item is not None]
