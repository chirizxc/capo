"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#AttributionSortBy``."""

from typing import Literal, TypeAlias, cast

AttributionSortBy: TypeAlias = Literal["LastModifiedDate",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttributionSortBy) -> str:
    return value


def deserialize_cbor(data: str) -> AttributionSortBy:
    return cast(AttributionSortBy, data)
