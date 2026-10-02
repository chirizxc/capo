"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedAdditionalAnalysesSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.inherited_additional_analyses_source

InheritedAdditionalAnalysesSourceList: TypeAlias = list[
    "capo_cleanrooms.types.inherited_additional_analyses_source.InheritedAdditionalAnalysesSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: InheritedAdditionalAnalysesSourceList) -> list:
    import capo_cleanrooms.types.inherited_additional_analyses_source

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.inherited_additional_analyses_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InheritedAdditionalAnalysesSourceList:
    import capo_cleanrooms.types.inherited_additional_analyses_source

    out: InheritedAdditionalAnalysesSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.inherited_additional_analyses_source.deserialize_json(
                item
            )
        )
    return out
