"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthoritySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.certificate_authority_activated_by
    import capo_eks.types.certificate_authority_created_by
    import capo_eks.types.certificate_authority_distribution_status
    import capo_eks.types.certificate_authority_signing_status
    import capo_eks.types.string
    import capo_eks.types.timestamp


class CertificateAuthoritySummary(TypedDict, closed=True):
    id: NotRequired["capo_eks.types.string.String"]
    """<p>The unique identifier of the certificate authority.</p>"""
    created_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the certificate authority was created.</p>"""
    created_by: NotRequired[
        "capo_eks.types.certificate_authority_created_by.CertificateAuthorityCreatedBy"
    ]
    """<p>The entity that created the certificate authority, either <code>CUSTOMER</code> or <code>EKS</code>.</p>"""
    activated_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the certificate authority was last activated. This value is absent if the certificate authority has never been activated.</p>"""
    activated_by: NotRequired[
        "capo_eks.types.certificate_authority_activated_by.CertificateAuthorityActivatedBy"
    ]
    """<p>The entity that most recently activated the certificate authority, either <code>CUSTOMER</code> or <code>EKS</code>.</p>"""
    signing_status: NotRequired[
        "capo_eks.types.certificate_authority_signing_status.CertificateAuthoritySigningStatus"
    ]
    """<p>The signing status of the certificate authority: <code>IN_USE</code>, <code>ACTIVATING</code>, or <code>NOT_USED</code>.</p>"""
    distribution_status: NotRequired[
        "capo_eks.types.certificate_authority_distribution_status.CertificateAuthorityDistributionStatus"
    ]
    """<p>The distribution status of the certificate authority: <code>IN_PROGRESS</code>, <code>COMPLETE</code>, <code>FAILED</code>, or <code>DELETING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthoritySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "created_at" in value:
        import capo_eks.types.timestamp

        out["createdAt"] = capo_eks.types.timestamp.serialize_json(value["created_at"])
    if "created_by" in value:
        import capo_eks.types.certificate_authority_created_by

        out["createdBy"] = (
            capo_eks.types.certificate_authority_created_by.serialize_json(
                value["created_by"]
            )
        )
    if "activated_at" in value:
        import capo_eks.types.timestamp

        out["activatedAt"] = capo_eks.types.timestamp.serialize_json(
            value["activated_at"]
        )
    if "activated_by" in value:
        import capo_eks.types.certificate_authority_activated_by

        out["activatedBy"] = (
            capo_eks.types.certificate_authority_activated_by.serialize_json(
                value["activated_by"]
            )
        )
    if "signing_status" in value:
        import capo_eks.types.certificate_authority_signing_status

        out["signingStatus"] = (
            capo_eks.types.certificate_authority_signing_status.serialize_json(
                value["signing_status"]
            )
        )
    if "distribution_status" in value:
        import capo_eks.types.certificate_authority_distribution_status

        out["distributionStatus"] = (
            capo_eks.types.certificate_authority_distribution_status.serialize_json(
                value["distribution_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CertificateAuthoritySummary:
    out: CertificateAuthoritySummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("createdAt") is not None:
        import capo_eks.types.timestamp

        out["created_at"] = capo_eks.types.timestamp.deserialize_json(data["createdAt"])
    if data.get("createdBy") is not None:
        import capo_eks.types.certificate_authority_created_by

        out["created_by"] = (
            capo_eks.types.certificate_authority_created_by.deserialize_json(
                data["createdBy"]
            )
        )
    if data.get("activatedAt") is not None:
        import capo_eks.types.timestamp

        out["activated_at"] = capo_eks.types.timestamp.deserialize_json(
            data["activatedAt"]
        )
    if data.get("activatedBy") is not None:
        import capo_eks.types.certificate_authority_activated_by

        out["activated_by"] = (
            capo_eks.types.certificate_authority_activated_by.deserialize_json(
                data["activatedBy"]
            )
        )
    if data.get("signingStatus") is not None:
        import capo_eks.types.certificate_authority_signing_status

        out["signing_status"] = (
            capo_eks.types.certificate_authority_signing_status.deserialize_json(
                data["signingStatus"]
            )
        )
    if data.get("distributionStatus") is not None:
        import capo_eks.types.certificate_authority_distribution_status

        out["distribution_status"] = (
            capo_eks.types.certificate_authority_distribution_status.deserialize_json(
                data["distributionStatus"]
            )
        )
    return out
