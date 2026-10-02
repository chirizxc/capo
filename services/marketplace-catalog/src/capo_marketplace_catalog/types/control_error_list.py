"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ControlErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.control_error

ControlErrorList: TypeAlias = list[
    "capo_marketplace_catalog.types.control_error.ControlError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlErrorList) -> list:
    import capo_marketplace_catalog.types.control_error

    out: list = []
    for item in value:
        out.append(capo_marketplace_catalog.types.control_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlErrorList:
    import capo_marketplace_catalog.types.control_error

    out: ControlErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_marketplace_catalog.types.control_error.deserialize_json(item))
    return out
