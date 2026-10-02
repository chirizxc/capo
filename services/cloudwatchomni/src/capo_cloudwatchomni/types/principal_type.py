"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PrincipalType``."""

from typing import Literal, TypeAlias, cast

"""Whether a principal is a user or a group."""
PrincipalType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrincipalType) -> str:
    return value


def deserialize_cbor(data: str) -> PrincipalType:
    return cast(PrincipalType, data)
