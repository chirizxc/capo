"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthorityCreatedBy``."""

from typing import Literal, TypeAlias, cast

CertificateAuthorityCreatedBy: TypeAlias = Literal[
    "EKS",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityCreatedBy) -> str:
    return value


def deserialize_json(data: str) -> CertificateAuthorityCreatedBy:
    return cast(CertificateAuthorityCreatedBy, data)
