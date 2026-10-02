"""Generated from Smithy shape ``com.amazonaws.connect#CreateAttachedFileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.file_id
    import capo_connect.types.file_status_type
    import capo_connect.types.iso8601_datetime


class CreateAttachedFileResponse(TypedDict, closed=True):
    file_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The unique identifier of the attached file resource (ARN).</p>"""
    file_id: NotRequired["capo_connect.types.file_id.FileId"]
    """<p>The unique identifier of the attached file resource.</p>"""
    creation_time: NotRequired["capo_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: <code>yyyy-MM-ddThh:mm:ss.SSSZ</code>. For example, <code>2024-05-03T02:41:28.172Z</code>.</p>"""
    file_status: NotRequired["capo_connect.types.file_status_type.FileStatusType"]
    """<p>The current status of the attached file. Valid values: <code>PROCESSING</code> | <code>APPROVED</code> | <code>REJECTED</code> | <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttachedFileResponse) -> dict:
    out: dict = {}
    if "file_arn" in value:
        out["FileArn"] = value["file_arn"]
    if "file_id" in value:
        out["FileId"] = value["file_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "file_status" in value:
        import capo_connect.types.file_status_type

        out["FileStatus"] = capo_connect.types.file_status_type.serialize_json(
            value["file_status"]
        )
    return out


def deserialize_json(data: dict) -> CreateAttachedFileResponse:
    out: CreateAttachedFileResponse = {}  # type: ignore[typeddict-item]
    if data.get("FileArn") is not None:
        out["file_arn"] = data["FileArn"]
    if data.get("FileId") is not None:
        out["file_id"] = data["FileId"]
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    if data.get("FileStatus") is not None:
        import capo_connect.types.file_status_type

        out["file_status"] = capo_connect.types.file_status_type.deserialize_json(
            data["FileStatus"]
        )
    return out
