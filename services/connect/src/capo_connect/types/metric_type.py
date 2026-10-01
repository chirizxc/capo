"""Generated from Smithy shape ``com.amazonaws.connect#MetricType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of the metric. Valid values: <code>AWS_MANAGED</code> | <code>CUSTOMER_MANAGED</code>.</p>"""
MetricType: TypeAlias = Literal[
    "AWS_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricType) -> str:
    return value


def deserialize_json(data: str) -> MetricType:
    return cast(MetricType, data)
