"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#RetryStrategy``."""

from typing import Literal, TypeAlias, cast

"""Retry strategy — determines which exceptions are retried."""
RetryStrategy: TypeAlias = Literal["ALL",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> RetryStrategy:
    return cast(RetryStrategy, data)
