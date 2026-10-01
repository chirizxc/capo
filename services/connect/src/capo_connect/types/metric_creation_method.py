"""Generated from Smithy shape ``com.amazonaws.connect#MetricCreationMethod``."""

from typing import Literal, TypeAlias, cast

"""<p>The method used to create a custom metric. Valid values: <code>SERVICE_LEVEL_BUILDER</code> | <code>METRIC_BUILDER</code>.</p>"""
MetricCreationMethod: TypeAlias = Literal[
    "SERVICE_LEVEL_BUILDER",
    "METRIC_BUILDER",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricCreationMethod) -> str:
    return value


def deserialize_json(data: str) -> MetricCreationMethod:
    return cast(MetricCreationMethod, data)
