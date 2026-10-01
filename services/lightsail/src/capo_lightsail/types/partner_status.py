"""Generated from Smithy shape ``com.amazonaws.lightsail#PartnerStatus``."""

from typing import Literal, TypeAlias, cast

PartnerStatus: TypeAlias = Literal[
    "Active",
    "Suspended",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartnerStatus:
    return cast(PartnerStatus, data)
