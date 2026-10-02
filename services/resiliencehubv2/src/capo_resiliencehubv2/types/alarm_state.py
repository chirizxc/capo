"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AlarmState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a CloudWatch alarm.</p>"""
AlarmState: TypeAlias = Literal[
    "OK",
    "ALARM",
    "INSUFFICIENT_DATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmState) -> str:
    return value


def deserialize_json(data: str) -> AlarmState:
    return cast(AlarmState, data)
