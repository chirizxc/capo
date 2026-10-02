"""Generated from Smithy shape ``com.amazonaws.connect#PreEvaluationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.pre_evaluation_filter

PreEvaluationFilterList: TypeAlias = list[
    "capo_connect.types.pre_evaluation_filter.PreEvaluationFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PreEvaluationFilterList) -> list:
    import capo_connect.types.pre_evaluation_filter

    out: list = []
    for item in value:
        out.append(capo_connect.types.pre_evaluation_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> PreEvaluationFilterList:
    import capo_connect.types.pre_evaluation_filter

    out: PreEvaluationFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.pre_evaluation_filter.deserialize_json(item))
    return out
