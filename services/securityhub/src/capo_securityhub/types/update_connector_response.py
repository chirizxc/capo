"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_connector_status
    import capo_securityhub.types.cspm_enablement_status


class UpdateConnectorResponse(TypedDict, closed=True):
    connector_status: NotRequired[
        "capo_securityhub.types.cspm_connector_status.CspmConnectorStatus"
    ]
    """<p>The connectivity status of the connector after the update.</p>"""
    enablement_status: NotRequired[
        "capo_securityhub.types.cspm_enablement_status.CspmEnablementStatus"
    ]
    """<p>The enablement status of the connector after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorResponse) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> UpdateConnectorResponse:
    out: UpdateConnectorResponse = {}  # type: ignore[typeddict-item]
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
