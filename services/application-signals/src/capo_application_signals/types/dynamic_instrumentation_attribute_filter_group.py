"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DynamicInstrumentationAttributeFilterGroup``."""

from typing import TypeAlias

DynamicInstrumentationAttributeFilterGroup: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(
    input_to_serialize: DynamicInstrumentationAttributeFilterGroup,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DynamicInstrumentationAttributeFilterGroup:
    out: DynamicInstrumentationAttributeFilterGroup = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
