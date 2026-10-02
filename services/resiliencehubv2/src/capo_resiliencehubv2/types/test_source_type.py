"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The purpose of a test monitoring source.</p>"""
TestSourceType: TypeAlias = Literal[
    "SUCCESS_CRITERIA",
    "OBSERVABILITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceType) -> str:
    return value


def deserialize_json(data: str) -> TestSourceType:
    return cast(TestSourceType, data)
