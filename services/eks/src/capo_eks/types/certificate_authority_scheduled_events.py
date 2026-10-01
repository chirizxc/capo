"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthorityScheduledEvents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.timestamp


class CertificateAuthorityScheduledEvents(TypedDict, closed=True):
    first_auto_activation: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The earliest Unix epoch timestamp in seconds at which Amazon EKS may automatically activate this certificate authority.</p>"""
    final_auto_activation: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds by which Amazon EKS will automatically activate this certificate authority if you haven't already activated it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthorityScheduledEvents) -> dict:
    out: dict = {}
    if "first_auto_activation" in value:
        import capo_eks.types.timestamp

        out["firstAutoActivation"] = capo_eks.types.timestamp.serialize_json(
            value["first_auto_activation"]
        )
    if "final_auto_activation" in value:
        import capo_eks.types.timestamp

        out["finalAutoActivation"] = capo_eks.types.timestamp.serialize_json(
            value["final_auto_activation"]
        )
    return out


def deserialize_json(data: dict) -> CertificateAuthorityScheduledEvents:
    out: CertificateAuthorityScheduledEvents = {}  # type: ignore[typeddict-item]
    if data.get("firstAutoActivation") is not None:
        import capo_eks.types.timestamp

        out["first_auto_activation"] = capo_eks.types.timestamp.deserialize_json(
            data["firstAutoActivation"]
        )
    if data.get("finalAutoActivation") is not None:
        import capo_eks.types.timestamp

        out["final_auto_activation"] = capo_eks.types.timestamp.deserialize_json(
            data["finalAutoActivation"]
        )
    return out
