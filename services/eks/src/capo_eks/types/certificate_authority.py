"""Generated from Smithy shape ``com.amazonaws.eks#CertificateAuthority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean
    import capo_eks.types.certificate_authority_activated_by
    import capo_eks.types.certificate_authority_created_by
    import capo_eks.types.certificate_authority_distribution_status
    import capo_eks.types.certificate_authority_scheduled_events
    import capo_eks.types.certificate_authority_signing_status
    import capo_eks.types.certificate_authority_validity
    import capo_eks.types.string
    import capo_eks.types.timestamp


class CertificateAuthority(TypedDict, closed=True):
    id: NotRequired["capo_eks.types.string.String"]
    """<p>The unique identifier of the certificate authority.</p>"""
    created_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the certificate authority was created.</p>"""
    created_by: NotRequired[
        "capo_eks.types.certificate_authority_created_by.CertificateAuthorityCreatedBy"
    ]
    """<p>The entity that created the certificate authority. Certificate authorities that you create are <code>CUSTOMER</code>; those that Amazon EKS provisions on your behalf, such as a cluster's initial certificate authority, are <code>EKS</code>.</p>"""
    activated_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the certificate authority was last activated as the cluster's signer. This value is absent if the certificate authority has never been activated.</p>"""
    activated_by: NotRequired[
        "capo_eks.types.certificate_authority_activated_by.CertificateAuthorityActivatedBy"
    ]
    """<p>The entity that most recently activated the certificate authority. A value of <code>EKS</code> indicates that Amazon EKS activated it automatically; <code>CUSTOMER</code> indicates that you activated it.</p>"""
    signing_status: NotRequired[
        "capo_eks.types.certificate_authority_signing_status.CertificateAuthoritySigningStatus"
    ]
    """<p>The signing status of the certificate authority. <code>IN_USE</code> means the certificate authority is currently signing certificates for the cluster, <code>ACTIVATING</code> means it's being promoted to the signer, and <code>NOT_USED</code> means it's trusted by the cluster (for example, a successor CA during a rotation, or a retired outgoing CA) but isn't the signer.</p>"""
    distribution_status: NotRequired[
        "capo_eks.types.certificate_authority_distribution_status.CertificateAuthorityDistributionStatus"
    ]
    """<p>The distribution status of the certificate authority, which tracks whether Amazon EKS has distributed its trust to the Amazon Web Services managed components in your cluster (the control plane, Amazon EKS Auto Mode instances, and Amazon Web Services Fargate nodes). Valid values are <code>IN_PROGRESS</code>, <code>COMPLETE</code>, <code>FAILED</code>, and <code>DELETING</code>. A successor CA can only be activated after its distribution status is <code>COMPLETE</code>.</p>"""
    validity: NotRequired[
        "capo_eks.types.certificate_authority_validity.CertificateAuthorityValidity"
    ]
    """<p>The validity period of the certificate authority's certificate.</p>"""
    scheduled_events: NotRequired[
        "capo_eks.types.certificate_authority_scheduled_events.CertificateAuthorityScheduledEvents"
    ]
    """<p>The scheduled auto-activation events for the certificate authority, computed from its validity period.</p>"""
    rollback_available: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether CA rollback is still available for this certificate authority. After you activate a successor CA, rollback lets you revert to the outgoing CA for a limited period while you finish updating any worker nodes or clients that were missed.</p>"""
    data: NotRequired["capo_eks.types.string.String"]
    """<p>The Base64-encoded public certificate of the certificate authority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateAuthority) -> dict:
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
    if "validity" in value:
        import capo_eks.types.certificate_authority_validity

        out["validity"] = capo_eks.types.certificate_authority_validity.serialize_json(
            value["validity"]
        )
    if "scheduled_events" in value:
        import capo_eks.types.certificate_authority_scheduled_events

        out["scheduledEvents"] = (
            capo_eks.types.certificate_authority_scheduled_events.serialize_json(
                value["scheduled_events"]
            )
        )
    if "rollback_available" in value:
        out["rollbackAvailable"] = value["rollback_available"]
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> CertificateAuthority:
    out: CertificateAuthority = {}  # type: ignore[typeddict-item]
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
    if data.get("validity") is not None:
        import capo_eks.types.certificate_authority_validity

        out["validity"] = (
            capo_eks.types.certificate_authority_validity.deserialize_json(
                data["validity"]
            )
        )
    if data.get("scheduledEvents") is not None:
        import capo_eks.types.certificate_authority_scheduled_events

        out["scheduled_events"] = (
            capo_eks.types.certificate_authority_scheduled_events.deserialize_json(
                data["scheduledEvents"]
            )
        )
    if data.get("rollbackAvailable") is not None:
        out["rollback_available"] = data["rollbackAvailable"]
    if data.get("data") is not None:
        out["data"] = data["data"]
    return out
