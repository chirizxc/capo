"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DomainStatus``."""

from typing import Literal, TypeAlias, cast

"""Current status of a domain."""
DomainStatus: TypeAlias = Literal["ACTIVE",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DomainStatus:
    return cast(DomainStatus, data)
