"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthorityDistributionStatus``."""

from typing import Literal, TypeAlias, cast

CertificateAuthorityDistributionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityDistributionStatus) -> str:
    return value


def deserialize_json(data: str) -> CertificateAuthorityDistributionStatus:
    return cast(CertificateAuthorityDistributionStatus, data)
