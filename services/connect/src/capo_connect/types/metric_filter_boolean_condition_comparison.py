"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterBooleanConditionComparison``."""

from typing import Literal, TypeAlias, cast

"""<p>The boolean comparison operator for metric filters. Valid values: <code>IS_TRUE</code> | <code>IS_FALSE</code>.</p>"""
MetricFilterBooleanConditionComparison: TypeAlias = Literal[
    "IS_TRUE",
    "IS_FALSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterBooleanConditionComparison) -> str:
    return value


def deserialize_json(data: str) -> MetricFilterBooleanConditionComparison:
    return cast(MetricFilterBooleanConditionComparison, data)
