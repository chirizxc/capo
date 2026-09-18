"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double


class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails(
    TypedDict, closed=True
):
    max: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The maximum amount of total local storage, in GB. </p>"""
    min: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The minimum amount of total local storage, in GB. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails,
) -> dict:
    out: dict = {}
    if "max" in value:
        out["Max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    if "min" in value:
        out["Min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails = {}  # type: ignore[typeddict-item]
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    if data.get("Min") is not None:
        out["min"] = float(data["Min"])
    return out
