"""Generated from Smithy shape ``com.amazonaws.artifact#GetComplianceInquiryMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.inquiry_id


class GetComplianceInquiryMetadataRequest(TypedDict, closed=True):
    compliance_inquiry_id: "capo_artifact.types.inquiry_id.InquiryId"
    """<p>Unique resource ID for the compliance inquiry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComplianceInquiryMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComplianceInquiryMetadataRequest:
    out: GetComplianceInquiryMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
