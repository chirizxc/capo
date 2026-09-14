"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_id
    import capo_qbusiness.types.attachment_name
    import capo_qbusiness.types.attachment_status
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.error_detail


class AttachmentOutput(TypedDict, closed=True):
    name: NotRequired["capo_qbusiness.types.attachment_name.AttachmentName"]
    """<p>The name of a file uploaded during chat.</p>"""
    status: NotRequired["capo_qbusiness.types.attachment_status.AttachmentStatus"]
    """<p>The status of a file uploaded during chat.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>An error associated with a file uploaded during chat.</p>"""
    attachment_id: NotRequired["capo_qbusiness.types.attachment_id.AttachmentId"]
    """<p>The unique identifier of the Amazon Q Business attachment.</p>"""
    conversation_id: NotRequired["capo_qbusiness.types.conversation_id.ConversationId"]
    """<p>The unique identifier of the Amazon Q Business conversation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_qbusiness.types.attachment_status

        out["status"] = capo_qbusiness.types.attachment_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    return out


def deserialize_json(data: dict) -> AttachmentOutput:
    out: AttachmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_qbusiness.types.attachment_status

        out["status"] = capo_qbusiness.types.attachment_status.deserialize_json(
            data["status"]
        )
    if data.get("error") is not None:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    return out
