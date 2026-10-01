"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

ExperimentDefinitionStatus: TypeAlias = Literal[
    "ACTIVE",
    "IDLE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentDefinitionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentDefinitionStatus:
    return cast(ExperimentDefinitionStatus, data)
