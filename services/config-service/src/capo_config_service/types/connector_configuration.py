"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.azure_connector_configuration


class ConnectorConfiguration(TypedDict, closed=True):
    azure: NotRequired[
        "capo_config_service.types.azure_connector_configuration.AzureConnectorConfiguration"
    ]
    """<p>The configuration for an Azure connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorConfiguration) -> dict:
    out: dict = {}
    if "azure" in value:
        import capo_config_service.types.azure_connector_configuration

        out["azure"] = (
            capo_config_service.types.azure_connector_configuration.serialize_aws_json_1_1(
                value["azure"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorConfiguration:
    out: ConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("azure") is not None:
        import capo_config_service.types.azure_connector_configuration

        out["azure"] = (
            capo_config_service.types.azure_connector_configuration.deserialize_aws_json_1_1(
                data["azure"]
            )
        )
    return out
