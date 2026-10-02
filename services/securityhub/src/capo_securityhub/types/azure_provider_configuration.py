"""Generated from Smithy shape ``com.amazonaws.securityhub#AzureProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.azure_region_list
    import capo_securityhub.types.azure_scope_configuration
    import capo_securityhub.types.non_empty_string


class AzureProviderConfiguration(TypedDict, closed=True):
    aws_config_connector_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the multi-cloud configuration connector used to establish the connection to Azure.</p>"""
    scope_configuration: NotRequired[
        "capo_securityhub.types.azure_scope_configuration.AzureScopeConfiguration"
    ]
    """<p>The scope configuration that defines which Azure resources are monitored.</p>"""
    azure_regions: NotRequired[
        "capo_securityhub.types.azure_region_list.AzureRegionList"
    ]
    """<p>The list of Azure regions to monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureProviderConfiguration) -> dict:
    out: dict = {}
    if "aws_config_connector_arn" in value:
        out["AWSConfigConnectorArn"] = value["aws_config_connector_arn"]
    if "scope_configuration" in value:
        import capo_securityhub.types.azure_scope_configuration

        out["ScopeConfiguration"] = (
            capo_securityhub.types.azure_scope_configuration.serialize_json(
                value["scope_configuration"]
            )
        )
    if "azure_regions" in value:
        import capo_securityhub.types.azure_region_list

        out["AzureRegions"] = capo_securityhub.types.azure_region_list.serialize_json(
            value["azure_regions"]
        )
    return out


def deserialize_json(data: dict) -> AzureProviderConfiguration:
    out: AzureProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AWSConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["AWSConfigConnectorArn"]
    if data.get("ScopeConfiguration") is not None:
        import capo_securityhub.types.azure_scope_configuration

        out["scope_configuration"] = (
            capo_securityhub.types.azure_scope_configuration.deserialize_json(
                data["ScopeConfiguration"]
            )
        )
    if data.get("AzureRegions") is not None:
        import capo_securityhub.types.azure_region_list

        out["azure_regions"] = (
            capo_securityhub.types.azure_region_list.deserialize_json(
                data["AzureRegions"]
            )
        )
    return out
