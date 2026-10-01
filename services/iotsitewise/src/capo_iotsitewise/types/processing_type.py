"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ProcessingType``."""

from typing import Literal, TypeAlias, cast

"""<p>The processing type for compute resources. Determines whether the task runs on standard CPU or GPU-accelerated hardware.</p>"""
ProcessingType: TypeAlias = Literal[
    "GENERIC_COMPUTE_PROCESSING",
    "HARDWARE_ACCELERATED_PROCESSING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProcessingType) -> str:
    return value


def deserialize_json(data: str) -> ProcessingType:
    return cast(ProcessingType, data)
