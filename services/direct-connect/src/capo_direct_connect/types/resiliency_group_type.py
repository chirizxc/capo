"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyGroupType``."""

from typing import Literal, TypeAlias, cast

ResiliencyGroupType: TypeAlias = Literal["Managed",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyGroupType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResiliencyGroupType:
    return cast(ResiliencyGroupType, data)
