"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorFilterName``."""

from typing import Literal, TypeAlias, cast

ConnectorFilterName: TypeAlias = Literal["provider",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorFilterName:
    return cast(ConnectorFilterName, data)
