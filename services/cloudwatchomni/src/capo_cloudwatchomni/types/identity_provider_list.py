"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IdentityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.identity_provider

IdentityProviderList: TypeAlias = list[
    "capo_cloudwatchomni.types.identity_provider.IdentityProvider"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityProviderList) -> list:
    import capo_cloudwatchomni.types.identity_provider

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.identity_provider.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IdentityProviderList:
    import capo_cloudwatchomni.types.identity_provider

    out: IdentityProviderList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.identity_provider.deserialize_cbor(item))
    return out
