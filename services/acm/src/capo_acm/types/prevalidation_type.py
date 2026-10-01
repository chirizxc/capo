"""Generated from Smithy shape ``com.amazonaws.acm#PrevalidationType``."""

from typing import Literal, TypeAlias, cast

PrevalidationType: TypeAlias = Literal["DNS_PREVALIDATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrevalidationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrevalidationType:
    return cast(PrevalidationType, data)
