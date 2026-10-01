"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OperationIdentifierSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.operation_identifier_set

OperationIdentifierSets: TypeAlias = list[
    "capo_cloudwatchomni.types.operation_identifier_set.OperationIdentifierSet"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationIdentifierSets) -> list:
    import capo_cloudwatchomni.types.operation_identifier_set

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatchomni.types.operation_identifier_set.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> OperationIdentifierSets:
    import capo_cloudwatchomni.types.operation_identifier_set

    out: OperationIdentifierSets = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatchomni.types.operation_identifier_set.deserialize_cbor(item)
        )
    return out
