"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#MultiviewLayoutList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.multiview_layout_type

MultiviewLayoutList: TypeAlias = list[
    "capo_mediapackagev2.types.multiview_layout_type.MultiviewLayoutType"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiviewLayoutList) -> list:
    import capo_mediapackagev2.types.multiview_layout_type

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.multiview_layout_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> MultiviewLayoutList:
    import capo_mediapackagev2.types.multiview_layout_type

    out: MultiviewLayoutList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediapackagev2.types.multiview_layout_type.deserialize_json(item)
        )
    return out
