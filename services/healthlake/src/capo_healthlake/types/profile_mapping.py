"""Generated from Smithy shape ``com.amazonaws.healthlake#ProfileMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.profile_mapping_key
    import capo_healthlake.types.profile_mapping_value

ProfileMapping: TypeAlias = dict[
    "capo_healthlake.types.profile_mapping_key.ProfileMappingKey",
    "capo_healthlake.types.profile_mapping_value.ProfileMappingValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ProfileMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> ProfileMapping:
    out: ProfileMapping = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
