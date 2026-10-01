"""Generated from Smithy shape ``com.amazonaws.billing#CreditStatus``."""

from typing import Literal, TypeAlias, cast

CreditStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CreditStatus:
    return cast(CreditStatus, data)
