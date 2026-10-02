"""Generated from Smithy shape ``com.amazonaws.securityhub#FreeTrialStatusValue``."""

from typing import Literal, TypeAlias, cast

FreeTrialStatusValue: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialStatusValue) -> str:
    return value


def deserialize_json(data: str) -> FreeTrialStatusValue:
    return cast(FreeTrialStatusValue, data)
