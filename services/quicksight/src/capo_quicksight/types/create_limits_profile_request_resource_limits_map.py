"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateLimitsProfileRequestResourceLimitsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.profile_limit_value
    import capo_quicksight.types.resource_type

CreateLimitsProfileRequestResourceLimitsMap: TypeAlias = dict[
    "capo_quicksight.types.resource_type.ResourceType",
    "capo_quicksight.types.profile_limit_value.ProfileLimitValue",
]


# --- restJson1 ser/de ---
def serialize_json(
    input_to_serialize: CreateLimitsProfileRequestResourceLimitsMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.profile_limit_value
        import capo_quicksight.types.resource_type

        out[capo_quicksight.types.resource_type.serialize_json(key)] = (
            capo_quicksight.types.profile_limit_value.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> CreateLimitsProfileRequestResourceLimitsMap:
    out: CreateLimitsProfileRequestResourceLimitsMap = {}
    for key, value in data.items():
        import capo_quicksight.types.resource_type

        if value is None:
            continue
        import capo_quicksight.types.profile_limit_value

        out[capo_quicksight.types.resource_type.deserialize_json(key)] = (
            capo_quicksight.types.profile_limit_value.deserialize_json(value)
        )
    return out
