"""Generated from Smithy shape ``com.amazonaws.inspector2#ProviderDetailCreate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_inspector2.types.azure_provider_detail_create


class _ProviderDetailCreate_azure(TypedDict, closed=True):
    azure: (
        "capo_inspector2.types.azure_provider_detail_create.AzureProviderDetailCreate"
    )


ProviderDetailCreate: TypeAlias = _ProviderDetailCreate_azure


# --- restJson1 ser/de ---
def serialize_json(value: ProviderDetailCreate) -> dict:
    if "azure" in value:
        import capo_inspector2.types.azure_provider_detail_create

        return {
            "azure": capo_inspector2.types.azure_provider_detail_create.serialize_json(
                value["azure"]
            )
        }
    else:
        raise SerializationError("ProviderDetailCreate: no variant present")


def deserialize_json(data: dict) -> ProviderDetailCreate:
    if data.get("azure") is not None:
        import capo_inspector2.types.azure_provider_detail_create

        return {
            "azure": capo_inspector2.types.azure_provider_detail_create.deserialize_json(
                data["azure"]
            )
        }
    else:
        raise DeserializationError("ProviderDetailCreate: no recognized variant key")
