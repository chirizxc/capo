"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationFilterKey``."""

from typing import Literal, TypeAlias, cast

AssociationFilterKey: TypeAlias = Literal[
    "InstanceId",
    "Name",
    "AssociationId",
    "AssociationStatusName",
    "LastExecutedBefore",
    "LastExecutedAfter",
    "AssociationName",
    "ResourceGroupName",
    "CloudConnectorId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationFilterKey:
    return cast(AssociationFilterKey, data)
