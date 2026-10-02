"""Generated from Smithy shape ``com.amazonaws.kinesis#PartitionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.partition_field

PartitionFieldList: TypeAlias = list[
    "capo_kinesis.types.partition_field.PartitionField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionFieldList) -> list:
    import capo_kinesis.types.partition_field

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.partition_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionFieldList:
    import capo_kinesis.types.partition_field

    out: PartitionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kinesis.types.partition_field.deserialize_aws_json_1_1(item))
    return out
