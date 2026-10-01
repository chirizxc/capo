"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.parameter_value

StringList: TypeAlias = list[
    "capo_resiliencehubv2.types.parameter_value.ParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return [item for item in data if item is not None]
