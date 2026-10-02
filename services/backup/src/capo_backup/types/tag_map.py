"""Generated from Smithy shape ``com.amazonaws.backup#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.tag_map_key_string
    import capo_backup.types.tag_map_value_string

TagMap: TypeAlias = dict[
    "capo_backup.types.tag_map_key_string.TagMapKeyString",
    "capo_backup.types.tag_map_value_string.TagMapValueString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
