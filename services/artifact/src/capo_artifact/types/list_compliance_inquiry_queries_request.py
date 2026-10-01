"""Generated from Smithy shape ``com.amazonaws.artifact#ListComplianceInquiryQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.inquiry_id
    import capo_artifact.types.max_results_attribute
    import capo_artifact.types.next_token_attribute


class ListComplianceInquiryQueriesRequest(TypedDict, closed=True):
    compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId"
    """<p>Unique resource ID for the compliance inquiry.</p>"""
    max_results: NotRequired[
        "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
    ]
    """<p>Maximum number of resources to return in the paginated response.</p>"""
    next_token: NotRequired[
        "capo_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComplianceInquiryQueriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListComplianceInquiryQueriesRequest:
    out: ListComplianceInquiryQueriesRequest = {}  # type: ignore[typeddict-item]
    return out
