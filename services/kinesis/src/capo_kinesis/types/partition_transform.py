"""Generated from Smithy shape ``com.amazonaws.kinesis#PartitionTransform``."""

from typing import Literal, TypeAlias, cast

PartitionTransform: TypeAlias = Literal["TIME_HOUR",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionTransform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartitionTransform:
    return cast(PartitionTransform, data)
