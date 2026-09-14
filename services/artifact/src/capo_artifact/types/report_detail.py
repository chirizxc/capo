"""Generated from Smithy shape ``com.amazonaws.artifact#ReportDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.acceptance_type
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.published_state
    import capo_artifact.types.report_id
    import capo_artifact.types.sequence_number_attribute
    import capo_artifact.types.short_string_attribute
    import capo_artifact.types.status_message
    import capo_artifact.types.timestamp_attribute
    import capo_artifact.types.upload_state
    import capo_artifact.types.version_attribute


class ReportDetail(TypedDict, closed=True):
    id: NotRequired["capo_artifact.types.report_id.ReportId"]
    """<p>Unique resource ID for the report resource.</p>"""
    name: NotRequired["capo_artifact.types.short_string_attribute.ShortStringAttribute"]
    """<p>Name for the report resource.</p>"""
    description: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Description for the report resource.</p>"""
    period_start: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating the report resource effective start.</p>"""
    period_end: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating the report resource effective end.</p>"""
    created_at: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the report resource was created.</p>"""
    last_modified_at: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the report resource was last modified.</p>"""
    deleted_at: NotRequired[
        "capo_artifact.types.timestamp_attribute.TimestampAttribute"
    ]
    """<p>Timestamp indicating when the report resource was deleted.</p>"""
    state: NotRequired["capo_artifact.types.published_state.PublishedState"]
    """<p>Current state of the report resource</p>"""
    arn: NotRequired["capo_artifact.types.long_string_attribute.LongStringAttribute"]
    """<p>ARN for the report resource.</p>"""
    series: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Series for the report resource.</p>"""
    category: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Category for the report resource.</p>"""
    company_name: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Associated company name for the report resource.</p>"""
    product_name: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Associated product name for the report resource.</p>"""
    term_arn: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Unique resource ARN for term resource.</p>"""
    version: NotRequired["capo_artifact.types.version_attribute.VersionAttribute"]
    """<p>Version for the report resource.</p>"""
    acceptance_type: NotRequired["capo_artifact.types.acceptance_type.AcceptanceType"]
    """<p>Acceptance type for report.</p>"""
    sequence_number: NotRequired[
        "capo_artifact.types.sequence_number_attribute.SequenceNumberAttribute"
    ]
    """<p>Sequence number to enforce optimistic locking.</p>"""
    upload_state: NotRequired["capo_artifact.types.upload_state.UploadState"]
    """<p>The current state of the document upload.</p>"""
    status_message: NotRequired["capo_artifact.types.status_message.StatusMessage"]
    """<p>The message associated with the current upload state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "period_start" in value:
        import capo_artifact.types.timestamp_attribute

        out["periodStart"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["period_start"]
        )
    if "period_end" in value:
        import capo_artifact.types.timestamp_attribute

        out["periodEnd"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["period_end"]
        )
    if "created_at" in value:
        import capo_artifact.types.timestamp_attribute

        out["createdAt"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import capo_artifact.types.timestamp_attribute

        out["lastModifiedAt"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["last_modified_at"]
        )
    if "deleted_at" in value:
        import capo_artifact.types.timestamp_attribute

        out["deletedAt"] = capo_artifact.types.timestamp_attribute.serialize_json(
            value["deleted_at"]
        )
    if "state" in value:
        import capo_artifact.types.published_state

        out["state"] = capo_artifact.types.published_state.serialize_json(
            value["state"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "series" in value:
        out["series"] = value["series"]
    if "category" in value:
        out["category"] = value["category"]
    if "company_name" in value:
        out["companyName"] = value["company_name"]
    if "product_name" in value:
        out["productName"] = value["product_name"]
    if "term_arn" in value:
        out["termArn"] = value["term_arn"]
    if "version" in value:
        out["version"] = value["version"]
    if "acceptance_type" in value:
        import capo_artifact.types.acceptance_type

        out["acceptanceType"] = capo_artifact.types.acceptance_type.serialize_json(
            value["acceptance_type"]
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    if "upload_state" in value:
        import capo_artifact.types.upload_state

        out["uploadState"] = capo_artifact.types.upload_state.serialize_json(
            value["upload_state"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ReportDetail:
    out: ReportDetail = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("periodStart") is not None:
        import capo_artifact.types.timestamp_attribute

        out["period_start"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["periodStart"]
        )
    if data.get("periodEnd") is not None:
        import capo_artifact.types.timestamp_attribute

        out["period_end"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["periodEnd"]
        )
    if data.get("createdAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["created_at"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["createdAt"]
        )
    if data.get("lastModifiedAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["last_modified_at"] = (
            capo_artifact.types.timestamp_attribute.deserialize_json(
                data["lastModifiedAt"]
            )
        )
    if data.get("deletedAt") is not None:
        import capo_artifact.types.timestamp_attribute

        out["deleted_at"] = capo_artifact.types.timestamp_attribute.deserialize_json(
            data["deletedAt"]
        )
    if data.get("state") is not None:
        import capo_artifact.types.published_state

        out["state"] = capo_artifact.types.published_state.deserialize_json(
            data["state"]
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("series") is not None:
        out["series"] = data["series"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("companyName") is not None:
        out["company_name"] = data["companyName"]
    if data.get("productName") is not None:
        out["product_name"] = data["productName"]
    if data.get("termArn") is not None:
        out["term_arn"] = data["termArn"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("acceptanceType") is not None:
        import capo_artifact.types.acceptance_type

        out["acceptance_type"] = capo_artifact.types.acceptance_type.deserialize_json(
            data["acceptanceType"]
        )
    if data.get("sequenceNumber") is not None:
        out["sequence_number"] = data["sequenceNumber"]
    if data.get("uploadState") is not None:
        import capo_artifact.types.upload_state

        out["upload_state"] = capo_artifact.types.upload_state.deserialize_json(
            data["uploadState"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
