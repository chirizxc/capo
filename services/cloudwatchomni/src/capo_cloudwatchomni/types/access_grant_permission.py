"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessGrantPermission``."""

from typing import Literal, TypeAlias, cast

"""Permission levels for AccessGrants. SPACE_ADMIN can manage grants within a space but cannot create spaces."""
AccessGrantPermission: TypeAlias = Literal[
    "SPACE_ADMIN",
    "READ",
    "READ_WRITE_DELETE",
    "CUSTOM",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessGrantPermission) -> str:
    return value


def deserialize_cbor(data: str) -> AccessGrantPermission:
    return cast(AccessGrantPermission, data)
