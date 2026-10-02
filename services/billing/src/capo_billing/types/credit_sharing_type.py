"""Generated from Smithy shape ``com.amazonaws.billing#CreditSharingType``."""

from typing import Literal, TypeAlias, cast

CreditSharingType: TypeAlias = Literal[
    "DEFAULT",
    "DISABLED",
    "CUSTOM",
    "COST_CATEGORY_RULE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditSharingType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CreditSharingType:
    return cast(CreditSharingType, data)
