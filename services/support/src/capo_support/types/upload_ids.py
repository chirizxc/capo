"""Generated from Smithy shape ``com.amazonaws.support#UploadIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.upload_id

UploadIds: TypeAlias = list["capo_support.types.upload_id.UploadId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UploadIds:
    return [item for item in data if item is not None]
