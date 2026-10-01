"""Generated from Smithy shape ``com.amazonaws.billing#PreferenceValue``."""

from typing import Literal, TypeAlias, cast

PreferenceValue: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreferenceValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PreferenceValue:
    return cast(PreferenceValue, data)
