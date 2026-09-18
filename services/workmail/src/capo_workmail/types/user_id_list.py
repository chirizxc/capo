"""Generated from Smithy shape ``com.amazonaws.workmail#UserIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.work_mail_identifier

UserIdList: TypeAlias = list[
    "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UserIdList:
    return [item for item in data if item is not None]
