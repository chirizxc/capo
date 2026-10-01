"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TaskIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.prospecting_task_identifier

TaskIdentifierList: TypeAlias = list[
    "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TaskIdentifierList:
    return [item for item in data if item is not None]
