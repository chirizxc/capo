"""Generated from Smithy shape ``com.amazonaws.securityhub#AzureUpdateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.azure_region_list
    import capo_securityhub.types.azure_scope_configuration


class AzureUpdateConfiguration(TypedDict, closed=True):
    scope_configuration: NotRequired[
        "capo_securityhub.types.azure_scope_configuration.AzureScopeConfiguration"
    ]
    """<p>The updated scope configuration.</p>"""
    azure_regions: NotRequired[
        "capo_securityhub.types.azure_region_list.AzureRegionList"
    ]
    """<p>The updated list of Azure regions to monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureUpdateConfiguration) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> AzureUpdateConfiguration:
    out: AzureUpdateConfiguration = {}  # type: ignore[typeddict-item]
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
