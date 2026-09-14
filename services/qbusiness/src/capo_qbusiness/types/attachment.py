"""Generated from Smithy shape ``com.amazonaws.qbusiness#Attachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_id
    import capo_qbusiness.types.attachment_name
    import capo_qbusiness.types.attachment_status
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.copy_from_source
    import capo_qbusiness.types.error_detail
    import capo_qbusiness.types.integer
    import capo_qbusiness.types.string
    import capo_qbusiness.types.timestamp


class Attachment(TypedDict, closed=True):
    attachment_id: NotRequired["capo_qbusiness.types.attachment_id.AttachmentId"]
    """<p>The identifier of the Amazon Q Business attachment.</p>"""
    conversation_id: NotRequired["capo_qbusiness.types.conversation_id.ConversationId"]
    """<p>The identifier of the Amazon Q Business conversation the attachment is associated with.</p>"""
    name: NotRequired["capo_qbusiness.types.attachment_name.AttachmentName"]
    """<p>Filename of the Amazon Q Business attachment.</p>"""
    copy_from: NotRequired["capo_qbusiness.types.copy_from_source.CopyFromSource"]
    """<p>A CopyFromSource containing a reference to the original source of the Amazon Q Business attachment.</p>"""
    file_type: NotRequired["capo_qbusiness.types.string.String"]
    """<p>Filetype of the Amazon Q Business attachment.</p>"""
    file_size: NotRequired["capo_qbusiness.types.integer.Integer"]
    """<p>Size in bytes of the Amazon Q Business attachment.</p>"""
    md5chksum: NotRequired["capo_qbusiness.types.string.String"]
    """<p>MD5 checksum of the Amazon Q Business attachment contents.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business attachment was created.</p>"""
    status: NotRequired["capo_qbusiness.types.attachment_status.AttachmentStatus"]
    """<p>AttachmentStatus of the Amazon Q Business attachment.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>ErrorDetail providing information about a Amazon Q Business attachment error. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attachment) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "copy_from" in value:
        import capo_qbusiness.types.copy_from_source

        out["copyFrom"] = capo_qbusiness.types.copy_from_source.serialize_json(
            value["copy_from"]
        )
    if "file_type" in value:
        out["fileType"] = value["file_type"]
    if "file_size" in value:
        out["fileSize"] = value["file_size"]
    if "md5chksum" in value:
        out["md5chksum"] = value["md5chksum"]
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "status" in value:
        import capo_qbusiness.types.attachment_status

        out["status"] = capo_qbusiness.types.attachment_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> Attachment:
    out: Attachment = {}  # type: ignore[typeddict-item]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("copyFrom") is not None:
        import capo_qbusiness.types.copy_from_source

        out["copy_from"] = capo_qbusiness.types.copy_from_source.deserialize_json(
            data["copyFrom"]
        )
    if data.get("fileType") is not None:
        out["file_type"] = data["fileType"]
    if data.get("fileSize") is not None:
        out["file_size"] = data["fileSize"]
    if data.get("md5chksum") is not None:
        out["md5chksum"] = data["md5chksum"]
    if data.get("createdAt") is not None:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("status") is not None:
        import capo_qbusiness.types.attachment_status

        out["status"] = capo_qbusiness.types.attachment_status.deserialize_json(
            data["status"]
        )
    if data.get("error") is not None:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    return out
