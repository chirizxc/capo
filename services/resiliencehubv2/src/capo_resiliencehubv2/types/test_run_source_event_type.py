"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceEventType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a test run source event. ALARM indicates an event produced from a CloudWatch alarm source.</p>"""
TestRunSourceEventType: TypeAlias = Literal["ALARM",]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceEventType) -> str:
    return value


def deserialize_json(data: str) -> TestRunSourceEventType:
    return cast(TestRunSourceEventType, data)
