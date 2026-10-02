"""Generated from Smithy shape ``com.amazonaws.connect#MetricSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.metric_search_criteria

MetricSearchConditionList: TypeAlias = list[
    "capo_connect.types.metric_search_criteria.MetricSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricSearchConditionList) -> list:
    import capo_connect.types.metric_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.metric_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricSearchConditionList:
    import capo_connect.types.metric_search_criteria

    out: MetricSearchConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.metric_search_criteria.deserialize_json(item))
    return out
