"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnvironmentParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string


class EnvironmentParameter(TypedDict, closed=True):
    key: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The environment key suggested by the Amazon SageMaker Inference Recommender.</p>"""
    value_type: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The value type suggested by the Amazon SageMaker Inference Recommender.</p>"""
    value: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The value suggested by the Amazon SageMaker Inference Recommender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value_type" in value:
        out["ValueType"] = value["value_type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentParameter:
    out: EnvironmentParameter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("ValueType") is not None:
        out["value_type"] = data["ValueType"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
