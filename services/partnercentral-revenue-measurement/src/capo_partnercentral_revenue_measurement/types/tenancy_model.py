"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#TenancyModel``."""

from typing import Literal, TypeAlias, cast

TenancyModel: TypeAlias = Literal[
    "MULTI_TENANT",
    "SINGLE_TENANT",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TenancyModel) -> str:
    return value


def deserialize_cbor(data: str) -> TenancyModel:
    return cast(TenancyModel, data)
