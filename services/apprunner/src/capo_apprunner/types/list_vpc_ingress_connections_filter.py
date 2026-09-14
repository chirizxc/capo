"""Generated from Smithy shape ``com.amazonaws.apprunner#ListVpcIngressConnectionsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.string


class ListVpcIngressConnectionsFilter(TypedDict, closed=True):
    service_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a service to filter by. </p>"""
    vpc_endpoint_id: NotRequired["capo_apprunner.types.string.String"]
    """<p>The ID of a VPC Endpoint to filter by. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcIngressConnectionsFilter) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["ServiceArn"] = value["service_arn"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcIngressConnectionsFilter:
    out: ListVpcIngressConnectionsFilter = {}  # type: ignore[typeddict-item]
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
