"""Generated from Smithy shape ``com.amazonaws.artifact#CreateComplianceInquiryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.inquiry_summary
    import capo_artifact.types.tags_map


class CreateComplianceInquiryResponse(TypedDict, closed=True):
    compliance_inquiry_summary: NotRequired[
        "capo_artifact.types.inquiry_summary.InquirySummary"
    ]
    """<p>Summary information about the created compliance inquiry.</p>"""
    tags: NotRequired["capo_artifact.types.tags_map.TagsMap"]
    """<p>Tags associated with the compliance inquiry resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComplianceInquiryResponse) -> dict:
    out: dict = {}
    if "compliance_inquiry_summary" in value:
        import capo_artifact.types.inquiry_summary

        out["complianceInquirySummary"] = (
            capo_artifact.types.inquiry_summary.serialize_json(
                value["compliance_inquiry_summary"]
            )
        )
    if "tags" in value:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateComplianceInquiryResponse:
    out: CreateComplianceInquiryResponse = {}  # type: ignore[typeddict-item]
    if data.get("complianceInquirySummary") is not None:
        import capo_artifact.types.inquiry_summary

        out["compliance_inquiry_summary"] = (
            capo_artifact.types.inquiry_summary.deserialize_json(
                data["complianceInquirySummary"]
            )
        )
    if data.get("tags") is not None:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.deserialize_json(data["tags"])
    return out
