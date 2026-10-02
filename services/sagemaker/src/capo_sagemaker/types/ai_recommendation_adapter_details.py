"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationAdapterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_adapter_model_package_entry_list
    import capo_sagemaker.types.ai_adapter_s3_entry_list


class AIRecommendationAdapterDetails(TypedDict, closed=True):
    model_package_arns: NotRequired[
        "capo_sagemaker.types.ai_adapter_model_package_entry_list.AIAdapterModelPackageEntryList"
    ]
    """<p>The list of LoRA adapters with their model package ARNs.</p>"""
    s3_uris: NotRequired[
        "capo_sagemaker.types.ai_adapter_s3_entry_list.AIAdapterS3EntryList"
    ]
    """<p>The list of LoRA adapters with their Amazon S3 URIs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationAdapterDetails) -> dict:
    out: dict = {}
    if "model_package_arns" in value:
        import capo_sagemaker.types.ai_adapter_model_package_entry_list

        out["ModelPackageArns"] = (
            capo_sagemaker.types.ai_adapter_model_package_entry_list.serialize_aws_json_1_1(
                value["model_package_arns"]
            )
        )
    if "s3_uris" in value:
        import capo_sagemaker.types.ai_adapter_s3_entry_list

        out["S3Uris"] = (
            capo_sagemaker.types.ai_adapter_s3_entry_list.serialize_aws_json_1_1(
                value["s3_uris"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationAdapterDetails:
    out: AIRecommendationAdapterDetails = {}  # type: ignore[typeddict-item]
    if data.get("ModelPackageArns") is not None:
        import capo_sagemaker.types.ai_adapter_model_package_entry_list

        out["model_package_arns"] = (
            capo_sagemaker.types.ai_adapter_model_package_entry_list.deserialize_aws_json_1_1(
                data["ModelPackageArns"]
            )
        )
    if data.get("S3Uris") is not None:
        import capo_sagemaker.types.ai_adapter_s3_entry_list

        out["s3_uris"] = (
            capo_sagemaker.types.ai_adapter_s3_entry_list.deserialize_aws_json_1_1(
                data["S3Uris"]
            )
        )
    return out
