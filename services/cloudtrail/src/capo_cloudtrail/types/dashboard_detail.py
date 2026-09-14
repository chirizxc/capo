"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DashboardDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_arn
    import capo_cloudtrail.types.dashboard_type


class DashboardDetail(TypedDict, closed=True):
    dashboard_arn: NotRequired["capo_cloudtrail.types.dashboard_arn.DashboardArn"]
    """<p> The ARN for the dashboard. </p>"""
    type: NotRequired["capo_cloudtrail.types.dashboard_type.DashboardType"]
    """<p> The type of dashboard. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DashboardDetail) -> dict:
    out: dict = {}
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "type" in value:
        import capo_cloudtrail.types.dashboard_type

        out["Type"] = capo_cloudtrail.types.dashboard_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DashboardDetail:
    out: DashboardDetail = {}  # type: ignore[typeddict-item]
    if data.get("DashboardArn") is not None:
        out["dashboard_arn"] = data["DashboardArn"]
    if data.get("Type") is not None:
        import capo_cloudtrail.types.dashboard_type

        out["type"] = capo_cloudtrail.types.dashboard_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
