"""Generated from Smithy shape ``com.amazonaws.eks#DescribeCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DescribeCertificateAuthorityRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    certificate_authority_id: "capo_eks.types.string.String"
    """<p>The ID of the certificate authority to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCertificateAuthorityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCertificateAuthorityRequest:
    out: DescribeCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    return out
