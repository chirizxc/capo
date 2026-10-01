"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_enablement_status
    import capo_securityhub.types.cspm_provider_summary
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.timestamp


class CspmConnectorSummary(TypedDict, closed=True):
    connector_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of the connector.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the connector.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description of the connector.</p>"""
    provider_summary: NotRequired[
        "capo_securityhub.types.cspm_provider_summary.CspmProviderSummary"
    ]
    """<p>A summary of the cloud provider configuration for the connector.</p>"""
    created_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The ISO 8601 UTC timestamp indicating when the connector was created.</p>"""
    created_by: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The service principal that created the connector.</p>"""
    enablement_status: NotRequired[
        "capo_securityhub.types.cspm_enablement_status.CspmEnablementStatus"
    ]
    """<p>The enablement status of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CspmConnectorSummary) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "provider_summary" in value:
        import capo_securityhub.types.cspm_provider_summary

        out["ProviderSummary"] = (
            capo_securityhub.types.cspm_provider_summary.serialize_json(
                value["provider_summary"]
            )
        )
    if "created_at" in value:
        import capo_securityhub.types.timestamp

        out["CreatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "enablement_status" in value:
        import capo_securityhub.types.cspm_enablement_status

        out["EnablementStatus"] = (
            capo_securityhub.types.cspm_enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CspmConnectorSummary:
    out: CspmConnectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ProviderSummary") is not None:
        import capo_securityhub.types.cspm_provider_summary

        out["provider_summary"] = (
            capo_securityhub.types.cspm_provider_summary.deserialize_json(
                data["ProviderSummary"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["created_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("EnablementStatus") is not None:
        import capo_securityhub.types.cspm_enablement_status

        out["enablement_status"] = (
            capo_securityhub.types.cspm_enablement_status.deserialize_json(
                data["EnablementStatus"]
            )
        )
    return out
