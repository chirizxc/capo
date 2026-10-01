"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.enablement_status
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.provider_summary
    import capo_securityhub.types.timestamp


class ConnectorSummary(TypedDict, closed=True):
    connector_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the connectorV2.</p>"""
    connector_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Name field contains the user-defined name assigned to the integration connector. This helps identify and manage multiple connectors within Security Hub.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description of the connectorV2.</p>"""
    provider_summary: NotRequired[
        "capo_securityhub.types.provider_summary.ProviderSummary"
    ]
    """<p>The connectorV2 third party provider configuration summary.</p>"""
    created_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>ISO 8601 UTC timestamp for the time create the connectorV2.</p>"""
    enablement_status: NotRequired[
        "capo_securityhub.types.enablement_status.EnablementStatus"
    ]
    """<p>The enablement status of the connector.</p>"""
    enablement_status_reason: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reason for the current enablement status. Provides additional context when the connector is in a failed state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSummary) -> dict:
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
        import capo_securityhub.types.provider_summary

        out["ProviderSummary"] = capo_securityhub.types.provider_summary.serialize_json(
            value["provider_summary"]
        )
    if "created_at" in value:
        import capo_securityhub.types.timestamp

        out["CreatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "enablement_status" in value:
        import capo_securityhub.types.enablement_status

        out["EnablementStatus"] = (
            capo_securityhub.types.enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    if "enablement_status_reason" in value:
        out["EnablementStatusReason"] = value["enablement_status_reason"]
    return out


def deserialize_json(data: dict) -> ConnectorSummary:
    out: ConnectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ProviderSummary") is not None:
        import capo_securityhub.types.provider_summary

        out["provider_summary"] = (
            capo_securityhub.types.provider_summary.deserialize_json(
                data["ProviderSummary"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["created_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("EnablementStatus") is not None:
        import capo_securityhub.types.enablement_status

        out["enablement_status"] = (
            capo_securityhub.types.enablement_status.deserialize_json(
                data["EnablementStatus"]
            )
        )
    if data.get("EnablementStatusReason") is not None:
        out["enablement_status_reason"] = data["EnablementStatusReason"]
    return out
