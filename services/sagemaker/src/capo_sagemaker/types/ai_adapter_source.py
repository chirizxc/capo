"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIAdapterSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_adapter_model_package_entry_list
    import capo_sagemaker.types.ai_adapter_s3_entry_list


class _AIAdapterSource_ModelPackageArns(TypedDict, closed=True):
    ModelPackageArns: "capo_sagemaker.types.ai_adapter_model_package_entry_list.AIAdapterModelPackageEntryList"


class _AIAdapterSource_S3Uris(TypedDict, closed=True):
    S3Uris: "capo_sagemaker.types.ai_adapter_s3_entry_list.AIAdapterS3EntryList"


AIAdapterSource: TypeAlias = _AIAdapterSource_ModelPackageArns | _AIAdapterSource_S3Uris


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIAdapterSource) -> dict:
    if "ModelPackageArns" in value:
        import capo_sagemaker.types.ai_adapter_model_package_entry_list

        return {
            "ModelPackageArns": capo_sagemaker.types.ai_adapter_model_package_entry_list.serialize_aws_json_1_1(
                value["ModelPackageArns"]
            )
        }
    elif "S3Uris" in value:
        import capo_sagemaker.types.ai_adapter_s3_entry_list

        return {
            "S3Uris": capo_sagemaker.types.ai_adapter_s3_entry_list.serialize_aws_json_1_1(
                value["S3Uris"]
            )
        }
    else:
        raise SerializationError("AIAdapterSource: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AIAdapterSource:
    if data.get("ModelPackageArns") is not None:
        import capo_sagemaker.types.ai_adapter_model_package_entry_list

        return {
            "ModelPackageArns": capo_sagemaker.types.ai_adapter_model_package_entry_list.deserialize_aws_json_1_1(
                data["ModelPackageArns"]
            )
        }
    elif data.get("S3Uris") is not None:
        import capo_sagemaker.types.ai_adapter_s3_entry_list

        return {
            "S3Uris": capo_sagemaker.types.ai_adapter_s3_entry_list.deserialize_aws_json_1_1(
                data["S3Uris"]
            )
        }
    else:
        raise DeserializationError("AIAdapterSource: no recognized variant key")
