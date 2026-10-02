"""Generated from Smithy shape ``com.amazonaws.connect#ExtractionDefinitionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.extraction_definition_summary

ExtractionDefinitionSummaryList: TypeAlias = list[
    "capo_connect.types.extraction_definition_summary.ExtractionDefinitionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionDefinitionSummaryList) -> list:
    import capo_connect.types.extraction_definition_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.extraction_definition_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExtractionDefinitionSummaryList:
    import capo_connect.types.extraction_definition_summary

    out: ExtractionDefinitionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.extraction_definition_summary.deserialize_json(item)
        )
    return out
