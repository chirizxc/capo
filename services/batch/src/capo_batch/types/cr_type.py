"""Generated from Smithy shape ``com.amazonaws.batch#CRType``."""

from typing import Literal, TypeAlias, cast

CRType: TypeAlias = Literal[
    "EC2",
    "SPOT",
    "FARGATE",
    "FARGATE_SPOT",
    "ECS_MANAGED_INSTANCES",
]


# --- restJson1 ser/de ---
def serialize_json(value: CRType) -> str:
    return value


def deserialize_json(data: str) -> CRType:
    return cast(CRType, data)
