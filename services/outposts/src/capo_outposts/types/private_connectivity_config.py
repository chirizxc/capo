"""Generated from Smithy shape ``com.amazonaws.outposts#PrivateConnectivityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.private_connectivity_status
    import capo_outposts.types.role_arn
    import capo_outposts.types.vpc_information_list


class PrivateConnectivityConfig(TypedDict, closed=True):
    role_arn: NotRequired["capo_outposts.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the service-linked role that Amazon Web Services Outposts creates and uses to provision and attach the network interfaces for private connectivity in your VPC. The role's permissions are scoped to the specific Outpost and VPC.</p>"""
    private_connectivity_status: NotRequired[
        "capo_outposts.types.private_connectivity_status.PrivateConnectivityStatus"
    ]
    """<p>The status of private connectivity for the Outpost. Valid values are <code>ENABLED</code> and <code>DISABLED</code>.</p>"""
    vpc_information_list: NotRequired[
        "capo_outposts.types.vpc_information_list.VpcInformationList"
    ]
    """<p>Information about the VPC used for private connectivity.</p>"""
    provisioning_role_arn: NotRequired["capo_outposts.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the provisioning role in your account that Amazon Web Services Outposts uses to establish the service link connection during Outpost installation. This field is present only when VPC endpoint-based provisioning is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectivityConfig) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "private_connectivity_status" in value:
        import capo_outposts.types.private_connectivity_status

        out["PrivateConnectivityStatus"] = (
            capo_outposts.types.private_connectivity_status.serialize_json(
                value["private_connectivity_status"]
            )
        )
    if "vpc_information_list" in value:
        import capo_outposts.types.vpc_information_list

        out["VpcInformationList"] = (
            capo_outposts.types.vpc_information_list.serialize_json(
                value["vpc_information_list"]
            )
        )
    if "provisioning_role_arn" in value:
        out["ProvisioningRoleArn"] = value["provisioning_role_arn"]
    return out


def deserialize_json(data: dict) -> PrivateConnectivityConfig:
    out: PrivateConnectivityConfig = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("PrivateConnectivityStatus") is not None:
        import capo_outposts.types.private_connectivity_status

        out["private_connectivity_status"] = (
            capo_outposts.types.private_connectivity_status.deserialize_json(
                data["PrivateConnectivityStatus"]
            )
        )
    if data.get("VpcInformationList") is not None:
        import capo_outposts.types.vpc_information_list

        out["vpc_information_list"] = (
            capo_outposts.types.vpc_information_list.deserialize_json(
                data["VpcInformationList"]
            )
        )
    if data.get("ProvisioningRoleArn") is not None:
        out["provisioning_role_arn"] = data["ProvisioningRoleArn"]
    return out
