"""Generated from Smithy shape ``com.amazonaws.appconfig#AttributeValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.attribute_key
    import capo_appconfig.types.attribute_value

AttributeValueMap: TypeAlias = dict[
    "capo_appconfig.types.attribute_key.AttributeKey",
    "capo_appconfig.types.attribute_value.AttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AttributeValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appconfig.types.attribute_value

        out[key] = capo_appconfig.types.attribute_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AttributeValueMap:
    out: AttributeValueMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_appconfig.types.attribute_value

        out[key] = capo_appconfig.types.attribute_value.deserialize_json(value)
    return out
