"""Generated from Smithy shape ``com.amazonaws.guardduty#AssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.association_summary

AssociationSummaryList: TypeAlias = list[
    "capo_guardduty.types.association_summary.AssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationSummaryList) -> list:
    import capo_guardduty.types.association_summary

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.association_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociationSummaryList:
    import capo_guardduty.types.association_summary

    out: AssociationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.association_summary.deserialize_json(item))
    return out
