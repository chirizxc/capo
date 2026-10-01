"""Generated from Smithy shape ``com.amazonaws.wafv2#CurrencyMode``."""

from typing import Literal, TypeAlias, cast

CurrencyMode: TypeAlias = Literal[
    "REAL",
    "TEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CurrencyMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CurrencyMode:
    return cast(CurrencyMode, data)
