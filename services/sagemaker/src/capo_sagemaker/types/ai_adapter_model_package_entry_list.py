"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIAdapterModelPackageEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_adapter_model_package_entry

AIAdapterModelPackageEntryList: TypeAlias = list[
    "capo_sagemaker.types.ai_adapter_model_package_entry.AIAdapterModelPackageEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIAdapterModelPackageEntryList) -> list:
    import capo_sagemaker.types.ai_adapter_model_package_entry

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_adapter_model_package_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIAdapterModelPackageEntryList:
    import capo_sagemaker.types.ai_adapter_model_package_entry

    out: AIAdapterModelPackageEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.ai_adapter_model_package_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
