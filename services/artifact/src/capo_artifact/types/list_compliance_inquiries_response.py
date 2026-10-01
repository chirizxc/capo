"""Generated from Smithy shape ``com.amazonaws.artifact#ListComplianceInquiriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.inquiries_list
    import capo_artifact.types.next_token_attribute


class ListComplianceInquiriesResponse(TypedDict, closed=True):
    compliance_inquiries: NotRequired[
        "capo_artifact.types.inquiries_list.InquiriesList"
    ]
    """<p>List of compliance inquiry resources.</p>"""
    next_token: NotRequired[
        "capo_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComplianceInquiriesResponse) -> dict:
    out: dict = {}
    if "compliance_inquiries" in value:
        import capo_artifact.types.inquiries_list

        out["complianceInquiries"] = capo_artifact.types.inquiries_list.serialize_json(
            value["compliance_inquiries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComplianceInquiriesResponse:
    out: ListComplianceInquiriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("complianceInquiries") is not None:
        import capo_artifact.types.inquiries_list

        out["compliance_inquiries"] = (
            capo_artifact.types.inquiries_list.deserialize_json(
                data["complianceInquiries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
