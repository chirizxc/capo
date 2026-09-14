"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_code
    import capo_bcm_pricing_calculator.types.key


class BatchCreateWorkloadEstimateUsageError(TypedDict, closed=True):
    key: NotRequired["capo_bcm_pricing_calculator.types.key.Key"]
    """<p> The key of the entry that caused the error. </p>"""
    error_code: NotRequired[
        "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_code.BatchCreateWorkloadEstimateUsageCode"
    ]
    """<p> The error code associated with the failed operation. </p>"""
    error_message: NotRequired["str"]
    """<p> A descriptive message for the error that occurred. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageError) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "error_code" in value:
        import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_code

        out["errorCode"] = (
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_code.serialize_aws_json_1_0(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateWorkloadEstimateUsageError:
    out: BatchCreateWorkloadEstimateUsageError = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("errorCode") is not None:
        import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_code

        out["error_code"] = (
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_code.deserialize_aws_json_1_0(
                data["errorCode"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
