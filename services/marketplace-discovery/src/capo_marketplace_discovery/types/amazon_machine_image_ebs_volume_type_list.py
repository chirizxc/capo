"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageEbsVolumeTypeList``."""

from typing import TypeAlias

AmazonMachineImageEbsVolumeTypeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageEbsVolumeTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> AmazonMachineImageEbsVolumeTypeList:
    return [item for item in data if item is not None]
