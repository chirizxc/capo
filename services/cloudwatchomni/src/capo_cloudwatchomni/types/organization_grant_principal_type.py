"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OrganizationGrantPrincipalType``."""

from typing import Literal, TypeAlias, cast

"""Principal types valid for organization-level domain access grants."""
OrganizationGrantPrincipalType: TypeAlias = Literal[
    "IDC_USER",
    "IDC_GROUP",
    "IAM_USER",
    "IAM_ROLE",
    "IAM_ROOT",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationGrantPrincipalType) -> str:
    return value


def deserialize_cbor(data: str) -> OrganizationGrantPrincipalType:
    return cast(OrganizationGrantPrincipalType, data)
