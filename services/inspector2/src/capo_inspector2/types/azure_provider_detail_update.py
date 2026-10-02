"""Generated from Smithy shape ``com.amazonaws.inspector2#AzureProviderDetailUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.azure_region_list
    import capo_inspector2.types.azure_scope_configuration_input


class AzureProviderDetailUpdate(TypedDict, closed=True):
    azure_regions: NotRequired[
        "capo_inspector2.types.azure_region_list.AzureRegionList"
    ]
    """<p>The updated Azure regions to scan.</p>"""
    scope_configuration: NotRequired[
        "capo_inspector2.types.azure_scope_configuration_input.AzureScopeConfigurationInput"
    ]
    """<p>The updated scope configuration that defines which Azure resources to scan.</p>"""
    auto_install_vm_scanner: NotRequired["bool"]
    """<p>Specifies whether to automatically install the VM scanner on connected Azure resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureProviderDetailUpdate) -> dict:
    out: dict = {}
    if "azure_regions" in value:
        import capo_inspector2.types.azure_region_list

        out["azureRegions"] = capo_inspector2.types.azure_region_list.serialize_json(
            value["azure_regions"]
        )
    if "scope_configuration" in value:
        import capo_inspector2.types.azure_scope_configuration_input

        out["scopeConfiguration"] = (
            capo_inspector2.types.azure_scope_configuration_input.serialize_json(
                value["scope_configuration"]
            )
        )
    if "auto_install_vm_scanner" in value:
        out["autoInstallVMScanner"] = value["auto_install_vm_scanner"]
    return out


def deserialize_json(data: dict) -> AzureProviderDetailUpdate:
    out: AzureProviderDetailUpdate = {}  # type: ignore[typeddict-item]
    if data.get("azureRegions") is not None:
        import capo_inspector2.types.azure_region_list

        out["azure_regions"] = capo_inspector2.types.azure_region_list.deserialize_json(
            data["azureRegions"]
        )
    if data.get("scopeConfiguration") is not None:
        import capo_inspector2.types.azure_scope_configuration_input

        out["scope_configuration"] = (
            capo_inspector2.types.azure_scope_configuration_input.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    if data.get("autoInstallVMScanner") is not None:
        out["auto_install_vm_scanner"] = data["autoInstallVMScanner"]
    return out
