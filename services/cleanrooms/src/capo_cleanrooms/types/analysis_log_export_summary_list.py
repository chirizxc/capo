"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisLogExportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export_summary

AnalysisLogExportSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_log_export_summary.AnalysisLogExportSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisLogExportSummaryList) -> list:
    import capo_cleanrooms.types.analysis_log_export_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.analysis_log_export_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalysisLogExportSummaryList:
    import capo_cleanrooms.types.analysis_log_export_summary

    out: AnalysisLogExportSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.analysis_log_export_summary.deserialize_json(item)
        )
    return out
