"""Generated from Smithy shape ``com.amazonaws.elementalinference#FilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.filter_value

FilterValueList: TypeAlias = list[
    "capo_elementalinference.types.filter_value.FilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValueList:
    return [item for item in data if item is not None]
