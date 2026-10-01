"""Generated from Smithy shape ``com.amazonaws.healthlake#TargetFormat``."""

from typing import Literal, TypeAlias, cast

TargetFormat: TypeAlias = Literal["FHIR_R4",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TargetFormat:
    return cast(TargetFormat, data)
