"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterNumberConditionComparison``."""

from typing import Literal, TypeAlias, cast

"""<p>The numeric comparison operator for metric filters. Valid values: <code>LESSER</code> | <code>LESSER_OR_EQUAL</code> | <code>GREATER</code> | <code>GREATER_OR_EQUAL</code>.</p>"""
MetricFilterNumberConditionComparison: TypeAlias = Literal[
    "LESSER",
    "LESSER_OR_EQUAL",
    "GREATER",
    "GREATER_OR_EQUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterNumberConditionComparison) -> str:
    return value


def deserialize_json(data: str) -> MetricFilterNumberConditionComparison:
    return cast(MetricFilterNumberConditionComparison, data)
