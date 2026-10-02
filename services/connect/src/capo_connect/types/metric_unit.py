"""Generated from Smithy shape ``com.amazonaws.connect#MetricUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>The display unit for metric data. Valid values: <code>INTEGER</code> | <code>DOUBLE</code> | <code>PERCENT</code> | <code>SECONDS</code>.</p>"""
MetricUnit: TypeAlias = Literal[
    "INTEGER",
    "DOUBLE",
    "PERCENT",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricUnit) -> str:
    return value


def deserialize_json(data: str) -> MetricUnit:
    return cast(MetricUnit, data)
