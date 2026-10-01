"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIAdapterModelPackageEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_adapter_id
    import capo_sagemaker.types.model_package_arn


class AIAdapterModelPackageEntry(TypedDict, closed=True):
    adapter_id: NotRequired["capo_sagemaker.types.ai_adapter_id.AIAdapterId"]
    """<p>A unique identifier for the adapter. This ID is used as the inference component name when the adapter is deployed. The ID must start and end with an alphanumeric character, can contain hyphens between alphanumeric characters, and can be up to 63 characters long.</p>"""
    model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package that contains the LoRA adapter artifacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIAdapterModelPackageEntry) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "model_package_arn" in value:
        out["ModelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIAdapterModelPackageEntry:
    out: AIAdapterModelPackageEntry = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("ModelPackageArn") is not None:
        out["model_package_arn"] = data["ModelPackageArn"]
    return out
