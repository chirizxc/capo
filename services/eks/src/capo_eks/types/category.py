"""Generated from Smithy shape ``com.amazonaws.eks#Category``."""

from typing import Literal, TypeAlias, cast

Category: TypeAlias = Literal[
    "UPGRADE_READINESS",
    "MISCONFIGURATION",
    "ROLLBACK_READINESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> str:
    return value


def deserialize_json(data: str) -> Category:
    return cast(Category, data)
