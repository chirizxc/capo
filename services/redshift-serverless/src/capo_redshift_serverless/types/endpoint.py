"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.vpc_endpoint_list


class Endpoint(TypedDict, closed=True):
    address: NotRequired["str"]
    """<p>The DNS address of the VPC endpoint.</p>"""
    port: NotRequired["int"]
    """<p>The port that Amazon Redshift Serverless listens on.</p>"""
    vpc_endpoints: NotRequired[
        "capo_redshift_serverless.types.vpc_endpoint_list.VpcEndpointList"
    ]
    """<p>An array of <code>VpcEndpoint</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["address"] = value["address"]
    if "port" in value:
        out["port"] = value["port"]
    if "vpc_endpoints" in value:
        import capo_redshift_serverless.types.vpc_endpoint_list

        out["vpcEndpoints"] = (
            capo_redshift_serverless.types.vpc_endpoint_list.serialize_aws_json_1_1(
                value["vpc_endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("address") is not None:
        out["address"] = data["address"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("vpcEndpoints") is not None:
        import capo_redshift_serverless.types.vpc_endpoint_list

        out["vpc_endpoints"] = (
            capo_redshift_serverless.types.vpc_endpoint_list.deserialize_aws_json_1_1(
                data["vpcEndpoints"]
            )
        )
    return out
