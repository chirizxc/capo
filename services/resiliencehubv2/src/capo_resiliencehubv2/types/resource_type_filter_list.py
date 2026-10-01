"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.resource_type_filter

ResourceTypeFilterList: TypeAlias = list[
    "capo_resiliencehubv2.types.resource_type_filter.ResourceTypeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceTypeFilterList:
    return [item for item in data if item is not None]
