"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageCidrIpAddressList``."""

from typing import TypeAlias

AmazonMachineImageCidrIpAddressList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageCidrIpAddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> AmazonMachineImageCidrIpAddressList:
    return [item for item in data if item is not None]
