"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthorityValidity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.timestamp


class CertificateAuthorityValidity(TypedDict, closed=True):
    not_before: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for the start of the certificate authority's validity period.</p>"""
    not_after: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for the end of the certificate authority's validity period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityValidity) -> dict:
    out: dict = {}
    if "not_before" in value:
        import capo_eks.types.timestamp

        out["notBefore"] = capo_eks.types.timestamp.serialize_json(value["not_before"])
    if "not_after" in value:
        import capo_eks.types.timestamp

        out["notAfter"] = capo_eks.types.timestamp.serialize_json(value["not_after"])
    return out


def deserialize_json(data: dict) -> CertificateAuthorityValidity:
    out: CertificateAuthorityValidity = {}  # type: ignore[typeddict-item]
    if data.get("notBefore") is not None:
        import capo_eks.types.timestamp

        out["not_before"] = capo_eks.types.timestamp.deserialize_json(data["notBefore"])
    if data.get("notAfter") is not None:
        import capo_eks.types.timestamp

        out["not_after"] = capo_eks.types.timestamp.deserialize_json(data["notAfter"])
    return out
