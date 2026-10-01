"""Generated from Smithy shape ``com.amazonaws.imagebuilder#RegionFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.region_failure

RegionFailureList: TypeAlias = list[
    "capo_imagebuilder.types.region_failure.RegionFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionFailureList) -> list:
    import capo_imagebuilder.types.region_failure

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.region_failure.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegionFailureList:
    import capo_imagebuilder.types.region_failure

    out: RegionFailureList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_imagebuilder.types.region_failure.deserialize_json(item))
    return out
