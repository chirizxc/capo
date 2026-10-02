"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceAttachmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.data_source_attachment_summary

DataSourceAttachmentSummaryList: TypeAlias = list[
    "capo_opensearch.types.data_source_attachment_summary.DataSourceAttachmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceAttachmentSummaryList) -> list:
    import capo_opensearch.types.data_source_attachment_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearch.types.data_source_attachment_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataSourceAttachmentSummaryList:
    import capo_opensearch.types.data_source_attachment_summary

    out: DataSourceAttachmentSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearch.types.data_source_attachment_summary.deserialize_json(item)
        )
    return out
