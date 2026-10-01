"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LimitClass``."""

from typing import Literal, TypeAlias, cast

LimitClass: TypeAlias = Literal["API_CATEGORY",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LimitClass:
    return cast(LimitClass, data)
