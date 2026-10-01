"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunDependencySource``."""

from typing import Literal, TypeAlias, cast

"""<p>The origin of a blocked dependency.</p>"""
TestRunDependencySource: TypeAlias = Literal[
    "DISCOVERED",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunDependencySource) -> str:
    return value


def deserialize_json(data: str) -> TestRunDependencySource:
    return cast(TestRunDependencySource, data)
