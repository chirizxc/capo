"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmProviderUpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.azure_update_configuration


class _CspmProviderUpdateConfiguration_Azure(TypedDict, closed=True):
    Azure: "capo_securityhub.types.azure_update_configuration.AzureUpdateConfiguration"


CspmProviderUpdateConfiguration: TypeAlias = _CspmProviderUpdateConfiguration_Azure


# --- restJson1 ser/de ---
def serialize_json(value: CspmProviderUpdateConfiguration) -> dict:
    if "Azure" in value:
        import capo_securityhub.types.azure_update_configuration

        return {
            "Azure": capo_securityhub.types.azure_update_configuration.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("CspmProviderUpdateConfiguration: no variant present")


def deserialize_json(data: dict) -> CspmProviderUpdateConfiguration:
    if data.get("Azure") is not None:
        import capo_securityhub.types.azure_update_configuration

        return {
            "Azure": capo_securityhub.types.azure_update_configuration.deserialize_json(
                data["Azure"]
            )
        }
    else:
        raise DeserializationError(
            "CspmProviderUpdateConfiguration: no recognized variant key"
        )
