"""Generated from Smithy shape ``com.amazonaws.glue#Count``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.nullable_integer

Count: TypeAlias = list["capo_glue.types.nullable_integer.NullableInteger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Count) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Count:
    return [item for item in data if item is not None]
