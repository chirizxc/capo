"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Classification of a pipeline execution failure.</p>"""
PipelineErrorCode: TypeAlias = Literal[
    "VALIDATION_ERROR",
    "INTERNAL_FAILURE",
    "EXECUTION_ERROR",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineErrorCode) -> str:
    return value


def deserialize_json(data: str) -> PipelineErrorCode:
    return cast(PipelineErrorCode, data)
