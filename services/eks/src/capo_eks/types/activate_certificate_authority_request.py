"""Generated from Smithy shape ``com.amazonaws.eks#ActivateCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class ActivateCertificateAuthorityRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    certificate_authority_id: "capo_eks.types.string.String"
    """<p>The ID of the certificate authority to activate as the cluster's signing certificate authority. This certificate authority must already exist on the cluster and have a <code>distributionStatus</code> of <code>COMPLETE</code>.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateCertificateAuthorityRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> ActivateCertificateAuthorityRequest:
    out: ActivateCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
