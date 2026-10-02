"""Generated from Smithy shape ``com.amazonaws.outposts#VpcInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.subnet_ids
    import capo_outposts.types.vpc_endpoint_id
    import capo_outposts.types.vpc_id


class VpcInformation(TypedDict, closed=True):
    vpc_id: NotRequired["capo_outposts.types.vpc_id.VpcId"]
    """<p>The ID of the VPC used for private connectivity.</p>"""
    subnet_ids: NotRequired["capo_outposts.types.subnet_ids.SubnetIds"]
    """<p>The IDs of the subnets associated with the VPC endpoint. Currently, only one subnet is supported.</p>"""
    vpc_endpoint_id: NotRequired["capo_outposts.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the interface VPC endpoint for the Amazon Web Services Outposts service. When specified, the endpoint must be in the <code>available</code> state and the specified subnets must be associated with it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInformation) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_outposts.types.subnet_ids

        out["SubnetIds"] = capo_outposts.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_json(data: dict) -> VpcInformation:
    out: VpcInformation = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_outposts.types.subnet_ids

        out["subnet_ids"] = capo_outposts.types.subnet_ids.deserialize_json(
            data["SubnetIds"]
        )
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
