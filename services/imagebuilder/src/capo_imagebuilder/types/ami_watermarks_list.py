"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AmiWatermarksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.ami_watermark_name

AmiWatermarksList: TypeAlias = list[
    "capo_imagebuilder.types.ami_watermark_name.AmiWatermarkName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AmiWatermarksList) -> list:
    return list(value)


def deserialize_json(data: list) -> AmiWatermarksList:
    return [item for item in data if item is not None]
