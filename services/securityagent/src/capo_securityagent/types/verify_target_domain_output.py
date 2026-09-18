"""Generated from Smithy shape ``com.amazonaws.securityagent#VerifyTargetDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.target_domain_id
    import capo_securityagent.types.target_domain_status


class VerifyTargetDomainOutput(TypedDict, closed=True):
    target_domain_id: NotRequired[
        "capo_securityagent.types.target_domain_id.TargetDomainId"
    ]
    """<p>The unique identifier of the target domain.</p>"""
    domain_name: NotRequired["str"]
    """<p>The domain name of the target domain.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was last updated, in UTC format.</p>"""
    verified_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was verified, in UTC format.</p>"""
    status: NotRequired[
        "capo_securityagent.types.target_domain_status.TargetDomainStatus"
    ]
    """<p>The verification status of the target domain.</p>"""
    verification_status_reason: NotRequired["str"]
    """<p>The reason for the current target domain verification status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyTargetDomainOutput) -> dict:
    out: dict = {}
    if "target_domain_id" in value:
        out["targetDomainId"] = value["target_domain_id"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "verified_at" in value:
        import capo_securityagent._protocol.serialize

        out["verifiedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["verified_at"]
        )
    if "status" in value:
        import capo_securityagent.types.target_domain_status

        out["status"] = capo_securityagent.types.target_domain_status.serialize_json(
            value["status"]
        )
    if "verification_status_reason" in value:
        out["verificationStatusReason"] = value["verification_status_reason"]
    return out


def deserialize_json(data: dict) -> VerifyTargetDomainOutput:
    out: VerifyTargetDomainOutput = {}  # type: ignore[typeddict-item]
    if data.get("targetDomainId") is not None:
        out["target_domain_id"] = data["targetDomainId"]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("verifiedAt") is not None:
        import datetime

        out["verified_at"] = datetime.datetime.fromisoformat(
            data["verifiedAt"].replace("Z", "+00:00")
        )
    if data.get("status") is not None:
        import capo_securityagent.types.target_domain_status

        out["status"] = capo_securityagent.types.target_domain_status.deserialize_json(
            data["status"]
        )
    if data.get("verificationStatusReason") is not None:
        out["verification_status_reason"] = data["verificationStatusReason"]
    return out
