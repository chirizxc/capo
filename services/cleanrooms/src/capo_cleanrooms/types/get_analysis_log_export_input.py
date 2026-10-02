"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetAnalysisLogExportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export_identifier
    import capo_cleanrooms.types.membership_identifier


class GetAnalysisLogExportInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership that the analysis log export belongs to. Currently accepts the membership ID.</p>"""
    analysis_log_export_identifier: "capo_cleanrooms.types.analysis_log_export_identifier.AnalysisLogExportIdentifier"
    """<p>The unique identifier of the analysis log export to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalysisLogExportInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnalysisLogExportInput:
    out: GetAnalysisLogExportInput = {}  # type: ignore[typeddict-item]
    return out
