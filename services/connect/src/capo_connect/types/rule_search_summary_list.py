"""Generated from Smithy shape ``com.amazonaws.connect#RuleSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.rule_search_summary

RuleSearchSummaryList: TypeAlias = list[
    "capo_connect.types.rule_search_summary.RuleSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSearchSummaryList) -> list:
    import capo_connect.types.rule_search_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.rule_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleSearchSummaryList:
    import capo_connect.types.rule_search_summary

    out: RuleSearchSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.rule_search_summary.deserialize_json(item))
    return out
