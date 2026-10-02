"""Generated from Smithy shape ``com.amazonaws.artifact#InquiriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_artifact.types.inquiry_summary

InquiriesList: TypeAlias = list["capo_artifact.types.inquiry_summary.InquirySummary"]


# --- restJson1 ser/de ---
def serialize_json(value: InquiriesList) -> list:
    import capo_artifact.types.inquiry_summary

    out: list = []
    for item in value:
        out.append(capo_artifact.types.inquiry_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InquiriesList:
    import capo_artifact.types.inquiry_summary

    out: InquiriesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_artifact.types.inquiry_summary.deserialize_json(item))
    return out
