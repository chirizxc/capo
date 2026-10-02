"""Generated from Smithy shape ``com.amazonaws.eks#CreateCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority_summary
    import capo_eks.types.update


class CreateCertificateAuthorityResponse(TypedDict, closed=True):
    update: NotRequired["capo_eks.types.update.Update"]
    """<p>An object representing the asynchronous update that adds the certificate authority to the cluster's trust bundle.</p>"""
    certificate_authority: NotRequired[
        "capo_eks.types.certificate_authority_summary.CertificateAuthoritySummary"
    ]
    """<p>Summary information about the certificate authority that was created, including its ID and initial signing and distribution status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCertificateAuthorityResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.serialize_json(value["update"])
    if "certificate_authority" in value:
        import capo_eks.types.certificate_authority_summary

        out["certificateAuthority"] = (
            capo_eks.types.certificate_authority_summary.serialize_json(
                value["certificate_authority"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCertificateAuthorityResponse:
    out: CreateCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
    if data.get("update") is not None:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.deserialize_json(data["update"])
    if data.get("certificateAuthority") is not None:
        import capo_eks.types.certificate_authority_summary

        out["certificate_authority"] = (
            capo_eks.types.certificate_authority_summary.deserialize_json(
                data["certificateAuthority"]
            )
        )
    return out
