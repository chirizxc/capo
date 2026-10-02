"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Classification of a compute node execution failure.</p>"""
ComputeNodeErrorCode: TypeAlias = Literal[
    "VALIDATION_ERROR",
    "INTERNAL_FAILURE",
    "EXECUTION_ERROR",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ComputeNodeErrorCode:
    return cast(ComputeNodeErrorCode, data)
