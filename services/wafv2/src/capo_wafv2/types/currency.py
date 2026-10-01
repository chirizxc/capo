"""Generated from Smithy shape ``com.amazonaws.wafv2#Currency``."""

from typing import Literal, TypeAlias, cast

Currency: TypeAlias = Literal["USDC",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Currency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Currency:
    return cast(Currency, data)
