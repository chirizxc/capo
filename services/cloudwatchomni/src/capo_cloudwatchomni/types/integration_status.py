"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

"""The current lifecycle state of an integration."""
IntegrationStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETED",
    "PENDING",
    "PENDING_OAUTH",
    "ERROR",
    "FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IntegrationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> IntegrationStatus:
    return cast(IntegrationStatus, data)
