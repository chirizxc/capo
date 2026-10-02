"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration

IntegrationList: TypeAlias = list["capo_cloudwatchomni.types.integration.Integration"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IntegrationList) -> list:
    import capo_cloudwatchomni.types.integration

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.integration.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IntegrationList:
    import capo_cloudwatchomni.types.integration

    out: IntegrationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.integration.deserialize_cbor(item))
    return out
