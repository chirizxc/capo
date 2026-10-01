"""Generated from Smithy shape ``com.amazonaws.artifact#InquirySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_artifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_artifact.types.input_source
    import capo_artifact.types.inquiry_id
    import capo_artifact.types.inquiry_status
    import capo_artifact.types.inquiry_status_message
    import capo_artifact.types.timestamp_attribute


class InquirySummary(TypedDict, closed=True):
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


# --- restJson1 ser/de ---
def serialize_json(value: InquirySummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> InquirySummary:
    out: InquirySummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("InquirySummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("InquirySummary.name required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("InquirySummary.id required")
    if data.get("status") is not None:
        import capo_artifact.types.inquiry_status

        out["status"] = capo_artifact.types.inquiry_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("InquirySummary.status required")
    if data.get("statusMessage") is not None:
        import capo_artifact.types.inquiry_status_message

        out["status_message"] = (
            capo_artifact.types.inquiry_status_message.deserialize_json(
                data["statusMessage"]
            )
        )
    else:
        raise DeserializationError("InquirySummary.status_message required")
    if data.get("inputSource") is not None:
        import capo_artifact.types.input_source

        out["input_source"] = capo_artifact.types.input_source.deserialize_json(
            data["inputSource"]
        )
    else:
        raise DeserializationError("InquirySummary.input_source required")
    if data.get("createdAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["created_at"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("InquirySummary.created_at required")
    return out
