"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RestoreStatus``."""

from typing import Literal, TypeAlias, cast

RestoreStatus: TypeAlias = Literal["RESTORING",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RestoreStatus:
    return cast(RestoreStatus, data)
