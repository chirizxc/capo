"""Generated from Smithy shape ``com.amazonaws.glue#IcebergPartitionSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iceberg_partition_spec

IcebergPartitionSpecList: TypeAlias = list[
    "capo_glue.types.iceberg_partition_spec.IcebergPartitionSpec"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergPartitionSpecList) -> list:
    import capo_glue.types.iceberg_partition_spec

    out: list = []
    for item in value:
        out.append(capo_glue.types.iceberg_partition_spec.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergPartitionSpecList:
    import capo_glue.types.iceberg_partition_spec

    out: IcebergPartitionSpecList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.iceberg_partition_spec.deserialize_aws_json_1_1(item)
        )
    return out
