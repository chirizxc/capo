"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OrganizationGrantPermission``."""

from typing import Literal, TypeAlias, cast

"""Permission level for an organization-scoped grant."""
OrganizationGrantPermission: TypeAlias = Literal["ADMIN",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationGrantPermission) -> str:
    return value


def deserialize_cbor(data: str) -> OrganizationGrantPermission:
    return cast(OrganizationGrantPermission, data)
