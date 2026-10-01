"""Generated from Smithy shape ``com.amazonaws.kinesis#S3TablesConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.s3_tables_configuration

S3TablesConfigurationList: TypeAlias = list[
    "capo_kinesis.types.s3_tables_configuration.S3TablesConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TablesConfigurationList) -> list:
    import capo_kinesis.types.s3_tables_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.s3_tables_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> S3TablesConfigurationList:
    import capo_kinesis.types.s3_tables_configuration

    out: S3TablesConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.s3_tables_configuration.deserialize_aws_json_1_1(item)
        )
    return out
