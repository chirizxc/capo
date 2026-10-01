"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

ResourceNotFoundExceptionReason: TypeAlias = Literal["RESOURCE_NOT_FOUND",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceNotFoundExceptionReason:
    return cast(ResourceNotFoundExceptionReason, data)
