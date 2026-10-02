"""Generated from Smithy shape ``com.amazonaws.quicksight#EffectiveLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.effective_limit

EffectiveLimitList: TypeAlias = list[
    "capo_quicksight.types.effective_limit.EffectiveLimit"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveLimitList) -> list:
    import capo_quicksight.types.effective_limit

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.effective_limit.serialize_json(item))
    return out


def deserialize_json(data: list) -> EffectiveLimitList:
    import capo_quicksight.types.effective_limit

    out: EffectiveLimitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.effective_limit.deserialize_json(item))
    return out
