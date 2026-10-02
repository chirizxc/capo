"""Generated from Smithy shape ``com.amazonaws.billing#ServiceLevelAccountUsage``."""

from typing_extensions import NotRequired, TypedDict


class ServiceLevelAccountUsage(TypedDict, closed=True):
    service_code: NotRequired["str"]
    """<p>The service code for which to return Support-eligible spend data.</p>"""
    total_support_eligible_spend: NotRequired["str"]
    """<p>The total support-eligible spend for the service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceLevelAccountUsage) -> dict:
    out: dict = {}
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "total_support_eligible_spend" in value:
        out["totalSupportEligibleSpend"] = value["total_support_eligible_spend"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceLevelAccountUsage:
    out: ServiceLevelAccountUsage = {}  # type: ignore[typeddict-item]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("totalSupportEligibleSpend") is not None:
        out["total_support_eligible_spend"] = data["totalSupportEligibleSpend"]
    return out
