"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceAttachmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.data_source_attachment_status
    import capo_opensearch.types.string


class DataSourceAttachmentSummary(TypedDict, closed=True):
    attachment_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The unique identifier assigned to the data source attachment.</p>"""
    data_source_arn: NotRequired["capo_opensearch.types.arn.ARN"]
    status: NotRequired[
        "capo_opensearch.types.data_source_attachment_status.DataSourceAttachmentStatus"
    ]
    """<p>The current status of the data source attachment. Valid values are <code>PENDING</code>, <code>ATTACHED</code>, and <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceAttachmentSummary) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "data_source_arn" in value:
        out["dataSourceArn"] = value["data_source_arn"]
    if "status" in value:
        import capo_opensearch.types.data_source_attachment_status

        out["status"] = (
            capo_opensearch.types.data_source_attachment_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceAttachmentSummary:
    out: DataSourceAttachmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    if data.get("dataSourceArn") is not None:
        out["data_source_arn"] = data["dataSourceArn"]
    if data.get("status") is not None:
        import capo_opensearch.types.data_source_attachment_status

        out["status"] = (
            capo_opensearch.types.data_source_attachment_status.deserialize_json(
                data["status"]
            )
        )
    return out
