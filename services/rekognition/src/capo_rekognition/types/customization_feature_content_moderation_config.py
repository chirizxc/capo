"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomizationFeatureContentModerationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.percent


class CustomizationFeatureContentModerationConfig(TypedDict, closed=True):
    confidence_threshold: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence level you plan to use to identify if unsafe content is present during inference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizationFeatureContentModerationConfig) -> dict:
    out: dict = {}
    if "confidence_threshold" in value:
        out["ConfidenceThreshold"] = (
            "NaN"
            if value["confidence_threshold"] != value["confidence_threshold"]
            else "Infinity"
            if value["confidence_threshold"] == float("inf")
            else "-Infinity"
            if value["confidence_threshold"] == float("-inf")
            else value["confidence_threshold"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomizationFeatureContentModerationConfig:
    out: CustomizationFeatureContentModerationConfig = {}  # type: ignore[typeddict-item]
    if data.get("ConfidenceThreshold") is not None:
        out["confidence_threshold"] = float(data["ConfidenceThreshold"])
    return out
