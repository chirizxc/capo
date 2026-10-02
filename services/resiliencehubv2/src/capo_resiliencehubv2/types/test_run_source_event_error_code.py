"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceEventErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The cause of a source event collection error.</p>"""
TestRunSourceEventErrorCode: TypeAlias = Literal[
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceEventErrorCode) -> str:
    return value


def deserialize_json(data: str) -> TestRunSourceEventErrorCode:
    return cast(TestRunSourceEventErrorCode, data)
