"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SageMakerModelContentTypeList``."""

from typing import TypeAlias

SageMakerModelContentTypeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerModelContentTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> SageMakerModelContentTypeList:
    return [item for item in data if item is not None]
