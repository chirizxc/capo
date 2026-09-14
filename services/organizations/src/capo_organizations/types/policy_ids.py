"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.policy_id

PolicyIds: TypeAlias = list["capo_organizations.types.policy_id.PolicyId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PolicyIds:
    return [item for item in data if item is not None]
