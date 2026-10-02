"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TaskNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.task_name

TaskNameList: TypeAlias = list["capo_partnercentral_selling.types.task_name.TaskName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TaskNameList:
    return [item for item in data if item is not None]
