"""Generated from Smithy shape ``com.amazonaws.securityhub#Features``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.feature_detail
    import capo_securityhub.types.feature_name_key

Features: TypeAlias = dict[
    "capo_securityhub.types.feature_name_key.FeatureNameKey",
    "capo_securityhub.types.feature_detail.FeatureDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Features) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_securityhub.types.feature_detail

        out[key] = capo_securityhub.types.feature_detail.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Features:
    out: Features = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_securityhub.types.feature_detail

        out[key] = capo_securityhub.types.feature_detail.deserialize_json(value)
    return out
