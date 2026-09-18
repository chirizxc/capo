"""Generated from Smithy shape ``com.amazonaws.signer#SigningJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.account_id
    import capo_signer.types.bool
    import capo_signer.types.display_name
    import capo_signer.types.job_id
    import capo_signer.types.platform_id
    import capo_signer.types.profile_name
    import capo_signer.types.profile_version
    import capo_signer.types.signed_object
    import capo_signer.types.signing_material
    import capo_signer.types.signing_status
    import capo_signer.types.source
    import capo_signer.types.timestamp


class SigningJob(TypedDict, closed=True):
    job_id: NotRequired["capo_signer.types.job_id.JobId"]
    """<p>The ID of the signing job.</p>"""
    source: NotRequired["capo_signer.types.source.Source"]
    """<p>A <code>Source</code> that contains information about a signing job's code image source.</p>"""
    signed_object: NotRequired["capo_signer.types.signed_object.SignedObject"]
    """<p>A <code>SignedObject</code> structure that contains information about a signing job's signed code image.</p>"""
    signing_material: NotRequired["capo_signer.types.signing_material.SigningMaterial"]
    """<p>A <code>SigningMaterial</code> object that contains the Amazon Resource Name (ARN) of the certificate used for the signing job.</p>"""
    created_at: NotRequired["capo_signer.types.timestamp.Timestamp"]
    """<p>The date and time that the signing job was created.</p>"""
    status: NotRequired["capo_signer.types.signing_status.SigningStatus"]
    """<p>The status of the signing job.</p>"""
    is_revoked: "capo_signer.types.bool.bool"
    """<p>Indicates whether the signing job is revoked.</p>"""
    profile_name: NotRequired["capo_signer.types.profile_name.ProfileName"]
    """<p>The name of the signing profile that created a signing job.</p>"""
    profile_version: NotRequired["capo_signer.types.profile_version.ProfileVersion"]
    """<p>The version of the signing profile that created a signing job.</p>"""
    platform_id: NotRequired["capo_signer.types.platform_id.PlatformId"]
    """<p>The unique identifier for a signing platform.</p>"""
    platform_display_name: NotRequired["capo_signer.types.display_name.DisplayName"]
    """<p>The name of a signing platform.</p>"""
    signature_expires_at: NotRequired["capo_signer.types.timestamp.Timestamp"]
    """<p>The time when the signature of a signing job expires.</p>"""
    job_owner: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the job owner.</p>"""
    job_invoker: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the job invoker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "source" in value:
        import capo_signer.types.source

        out["source"] = capo_signer.types.source.serialize_json(value["source"])
    if "signed_object" in value:
        import capo_signer.types.signed_object

        out["signedObject"] = capo_signer.types.signed_object.serialize_json(
            value["signed_object"]
        )
    if "signing_material" in value:
        import capo_signer.types.signing_material

        out["signingMaterial"] = capo_signer.types.signing_material.serialize_json(
            value["signing_material"]
        )
    if "created_at" in value:
        import capo_signer.types.timestamp

        out["createdAt"] = capo_signer.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "status" in value:
        import capo_signer.types.signing_status

        out["status"] = capo_signer.types.signing_status.serialize_json(value["status"])
    out["isRevoked"] = value.get("is_revoked", False)
    if "profile_name" in value:
        out["profileName"] = value["profile_name"]
    if "profile_version" in value:
        out["profileVersion"] = value["profile_version"]
    if "platform_id" in value:
        out["platformId"] = value["platform_id"]
    if "platform_display_name" in value:
        out["platformDisplayName"] = value["platform_display_name"]
    if "signature_expires_at" in value:
        import capo_signer.types.timestamp

        out["signatureExpiresAt"] = capo_signer.types.timestamp.serialize_json(
            value["signature_expires_at"]
        )
    if "job_owner" in value:
        out["jobOwner"] = value["job_owner"]
    if "job_invoker" in value:
        out["jobInvoker"] = value["job_invoker"]
    return out


def deserialize_json(data: dict) -> SigningJob:
    out: SigningJob = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("source") is not None:
        import capo_signer.types.source

        out["source"] = capo_signer.types.source.deserialize_json(data["source"])
    if data.get("signedObject") is not None:
        import capo_signer.types.signed_object

        out["signed_object"] = capo_signer.types.signed_object.deserialize_json(
            data["signedObject"]
        )
    if data.get("signingMaterial") is not None:
        import capo_signer.types.signing_material

        out["signing_material"] = capo_signer.types.signing_material.deserialize_json(
            data["signingMaterial"]
        )
    if data.get("createdAt") is not None:
        import capo_signer.types.timestamp

        out["created_at"] = capo_signer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("status") is not None:
        import capo_signer.types.signing_status

        out["status"] = capo_signer.types.signing_status.deserialize_json(
            data["status"]
        )
    if data.get("isRevoked") is not None:
        out["is_revoked"] = data["isRevoked"]
    else:
        out["is_revoked"] = False
    if data.get("profileName") is not None:
        out["profile_name"] = data["profileName"]
    if data.get("profileVersion") is not None:
        out["profile_version"] = data["profileVersion"]
    if data.get("platformId") is not None:
        out["platform_id"] = data["platformId"]
    if data.get("platformDisplayName") is not None:
        out["platform_display_name"] = data["platformDisplayName"]
    if data.get("signatureExpiresAt") is not None:
        import capo_signer.types.timestamp

        out["signature_expires_at"] = capo_signer.types.timestamp.deserialize_json(
            data["signatureExpiresAt"]
        )
    if data.get("jobOwner") is not None:
        out["job_owner"] = data["jobOwner"]
    if data.get("jobInvoker") is not None:
        out["job_invoker"] = data["jobInvoker"]
    return out
