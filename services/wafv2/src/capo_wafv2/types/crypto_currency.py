"""Generated from Smithy shape ``com.amazonaws.wafv2#CryptoCurrency``."""

from typing import Literal, TypeAlias, cast

CryptoCurrency: TypeAlias = Literal["USDC",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CryptoCurrency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CryptoCurrency:
    return cast(CryptoCurrency, data)
