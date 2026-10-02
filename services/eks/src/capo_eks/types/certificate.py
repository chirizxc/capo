"""Generated from Smithy shape ``com.amazonaws.eks#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.active_certificate_authority
    import capo_eks.types.string


class Certificate(TypedDict, closed=True):
    data: NotRequired["capo_eks.types.string.String"]
    """<p>The Base64-encoded certificate data required to communicate with your cluster. Add this to the <code>certificate-authority-data</code> section of the <code>kubeconfig</code> file for your cluster.</p>"""
    active: NotRequired[
        "capo_eks.types.active_certificate_authority.ActiveCertificateAuthority"
    ]
    """<p>An object identifying the certificate authority that is currently signing certificates for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Certificate) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    if "active" in value:
        import capo_eks.types.active_certificate_authority

        out["active"] = capo_eks.types.active_certificate_authority.serialize_json(
            value["active"]
        )
    return out


def deserialize_json(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("active") is not None:
        import capo_eks.types.active_certificate_authority

        out["active"] = capo_eks.types.active_certificate_authority.deserialize_json(
            data["active"]
        )
    return out
