"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OrganizationCredentialType``."""

from typing import Literal, TypeAlias, cast

"""Selects which member-account credential GetSpaceCredentialsForOrganization returns."""
OrganizationCredentialType: TypeAlias = Literal["SPACE_OPERATION",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationCredentialType) -> str:
    return value


def deserialize_cbor(data: str) -> OrganizationCredentialType:
    return cast(OrganizationCredentialType, data)
