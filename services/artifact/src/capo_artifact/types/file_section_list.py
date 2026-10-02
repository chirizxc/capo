"""Generated from Smithy shape ``com.amazonaws.artifact#FileSectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_artifact.types.short_string_attribute

FileSectionList: TypeAlias = list[
    "capo_artifact.types.short_string_attribute.ShortStringAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSectionList) -> list:
    return list(value)


def deserialize_json(data: list) -> FileSectionList:
    return [item for item in data if item is not None]
