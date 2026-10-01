"""Generated from Smithy shape ``com.amazonaws.eks#DeleteCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority_summary
    import capo_eks.types.update


class DeleteCertificateAuthorityResponse(TypedDict, closed=True):
    update: NotRequired["capo_eks.types.update.Update"]
    """<p>An object representing the asynchronous update that removes the certificate authority from the cluster's trust bundle.</p>"""
    certificate_authority: NotRequired[
        "capo_eks.types.certificate_authority_summary.CertificateAuthoritySummary"
    ]
    """<p>Summary information about the certificate authority that is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCertificateAuthorityResponse) -> dict:
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


def deserialize_json(data: dict) -> DeleteCertificateAuthorityResponse:
    out: DeleteCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
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
