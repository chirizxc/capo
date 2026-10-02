"""Generated from Smithy shape ``com.amazonaws.securityhub#FreeTrialType``."""

from typing import Literal, TypeAlias, cast

FreeTrialType: TypeAlias = Literal[
    "SECURITY_HUB_V2",
    "SECURITY_HUB_V2_MULTI_CLOUD_AZURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialType) -> str:
    return value


def deserialize_json(data: str) -> FreeTrialType:
    return cast(FreeTrialType, data)
