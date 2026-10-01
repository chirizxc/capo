"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DiversityValuesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.diversity_cap_value
    import capo_customer_profiles.types.diversity_placeholder_name

DiversityValuesMap: TypeAlias = dict[
    "capo_customer_profiles.types.diversity_placeholder_name.DiversityPlaceholderName",
    "capo_customer_profiles.types.diversity_cap_value.DiversityCapValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DiversityValuesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DiversityValuesMap:
    out: DiversityValuesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
