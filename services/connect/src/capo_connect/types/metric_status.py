"""Generated from Smithy shape ``com.amazonaws.connect#MetricStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The publish status of a metric. Valid values: <code>PUBLISHED</code> | <code>SAVED</code>.</p>"""
MetricStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricStatus) -> str:
    return value


def deserialize_json(data: str) -> MetricStatus:
    return cast(MetricStatus, data)
