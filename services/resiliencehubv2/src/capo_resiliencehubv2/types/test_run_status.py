"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a test run through its lifecycle.</p>"""
TestRunStatus: TypeAlias = Literal[
    "INITIALIZING",
    "RUNNING",
    "STOPPING",
    "PASSED",
    "FAILED",
    "STOPPED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunStatus) -> str:
    return value


def deserialize_json(data: str) -> TestRunStatus:
    return cast(TestRunStatus, data)
