"""Generated from Smithy shape ``com.amazonaws.sagemaker#EksRoleAccessEntries``."""

from typing import TypeAlias

EksRoleAccessEntries: TypeAlias = list["str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EksRoleAccessEntries) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EksRoleAccessEntries:
    return [item for item in data if item is not None]
