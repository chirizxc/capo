"""Generated from Smithy shape ``com.amazonaws.artifact#InquiryDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_artifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_artifact.types.input_source
    import capo_artifact.types.inquiry_id
    import capo_artifact.types.inquiry_status
    import capo_artifact.types.inquiry_status_message
    import capo_artifact.types.inquiry_support_mode
    import capo_artifact.types.timestamp_attribute


class InquiryDetail(TypedDict, closed=True):
    arn: "str"
    """<p>ARN of the compliance inquiry resource.</p>"""
    name: "str"
    """<p>Title of the inquiry.</p>"""
    id: "capo_artifact.types.inquiry_id.InquiryId"
    """<p>Unique resource ID for the compliance inquiry.</p>"""
    status: "capo_artifact.types.inquiry_status.InquiryStatus"
    """<p>Current processing status of the inquiry.</p>"""
    status_message: "capo_artifact.types.inquiry_status_message.InquiryStatusMessage"
    """<p>Status message providing additional context.</p>"""
    input_source: "capo_artifact.types.input_source.InputSource"
    """<p>Type of inquiry content (text or file).</p>"""
    created_at: "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    """<p>Timestamp indicating when the resource was created.</p>"""
    updated_at: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the resource was last modified.</p>"""
    support_mode: NotRequired[
        "capo_artifact.types.inquiry_support_mode.InquirySupportMode"
    ]
    """<p>Support mode for this inquiry. AI_ONLY provides AI-generated responses. FULL_SUPPORT includes human expert review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InquiryDetail) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    import capo_artifact.types.inquiry_status

    out["status"] = capo_artifact.types.inquiry_status.serialize_json(value["status"])
    import capo_artifact.types.inquiry_status_message

    out["statusMessage"] = capo_artifact.types.inquiry_status_message.serialize_json(
        value["status_message"]
    )
    import capo_artifact.types.input_source

    out["inputSource"] = capo_artifact.types.input_source.serialize_json(
        value["input_source"]
    )
    import capo_artifact.types.timestamp_attribute

    out["createdAt"] = capo_artifact.types.timestamp_attribute.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_artifact.types.timestamp_attribute

        out["updatedAt"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["updated_at"]
        )
    if "support_mode" in value:
        import capo_artifact.types.inquiry_support_mode

        out["supportMode"] = capo_artifact.types.inquiry_support_mode.serialize_json(
            value["support_mode"]
        )
    return out


def deserialize_json(data: dict) -> InquiryDetail:
    out: InquiryDetail = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("InquiryDetail.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("InquiryDetail.name required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("InquiryDetail.id required")
    if data.get("status") is not None:
        import capo_artifact.types.inquiry_status

        out["status"] = capo_artifact.types.inquiry_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("InquiryDetail.status required")
    if data.get("statusMessage") is not None:
        import capo_artifact.types.inquiry_status_message

        out["status_message"] = (
            capo_artifact.types.inquiry_status_message.deserialize_json(
                data["statusMessage"]
            )
        )
    else:
        raise DeserializationError("InquiryDetail.status_message required")
    if data.get("inputSource") is not None:
        import capo_artifact.types.input_source

        out["input_source"] = capo_artifact.types.input_source.deserialize_json(
            data["inputSource"]
        )
    else:
        raise DeserializationError("InquiryDetail.input_source required")
    if data.get("createdAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["created_at"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("InquiryDetail.created_at required")
    if data.get("updatedAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["updated_at"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["updatedAt"]
        )
    if data.get("supportMode") is not None:
        import capo_artifact.types.inquiry_support_mode

        out["support_mode"] = capo_artifact.types.inquiry_support_mode.deserialize_json(
            data["supportMode"]
        )
    return out
