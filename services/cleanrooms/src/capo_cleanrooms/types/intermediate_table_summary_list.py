"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_summary

IntermediateTableSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.intermediate_table_summary.IntermediateTableSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableSummaryList) -> list:
    import capo_cleanrooms.types.intermediate_table_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.intermediate_table_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntermediateTableSummaryList:
    import capo_cleanrooms.types.intermediate_table_summary

    out: IntermediateTableSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.intermediate_table_summary.deserialize_json(item)
        )
    return out
