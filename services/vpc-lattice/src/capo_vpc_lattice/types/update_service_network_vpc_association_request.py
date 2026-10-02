"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceNetworkVpcAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.dns_options
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.service_network_vpc_association_identifier


class UpdateServiceNetworkVpcAssociationRequest(TypedDict, closed=True):
    service_network_vpc_association_identifier: "capo_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier"
    """<p>The ID or ARN of the association.</p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups.</p>"""
    private_dns_enabled: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled for the VPC association. </p>"""
    dns_options: NotRequired["capo_vpc_lattice.types.dns_options.DnsOptions"]
    """<p> DNS options for the service network VPC association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceNetworkVpcAssociationRequest) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "dns_options" in value:
        import capo_vpc_lattice.types.dns_options

        out["dnsOptions"] = capo_vpc_lattice.types.dns_options.serialize_json(
            value["dns_options"]
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceNetworkVpcAssociationRequest:
    out: UpdateServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("securityGroupIds") is not None:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("privateDnsEnabled") is not None:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if data.get("dnsOptions") is not None:
        import capo_vpc_lattice.types.dns_options

        out["dns_options"] = capo_vpc_lattice.types.dns_options.deserialize_json(
            data["dnsOptions"]
        )
    return out
