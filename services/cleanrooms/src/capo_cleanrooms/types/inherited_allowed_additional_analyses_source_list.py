"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedAllowedAdditionalAnalysesSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.inherited_allowed_additional_analyses_source

InheritedAllowedAdditionalAnalysesSourceList: TypeAlias = list[
    "capo_cleanrooms.types.inherited_allowed_additional_analyses_source.InheritedAllowedAdditionalAnalysesSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: InheritedAllowedAdditionalAnalysesSourceList) -> list:
    import capo_cleanrooms.types.inherited_allowed_additional_analyses_source

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.inherited_allowed_additional_analyses_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InheritedAllowedAdditionalAnalysesSourceList:
    import capo_cleanrooms.types.inherited_allowed_additional_analyses_source

    out: InheritedAllowedAdditionalAnalysesSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.inherited_allowed_additional_analyses_source.deserialize_json(
                item
            )
        )
    return out
