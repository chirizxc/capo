"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StopConditionSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The source of a test stop condition, matching AWS Fault Injection Service (AWS FIS) stop condition sources.</p>"""
StopConditionSource: TypeAlias = Literal[
    "aws:cloudwatch:alarm",
    "none",
]


# --- restJson1 ser/de ---
def serialize_json(value: StopConditionSource) -> str:
    return value


def deserialize_json(data: str) -> StopConditionSource:
    return cast(StopConditionSource, data)
