"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceOutcome``."""

from typing import Literal, TypeAlias, cast

"""<p>The evaluation outcome of a test run success criteria source.</p>"""
TestSourceOutcome: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceOutcome) -> str:
    return value


def deserialize_json(data: str) -> TestSourceOutcome:
    return cast(TestSourceOutcome, data)
