"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ApiGatewayProxySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.api_gateway_endpoint_type
    import capo_migration_hub_refactor_spaces.types.api_gateway_id
    import capo_migration_hub_refactor_spaces.types.nlb_arn
    import capo_migration_hub_refactor_spaces.types.nlb_name
    import capo_migration_hub_refactor_spaces.types.stage_name
    import capo_migration_hub_refactor_spaces.types.uri
    import capo_migration_hub_refactor_spaces.types.vpc_link_id


class ApiGatewayProxySummary(TypedDict, closed=True):
    proxy_url: NotRequired["capo_migration_hub_refactor_spaces.types.uri.Uri"]
    """<p>The endpoint URL of the API Gateway proxy. </p>"""
    api_gateway_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.api_gateway_id.ApiGatewayId"
    ]
    """<p>The resource ID of the API Gateway for the proxy. </p>"""
    vpc_link_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.vpc_link_id.VpcLinkId"
    ]
    """<p>The <code>VpcLink</code> ID of the API Gateway proxy. </p>"""
    nlb_arn: NotRequired["capo_migration_hub_refactor_spaces.types.nlb_arn.NlbArn"]
    """<p>The Amazon Resource Name (ARN) of the Network Load Balancer configured by the API Gateway proxy. </p>"""
    nlb_name: NotRequired["capo_migration_hub_refactor_spaces.types.nlb_name.NlbName"]
    """<p>The name of the Network Load Balancer that is configured by the API Gateway proxy. </p>"""
    endpoint_type: NotRequired[
        "capo_migration_hub_refactor_spaces.types.api_gateway_endpoint_type.ApiGatewayEndpointType"
    ]
    """<p>The type of API Gateway endpoint created. </p>"""
    stage_name: NotRequired[
        "capo_migration_hub_refactor_spaces.types.stage_name.StageName"
    ]
    """<p>The name of the API Gateway stage. The name defaults to <code>prod</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayProxySummary) -> dict:
    out: dict = {}
    if "proxy_url" in value:
        out["ProxyUrl"] = value["proxy_url"]
    if "api_gateway_id" in value:
        out["ApiGatewayId"] = value["api_gateway_id"]
    if "vpc_link_id" in value:
        out["VpcLinkId"] = value["vpc_link_id"]
    if "nlb_arn" in value:
        out["NlbArn"] = value["nlb_arn"]
    if "nlb_name" in value:
        out["NlbName"] = value["nlb_name"]
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    return out


def deserialize_json(data: dict) -> ApiGatewayProxySummary:
    out: ApiGatewayProxySummary = {}  # type: ignore[typeddict-item]
    if data.get("ProxyUrl") is not None:
        out["proxy_url"] = data["ProxyUrl"]
    if data.get("ApiGatewayId") is not None:
        out["api_gateway_id"] = data["ApiGatewayId"]
    if data.get("VpcLinkId") is not None:
        out["vpc_link_id"] = data["VpcLinkId"]
    if data.get("NlbArn") is not None:
        out["nlb_arn"] = data["NlbArn"]
    if data.get("NlbName") is not None:
        out["nlb_name"] = data["NlbName"]
    if data.get("EndpointType") is not None:
        out["endpoint_type"] = data["EndpointType"]
    if data.get("StageName") is not None:
        out["stage_name"] = data["StageName"]
    return out
