"""Generated from Smithy shape ``com.amazonaws.transfer#ProxyMode``."""

from typing import Literal, TypeAlias, cast

ProxyMode: TypeAlias = Literal[
    "NONE",
    "PROXY_PROTOCOL_V2_ENFORCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProxyMode:
    return cast(ProxyMode, data)
