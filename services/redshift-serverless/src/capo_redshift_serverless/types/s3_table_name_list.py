"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#S3TableNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.s3_table_name

S3TableNameList: TypeAlias = list[
    "capo_redshift_serverless.types.s3_table_name.S3TableName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TableNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> S3TableNameList:
    return [item for item in data if item is not None]
