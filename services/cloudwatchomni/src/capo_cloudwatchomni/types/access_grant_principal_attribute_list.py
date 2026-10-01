"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessGrantPrincipalAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_grant_principal_attribute

AccessGrantPrincipalAttributeList: TypeAlias = list[
    "capo_cloudwatchomni.types.access_grant_principal_attribute.AccessGrantPrincipalAttribute"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessGrantPrincipalAttributeList) -> list:
    import capo_cloudwatchomni.types.access_grant_principal_attribute

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatchomni.types.access_grant_principal_attribute.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AccessGrantPrincipalAttributeList:
    import capo_cloudwatchomni.types.access_grant_principal_attribute

    out: AccessGrantPrincipalAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatchomni.types.access_grant_principal_attribute.deserialize_cbor(
                item
            )
        )
    return out
