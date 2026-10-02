"""Generated from Smithy shape ``com.amazonaws.backup#AccessPointMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.access_point_metadata_map_key_string
    import capo_backup.types.access_point_metadata_map_value_string

AccessPointMetadataMap: TypeAlias = dict[
    "capo_backup.types.access_point_metadata_map_key_string.AccessPointMetadataMapKeyString",
    "capo_backup.types.access_point_metadata_map_value_string.AccessPointMetadataMapValueString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AccessPointMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AccessPointMetadataMap:
    out: AccessPointMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
