"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_connector_status
    import capo_securityhub.types.cspm_enablement_status
    import capo_securityhub.types.non_empty_string


class CreateConnectorResponse(TypedDict, closed=True):
    connector_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of the connector.</p>"""
    connector_status: NotRequired[
        "capo_securityhub.types.cspm_connector_status.CspmConnectorStatus"
    ]
    """<p>The connectivity status of the connector.</p>"""
    enablement_status: NotRequired[
        "capo_securityhub.types.cspm_enablement_status.CspmEnablementStatus"
    ]
    """<p>The enablement status of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "connector_status" in value:
        import capo_securityhub.types.cspm_connector_status

        out["ConnectorStatus"] = (
            capo_securityhub.types.cspm_connector_status.serialize_json(
                value["connector_status"]
            )
        )
    if "enablement_status" in value:
        import capo_securityhub.types.cspm_enablement_status

        out["EnablementStatus"] = (
            capo_securityhub.types.cspm_enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateConnectorResponse:
    out: CreateConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorArn") is not None:
        out["connector_arn"] = data["ConnectorArn"]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    if data.get("ConnectorStatus") is not None:
        import capo_securityhub.types.cspm_connector_status

        out["connector_status"] = (
            capo_securityhub.types.cspm_connector_status.deserialize_json(
                data["ConnectorStatus"]
            )
        )
    if data.get("EnablementStatus") is not None:
        import capo_securityhub.types.cspm_enablement_status

        out["enablement_status"] = (
            capo_securityhub.types.cspm_enablement_status.deserialize_json(
                data["EnablementStatus"]
            )
        )
    return out
