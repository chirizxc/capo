"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a test run monitoring-source snapshot.</p>"""
TestRunSourceType: TypeAlias = Literal[
    "SUCCESS_CRITERIA",
    "OBSERVABILITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceType) -> str:
    return value


def deserialize_json(data: str) -> TestRunSourceType:
    return cast(TestRunSourceType, data)
