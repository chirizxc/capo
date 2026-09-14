"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2TransitGatewayDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEc2TransitGatewayDetails(TypedDict, closed=True):
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the transit gateway. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description of the transit gateway. </p>"""
    default_route_table_propagation: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Turn on or turn off automatic propagation of routes to the default propagation route table. </p>"""
    auto_accept_shared_attachments: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Turn on or turn off automatic acceptance of attachment requests. </p>"""
    default_route_table_association: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Turn on or turn off automatic association with the default association route table. </p>"""
    transit_gateway_cidr_blocks: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The transit gateway Classless Inter-Domain Routing (CIDR) blocks. </p>"""
    association_default_route_table_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the default association route table. </p>"""
    propagation_default_route_table_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the default propagation route table. </p>"""
    vpn_ecmp_support: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Turn on or turn off Equal Cost Multipath Protocol (ECMP) support. </p>"""
    dns_support: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Turn on or turn off DNS support. </p>"""
    multicast_support: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether multicast is supported on the transit gateway. </p>"""
    amazon_side_asn: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>A private Autonomous System Number (ASN) for the Amazon side of a BGP session. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2TransitGatewayDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_route_table_propagation" in value:
        out["DefaultRouteTablePropagation"] = value["default_route_table_propagation"]
    if "auto_accept_shared_attachments" in value:
        out["AutoAcceptSharedAttachments"] = value["auto_accept_shared_attachments"]
    if "default_route_table_association" in value:
        out["DefaultRouteTableAssociation"] = value["default_route_table_association"]
    if "transit_gateway_cidr_blocks" in value:
        import capo_securityhub.types.non_empty_string_list

        out["TransitGatewayCidrBlocks"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["transit_gateway_cidr_blocks"]
            )
        )
    if "association_default_route_table_id" in value:
        out["AssociationDefaultRouteTableId"] = value[
            "association_default_route_table_id"
        ]
    if "propagation_default_route_table_id" in value:
        out["PropagationDefaultRouteTableId"] = value[
            "propagation_default_route_table_id"
        ]
    if "vpn_ecmp_support" in value:
        out["VpnEcmpSupport"] = value["vpn_ecmp_support"]
    if "dns_support" in value:
        out["DnsSupport"] = value["dns_support"]
    if "multicast_support" in value:
        out["MulticastSupport"] = value["multicast_support"]
    if "amazon_side_asn" in value:
        out["AmazonSideAsn"] = value["amazon_side_asn"]
    return out


def deserialize_json(data: dict) -> AwsEc2TransitGatewayDetails:
    out: AwsEc2TransitGatewayDetails = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultRouteTablePropagation") is not None:
        out["default_route_table_propagation"] = data["DefaultRouteTablePropagation"]
    if data.get("AutoAcceptSharedAttachments") is not None:
        out["auto_accept_shared_attachments"] = data["AutoAcceptSharedAttachments"]
    if data.get("DefaultRouteTableAssociation") is not None:
        out["default_route_table_association"] = data["DefaultRouteTableAssociation"]
    if data.get("TransitGatewayCidrBlocks") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["transit_gateway_cidr_blocks"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["TransitGatewayCidrBlocks"]
            )
        )
    if data.get("AssociationDefaultRouteTableId") is not None:
        out["association_default_route_table_id"] = data[
            "AssociationDefaultRouteTableId"
        ]
    if data.get("PropagationDefaultRouteTableId") is not None:
        out["propagation_default_route_table_id"] = data[
            "PropagationDefaultRouteTableId"
        ]
    if data.get("VpnEcmpSupport") is not None:
        out["vpn_ecmp_support"] = data["VpnEcmpSupport"]
    if data.get("DnsSupport") is not None:
        out["dns_support"] = data["DnsSupport"]
    if data.get("MulticastSupport") is not None:
        out["multicast_support"] = data["MulticastSupport"]
    if data.get("AmazonSideAsn") is not None:
        out["amazon_side_asn"] = data["AmazonSideAsn"]
    return out
