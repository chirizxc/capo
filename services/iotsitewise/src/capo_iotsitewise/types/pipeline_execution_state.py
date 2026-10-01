"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineExecutionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a pipeline execution.</p>"""
PipelineExecutionState: TypeAlias = Literal[
    "NOT_STARTED",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLING",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineExecutionState) -> str:
    return value


def deserialize_json(data: str) -> PipelineExecutionState:
    return cast(PipelineExecutionState, data)
