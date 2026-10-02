"""Generated from Smithy shape ``com.amazonaws.inspector2#ProviderDetailUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_inspector2.types.azure_provider_detail_update


class _ProviderDetailUpdate_azure(TypedDict, closed=True):
    azure: (
        "capo_inspector2.types.azure_provider_detail_update.AzureProviderDetailUpdate"
    )


ProviderDetailUpdate: TypeAlias = _ProviderDetailUpdate_azure


# --- restJson1 ser/de ---
def serialize_json(value: ProviderDetailUpdate) -> dict:
    if "azure" in value:
        import capo_inspector2.types.azure_provider_detail_update

        return {
            "azure": capo_inspector2.types.azure_provider_detail_update.serialize_json(
                value["azure"]
            )
        }
    else:
        raise SerializationError("ProviderDetailUpdate: no variant present")


def deserialize_json(data: dict) -> ProviderDetailUpdate:
    if data.get("azure") is not None:
        import capo_inspector2.types.azure_provider_detail_update

        return {
            "azure": capo_inspector2.types.azure_provider_detail_update.deserialize_json(
                data["azure"]
            )
        }
    else:
        raise DeserializationError("ProviderDetailUpdate: no recognized variant key")
