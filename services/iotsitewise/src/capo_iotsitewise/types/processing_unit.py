"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ProcessingUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>The processing unit allocation that determines the vCPU, memory, and GPU resources assigned to a task. Available units depend on the processing type.</p>"""
ProcessingUnit: TypeAlias = Literal[
    "UNITS_2",
    "UNITS_4",
    "UNITS_8",
    "UNITS_12",
    "UNITS_16",
    "UNITS_24",
    "UNITS_32",
    "UNITS_36",
    "UNITS_48",
    "UNITS_60",
    "UNITS_64",
    "UNITS_72",
    "UNITS_84",
    "UNITS_96",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProcessingUnit) -> str:
    return value


def deserialize_json(data: str) -> ProcessingUnit:
    return cast(ProcessingUnit, data)
