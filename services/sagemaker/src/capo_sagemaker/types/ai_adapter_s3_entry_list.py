"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIAdapterS3EntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_adapter_s3_entry

AIAdapterS3EntryList: TypeAlias = list[
    "capo_sagemaker.types.ai_adapter_s3_entry.AIAdapterS3Entry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIAdapterS3EntryList) -> list:
    import capo_sagemaker.types.ai_adapter_s3_entry

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_adapter_s3_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIAdapterS3EntryList:
    import capo_sagemaker.types.ai_adapter_s3_entry

    out: AIAdapterS3EntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.ai_adapter_s3_entry.deserialize_aws_json_1_1(item)
        )
    return out
