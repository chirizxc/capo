"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunStatus``."""

from typing import Literal, TypeAlias, cast

ExperimentRunStatus: TypeAlias = Literal[
    "RUNNING",
    "DONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentRunStatus:
    return cast(ExperimentRunStatus, data)
