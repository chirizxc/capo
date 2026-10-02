"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OperationIdentifierSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.operation_identifier_key
    import capo_cloudwatchomni.types.operation_identifier_value

OperationIdentifierSet: TypeAlias = dict[
    "capo_cloudwatchomni.types.operation_identifier_key.OperationIdentifierKey",
    "capo_cloudwatchomni.types.operation_identifier_value.OperationIdentifierValue",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: OperationIdentifierSet) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> OperationIdentifierSet:
    out: OperationIdentifierSet = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
