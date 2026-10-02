"""Generated from Smithy shape ``com.amazonaws.quicksight#AppSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.app_summary

AppSummaryList: TypeAlias = list["capo_quicksight.types.app_summary.AppSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: AppSummaryList) -> list:
    import capo_quicksight.types.app_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.app_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppSummaryList:
    import capo_quicksight.types.app_summary

    out: AppSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.app_summary.deserialize_json(item))
    return out
