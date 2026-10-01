"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#EncryptionStrategy``."""

from typing import Literal, TypeAlias, cast

"""Which kind of KMS key protects a resource's data at rest."""
EncryptionStrategy: TypeAlias = Literal[
    "AWS_OWNED",
    "CUSTOMER_MANAGED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EncryptionStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> EncryptionStrategy:
    return cast(EncryptionStrategy, data)
