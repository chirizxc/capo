"""Generated from Smithy shape ``com.amazonaws.eks#DescribeCertificateAuthorityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority


class DescribeCertificateAuthorityResponse(TypedDict, closed=True):
    certificate_authority: NotRequired[
        "capo_eks.types.certificate_authority.CertificateAuthority"
    ]
    """<p>An object containing detailed information about the certificate authority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCertificateAuthorityResponse) -> dict:
    out: dict = {}
    if "certificate_authority" in value:
        import capo_eks.types.certificate_authority

        out["certificateAuthority"] = (
            capo_eks.types.certificate_authority.serialize_json(
                value["certificate_authority"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeCertificateAuthorityResponse:
    out: DescribeCertificateAuthorityResponse = {}  # type: ignore[typeddict-item]
    if data.get("certificateAuthority") is not None:
        import capo_eks.types.certificate_authority

        out["certificate_authority"] = (
            capo_eks.types.certificate_authority.deserialize_json(
                data["certificateAuthority"]
            )
        )
    return out
