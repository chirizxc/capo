"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DetailedPipelineErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The error code for a detailed pipeline error entry.</p>"""
DetailedPipelineErrorCode: TypeAlias = Literal[
    "VALIDATION_ERROR",
    "INTERNAL_FAILURE",
    "EXECUTION_ERROR",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailedPipelineErrorCode) -> str:
    return value


def deserialize_json(data: str) -> DetailedPipelineErrorCode:
    return cast(DetailedPipelineErrorCode, data)
