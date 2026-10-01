"""Generated from Smithy shape ``com.amazonaws.eks#ActiveCertificateAuthority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority_activated_by
    import capo_eks.types.string


class ActiveCertificateAuthority(TypedDict, closed=True):
    id: NotRequired["capo_eks.types.string.String"]
    """<p>The unique identifier of the certificate authority that is currently signing certificates for the cluster.</p>"""
    activated_by: NotRequired[
        "capo_eks.types.certificate_authority_activated_by.CertificateAuthorityActivatedBy"
    ]
    """<p>The entity that activated the current signing certificate authority, either <code>CUSTOMER</code> or <code>EKS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveCertificateAuthority) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "activated_by" in value:
        import capo_eks.types.certificate_authority_activated_by

        out["activatedBy"] = (
            capo_eks.types.certificate_authority_activated_by.serialize_json(
                value["activated_by"]
            )
        )
    return out


def deserialize_json(data: dict) -> ActiveCertificateAuthority:
    out: ActiveCertificateAuthority = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("activatedBy") is not None:
        import capo_eks.types.certificate_authority_activated_by

        out["activated_by"] = (
            capo_eks.types.certificate_authority_activated_by.deserialize_json(
                data["activatedBy"]
            )
        )
    return out
