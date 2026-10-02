"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmProviderSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_connector_provider_name
    import capo_securityhub.types.cspm_connector_status
    import capo_securityhub.types.cspm_provider_detail


class CspmProviderSummary(TypedDict, closed=True):
    provider_name: NotRequired[
        "capo_securityhub.types.cspm_connector_provider_name.CspmConnectorProviderName"
    ]
    """<p>The name of the cloud provider.</p>"""
    connector_status: NotRequired[
        "capo_securityhub.types.cspm_connector_status.CspmConnectorStatus"
    ]
    """<p>The connectivity status of the connector.</p>"""
    provider_configuration: NotRequired[
        "capo_securityhub.types.cspm_provider_detail.CspmProviderDetail"
    ]
    """<p>The provider configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CspmProviderSummary) -> dict:
    out: dict = {}
    if "provider_name" in value:
        import capo_securityhub.types.cspm_connector_provider_name

        out["ProviderName"] = (
            capo_securityhub.types.cspm_connector_provider_name.serialize_json(
                value["provider_name"]
            )
        )
    if "connector_status" in value:
        import capo_securityhub.types.cspm_connector_status

        out["ConnectorStatus"] = (
            capo_securityhub.types.cspm_connector_status.serialize_json(
                value["connector_status"]
            )
        )
    if "provider_configuration" in value:
        import capo_securityhub.types.cspm_provider_detail

        out["ProviderConfiguration"] = (
            capo_securityhub.types.cspm_provider_detail.serialize_json(
                value["provider_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CspmProviderSummary:
    out: CspmProviderSummary = {}  # type: ignore[typeddict-item]
    if data.get("ProviderName") is not None:
        import capo_securityhub.types.cspm_connector_provider_name

        out["provider_name"] = (
            capo_securityhub.types.cspm_connector_provider_name.deserialize_json(
                data["ProviderName"]
            )
        )
    if data.get("ConnectorStatus") is not None:
        import capo_securityhub.types.cspm_connector_status

        out["connector_status"] = (
            capo_securityhub.types.cspm_connector_status.deserialize_json(
                data["ConnectorStatus"]
            )
        )
    if data.get("ProviderConfiguration") is not None:
        import capo_securityhub.types.cspm_provider_detail

        out["provider_configuration"] = (
            capo_securityhub.types.cspm_provider_detail.deserialize_json(
                data["ProviderConfiguration"]
            )
        )
    return out
