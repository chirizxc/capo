"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.data_source_configuration
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.data_source_name
    import capo_qbusiness.types.data_source_vpc_configuration
    import capo_qbusiness.types.description
    import capo_qbusiness.types.document_enrichment_configuration
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.media_extraction_configuration
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.sync_schedule


class UpdateDataSourceRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p> The identifier of the Amazon Q Business application the data source is attached to.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index attached to the data source connector.</p>"""
    data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector.</p>"""
    display_name: NotRequired["capo_qbusiness.types.data_source_name.DataSourceName"]
    """<p>A name of the data source connector.</p>"""
    configuration: NotRequired[
        "capo_qbusiness.types.data_source_configuration.DataSourceConfiguration"
    ]
    vpc_configuration: NotRequired[
        "capo_qbusiness.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    description: NotRequired["capo_qbusiness.types.description.Description"]
    """<p>The description of the data source connector.</p>"""
    sync_schedule: NotRequired["capo_qbusiness.types.sync_schedule.SyncSchedule"]
    """<p>The chosen update frequency for your data source.</p>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.</p>"""
    document_enrichment_configuration: NotRequired[
        "capo_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
    ]
    media_extraction_configuration: NotRequired[
        "capo_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>The configuration for extracting information from media in documents for your data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "configuration" in value:
        out["configuration"] = value["configuration"]
    if "vpc_configuration" in value:
        import capo_qbusiness.types.data_source_vpc_configuration

        out["vpcConfiguration"] = (
            capo_qbusiness.types.data_source_vpc_configuration.serialize_json(
                value["vpc_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "sync_schedule" in value:
        out["syncSchedule"] = value["sync_schedule"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "document_enrichment_configuration" in value:
        import capo_qbusiness.types.document_enrichment_configuration

        out["documentEnrichmentConfiguration"] = (
            capo_qbusiness.types.document_enrichment_configuration.serialize_json(
                value["document_enrichment_configuration"]
            )
        )
    if "media_extraction_configuration" in value:
        import capo_qbusiness.types.media_extraction_configuration

        out["mediaExtractionConfiguration"] = (
            capo_qbusiness.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    if data.get("vpcConfiguration") is not None:
        import capo_qbusiness.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_qbusiness.types.data_source_vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("syncSchedule") is not None:
        out["sync_schedule"] = data["syncSchedule"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("documentEnrichmentConfiguration") is not None:
        import capo_qbusiness.types.document_enrichment_configuration

        out["document_enrichment_configuration"] = (
            capo_qbusiness.types.document_enrichment_configuration.deserialize_json(
                data["documentEnrichmentConfiguration"]
            )
        )
    if data.get("mediaExtractionConfiguration") is not None:
        import capo_qbusiness.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            capo_qbusiness.types.media_extraction_configuration.deserialize_json(
                data["mediaExtractionConfiguration"]
            )
        )
    return out
