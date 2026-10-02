"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleRecommendationRunAdditionalRunOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string


class DataQualityRuleRecommendationRunAdditionalRunOptions(TypedDict, closed=True):
    custom_log_group_prefix: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A custom prefix for the CloudWatch log group names. When specified, recommendation run logs are written to <code><CustomLogGroupPrefix>/error</code> and <code><CustomLogGroupPrefix>/output</code> instead of the default <code>/aws-glue/data-quality/error</code> and <code>/aws-glue/data-quality/output</code> log groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DataQualityRuleRecommendationRunAdditionalRunOptions,
) -> dict:
    out: dict = {}
    if "custom_log_group_prefix" in value:
        out["CustomLogGroupPrefix"] = value["custom_log_group_prefix"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DataQualityRuleRecommendationRunAdditionalRunOptions:
    out: DataQualityRuleRecommendationRunAdditionalRunOptions = {}  # type: ignore[typeddict-item]
    if data.get("CustomLogGroupPrefix") is not None:
        out["custom_log_group_prefix"] = data["CustomLogGroupPrefix"]
    return out
