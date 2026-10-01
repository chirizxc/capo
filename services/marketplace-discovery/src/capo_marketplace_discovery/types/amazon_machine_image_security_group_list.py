"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageSecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.amazon_machine_image_security_group

AmazonMachineImageSecurityGroupList: TypeAlias = list[
    "capo_marketplace_discovery.types.amazon_machine_image_security_group.AmazonMachineImageSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageSecurityGroupList) -> list:
    import capo_marketplace_discovery.types.amazon_machine_image_security_group

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.amazon_machine_image_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AmazonMachineImageSecurityGroupList:
    import capo_marketplace_discovery.types.amazon_machine_image_security_group

    out: AmazonMachineImageSecurityGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_discovery.types.amazon_machine_image_security_group.deserialize_json(
                item
            )
        )
    return out
