"""Generated from Smithy shape ``com.amazonaws.quicksight#DlpSettingSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dlp_setting_summary

DlpSettingSummaryList: TypeAlias = list[
    "capo_quicksight.types.dlp_setting_summary.DlpSettingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DlpSettingSummaryList) -> list:
    import capo_quicksight.types.dlp_setting_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dlp_setting_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DlpSettingSummaryList:
    import capo_quicksight.types.dlp_setting_summary

    out: DlpSettingSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.dlp_setting_summary.deserialize_json(item))
    return out
