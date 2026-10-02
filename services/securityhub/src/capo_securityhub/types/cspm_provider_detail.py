"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmProviderDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.azure_detail


class _CspmProviderDetail_Azure(TypedDict, closed=True):
    Azure: "capo_securityhub.types.azure_detail.AzureDetail"


CspmProviderDetail: TypeAlias = _CspmProviderDetail_Azure


# --- restJson1 ser/de ---
def serialize_json(value: CspmProviderDetail) -> dict:
    if "Azure" in value:
        import capo_securityhub.types.azure_detail

        return {
            "Azure": capo_securityhub.types.azure_detail.serialize_json(value["Azure"])
        }
    else:
        raise SerializationError("CspmProviderDetail: no variant present")


def deserialize_json(data: dict) -> CspmProviderDetail:
    if data.get("Azure") is not None:
        import capo_securityhub.types.azure_detail

        return {
            "Azure": capo_securityhub.types.azure_detail.deserialize_json(data["Azure"])
        }
    else:
        raise DeserializationError("CspmProviderDetail: no recognized variant key")
