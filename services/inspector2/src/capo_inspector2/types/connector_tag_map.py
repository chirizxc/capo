"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.connector_tag_key
    import capo_inspector2.types.connector_tag_value

ConnectorTagMap: TypeAlias = dict[
    "capo_inspector2.types.connector_tag_key.ConnectorTagKey",
    "capo_inspector2.types.connector_tag_value.ConnectorTagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConnectorTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConnectorTagMap:
    out: ConnectorTagMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
