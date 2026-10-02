"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DependencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_dependency

DependencyList: TypeAlias = list[
    "capo_cleanrooms.types.intermediate_table_dependency.IntermediateTableDependency"
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyList) -> list:
    import capo_cleanrooms.types.intermediate_table_dependency

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.intermediate_table_dependency.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DependencyList:
    import capo_cleanrooms.types.intermediate_table_dependency

    out: DependencyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.intermediate_table_dependency.deserialize_json(item)
        )
    return out
