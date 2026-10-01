"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_ssm.types.azure_configuration


class _CloudConnectorConfiguration_AzureConfiguration(TypedDict, closed=True):
    AzureConfiguration: "capo_ssm.types.azure_configuration.AzureConfiguration"


CloudConnectorConfiguration: TypeAlias = _CloudConnectorConfiguration_AzureConfiguration


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorConfiguration) -> dict:
    if "AzureConfiguration" in value:
        import capo_ssm.types.azure_configuration

        return {
            "AzureConfiguration": capo_ssm.types.azure_configuration.serialize_aws_json_1_1(
                value["AzureConfiguration"]
            )
        }
    else:
        raise SerializationError("CloudConnectorConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CloudConnectorConfiguration:
    if data.get("AzureConfiguration") is not None:
        import capo_ssm.types.azure_configuration

        return {
            "AzureConfiguration": capo_ssm.types.azure_configuration.deserialize_aws_json_1_1(
                data["AzureConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "CloudConnectorConfiguration: no recognized variant key"
        )
