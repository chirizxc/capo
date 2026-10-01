"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterStringConditionComparison``."""

from typing import Literal, TypeAlias, cast

"""<p>The string comparison operator for metric filters. Valid values: <code>MATCHES_ANY</code> | <code>MATCHES_NONE</code>.</p>"""
MetricFilterStringConditionComparison: TypeAlias = Literal[
    "MATCHES_ANY",
    "MATCHES_NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterStringConditionComparison) -> str:
    return value


def deserialize_json(data: str) -> MetricFilterStringConditionComparison:
    return cast(MetricFilterStringConditionComparison, data)
