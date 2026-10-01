"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIAdapterS3Entry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_adapter_id
    import capo_sagemaker.types.s3_uri


class AIAdapterS3Entry(TypedDict, closed=True):
    adapter_id: NotRequired["capo_sagemaker.types.ai_adapter_id.AIAdapterId"]
    """<p>A unique identifier for the adapter. This ID is used as the inference component name when the adapter is deployed. The ID must start and end with an alphanumeric character, can contain hyphens between alphanumeric characters, and can be up to 63 characters long.</p>"""
    s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI of the directory that contains the LoRA adapter artifacts in PEFT format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIAdapterS3Entry) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIAdapterS3Entry:
    out: AIAdapterS3Entry = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    return out
