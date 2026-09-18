"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateUsageQuantity``."""

from typing_extensions import NotRequired, TypedDict


class WorkloadEstimateUsageQuantity(TypedDict, closed=True):
    unit: NotRequired["str"]
    """<p> The unit of measurement for the usage quantity. </p>"""
    amount: NotRequired["float"]
    """<p> The numeric value of the usage quantity. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateUsageQuantity) -> dict:
    out: dict = {}
    if "unit" in value:
        out["unit"] = value["unit"]
    if "amount" in value:
        out["amount"] = (
            "NaN"
            if value["amount"] != value["amount"]
            else "Infinity"
            if value["amount"] == float("inf")
            else "-Infinity"
            if value["amount"] == float("-inf")
            else value["amount"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkloadEstimateUsageQuantity:
    out: WorkloadEstimateUsageQuantity = {}  # type: ignore[typeddict-item]
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    if data.get("amount") is not None:
        out["amount"] = float(data["amount"])
    return out
