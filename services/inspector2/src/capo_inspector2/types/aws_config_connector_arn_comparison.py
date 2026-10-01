"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsConfigConnectorArnComparison``."""

from typing import Literal, TypeAlias, cast

AwsConfigConnectorArnComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: AwsConfigConnectorArnComparison) -> str:
    return value


def deserialize_json(data: str) -> AwsConfigConnectorArnComparison:
    return cast(AwsConfigConnectorArnComparison, data)
