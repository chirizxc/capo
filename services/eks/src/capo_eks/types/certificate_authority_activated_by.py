"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthorityActivatedBy``."""

from typing import Literal, TypeAlias, cast

CertificateAuthorityActivatedBy: TypeAlias = Literal[
    "EKS",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityActivatedBy) -> str:
    return value


def deserialize_json(data: str) -> CertificateAuthorityActivatedBy:
    return cast(CertificateAuthorityActivatedBy, data)
