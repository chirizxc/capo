"""Generated from Smithy shape ``com.amazonaws.glue#ObservationMode``."""

from typing import Literal, TypeAlias, cast

ObservationMode: TypeAlias = Literal[
    "SCHEDULED",
    "FIXED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObservationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObservationMode:
    return cast(ObservationMode, data)
