"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_version_summary

IntermediateTableVersionSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.intermediate_table_version_summary.IntermediateTableVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableVersionSummaryList) -> list:
    import capo_cleanrooms.types.intermediate_table_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.intermediate_table_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IntermediateTableVersionSummaryList:
    import capo_cleanrooms.types.intermediate_table_version_summary

    out: IntermediateTableVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.intermediate_table_version_summary.deserialize_json(
                item
            )
        )
    return out
