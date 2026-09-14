"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FieldNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.name

FieldNameList: TypeAlias = list["capo_customer_profiles.types.name.name"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> FieldNameList:
    return [item for item in data if item is not None]
