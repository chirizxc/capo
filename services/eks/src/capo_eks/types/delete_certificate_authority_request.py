"""Generated from Smithy shape ``com.amazonaws.eks#DeleteCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DeleteCertificateAuthorityRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    certificate_authority_id: "capo_eks.types.string.String"
    """<p>The ID of the certificate authority to delete. You can't delete the certificate authority that's currently signing certificates for the cluster.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCertificateAuthorityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCertificateAuthorityRequest:
    out: DeleteCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    return out
