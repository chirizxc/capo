"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string


class ModelMetadataSummary(TypedDict, closed=True):
    domain: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning domain of the model.</p>"""
    framework: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning framework of the model.</p>"""
    task: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning task of the model.</p>"""
    model: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The name of the model.</p>"""
    framework_version: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The framework version of the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetadataSummary) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "framework" in value:
        out["Framework"] = value["framework"]
    if "task" in value:
        out["Task"] = value["task"]
    if "model" in value:
        out["Model"] = value["model"]
    if "framework_version" in value:
        out["FrameworkVersion"] = value["framework_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelMetadataSummary:
    out: ModelMetadataSummary = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Framework") is not None:
        out["framework"] = data["Framework"]
    if data.get("Task") is not None:
        out["task"] = data["Task"]
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("FrameworkVersion") is not None:
        out["framework_version"] = data["FrameworkVersion"]
    return out
