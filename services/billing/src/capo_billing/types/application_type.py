"""Generated from Smithy shape ``com.amazonaws.billing#ApplicationType``."""

from typing import Literal, TypeAlias, cast

ApplicationType: TypeAlias = Literal[
    "BEFORE_CROSS_SERVICE_DISCOUNTS",
    "AFTER_DISCOUNTS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApplicationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ApplicationType:
    return cast(ApplicationType, data)
