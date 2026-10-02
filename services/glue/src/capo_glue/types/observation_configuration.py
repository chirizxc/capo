"""Generated from Smithy shape ``com.amazonaws.glue#ObservationConfiguration``."""

from typing import Literal, TypeAlias, cast

ObservationConfiguration: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObservationConfiguration) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObservationConfiguration:
    return cast(ObservationConfiguration, data)
