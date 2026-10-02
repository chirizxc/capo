"""Generated from Smithy shape ``com.amazonaws.outposts#RackScalingType``."""

from typing import Literal, TypeAlias, cast

RackScalingType: TypeAlias = Literal[
    "SINGLE_RACK",
    "MULTI_RACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: RackScalingType) -> str:
    return value


def deserialize_json(data: str) -> RackScalingType:
    return cast(RackScalingType, data)
