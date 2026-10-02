"""Generated from Smithy shape ``com.amazonaws.support#CompletedUploadList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.completed_upload

CompletedUploadList: TypeAlias = list[
    "capo_support.types.completed_upload.CompletedUpload"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompletedUploadList) -> list:
    import capo_support.types.completed_upload

    out: list = []
    for item in value:
        out.append(capo_support.types.completed_upload.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CompletedUploadList:
    import capo_support.types.completed_upload

    out: CompletedUploadList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_support.types.completed_upload.deserialize_aws_json_1_1(item))
    return out
