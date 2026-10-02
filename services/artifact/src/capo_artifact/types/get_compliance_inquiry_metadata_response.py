"""Generated from Smithy shape ``com.amazonaws.artifact#GetComplianceInquiryMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.inquiry_detail
    import capo_artifact.types.tags_map


class GetComplianceInquiryMetadataResponse(TypedDict, closed=True):
    compliance_inquiry_detail: NotRequired[
        "capo_artifact.types.inquiry_detail.InquiryDetail"
    ]
    """<p>Detailed information about the compliance inquiry.</p>"""
    tags: NotRequired["capo_artifact.types.tags_map.TagsMap"]
    """<p>Tags associated with the compliance inquiry resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComplianceInquiryMetadataResponse) -> dict:
    out: dict = {}
    if "compliance_inquiry_detail" in value:
        import capo_artifact.types.inquiry_detail

        out["complianceInquiryDetail"] = (
            capo_artifact.types.inquiry_detail.serialize_json(
                value["compliance_inquiry_detail"]
            )
        )
    if "tags" in value:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetComplianceInquiryMetadataResponse:
    out: GetComplianceInquiryMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("complianceInquiryDetail") is not None:
        import capo_artifact.types.inquiry_detail

        out["compliance_inquiry_detail"] = (
            capo_artifact.types.inquiry_detail.deserialize_json(
                data["complianceInquiryDetail"]
            )
        )
    if data.get("tags") is not None:
        import capo_artifact.types.tags_map

        out["tags"] = capo_artifact.types.tags_map.deserialize_json(data["tags"])
    return out
