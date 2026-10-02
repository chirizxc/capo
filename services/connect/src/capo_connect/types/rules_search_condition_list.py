"""Generated from Smithy shape ``com.amazonaws.connect#RulesSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.rules_search_criteria

RulesSearchConditionList: TypeAlias = list[
    "capo_connect.types.rules_search_criteria.RulesSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: RulesSearchConditionList) -> list:
    import capo_connect.types.rules_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.rules_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> RulesSearchConditionList:
    import capo_connect.types.rules_search_criteria

    out: RulesSearchConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.rules_search_criteria.deserialize_json(item))
    return out
