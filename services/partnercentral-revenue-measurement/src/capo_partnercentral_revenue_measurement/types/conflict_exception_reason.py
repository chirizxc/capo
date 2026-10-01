"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionReason: TypeAlias = Literal[
    "CONFLICT_CLIENT_TOKEN",
    "CONCURRENT_MODIFICATION",
    "RESOURCE_ALREADY_EXISTS",
    "REVISION_MISMATCH",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConflictExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> ConflictExceptionReason:
    return cast(ConflictExceptionReason, data)
