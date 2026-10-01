"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IdentityProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.identity_center_configuration


class IdentityProviderConfiguration(TypedDict, closed=True):
    identity_center_configuration: NotRequired[
        "capo_cloudwatchomni.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """Identity Center configuration. Required when identityProviders includes IDC."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityProviderConfiguration) -> dict:
    out: dict = {}
    if "identity_center_configuration" in value:
        import capo_cloudwatchomni.types.identity_center_configuration

        out["identityCenterConfiguration"] = (
            capo_cloudwatchomni.types.identity_center_configuration.serialize_cbor(
                value["identity_center_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> IdentityProviderConfiguration:
    out: IdentityProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("identityCenterConfiguration") is not None:
        import capo_cloudwatchomni.types.identity_center_configuration

        out["identity_center_configuration"] = (
            capo_cloudwatchomni.types.identity_center_configuration.deserialize_cbor(
                data["identityCenterConfiguration"]
            )
        )
    return out
