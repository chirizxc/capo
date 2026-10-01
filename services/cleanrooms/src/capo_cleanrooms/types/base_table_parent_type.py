"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BaseTableParentType``."""

from typing import Literal, TypeAlias, cast

BaseTableParentType: TypeAlias = Literal[
    "DIRECT",
    "INDIRECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: BaseTableParentType) -> str:
    return value


def deserialize_json(data: str) -> BaseTableParentType:
    return cast(BaseTableParentType, data)
