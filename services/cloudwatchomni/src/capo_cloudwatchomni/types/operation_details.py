"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OperationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.operation_identifier_sets
    import capo_cloudwatchomni.types.operation_name

OperationDetails: TypeAlias = dict[
    "capo_cloudwatchomni.types.operation_name.OperationName",
    "capo_cloudwatchomni.types.operation_identifier_sets.OperationIdentifierSets",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: OperationDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cloudwatchomni.types.operation_identifier_sets

        out[key] = capo_cloudwatchomni.types.operation_identifier_sets.serialize_cbor(
            value
        )
    return out


def deserialize_cbor(data: dict) -> OperationDetails:
    out: OperationDetails = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_cloudwatchomni.types.operation_identifier_sets

        out[key] = capo_cloudwatchomni.types.operation_identifier_sets.deserialize_cbor(
            value
        )
    return out
