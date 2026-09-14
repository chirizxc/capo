"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLDataSplitConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.validation_fraction


class AutoMLDataSplitConfig(TypedDict, closed=True):
    validation_fraction: NotRequired[
        "capo_sagemaker.types.validation_fraction.ValidationFraction"
    ]
    """<p>The validation fraction (optional) is a float that specifies the portion of the training dataset to be used for validation. The default value is 0.2, and values must be greater than 0 and less than 1. We recommend setting this value to be less than 0.5.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLDataSplitConfig) -> dict:
    out: dict = {}
    if "validation_fraction" in value:
        out["ValidationFraction"] = (
            "NaN"
            if value["validation_fraction"] != value["validation_fraction"]
            else "Infinity"
            if value["validation_fraction"] == float("inf")
            else "-Infinity"
            if value["validation_fraction"] == float("-inf")
            else value["validation_fraction"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLDataSplitConfig:
    out: AutoMLDataSplitConfig = {}  # type: ignore[typeddict-item]
    if data.get("ValidationFraction") is not None:
        out["validation_fraction"] = float(data["ValidationFraction"])
    return out
