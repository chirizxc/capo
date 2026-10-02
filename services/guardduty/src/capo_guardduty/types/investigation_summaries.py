"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_summary

InvestigationSummaries: TypeAlias = list[
    "capo_guardduty.types.investigation_summary.InvestigationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationSummaries) -> list:
    import capo_guardduty.types.investigation_summary

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.investigation_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvestigationSummaries:
    import capo_guardduty.types.investigation_summary

    out: InvestigationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.investigation_summary.deserialize_json(item))
    return out
