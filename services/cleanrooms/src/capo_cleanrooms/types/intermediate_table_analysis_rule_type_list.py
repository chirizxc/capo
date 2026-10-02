"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableAnalysisRuleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type

IntermediateTableAnalysisRuleTypeList: TypeAlias = list[
    "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableAnalysisRuleTypeList) -> list:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.intermediate_table_analysis_rule_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IntermediateTableAnalysisRuleTypeList:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type

    out: IntermediateTableAnalysisRuleTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.intermediate_table_analysis_rule_type.deserialize_json(
                item
            )
        )
    return out
