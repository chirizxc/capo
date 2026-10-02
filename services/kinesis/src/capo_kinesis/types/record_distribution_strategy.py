"""Generated from Smithy shape ``com.amazonaws.kinesis#RecordDistributionStrategy``."""

from typing import Literal, TypeAlias, cast

RecordDistributionStrategy: TypeAlias = Literal[
    "AUTO",
    "USER_PARTITION_KEY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordDistributionStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordDistributionStrategy:
    return cast(RecordDistributionStrategy, data)
