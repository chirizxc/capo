"""Generated from Smithy shape ``com.amazonaws.quicksight#LimitUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>The unit of measurement for a resource limit value.</p>"""
LimitUnit: TypeAlias = Literal[
    "MB",
    "GB",
    "HOURS",
    "DAYS",
]


# --- restJson1 ser/de ---
def serialize_json(value: LimitUnit) -> str:
    return value


def deserialize_json(data: str) -> LimitUnit:
    return cast(LimitUnit, data)
