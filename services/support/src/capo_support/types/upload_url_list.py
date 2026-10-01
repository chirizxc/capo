"""Generated from Smithy shape ``com.amazonaws.support#UploadUrlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.upload_url

UploadUrlList: TypeAlias = list["capo_support.types.upload_url.UploadUrl"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadUrlList) -> list:
    import capo_support.types.upload_url

    out: list = []
    for item in value:
        out.append(capo_support.types.upload_url.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UploadUrlList:
    import capo_support.types.upload_url

    out: UploadUrlList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_support.types.upload_url.deserialize_aws_json_1_1(item))
    return out
