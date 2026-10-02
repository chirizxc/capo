"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.nat_gateway_mapping

NatGatewayMappingsList: TypeAlias = list[
    "capo_network_firewall.types.nat_gateway_mapping.NatGatewayMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayMappingsList) -> list:
    import capo_network_firewall.types.nat_gateway_mapping

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.nat_gateway_mapping.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NatGatewayMappingsList:
    import capo_network_firewall.types.nat_gateway_mapping

    out: NatGatewayMappingsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.nat_gateway_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
