"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeExecutionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of an individual compute node execution.</p>"""
ComputeNodeExecutionState: TypeAlias = Literal[
    "NOT_STARTED",
    "QUEUED",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeExecutionState) -> str:
    return value


def deserialize_json(data: str) -> ComputeNodeExecutionState:
    return cast(ComputeNodeExecutionState, data)
