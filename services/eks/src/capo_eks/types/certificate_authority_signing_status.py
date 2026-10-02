"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthoritySigningStatus``."""

from typing import Literal, TypeAlias, cast

CertificateAuthoritySigningStatus: TypeAlias = Literal[
    "NOT_USED",
    "ACTIVATING",
    "IN_USE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthoritySigningStatus) -> str:
    return value


def deserialize_json(data: str) -> CertificateAuthoritySigningStatus:
    return cast(CertificateAuthoritySigningStatus, data)
