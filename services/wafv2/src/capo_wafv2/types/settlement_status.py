"""Generated from Smithy shape ``com.amazonaws.wafv2#SettlementStatus``."""

from typing import Literal, TypeAlias, cast

SettlementStatus: TypeAlias = Literal[
    "SETTLED",
    "PENDING",
    "FAILED",
    "SERVICE_ERROR",
    "SKIPPED_ORIGIN_ERROR",
    "DUPLICATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettlementStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettlementStatus:
    return cast(SettlementStatus, data)
