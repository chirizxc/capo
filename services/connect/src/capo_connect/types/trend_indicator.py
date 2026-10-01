"""Generated from Smithy shape ``com.amazonaws.connect#TrendIndicator``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies how to interpret a positive trend in metric data. Valid values: <code>POSITIVE</code> | <code>NEGATIVE</code> | <code>NEUTRAL</code>.</p>"""
TrendIndicator: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrendIndicator) -> str:
    return value


def deserialize_json(data: str) -> TrendIndicator:
    return cast(TrendIndicator, data)
