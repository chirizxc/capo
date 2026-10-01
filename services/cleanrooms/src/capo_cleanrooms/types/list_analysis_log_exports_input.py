"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListAnalysisLogExportsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export_status
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.uuid


class ListAnalysisLogExportsInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership to list analysis log exports for. Currently accepts the membership ID.</p>"""
    analysis_identifier: NotRequired["capo_cleanrooms.types.uuid.UUID"]
    """<p>A filter on the unique identifier of the protected query that the analysis logs were exported for.</p>"""
    status: NotRequired[
        "capo_cleanrooms.types.analysis_log_export_status.AnalysisLogExportStatus"
    ]
    """<p>A filter on the status of the analysis log export.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalysisLogExportsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAnalysisLogExportsInput:
    out: ListAnalysisLogExportsInput = {}  # type: ignore[typeddict-item]
    return out
