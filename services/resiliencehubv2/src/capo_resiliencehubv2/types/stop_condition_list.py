"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StopConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.stop_condition

StopConditionList: TypeAlias = list[
    "capo_resiliencehubv2.types.stop_condition.StopCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: StopConditionList) -> list:
    import capo_resiliencehubv2.types.stop_condition

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.stop_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> StopConditionList:
    import capo_resiliencehubv2.types.stop_condition

    out: StopConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.stop_condition.deserialize_json(item))
    return out
