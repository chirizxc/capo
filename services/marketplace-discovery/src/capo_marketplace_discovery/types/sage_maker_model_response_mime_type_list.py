"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SageMakerModelResponseMimeTypeList``."""

from typing import TypeAlias

SageMakerModelResponseMimeTypeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerModelResponseMimeTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> SageMakerModelResponseMimeTypeList:
    return [item for item in data if item is not None]
