"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunEventType``."""

from typing import Literal, TypeAlias, cast

ExperimentRunEventType: TypeAlias = Literal[
    "RUN_STARTED",
    "EXPOSURE_UPDATED",
    "OVERRIDES_UPDATED",
    "RUN_STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunEventType) -> str:
    return value


def deserialize_json(data: str) -> ExperimentRunEventType:
    return cast(ExperimentRunEventType, data)
