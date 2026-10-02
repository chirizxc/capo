"""Generated from Smithy shape ``com.amazonaws.connect#AvailableFilterType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of an available metric filter. Valid values: <code>METRIC_LEVEL</code> | <code>RESOURCE_LEVEL</code>.</p>"""
AvailableFilterType: TypeAlias = Literal[
    "METRIC_LEVEL",
    "RESOURCE_LEVEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailableFilterType) -> str:
    return value


def deserialize_json(data: str) -> AvailableFilterType:
    return cast(AvailableFilterType, data)
