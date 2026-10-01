"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthoritySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority_summary

CertificateAuthoritySummaryList: TypeAlias = list[
    "capo_eks.types.certificate_authority_summary.CertificateAuthoritySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthoritySummaryList) -> list:
    import capo_eks.types.certificate_authority_summary

    out: list = []
    for item in value:
        out.append(capo_eks.types.certificate_authority_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CertificateAuthoritySummaryList:
    import capo_eks.types.certificate_authority_summary

    out: CertificateAuthoritySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eks.types.certificate_authority_summary.deserialize_json(item))
    return out
