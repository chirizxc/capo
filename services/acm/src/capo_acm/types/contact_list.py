"""Generated from Smithy shape ``com.amazonaws.acm#ContactList``."""

from typing import TypeAlias

ContactList: TypeAlias = list["str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ContactList:
    return [item for item in data if item is not None]
