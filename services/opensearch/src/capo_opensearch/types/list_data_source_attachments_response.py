"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDataSourceAttachmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.data_source_attachment_summary_list
    import capo_opensearch.types.string


class ListDataSourceAttachmentsResponse(TypedDict, closed=True):
    attachments: NotRequired[
        "capo_opensearch.types.data_source_attachment_summary_list.DataSourceAttachmentSummaryList"
    ]
    """<p>A list of data source attachment summaries for the specified application.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>The pagination token to use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourceAttachmentsResponse) -> dict:
    out: dict = {}
    if "attachments" in value:
        import capo_opensearch.types.data_source_attachment_summary_list

        out["attachments"] = (
            capo_opensearch.types.data_source_attachment_summary_list.serialize_json(
                value["attachments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSourceAttachmentsResponse:
    out: ListDataSourceAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("attachments") is not None:
        import capo_opensearch.types.data_source_attachment_summary_list

        out["attachments"] = (
            capo_opensearch.types.data_source_attachment_summary_list.deserialize_json(
                data["attachments"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
