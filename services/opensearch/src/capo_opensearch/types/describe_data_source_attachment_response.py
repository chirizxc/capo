"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDataSourceAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.data_source_attachment_status
    import capo_opensearch.types.id
    import capo_opensearch.types.string


class DescribeDataSourceAttachmentResponse(TypedDict, closed=True):
    attachment_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The unique identifier assigned to the data source attachment.</p>"""
    id: NotRequired["capo_opensearch.types.id.Id"]
    """<p>The unique identifier of the OpenSearch application.</p>"""
    arn: NotRequired["capo_opensearch.types.arn.ARN"]
    data_source_arn: NotRequired["capo_opensearch.types.arn.ARN"]
    status: NotRequired[
        "capo_opensearch.types.data_source_attachment_status.DataSourceAttachmentStatus"
    ]
    """<p>The status of the data source attachment. Valid values are <code>PENDING</code>, <code>ATTACHED</code>, and <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSourceAttachmentResponse) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
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


def deserialize_json(data: dict) -> DescribeDataSourceAttachmentResponse:
    out: DescribeDataSourceAttachmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
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
